# b.well Technical Interview Challenge

The goal of this challenge is to build a basic Django application using Python that implements a JSON REST API using `django-rest-framework` and the [Chicago health inspections dataset](https://data.cityofchicago.org/api/views/4ijn-s7e5/rows.csv?accessType=DOWNLOAD) found on [healthdata.gov](https://healthdata.gov/search/type/dataset).

This project hopes to demonstrate the following stated skill targets:

* can build a basic Django application
* can use appropriate Django ORM models
* can use a third-party plugin with Django
* can deliver data over a RESTful interface
* can build appropriate unit tests for an API endoint
* can handle database migrations with Django

This project hopes to also demonstrate some additional skills:

* demonstrate how an API can evolve while supporting legacy clients through versioning
* provide a convention for API versioning that allows for new versions to be added easily
* demonstrate environment management using `pipenv`

## Getting started

### Prerequisites

* Python 2.7+
* `pipenv`

To install `pipenv`, run the following:

```bash
$ pip install pipenv
Collecting pipenv
<truncated>
pipenv installed successfully
```

### Installing

1. clone the repo and change directories into it:

    ```bash
    $ git clone git@github.com:d-m/bwell.git bwell
    Cloning into 'bwell'...
    remote: Enumerating objects: 111, done.
    remote: Counting objects: 100% (111/111), done.
    remote: Compressing objects: 100% (55/55), done.
    remote: Total 111 (delta 53), reused 111 (delta 53), pack-reused 0
    Receiving objects: 100% (111/111), 37.81 KiB | 7.56 MiB/s, done.
    Resolving deltas: 100% (53/53), done.
    $ cd bwell

    ```

1. Install with development dependencies:

    ```bash
    $ pipenv install --dev
    pipenv install --dev
    Creating a virtualenv for this project...
    Pipfile: /<truncated>/Pipfile
    Using /usr/bin/python (2.7.10) to create virtualenv...
    ⠋ Creating virtual environment...Already using interpreter /usr/bin/python
    New python executable in /home/.local/share/virtualenvs/bwell-alC5uoXR/bin/python
    Installing setuptools, pip, wheel...
    done.

    ✔ Successfully created virtual environment! 
    Virtualenv location: /home/.local/share/virtualenvs/bwell-alC5uoXR
    Installing dependencies from Pipfile.lock (4e4e6c)...
    🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 92/92 — 00:00:20
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
    ```

1. Activate the shell so that all further commands are done in the virtualenv:

    ```bash
    $ pipenv shell
    Launching subshell in virtual environment...
    . /home/.local/share/virtualenvs/bwell-alC5uoXR/bin/activate
    ```

1. Migrate the database

    ```bash
    $ python manage.py migrate
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying health_inspections.0001_initial... OK
    Applying health_inspections.0002_load_inspection_data...[2019-06-20 02:04:37] INFO Opening inspection_data.csv
    [2019-06-20 02:04:39] INFO Finished. 0 failures and 1000 successes
    OK
    Applying sessions.0001_initial... OK
    ```

    The migration downloads the source data. Because it is somewhat large (approximately 200mb), the script caches the data in the current directory and will use the downloaded file if the database is deleted and and recreated. It also stops after processing the first 1000 rows.

    > Note: You may see an error in the logs: this is okay. The source data is not to be trusted and the migration does some data cleaning before creating entries in the database. Any errors are logged to the screen.

### Running the tests

You can run the test using the Django test runner or using `pytest`. The latter was included primarily for integration with VS Code.

To run the tests:

```bash
$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..................
----------------------------------------------------------------------
Ran 18 tests in 0.251s

OK
Destroying test database for alias 'default'...
```

### Starting the server

To start the server, run:

```bash
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
June 20, 2019 - 02:10:13
Django version 1.11.6, using settings 'bwell.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Navigate to [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/) and [http://localhost:8000/api/v2/](http://localhost:8000/api/v2/).

## Todo

* Create separate settings files for test, development, and production. This would clean up some of the hacks in the current settings file that are used for determining if tests are running (to skip the data load migration) and make it easier to load some settings from the environment during production, like the django secret.
* The establishment resources at [http://localhost:8000/api/v2/establishments](http://localhost:8000/api/v2/establishments) endpoint includes an `inspections` key containing a list of all inspections at that establishment. In the current data set, there are only a few inspections per establishment, however that may not always be the case. Because this can grow unbounded, it would be better to point this key to another url, say [http://localhost:8000/api/v2/establishments/1/inspections], where the inspection resources themselves can be returned and paginated as well.
* Add location via GeoDjango. It's in the dataset and I played around with creating a container with SpatiaLite to run this application but it would have taken me too long