from django.contrib import admin
from django.contrib.auth.models import Group
# from users.models import Profile
# from .forms import PersoUserRegisterForm, PersoUserUpdateForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import PersoUser


# class PersoUserAdmin(UserAdmin):

#     form = PersoUserUpdateForm
#     add_form = PersoUserRegisterForm

#     fieldsets = [
#         ("Identification", {
#          "fields": ("username", "email", "password")}),
#         ("Info", {"fields": ("first_name", "last_name")}),
#         ("Permissions", {"fields": ("is_admin",)})
#     ]

#     list_display = ["username", "email", "first_name",
#                     "last_name", ]
#     list_filter = ["username",
#                    "is_admin"]

#     search_fields = ["username"]
#     ordering = ["username"]
#     filter_horizontal = ()

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ("username", 'email', 'password1', 'password2'),
#         }),
#     )

# admin.site.register(Profile)

admin.site.register(PersoUser)
# admin.site.unregister(Group)
