import unittest

from curl_builder import build_curl_command


class TestCurlBuilder(unittest.TestCase):

    def test_get_request(self):
        curl = build_curl_command(
            method="GET",
            url="https://api.example.com/users"
        )

        self.assertIn("curl", curl)
        self.assertIn("GET", curl)
        self.assertIn("https://api.example.com/users", curl)

    def test_post_request(self):
        curl = build_curl_command(
            method="POST",
            url="https://api.example.com/users",
            body={"name": "John"}
        )

        self.assertIn("POST", curl)
        self.assertIn("John", curl)

    def test_headers(self):
        curl = build_curl_command(
            method="GET",
            url="https://api.example.com/users",
            headers={"Authorization": "Bearer token"}
        )

        self.assertIn("Authorization", curl)

    def test_query_params(self):
        curl = build_curl_command(
            method="GET",
            url="https://api.example.com/users?page=1"
        )

        self.assertIn("page=1", curl)


if __name__ == "__main__":
    unittest.main()