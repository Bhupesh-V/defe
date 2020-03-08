import unittest
from core import core
from app import app


class WebAppTest(unittest.TestCase):
    # function to set up testing connection

    def set_up(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def tear_down(self):
        pass

    def test_about(self):
        response = self.app.get("/about", follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class TestRunGetDomain(unittest.TestCase):
    def test_run(self):
        self.assertEqual(
            core.get_domain("https://xyz.com"), "xyz.com", "Something Wrong"
        )


if __name__ == "__main__":
    unittest.main()
