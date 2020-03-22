from django.shortcuts import render , HttpResponse,redirect
from websitedata.models import *
from .oauth import Oauth
from userdata.models import *
from .discord_handler import SocketSend





# Create your views here.


def get_event(request, item_name):
    E = Events.get(pk = item_name)
    return render(request, 'event.html', {'E':E,'Team':Team})

def get_project(request,item_name):
    Project = Projects.get(pk = item_name)
    return render(request,'project.html',{'Project':Project,'Team':Team})   
    
Slides = Slider.objects.all()
News = News.objects.all()
Team = Team.objects.all()
Upcoming = Events.objects.filter(status='Upcoming')
RecEvents = Events.objects.filter(status='Ended').order_by('enddate')[:3]
LiveEvents = Events.objects.filter(status='Live')
Events = Events.objects.filter(status__in=['Live','Ended'])
Projects = Projects.objects.all()
Memberx = Members.objects.all().order_by('perks')[:10]
Privacy = Privacy.objects.all()
Changes = Changes.objects.all()



def index(request):
    return render(request,"index.html",{'Slides':Slides,'News':News,'Team':Team,'Upcoming':Upcoming,'RecEvents':RecEvents,'Projects':Projects,'LiveEvents':LiveEvents})

def projects(request):
    return render(request,"projects.html",{'Team':Team,"Projects" : Projects})    

def events(request):
    return render(request,"events.html",{'Events':Events,'Team':Team,'Upcoming':Upcoming})        
    
def verify(request):
    return render(request,"verification.html",{'Oauth':Oauth})        

def contact(request):
    return render(request,"contact.html",{'Team':Team})     


def event(request):
    return render(request,"event.html",{'Team':Team})      


def vamp(request):
    return render(request,"event.html",{"E":E,'Team':Team})                

def verified(request):
    code = request.GET.get("code")
    access_token = Oauth.get_access_token(code)
    user_json = Oauth.get_user_json(access_token)
    id = user_json.get("id")  
    email = user_json.get("email")
    if email:   
        Verified = True
        Members.objects.filter(user_id = id).update(email=email,verified=True)
        package = {"Verify":id}
        SocketSend(package)
    if id is None :
        return render(request,"verification.html",{'Oauth':Oauth})
    else :  
        return render(request,"verification.html",{'Verified':Verified})  

def members(request):
    return render(request,"members.html",{'Team':Team,'Members':Memberx})    

def credits(request):
    return render(request,"credits.html")    

def privacypolicy(request):
    return render(request,"privacy.html",{'Privacy':Privacy,'Change':Changes,'Team':Team})     

#UNDER DEVELOPMENT
def announcements(request):
    return render(request,"announcements.html",{'Team':Team})       

def rules(request):
    return render(request,"rules.html",{'Team':Team})

def staff(request):
    pass

def privacy(request):
    pass

