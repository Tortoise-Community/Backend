from datetime import datetime, timezone

from django.views import View
from django.conf import settings
from django.shortcuts import render

from utils.oauth import Oauth
from utils.mixins import ModelDataMixin, ResponseMixin
from utils.tools import bot_socket, webhook
from utils.handlers import EmailHandler, log_error

from websitedata.models import Events
from userdata.models import Developers, Projects, Members


class ProjectView(ModelDataMixin, View, ResponseMixin):
    model = Projects
    template_name = 'projects.html'
    context = {}

    def get(self, request, item_no=None):
        if item_no is not None:
            self.context = self.get_blog_context()
            self.template_name = 'project.html'
            try:
                project = self.model.objects.get(pk=item_no)
                self.context['project'] = project
            except self.model.DoesNotExist:
                return self.http_responce_404()
        else:
            self.context = self.get_common_context()
            self.context['projects'] = self.model.objects.all().order_by('id')

        return render(request, self.template_name, self.context)


class EventView(ModelDataMixin, ResponseMixin, View):
    model = Events
    template_name = 'events.html'
    context = {}

    def get(self, request, item_no=None):
        if item_no is not None:
            self.context = self.get_blog_context()
            self.template_name = 'event.html'
            try:
                event = self.model.objects.get(pk=item_no)
                if event.status == "Upcoming":
                    return self.http_responce_401()
                self.context['event'] = event
            except self.model.DoesNotExist:
                return self.http_responce_404()
        else:
            self.get_events_context()
        return render(request, self.template_name, self.context)


class IndexView(ModelDataMixin, View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        self.get_main_context()
        return render(request, self.template_name, self.context)


class VerificationHandlerView(ModelDataMixin, View):

    template_name = 'verification_handler.html'
    verified = False
    context = {"Oauth": Oauth}
    user_json = None
    access_token = None
    user_id = None
    email = None

    def get(self, request):
        code = request.GET.get('code')
        self.email = None
        if code is not None:
            self.access_token = Oauth.get_access_token(code)
            self.user_json = Oauth.get_user_json(self.access_token)
            self.user_id = self.user_json.get('id')
            self.email = self.user_json.get('email')
        self.context['emailerror'] = False  # noqa
        self.context['verified'] = False  # noqa
        self.context['joined'] = True  # noqa
        self.context['error'] = False  # noqa
        self.context['alterror'] = False  # noqa
        self.get_blog_context()
        if code is None:
            pass
        elif self.email is not None:
            try:
                member = Members.objects.get(email=self.email)
                if member.user_id != int(self.user_id):
                    self.context["alterror"] = True  # noqa
                    return render(request, self.template_name, self.context)
            except Members.DoesNotExist:
                pass
            self.context['verified'] = True # noqa
            try:
                member_obj = Members.objects.get(user_id=self.user_id)
            except Members.DoesNotExist:
                member_obj = None
            # checks if member object exits (joined the server)
            if member_obj:
                # check if the member is already verified
                if getattr(member_obj, "verified") is True:
                    message = ("You are already vefified.\nIf you still can't send messages to the server, please "
                               "reply to this message with 'M' and choose Mod mail (contact staff) option by reacting "
                               "to the corresponding button.\n\nThank you!")
                    bot_socket.dm_user(int(self.user_id), message=message)
                # if member is not verified, do verification
                else:
                    Members.objects.filter(user_id=self.user_id).update(email=self.email, verified=True)
                    self.context['joined'] = True  # noqa
                    bot_socket.verify(self.user_id)
            # member object does not exist, so adding member
            else:
                name = self.user_json.get('username')
                tag = self.user_json.get('discriminator')
                # trys to add member to the database
                try:
                    data = Members(user_id=self.user_id,
                                   guild_id=settings.SERVER_ID,
                                   email=self.email,
                                   join_date=datetime.now(timezone.utc).isoformat(),
                                   verified=True,
                                   name=name,
                                   tag=tag,
                                   member=False
                                   )
                    data.save()
                    self.context['joined'] = False  # noqa
                # if exception occurs, shows internal server error
                except Exception as exp:
                    self.context["error"] = True # noqa
                    self.context['verified'] = False  # noqa
                    embed = {"title": "Internal Server Error",
                             "description": f"`{exp}`\n\n"
                                            f"Username: {name}\n"
                                            f"Tag: {tag}\n"
                                            f"email: ||{self.email}||",
                             "color": 0xff0000
                             }
                    # alerts staff using websockets
                    webhook.send_embed(embed)
        else:
            self.context['emailerror'] = True # noqa
        return render(request, self.template_name, self.context)


class VerificationView(ModelDataMixin, View):
    template_name = 'verification.html'
    context = {"Oauth": Oauth}

    def get(self, request):
        # status = request.GET.get('status')
        # self.context['emailerror'] = False  # noqa
        # self.context['verified'] = False  # noqa
        # self.context['notjoined'] = False  # noqa
        # self.context['error'] = False  # noqa
        # if status is not None:
        #     self.context[status] = True
        self.context['emailerror'] = False  # noqa
        self.context['verified'] = False  # noqa
        self.context['joined'] = True  # noqa
        self.context['error'] = False  # noqa
        self.get_blog_context()
        return render(request, self.template_name, self.context)


class DeveloperView(ModelDataMixin, View):
    model = Developers
    template_name = 'developers.html'

    def get(self, request):
        self.context['Members'] = self.model.objects.all().order_by('-perks')[:20]
        self.get_blog_context()
        return render(request, self.template_name, self.context)


class TemplateView(ModelDataMixin, View):
    template_name = 'privacy.html'

    def get(self, request):
        self.get_generic_context()
        return render(request, self.template_name, self.context)


class ContactView(ModelDataMixin, View):
    params = ('name', 'email', 'subject', 'othersub', 'username', 'tag',
              'infraction-type', 'date', 'reason', 'sponsor-type', 'issue',
              'server-name', 'server-topic', 'server-invite', 'message')
    template_name = "contact.html"

    def get(self, request):
        self.get_common_context()
        return render(request, self.template_name, self.context)

    def post(self, request):
        data = {}
        self.get_common_context()
        for param in self.params:
            try:
                value = request.POST[param]
                if value != '':
                    data[param] = value
            except Exception as exp:
                log_error(exp, "Item unavailable, Ignoring...")
        EmailHandler(recipient=data['email'], name=data['name'], subject=data['subject'], pre=True)
        bot_socket.send_contact_data(data)
        return render(request, self.template_name, self.context)
