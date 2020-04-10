from . import settings ,views 
from django.shortcuts import render , HttpResponse,redirect
from django.core.mail import send_mail
from .discord_handler import SocketSend
from .models import SiteUrls

def send_data(**payload):
    package = {"endpoint":"contact","data":payload}
    SocketSend(package)
    



#Contact data
def contact(request,method=['GET','POST']):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST['email']
        subject = request.POST['subject']
        other = request.POST['othersub']
        username = request.POST['username']
        tag = request.POST['tag']
        infraction_type = request.POST.get('infraction-type','None')
        date = request.POST['date']
        reason = request.POST['reason']
        sponsor_type = request.POST.get('sponsor-type','None')
        issue = request.POST['issue']
        server_name = request.POST['server-name']
        server_topic = request.POST['server-topic']
        server_invite = request.POST['server-invite']
        message = request.POST['message']
        try: 
         msg = get_message(name,subject)
         send_mail(subject, msg, 'Tortoise Community <tortoisecommunity@gmail.com>', ['{}'.format(email)])

        except:
         pass
        try: 
          send_data(name=name,email=email,subject=subject,other=other,username=username,tag=tag,infraction_type=infraction_type,date=date,reason=reason,sponsor_type=sponsor_type,issue=issue,server_name=server_name,server_topic=server_topic,server_invite=server_invite,message=message)
        except:
            pass    
        H =True
        return render(request,"contact.html",{'Team':views.Team,'H':H,'siteurls':SiteUrls})
    else:
        return render(request,"contact.html",{'Team':views.Team,'siteurls':SiteUrls})    




def get_message(name,subject):
    if subject == "Appeal-Infraction":
        content = "Your infraction appeal is received\nOur staff will go through it soon.\nWe'll notify you here within 3 days with the updates so make sure you check your mail frequently"
    elif subject == 'Partnership':
        content = "Thank you for showing interest to partner up with our server.\nWe will look into the details and have one of our staff sent over. Hope you have read the partnering policies and terms.\nYou can always reveiew them here:"
    elif subject == "Sponsorship":
        content = "Thank you for showing your interest in sponsoring us, We'll review the details and contact you here to discuss the sponsorship terms and policies withing 2-3 days." 
    elif subject == 'Report-User':
        content = "Thank you for reporting the user.\nNote that we take all reports seriously,The user could even be banned from the community if the graveness of the act demands him/her to be.\nSo we won't be tolerating attempts to frame someone or fake reports.So please don't indulge in such activites or you could face consequences."           
    elif subject == 'Issue-Report':
        content = "Thank you for taking the time to report the issue.\nWe'll look into it soon and solve the matter."
    else :
       content = "Thank you for contacting us.\nWe will review the details submitted below and reach you here.So make sure you check your emails frequently"  

    message = "Hi "+name+"!\n\n"+content+"\n\nTortoise Community"
    return message