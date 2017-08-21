from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )

User = get_user_model()

from django.utils import timezone

from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect, HttpResponse

from .forms import UserLoginForm, UserRegisterForm

from profiles.forms import ProfileForm

from profiles.models import Profile

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if not request.user.is_authenticated():

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/inicio")
    return render(request, "login.html", {"form":form})


def register_view(request):
        if request.user.is_authenticated():
            form = UserRegisterForm(request.POST or None)
            form2 = ProfileForm(request.POST or None)
        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get("email")
            nombre = form.cleaned_data.get("first_name")
            apellido = form.cleaned_data.get("last_name")
            new_user = User(username=username, password=password, email=email, first_name=nombre, last_name=apellido, is_staff=True)
            new_user.save()
            #login(request, new_user)
            user = new_user.id
            print(new_user.id)


        if form2.is_valid():

            profile = form2.save(commit=False)

            birthdate_data = form2.cleaned_data.get("birthdate")

            profile.birthdate = birthdate_data

            profile.user_id = user

            profile.fecha_cargo = timezone.now()
            profile.ultimateupdate = timezone.now()

            profile.save()
            profile.id
            print(profile.id)
            return HttpResponseRedirect('/inicio')

        context = {
        "form2": form2,
        }
        return render(request, "user.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")




from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
 
class CaseInsensitiveModelBackend(ModelBackend):
  def authenticate(self, username=None, password=None):
    try:
      user = User.objects.get(username__iexact=username)
      if user.check_password(password):
        return user
      return None
    except User.DoesNotExist:
      return None