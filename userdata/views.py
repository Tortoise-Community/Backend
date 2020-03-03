from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import Members
from .serializers import *
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def members(request):
    if request.method == 'POST':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = MemberSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201,safe=False)   
        else:
         return JsonResponse('{"response":"error"}')
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


def api():
    return render(request,'api.html')
