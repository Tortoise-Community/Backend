
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Project, Event
from .serializers import ProjectSerializer, EventSerializer

from core.utils.mixins import ResponseMixin  # TODO: REFACTOR


class ProjectView(APIView, ResponseMixin):
    model = Project
    serializers = ProjectSerializer
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, slug=None):
        if slug is not None:
            queryset = get_object_or_404(self.model, slug=slug)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.all()
            serializer = self.serializers(queryset, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)


class EventView(APIView, ResponseMixin):
    model = Event
    serializers = EventSerializer
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, slug=None):
        if slug is not None:
            queryset = get_object_or_404(self.model, slug=slug)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.all()
            serializer = self.serializers(queryset, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
