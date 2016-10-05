from django.test import TestCase, RequestFactory
from seeker.views import register_user

# Unit Test
class UserTestCase(TestCase):

	def setUp(self):
		self.factory = RequestFactory()

	def test_registration_page(self):
		request = self.factory.get('/accounts/register')

		response = register_user(request)
		self.assertEqual(response.status_code, 200)
