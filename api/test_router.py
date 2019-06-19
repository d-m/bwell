import sys
import mock
import unittest
from rest_framework import routers
import router


class GetRouterTest(unittest.TestCase):
    version = 'v2'
    good_app_path = 'good_app'
    bad_app_path = 'bad_app'

    @classmethod
    def setUpClass(cls):
        sys.modules['good_app'] = mock.MagicMock()
        sys.modules['good_app'].v2.router.router = routers.SimpleRouter()
        sys.modules['good_app.v2'] = mock.MagicMock()
        sys.modules['good_app.v2.router'] = mock.MagicMock()

        sys.modules['bad_app'] = mock.MagicMock()

    def test_good_app(self):
        """Test a good app that conforms to the convention in router.py module
        docstring.
        """
        test_router = router.get_router(self.good_app_path, self.version)
        self.assertIsInstance(test_router, routers.SimpleRouter)

    def test_bad_app(self):
        """Test an app that doesn't contain an API version package."""
        self.assertRaises(
            ImportError,
            router.get_router,
            self.bad_app_path,
            self.version
        )


class GetRoutesTest(unittest.TestCase):
    expected_routes = [1, 2, 3, 4]
    version = 'v2'
    app_module_paths = ['good_app', 'good_app2', 'bad_app']

    @classmethod
    def setUpClass(cls):
        sys.modules['good_app'] = mock.MagicMock()
        sys.modules['good_app'].v2.router.router = routers.SimpleRouter()
        sys.modules['good_app'].v2.router.router.registry = [1, 2]
        sys.modules['good_app.v2'] = mock.MagicMock()
        sys.modules['good_app.v2.router'] = mock.MagicMock()
        sys.modules['good_app'].v1.router.router = routers.SimpleRouter()
        sys.modules['good_app'].v1.router.router.registry = [5, 6]
        sys.modules['good_app.v1'] = mock.MagicMock()
        sys.modules['good_app.v1.router'] = mock.MagicMock()
        sys.modules['good_app2'] = mock.MagicMock()
        sys.modules['good_app2'].v2.router.router = routers.SimpleRouter()
        sys.modules['good_app2'].v2.router.router.registry = [3, 4]
        sys.modules['good_app2.v2'] = mock.MagicMock()
        sys.modules['good_app2.v2.router'] = mock.MagicMock()
        sys.modules['bad_app'] = mock.MagicMock()

    def test_get_routes(self):
        """Test that the get_routes function returns a list of all the routes
        for the supplied modules and a specific API version.
        """
        routes = router.get_routes(self.app_module_paths, self.version)
        self.assertEqual(routes, self.expected_routes)
