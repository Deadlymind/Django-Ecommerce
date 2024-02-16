from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect

from .forms import SignupForm, UserActivateForm
from .models import Porfile

# Create your views here.

def signup(request):
    pass
    """
    -- create new user --
    -- send email code --
    -- redirect to activate --
    """
    # if request.user.is_authenticated:
    #     return redirect('/')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save(commit=False)
            user.is_active = False
            form.save() # trigger signal --> create profile --> send code
            profile = Porfile.objects.get(user__username=username)
            # send email code
            send_mail(
                "Activate your account",
                f"Welcome {username}\n Use this code {profile.code} to activate your account",
                "oussamaayari2014@gmail.com",
                [email],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')

    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_activate(request, username):
    """
    -- activate user --
    -- redirect to login --
    """
    profile = Porfile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''
                user = User.objects.get(username=username)
                user.is_active = True
                user.save()
                profile.save()

                return redirect('/accounts/login')

    else:
        form = UserActivateForm()
    return render(request, 'accounts/activate.html', {'form': form})