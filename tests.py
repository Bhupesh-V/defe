import unittest
from core import feedcore
from app import app


# class WebAppTest(unittest.TestCase):
#     # function to set up testing connection

#     def set_up(self):
#         app.config["TESTING"] = True
#         app.config["DEBUG"] = True
#         self.app = app.test_client()
#         self.assertEqual(app.debug, False)

#     def tear_down(self):
#         pass

#     def test_about(self):
#         response = self.app.get("/about", follow_redirects=True)
#         self.assertEqual(response.status_code, 200)


class TestRunGetDomain(unittest.TestCase):
    def test_run(self):
        self.assertEqual(
            feedcore.get_domain("https://xyz.com"), "xyz.com", "Something Wrong"
        )


class TestRunReadData(unittest.TestCase):
    def test_run_general(self):
        self.assertIsNotNone(
            feedcore.read_data("general")
        )

    def test_run_podcasts(self):
        self.assertIsNotNone(
            feedcore.read_data("podcasts")
        )

    def test_run_news(self):
        self.assertIsNotNone(
            feedcore.read_data("news")
        )

    def test_run_newsletters(self):
        self.assertIsNotNone(
            feedcore.read_data("newsletters")
        )


if __name__ == "__main__":
    unittest.main()
