from test_app.tests.test_setup import TestSetUp


class RegisterLoginViews(TestSetUp):

    def test_user_can_register(self):
        res = self.client.post(self.register_url, self.user_register_data)
        self.assertEqual(res.status_code, 201)

    def test_user_can_login_correctly(self):
        self.test_user_can_register()
        res = self.client.post(self.login_url, self.user_login_data)
        self.assertEqual(res.status_code, 200)

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_cannot_login_with_no_data(self):
        res = self.client.post(self.login_url)
        self.assertEqual(res.status_code, 400)

