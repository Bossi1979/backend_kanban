from django.contrib.auth.models import User


def get_username_by_email(request):
    """
    Retrieve the username associated with the provided email address.

    Parameters:
        request (Request): A Django request object containing the email address in its data.

    Returns:
        str: The username associated with the provided email address.

    Raises:
        User.DoesNotExist: If no user is found with the provided email address.
    """
    email = request.data.get('email')
    user = User.objects.get(email=email)
    return user.username


def login_failed():
    """
    Generate a dictionary indicating a failed login attempt.

    Returns:
        dict: A dictionary containing an error message indicating the login failure.
    """
    return {
        'error': 'Login failed',
    }
    
    
def login_successful(user, token):
    """
    Generate a dictionary containing user information upon successful login.

    Parameters:
        user (User): A Django User object representing the logged-in user.
        token (Token): A Django Rest Framework token object associated with the user.

    Returns:
        dict: A dictionary containing the username, email, token, and a success message.

    Example:
        {
            'username': 'example_username',
            'email': 'example@example.com',
            'token': 'example_token',
            'error': 'none'
        }
    """
    return {
            'username': user.username,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'token': token.key,
            'error': 'none',
        }