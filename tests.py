import unittest
from core import feedcore
from app import app

app.testing = True


class WebAppTests(unittest.TestCase):

    def test_main_page(self):
        with app.test_client() as client:
            response = client.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_feeders(self):
        with app.test_client() as client:
            response = client.get('/feeders', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_support(self):
        with app.test_client() as client:
            response = client.get('/support', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_feedback(self):
        with app.test_client() as client:
            response = client.get('/feedback', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_service_worker(self):
        with app.test_client() as client:
            response = client.get('/sw.js', follow_redirects=True)
            self.assertEqual(response.status_code, 200)


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
