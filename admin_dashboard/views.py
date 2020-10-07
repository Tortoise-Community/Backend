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
