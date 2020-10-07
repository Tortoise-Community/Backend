from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm
from utils.oauth import Oauth
# from userdata.models import Admins
oauth = Oauth(redirect_uri="http://dashboard.tortoisecommunity.co:8000/login/")


class LoginView(View):
    template_name = "dashboard/accounts/login.html"
    context = {}
    user_json = None
    access_token = None
    user_id = None
    email = None

    def get(self, request):
        code = request.GET.get('code', None)
        self.email = None
        if code is not None:
            self.access_token = oauth.get_access_token(code)
            self.user_json = oauth.get_user_json(self.access_token)
            self.user_id = self.user_json.get('id')
            self.email = self.user_json.get('email')

        return render(request, self.template_name, {"Oauth": oauth})

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/panel")


class GuildPanelView(View):
    template_name = "dashboard/index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name)


class ServerView(View):
    context = {}

    def get(self, request, template_name):
        return render(request, f"dashboard/{template_name}.html")


class BotView(View):
    context = {}

    def get(self, request, template_name):
        return render(request, f"dashboard/bot-{template_name}.html")


@login_required
def logout_request(request):
    logout(request)
    return redirect('login')


class RegisterView(View):
    template_name = "dashboard/accounts/register.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name)
