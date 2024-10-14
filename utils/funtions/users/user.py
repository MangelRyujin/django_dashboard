from apps.accounts.models import User

def total_users():
    return User.objects.filter(is_staff=False).count() or 0
