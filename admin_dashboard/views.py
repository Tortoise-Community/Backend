from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from utils.oauth import Oauth
from utils.encryption import Encryption
from userdata.models import Admins
from utils.operations import create_admin, update_guilds, get_admin_guild_list
oauth = Oauth(redirect_uri="http://dashboard.tortoisecommunity.co:8000/login/", scope="guilds%20identify%20email")
encryption = Encryption()


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
        if self.user_id and self.email is not None:
            password = encryption.encrypted_user_pass(self.user_id, self.email)
            guilds = oauth.get_guild_info_json(self.access_token)
            admin_guilds = get_admin_guild_list(guilds)
            if len(admin_guilds) == 0:
                return  # TODO: DELETE EXISTING CREDENTIALS AND SEND MESSAGE
            user = authenticate(username=self.user_id, password=password)
            if user is not None:
                login(request, user)
                admin_user = Admins.objects.get(user_id=self.user_id)
                update_guilds(admin_user, admin_guilds)
            else:
                create_admin(user_json=self.user_json, admin_guilds=admin_guilds, password=password)
        # TODO: IMPLEMENT AUTHENTICATION
        return render(request, self.template_name, {"Oauth": oauth})


class GuildPanelView(View):
    template_name = "dashboard/index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name)


@login_required
def logout_request(request):
    logout(request)
    return redirect('login')
