from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
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
            return HttpResponseRedirect("/admin_home")

        else:
            messages.error(request, "Invalid Login Details")
            return redirect("/")  # Ensure your template supports messages



def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : " + request.user.email + " usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")


def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")

def admin_home(request):
    return render(request, "admin_home.html")