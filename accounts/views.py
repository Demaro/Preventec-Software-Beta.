from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )

User = get_user_model()

from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect, HttpResponse

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/principal")
    return render(request, "login.html", {"form":form, "title": title})


def register_view(request):
        if request.user.is_authenticated():
            form = UserRegisterForm(request.POST or None)
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
            return HttpResponseRedirect('crear_perfil/%s/' % new_user.id)


        return render(request, "user.html", )


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