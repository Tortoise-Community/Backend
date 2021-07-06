from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from utils.oauth import Oauth
from utils.mixins import ResponseMixin
from utils.decorators import permission_required
from utils.hash import Hashing
from tortoise_api.models import Admin, MemberWarning, Infraction, Guild
from utils.operations import create_admin, update_guilds, get_admin_guild_list

oauth = Oauth(redirect_uri="http://dash.tortoisecommunity.co:8000/", scope="guilds%20identify%20email")

hasing = Hashing()


class LoginView(View):
    template_name = "accounts/login.html"
    context = {}
    user_json = None
    access_token = None
    user_id = None
    email = None

    def get(self, request):
        code = request.GET.get('code', None)
        self.email = None
        msg = None
        if code is not None:
            self.access_token = oauth.get_access_token(code)
            self.user_json = oauth.get_user_json(self.access_token)
            self.user_id = self.user_json.get('id')
            self.email = self.user_json.get('email')
        if self.user_id and self.email is not None:
            password = hasing.hashed_user_pass(self.user_id, self.email)
            guilds = oauth.get_guild_info_json(self.access_token)
            admin_guilds = get_admin_guild_list(guilds)
            if not len(admin_guilds) == 0:
                user = authenticate(username=self.user_id, password=password)
                if user is not None:
                    admin_user = Admin.objects.get(user_id=self.user_id)
                    update_guilds(admin_user, admin_guilds)
                else:
                    user = create_admin(user_json=self.user_json, admin_guilds=admin_guilds, password=password)
                login(request, user)
                return redirect("/guild/{}/".format(admin_guilds[0]))
            else:
                msg = "You don't have the permissions to access the dashboard"
        return render(request, self.template_name, {"Oauth": oauth, "msg": msg})


@method_decorator(permission_required, name="dispatch")
class GuildPanelView(View, LoginRequiredMixin, ResponseMixin):
    template_name = "dashboard.html"
    context = {}
    model = Admin

    def get(self, request, guild_id):
        admin_guilds = request.user.admin.get_admin_guild_names()
        if int(guild_id) in admin_guilds:
            self.context["guilds"] = admin_guilds
            return render(request, self.template_name, self.context)


@method_decorator(permission_required, name="dispatch")
class GuildRulesView(View, LoginRequiredMixin):
    template_name = "dash-rules.html"
    context = {}

    def get(self, request, guild_id):
        # guild = Guild.objects.get(id=guild_id)
        return render(request, self.template_name)


@method_decorator(permission_required, name="dispatch")
class GuildRolesView(View, LoginRequiredMixin):
    template_name = "dash-roles.html"
    context = {}

    def get(self, request, guild_id):
        guild = Guild.objects.get(id=guild_id)
        print(guild.unused_emotes)
        return render(request, self.template_name)


@method_decorator(permission_required, name="dispatch")
class GuildInfractionView(View, LoginRequiredMixin):
    template_name = "infractions.html"
    model = Infraction
    context = {}

    def get(self, request, guild_id):
        infractions = self.model.objects.filter(member__guild__id=guild_id)
        return render(request, self.template_name, {"infractions": infractions})

    def post(self, request, guild_id):
        msg = None
        if request.user.is_authenticated:
            warning_id = request.POST.get("warning_id")
            try:
                warning = MemberWarning.objects.get(id=warning_id)
                if warning.member.guild in request.user.admins.guild.all():
                    warning.delete()
                    msg = "Data deleted successfully!"
                else:
                    msg = "You don't have the necessary permission for this operation"
            except MemberWarning.DoesNotExist:
                msg = "Something went wrong!. Please try again later"

        infractions = self.model.objects.filter(member__guild__id=guild_id)
        return render(request, self.template_name, {"infractions": infractions, "msg": msg})


@method_decorator(permission_required, name="dispatch")
class GuildWarningsView(View, LoginRequiredMixin):
    template_name = "dash-warnings.html"
    model = MemberWarning

    def get(self, request, guild_id):
        warnings = self.model.objects.filter(member__guild__id=guild_id)
        return render(request, self.template_name, {"warnings": warnings})


@method_decorator(permission_required, name="dispatch")
class BotSecurityView(View, LoginRequiredMixin):
    template_name = "bot-security.html"

    def get(self, request, guild_id):
        return render(request, self.template_name)


@method_decorator(permission_required, name="dispatch")
class BotLoggingView(View, LoginRequiredMixin):
    template_name = "bot-logging.html"

    def get(self, request, guild_id):
        return render(request, self.template_name)


@method_decorator(permission_required, name="dispatch")
class BotUtilityView(View, LoginRequiredMixin):
    template_name = "bot-utility.html"

    def get(self, request, guild_id):
        return render(request, self.template_name)


@method_decorator(permission_required, name="dispatch")
class BotMusicView(View, LoginRequiredMixin):
    template_name = "bot-music.html"

    def get(self, request, guild_id):
        return render(request, self.template_name)


@method_decorator(permission_required, name="dispatch")
class BotFunView(View, LoginRequiredMixin):
    template_name = "bot-fun.html"

    def get(self, request, guild_id):
        return render(request, self.template_name)


@method_decorator(permission_required, name="dispatch")
class BotOtherView(View, LoginRequiredMixin):
    template_name = "bot-other.html"

    def get(self, request, guild_id):
        return render(request, self.template_name)


@login_required
def logout_request(request):
    logout(request)
    return redirect('login')
