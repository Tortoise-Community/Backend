from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
# Create your views here.



@csrf_exempt
@api_view(['GET'])
@permission_classes([])
def ping(request):
	return JsonResponse({"status":200},status=200,safe=False)
   

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def members(request):
    if request.method == 'POST':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = MemberPostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201,safe=False)   
        else:
         return JsonResponse('{"response":500}')
    elif request.method == 'GET':
        queryset = Members.objects.all()
        serializer = AllSerializer(queryset,many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['PUT','DELETE','GET'])
@permission_classes((IsAuthenticated, ))
def members_edit(request,id):
    queryset = get_object_or_404(Members,user_id = id)

    if request.method == 'GET':
        serializer = AllSerializer(queryset)
        return JsonResponse (serializer.data,safe=False)

    elif request.method == 'PUT':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = AllSerializer(queryset,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)   
        else:
         return JsonResponse(serializer.errors,status =400)

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status=204)     

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def projects(request):
    if request.method == 'POST':
         return JsonResponse(serializer.error,status=405)
    elif request.method == 'GET':
        queryset = Projects.objects.all()
        serializer = GithubSerializer(queryset,many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['PUT','GET'])
@permission_classes((IsAuthenticated, ))
def projects_edit(request,pk):
    queryset = get_object_or_404(Projects,pk = pk)
    if request.method == "GET":
        serializer = ProjectSerializer(queryset)
        return JsonResponse (serializer.data,safe=False)
    elif request.method == "PUT":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = ProjectSerializer(queryset,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)   
        else:
         return JsonResponse(serializer.errors,status =400)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def is_verified(request,id):
    queryset = get_object_or_404(Members,user_id = id)
    serializer = VerificationSerializer(queryset)
    return JsonResponse (serializer.data,safe=False)
    
@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_top_members(request):
    queryset  = Members.objects.all().order_by('perks')[:10]
    serializer = TopSerializer(queryset,many=True)
    return JsonResponse(serializer.data,safe=False)
        


@csrf_exempt
@api_view(['PUT','GET'])
@permission_classes((IsAuthenticated, ))
def get_member_roles(request,id):
    queryset = get_object_or_404(Members,user_id = id)
    if request.method == 'GET':
        serializer = MemberRoleSerializer(queryset)
        return JsonResponse (serializer.data,safe=False)
    elif request.method == 'PUT':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = MemberRoleSerializer(queryset,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)   
        else:
         return JsonResponse(serializer.errors,status =400)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_rules(request):
    queryset  = Rules.objects.all()
    serializer = RulesSerializer(queryset,many=True)
    return JsonResponse(serializer.data,safe=False)   
    
    
@csrf_exempt
@api_view(['PUT','GET'])
@permission_classes((IsAuthenticated, ))
def bot_status(request,id):
	queryset = get_object_or_404(ServerUtils,guild_id = id)
   if request.method == 'GET':
   	serializer = StatusSerializer(queryset)
   	return JsonResponse(serializer.data,safe=False)
   elif request.method == 'PUT':
   	json_parser = JSONParser()
   	data = json_parser.parse(request)
   	serializer = StatusSerializer(queryset,data=data)
   	if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)   
        else:
         return JsonResponse(serializer.errors,status =400)	
         
@csrf_exempt
@api_view(['PUT','GET'])
@permission_classes((IsAuthenticated, ))
def get_services(request,id):
	queryset = get_object_or_404(ServerUtils,guild_id = id)
   if request.method == 'GET':
   	serializer = ServiceSerializer(queryset)
   	return JsonResponse(serializer.data,safe=False)
   elif request.method == 'PUT':
   	json_parser = JSONParser()
   	data = json_parser.parse(request)
   	serializer = ServiceSerializer(queryset,data=data)
   	if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)   
        else:
         return JsonResponse(serializer.errors,status =400)        
         
	
	
	
	
	    
    
          