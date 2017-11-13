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

from profiles.models import Profile, Perfil_Obrero

from .serializers import UserSerializer
from rest_framework import viewsets, status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 


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
        form = UserRegisterForm(request.POST or None)
        if request.user.is_authenticated():
            if form.is_valid():
                instance = form.save(commit=False)
                instance.is_staff   = "True"
                instance.save()
                print(instance.id)
                id_user = instance.id
                return HttpResponseRedirect('/crear_perfil_staff/%s' % id_user )

        context = {
            "form": form,
        }
        return render(request, "create_staff.html", context)






def view_users(request):
    obj = Profile.objects.all().order_by("-id")
    obj2   = Perfil_Obrero.objects.all().order_by("-id")

    context = {

        "obj": obj,
        "obj2": obj2,
    }
    return render(request, "user.html", context)



def logout_view(request):
    logout(request)
    return redirect("/")


"""
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
            return HttpResponseRedirect('/crear_usuario')
"""

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