from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method =="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is not Matching")
            return render(request, "signup.html")
        elif User.objects.filter(username=email).exists():
            messages.info(request, 'Email Already Taken')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            return redirect('/auth/login')

    return render(request,"signup.html")
 