"""This module automatically generates urls and an API root view for each API
version defined in settings at settings['REST_FRAMEWORK']['ALLOWED_VERSIONS'].

To use it, there are three requirements:

1. all allowed versions are defined at
   settings['REST_FRAMEWORK']['ALLOWED_VERSIONS']
2. you want to use django rest framework's namespaced versioning with urls like
   https://host/api/v1/ and https://host/api/v2/
3. Apps with API endpoints contain a folder named after
the API version with a router.py like so:

```
<app_folder>/
    <api_version>/
        __init__.py
        router.py
```

In router.py, there needs to be a rest_framework.routers object named router:

```python
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
# add routes to router
```

This module combines the registries for each router object corresponding to
each version and appends them to a path corresponding to that version. For
example, for API version 'v1' this code will import the v1.router.router in
every app registered in settings, grab all the routes, and include them at the
'v1/' url path.

Because APIs typically only change when their endpoints or serializations
change, it's a good idea to also put the serializers.py, views.py, and tests.py
in the version folder along with the router.py.
"""
from django.apps import apps
from rest_framework.settings import api_settings
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

APP_PATHS = [app.name for app in apps.get_app_configs()]
API_VERSIONS = api_settings.ALLOWED_VERSIONS


def get_router(module_path, version):
    """Attempt to import and return a router object from the module_path
    corresponding to a specific version.

    This code assumes that the router object is named `router` and located in
    the `<module>.<version>.router module`.

    We don't worry about raising an ImportError here because we will use it
    for flow control later.
    """
    module = __import__('{}.{}.router'.format(module_path, version))
    return getattr(module, version).router.router


def get_routes(app_module_paths, version):
    """Return a list of routes across all apps corresponding to a specific API
    version.
    """
    routes = []
    for app_module_path in app_module_paths:
        try:
            router = get_router(app_module_path, version)
            routes.extend(router.registry)
        except ImportError:
            pass
    return routes


urlpatterns = []
for version in API_VERSIONS:
    base_router = DefaultRouter()
    base_router.registry.extend(get_routes(APP_PATHS, version))
    urlpatterns.append(
        url(
            '{}/'.format(version),
            include(base_router.urls, namespace=version)
        )
    )
