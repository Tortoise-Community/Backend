from django.shortcuts import render
from websitedata.models import *
from utils.oauth import Oauth
from userdata.models import *
from .discord_handler import SocketSend
from .models import SiteUrls
from django.views import View


class UtilityMixin(object):
    context = {}
    news = News.objects.all()
    team = Team.objects.all()
    privacy = Privacy.objects.all()
    siteurls = SiteUrls
    changes = Changes.objects.all()
    rules = Rules.objects.all().order_by('number')[1:]

    def get_common_context(self):
        self.context["team"] = self.team
        self.context["siteurls"] = self.siteurls
        self.context["news"] = self.news
        return self.context

    def get_blog_context(self):
        self.context["siteurls"] = self.siteurls



class ProjectView(UtilityMixin, View):
    model = Projects
    template_name = 'projects.html'
    context = {}
    def get(self, request, id=None):

        if id is not None:
            self.context = get_blog_context()
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
            self.context = get_blog_context()
            self.template_name = 'event.html'
            project = self.model.objects.get(pk=id)
            self.context['event'] = project
        else:
            self.context = self.get_common_context()
            self.context['events'] = self.model.objects.all().order_by('id')

        return render(request, self.template_name, self.context)




def get_event(request, item_name):
    E = Events.get(pk = item_name)
    return render(request, 'event.html', {'E':E,'Team':Team,'siteurls':SiteUrls})



Slides = Slider.objects.all()
News = News.objects.all()
Team = Team.objects.all()
Upcoming = Events.objects.filter(status='Upcoming')
RecEvents = Events.objects.filter(status='Ended').order_by('enddate')[:3]
LiveEvents = Events.objects.filter(status='Live')
Events = Events.objects.filter(status__in=['Live', 'Ended'])
Projects = Projects.objects.all().order_by('id')
Privacy = Privacy.objects.all()
Changes = Changes.objects.all()
Rules = Rules.objects.all().order_by('number')[1:]



def index(request):
    return render(request,"index.html",{'Slides':Slides,'News':News,'Team':Team,'Upcoming':Upcoming,'RecEvents':RecEvents,'Projects':Projects,'LiveEvents':LiveEvents,'siteurls':SiteUrls})

def events(request):
    return render(request,"events.html",{'Events':Events,'Team':Team,'Upcoming':Upcoming,'siteurls':SiteUrls})


def verified(request):
    code = request.GET.get("code")
    access_token = Oauth.get_access_token(code)
    user_json = Oauth.get_user_json(access_token)
    id = user_json.get("id")
    email = user_json.get("email")
    if email:
        Verified = True
        try:
           Members.objects.filter(user_id = id).update(email=email,verified=True)
           package = {"endpoint":"verify","data":id}
           SocketSend(package)
        except:
            pass
    if code is None :
        emailerror = False
        return render(request,"verification.html",{'Oauth':Oauth,'emailerror':emailerror,'siteurls':SiteUrls})
    elif email is None:
        emailerror = True
        return render(request,"verification.html",{'Oauth':Oauth,'emailerror':emailerror,'siteurls':SiteUrls})
    else :
        return render(request,"verification.html",{'Verified':Verified,'siteurls':SiteUrls})

def members(request):
    Developerx = Developers.objects.all().order_by('-perks')[:20]
    return render(request,"members.html",{'Team':Team,'Members':Developerx,'siteurls':SiteUrls})

def credits(request):
    return render(request,"credits.html")

def privacypolicy(request):
    return render(request,"privacy.html",{'Privacy':Privacy,'Change':Changes,'Team':Team,'siteurls':SiteUrls})

def rules(request):
    return render(request,"rules.html",{'Rules':Rules,'Team':Team,'siteurls':SiteUrls})





