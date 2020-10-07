from django.shortcuts import render
from django.views import View
# Create your views here.


class LoginView(View):
    template_name = "dashboard/accounts/login.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name)


class PanelView(View):
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