from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import CustomUser, Courses, Staffs, Students, Subjects
# Register your models here.

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)
admin.site.register(Courses)
admin.site.register(Staffs)
admin.site.register(Students)
admin.site.register(Subjects)