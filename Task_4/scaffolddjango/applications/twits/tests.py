import unittest
from rest_framework.test import APIClient, APITestCase

import django
django.setup()


class MyTestCase(APITestCase):
    def test_something(self):
        client = APIClient()
        response = client.get('/api/twits/movie/', format='json')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
