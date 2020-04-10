from django.shortcuts import render , HttpResponse,redirect
from websitedata.models import *
from .oauth import Oauth
from userdata.models import *
from .discord_handler import SocketSend
from .models import SiteUrls




# Create your views here.


def get_event(request, item_name):
    E = Events.get(pk = item_name)
    return render(request, 'event.html', {'E':E,'Team':Team,'siteurls':SiteUrls})

def get_project(request,item_name):
    Project = Projects.get(pk = item_name)
    return render(request,'project.html',{'Project':Project,'Team':Team,'siteurls':SiteUrls})   
    
Slides = Slider.objects.all()
News = News.objects.all()
Team = Team.objects.all()
Upcoming = Events.objects.filter(status='Upcoming')
RecEvents = Events.objects.filter(status='Ended').order_by('enddate')[:3]
LiveEvents = Events.objects.filter(status='Live')
Events = Events.objects.filter(status__in=['Live','Ended'])
Projects = Projects.objects.all().order_by('id')
Memberx = Members.objects.all().order_by('-perks')[:20]
Privacy = Privacy.objects.all()
Changes = Changes.objects.all()
Rules = Rules.objects.all().order_by('number')[1:]



def index(request):
    return render(request,"index.html",{'Slides':Slides,'News':News,'Team':Team,'Upcoming':Upcoming,'RecEvents':RecEvents,'Projects':Projects,'LiveEvents':LiveEvents,'siteurls':SiteUrls})

def projects(request):
    return render(request,"projects.html",{'Team':Team,"Projects" : Projects,'siteurls':SiteUrls})    

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
    return render(request,"members.html",{'Team':Team,'Members':Memberx,'siteurls':SiteUrls})    

def credits(request):
    return render(request,"credits.html")    

def privacypolicy(request):
    return render(request,"privacy.html",{'Privacy':Privacy,'Change':Changes,'Team':Team,'siteurls':SiteUrls})           

def rules(request):
    return render(request,"rules.html",{'Rules':Rules,'Team':Team,'siteurls':SiteUrls})


