from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    def has_group(user):
        if not user.is_authenticated:
            return False
        
        if hasattr(user, 'groups'):
            return bool(user.groups.filter(name__in=group_names))
        
        return False
    return user_passes_test(has_group, login_url='/', redirect_field_name='next')