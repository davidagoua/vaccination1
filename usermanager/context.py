from usermanager.models import UserRole


def user_role(request):
    return {role.name: role.name for role in list(UserRole)}
