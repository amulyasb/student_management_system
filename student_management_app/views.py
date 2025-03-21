from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.urls import reverse
from student_management_app import EmailBackEnd
from django.shortcuts import render, redirect

# Create your views here.
def showDemoPage(request):
    return render(request, "demo.html")


def showLoginPage(request):
    return render(request, "login_page.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = EmailBackEnd.EmailBackEnd.authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('admin_home')
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse('staff_home'))
            elif user.user_type == "3":
                return HttpResponseRedirect(reverse('student_home'))
            else:
                return HttpResponse("Invalid User")


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : " + request.user.email + " usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")


def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")

