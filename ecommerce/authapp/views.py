from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes,DjangoUnicodeDecodeError, force_str




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


def login(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            auth.login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/login')

    return render(request, 'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')



class RequestResetEmailView(View):
    def get(self, request):
        return render(request, 'request-reset-email.html')
    
    def post(self, request):
        email = request.POST['email']
        user = User.objects.filter(email=email)

        if user.exists():
            email_subject = '[Reset Your Password]'
            message = render_to_string('reset-user-password.html', {
                'domain': '127.0.0.1:8000',
                'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token': PasswordResetTokenGenerator().make_token(user[0])
            })
            messages.info(request, f"WE HAVE SENT YOU AN EMAIL WITH INSTRUCTIONS ON HOW TO RESET THE PASSWORD {message} ")
            return render(request, 'request-reset-email.html')


class SetNewPasswordView(View):
    def get(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.warning(request, "Password Reset Link is Invalid")
                return render(request, 'request-reset-email.html')

        except (DjangoUnicodeDecodeError, User.DoesNotExist):
            pass

        return render(request, 'set-new-password.html', context)

    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, "Password is Not Matching")
            return render(request, 'set-new-password.html', context)
        
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            messages.success(request, "Password Reset Success Please Login with New Password")
            return redirect('/auth/login/')

        except (DjangoUnicodeDecodeError, User.DoesNotExist):
            messages.error(request, "Something Went Wrong")
            return render(request, 'set-new-password.html', context)

        return render(request, 'set-new-password.html', context)
