from django.shortcuts import render
from websitedata.models import *
from utils.oauth import Oauth
from userdata.models import *
from .discord_handler import SocketSend
from .models import SiteUrls
from django.views import View


class UtilityMixin(object):
    context = {}
    siteurls = SiteUrls # noqa
    news = News.objects.all()
    team = Team.objects.all()
    slider = Slider.objects.all()
    events = Events.objects.all()
    privacy = Privacy.objects.all()
    changes = Changes.objects.all()
    rules = Rules.objects.all().order_by('number')[1:]


    def get_main_context(self):
        self.context['slides'] = self.slider
        self.get_common_context()
        self.get_category_events()
        return self.context

    def get_events_context(self):
        self.context['events'] = self.events.filter(status__in=['Live', 'Ended']).order_by('-id')
        self.get_upcoming_context()
        self.get_common_context()
        return self.context

    def get_upcoming_context(self):
        self.context['upcoming'] = self.events.filter(status='Upcoming')[:2]
        return self.context


    def get_category_events(self):
        self.context['levents'] = self.events.filter(status='Live')[:2] # noqa
        self.context['revents'] = self.events.filter(status='Ended')[:3] # noqa
        self.get_upcoming_context()
        return self.context

    def get_common_context(self):
        self.context["team"] = self.team
        self.context["siteurls"] = self.siteurls # noqa
        self.context["news"] = self.news
        return self.context

    def get_blog_context(self):
        self.context["siteurls"] = self.siteurls  # noqa
        return  self.context

    def get_generic_context(self):
        self.context["privacy"] = self.privacy
        self.context['rules'] = self.rules
        self.context['changes'] = self.changes
        self.get_blog_context()



class ProjectView(UtilityMixin, View):
    model = Projects
    template_name = 'projects.html'
    context = {}
    def get(self, request, id=None):

        if id is not None:
            self.context = self.get_blog_context()
            self.template_name = 'project.html'
            project = self.model.objects.get(pk=id)
            self.context['project'] = project
        else:
            self.context = self.get_common_context()
            self.context['projects'] = self.model.objects.all().order_by('id')

        return render(request, self.template_name, self.context)


class EventView(UtilityMixin, View):
    model = Events
    template_name = 'events.html'
    context = {}
    def get(self, request, id=None):

        if id is not None:
            self.context = self.get_blog_context()
            self.template_name = 'event.html'
            project = self.model.objects.get(pk=id)
            self.context['event'] = project
        else:
            self.get_events_context()

        return render(request, self.template_name, self.context)


class IndexView(UtilityMixin, View):
    template_name = 'index.html'
    context = {}
    def get(self, request):
        self.get_main_context()
        return render(request, self.template_name, self.context)


class VerificationView(UtilityMixin, View):

    verified = False
    template_name = 'verification.html'
    context = {"Oauth":Oauth}

    def get(self, request):
        code = request.GET.get('code')
        access_token = Oauth.get_access_token(code)
        user_json = Oauth.get_user_json(access_token)
        id = user_json.get('id')
        email = user_json.get('email')
        self.get_blog_context()
        if email is not None:
            self.context['verified'] = True
        if id is None:
            self.context['emailerror'] = False # noqa
            self.context['verified'] = False
        elif email is None:
            self.context['emailerror'] = True # noqa
            self.context['verified'] = False
        else:
            self.context['emailerror'] = False # noqa
            self.context['verified'] = False
        return render(request, self.template_name, self.context)


class DeveloperView(UtilityMixin, View):
    template_name = 'developers.html'
    model = Developers
    def get(self, request):
        self.context['Members'] = self.model.objects.all().order_by('-perks')[:20]
        self.get_blog_context()
        return render(request, self.template_name, self.context)


class TemplateView(UtilityMixin, View):
    template_name = 'privacy.html'
    def get(self, request):
        self.get_generic_context()
        return render(request, self.template_name, self.context)




