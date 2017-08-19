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

    if request.user.is_authenticated:
        return HttpResponseRedirect('/principal')
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/principal")
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
            new_user = User(username=username, password=password, email=email, first_name=nombre, last_name=apellido)
            new_user.save()
            #login(request, new_user)
            new_user.id
            print(new_user.id)

        if form2.is_valid():

            rut_data = form2.cleaned_data.get("rut")
            birthdate_data = form2.cleaned_data.get("birthdate")
            avatar_data = form2.cleaned_data.get("avatar")
            cargo_data = form2.cleaned_data.get("cargo")
            especialidad_data = form2.cleaned_data.get("especialidad")
            contrato_data = form2.cleaned_data.get("contrato")
            legales_asoc_data = form2.cleaned_data.get("legales_asoc")

            new_profile = Profile(user_id=new_user.id, rut=rut_data, birthdate=birthdate_data, avatar=avatar_data, cargo=cargo_data, especialidad=especialidad_data, contrato=contrato_data, legales_asoc=legales_asoc_data, ultimateupdate = timezone.now(), inicio_cargo=timezone.now())

            new_profile.save()
            new_profile.id
            print(new_profile.id)
            return HttpResponseRedirect('/principal')

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