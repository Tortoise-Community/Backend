from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.mixins import ResponseMixin
from .models import Members, Projects, Rules, ServerUtils, Developers, Suggestions
from .serializers import (MemberDataSerializer, DeveloperSerializer, SuggestionSerializer, TopMemberSerializer,
                          SuggestionPutSerializer, ProjectStatsSerializer, RulesSerializer, ServerMetaSerializer)


class MemberDataView(APIView, ResponseMixin):
    model = Members
    serializers = MemberDataSerializer

    def get(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, user_id=item_id)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.all()
            serializer = self.serializers(queryset, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request, item_id=None):
        if item_id is not None:
            return self.json_response_405()
        else:
            serializer = self.serializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return self.json_response_500()

    def put(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, user_id=item_id)
            serializer = self.serializers(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return self.json_response_500()
        else:
            return self.json_response_405()

    def delete(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, user_id=item_id)
            queryset.delete()
            return self.json_response_204()
        else:
            return self.json_response_405()


class DynamicMemberView(APIView, ResponseMixin):
    model = Members
    serializers = None

    def get(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, user_id=item_id)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.filter(member=True).order_by('-perks')[:20]
            serializer = TopMemberSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

    def put(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, user_id=item_id)
            serializer = self.serializers(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return self.json_response_500()


class SuggestionDataView(APIView, ResponseMixin):
    model = Suggestions
    serializers = SuggestionSerializer

    def get(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, message_id=item_id)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.filter(status="Under Review")
            serializer = self.serializers(queryset, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request, item_id=None):
        if item_id is not None:
            return self.json_response_405()
        else:
            serializer = self.serializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return self.json_response_500()

    def put(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, message_id=item_id)
            serializer = SuggestionPutSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return self.json_response_500()
        else:
            return self.json_response_405()

    def delete(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, message_id=item_id)
            if queryset:
                queryset.delete()
                return self.json_response_204()
            return self.json_response_400()
        else:
            return self.json_response_405()


class ProjectStatsView(APIView, ResponseMixin):
    model = Projects
    serializers = ProjectStatsSerializer

    def get(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, pk=item_id)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.all()
            serializer = self.serializers(queryset, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

    def put(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, pk=item_id)
            serializer = self.serializers(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return self.json_response_500()
        else:
            return self.json_response_405()


class RulesDataView(APIView, ResponseMixin):
    model = Rules
    serializers = RulesSerializer

    def get(self, request):
        queryset = self.model.objects.all().order_by('number')
        serializer = self.serializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class DeveloperDataView(APIView, ResponseMixin):
    model = Developers
    serializers = DeveloperSerializer

    def get(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, no=item_id)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.all()
            serializer = self.serializers(queryset, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

    def put(self, request, item_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, no=item_id)
            serializer = self.serializers(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return self.json_response_500()
        else:
            return self.json_response_405()


class ServerMetaView(APIView, ResponseMixin):
    model = ServerUtils
    serializers = ServerMetaSerializer

    def get(self, request, item_id):
        queryset = get_object_or_404(self.model, guild_id=item_id)
        serializer = self.serializers(queryset)
        return Response(serializer.data, status=200)

    def put(self, request, item_id):
        queryset = get_object_or_404(self.model, guild_id=item_id)
        serializer = self.serializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return self.json_response_500()
