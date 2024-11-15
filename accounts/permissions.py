from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied

from functools import wraps


def group_required(group):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group).exists():
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return _wrapped_view
    return decorator

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated or not any(role in request.user.role.split(',') for role in roles):
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


#Pour les classes

class GroupRequiredMixin(UserPassesTestMixin):
    group = None
    def test_func(self):
        return self.request.user.groups.filter(name=self.group).exists()

class RoleRequiredMixin(UserPassesTestMixin):
    roles = []
    def test_func(self):
        if not(
                self.request.user.is_authenticated
                and any(role in self.request.user.role.split(',') for role in self.roles)
        ):
            raise PermissionDenied
        return True

