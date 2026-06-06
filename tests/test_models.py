import unittest

from models import RequestModel


class TestModels(unittest.TestCase):

    def test_request_model(self):
        request = RequestModel(
            method="GET",
            url="https://api.example.com/users"
        )

        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            "https://api.example.com/users"
        )


if __name__ == "__main__":
    unittest.main()