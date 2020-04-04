import unittest
from core import feedcore
from app import app

# import urllib.request

app.testing = True

# HEADERS = {"User-Agent": "Mozilla/5.0"}


# class TestFeeders(unittest.TestCase):
#     def test_general_feeders(self):
#         data = feedcore.read_data("general")
#         for item in data:
#             try:
#                 req = urllib.request.Request(item["link"], headers=HEADERS)
#                 with urllib.request.urlopen(req, timeout=4) as response:
#                     response.read()
#                     print(item["link"])
#             except urllib.error.HTTPError as e:
#                 print(e, item["link"])


class WebAppTests(unittest.TestCase):
    def test_main_page(self):
        with app.test_client() as client:
            response = client.get("/", follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_feeders(self):
        with app.test_client() as client:
            response = client.get("/feeders", follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_support(self):
        with app.test_client() as client:
            response = client.get("/support", follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_feedback(self):
        with app.test_client() as client:
            response = client.get("/feedback", follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_service_worker(self):
        with app.test_client() as client:
            response = client.get("/sw.js", follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_general(self):
        with app.test_client() as client:
            response = client.get("/general", follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_podcasts(self):
        with app.test_client() as client:
            response = client.get("/podcasts", follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_news(self):
        with app.test_client() as client:
            response = client.get("/news", follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_newsletters(self):
        with app.test_client() as client:
            response = client.get("/newsletters", follow_redirects=True)
            self.assertEqual(response.status_code, 200)


class TestRunGetDomain(unittest.TestCase):
    def test_run(self):
        self.assertEqual(
            feedcore.get_domain("https://xyz.com"), "xyz.com", "Something Wrong"
        )


class TestRunReadData(unittest.TestCase):
    def test_run_general(self):
        self.assertIsNotNone(feedcore.read_data("general"))

    def test_run_podcasts(self):
        self.assertIsNotNone(feedcore.read_data("podcasts"))

    def test_run_news(self):
        self.assertIsNotNone(feedcore.read_data("news"))

    def test_run_newsletters(self):
        self.assertIsNotNone(feedcore.read_data("newsletters"))


if __name__ == "__main__":
    unittest.main()
