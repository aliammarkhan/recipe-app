from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    # test to check if email is normalized
    def test_check_email_normalized(self):
        """ testing if email is all lower case"""
        
        email = 'bio@TEST.COM'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email,email.lower())
        
        
    def test_email_provided(self):
        """ Test if the user has entered an email or not"""
        with self.assertRaises(ValueError): #fail test of value error not raise
            user = get_user_model().objects.create_user(None,'pass')
            
            
    def test_super_user(self):
        """ Testing if the created user is the super user"""
        user = get_user_model().objects.create_super_user('test@gmail.com','pass123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)