from django.contrib import admin
from .models import User,UserCopy


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "phone_no",
        "city",
        "state",
        "registration",
    ]


admin.site.register(User, UserAdmin)
class UserCopyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_name",
        "status",
        "email",
        "phone_no",
        "profile_img",
        "address",
        "date",
    ]


admin.site.register(UserCopy, UserCopyAdmin)
