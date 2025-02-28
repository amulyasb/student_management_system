"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student_management_app import views, HodViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo',views.showDemoPage, name="demo"),
    path('',views.showLoginPage, name="show_login"),
    path('doLogin',views.doLogin, name="do_login"),
    path('get_user_details',views.GetUserDetails, name="get_user_details"),
    path('logout_user',views.LogoutUser, name="logout_user"),
    path('admin_home',HodViews.admin_home, name="admin_home"),
    path('add_staff',HodViews.add_staff, name="add_staff"),
    path('manage_staff', HodViews.manage_staff,name="manage_staff"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    path('add_course', HodViews.add_course,name="add_course"),
    path('add_course_save', HodViews.add_course_save,name="add_course_save"),
    path('manage_course', HodViews.manage_course,name="manage_course"),


]
