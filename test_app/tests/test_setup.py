from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_register_data = {
            'username': '100029', 'password': 'password-random', 'email': 'email@email.com', 'first_name': 'userTwo',
            'gender': 'Male', 'last_name': 'last', 'mobile': 4422
        }
        self.user_login_data = {
            'username': '100029',
            'password': 'password-random',
        }
        # self.api_authentication()
        return super().setUp()

    # def api_authentication(self):
    #     self.token = Token.objects.get(user=self.user)
    #     self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def tearDown(self):
        return super().tearDown()
