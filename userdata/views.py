from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.mixins import ResponseMixin
from django.conf import settings
from .models import Member, Projects, Rules, Guild, Suggestions, User
from .serializers import (MemberDataSerializer, SuggestionSerializer, TopMemberSerializer, MemberSerializer,
                          SuggestionPutSerializer, ProjectStatsSerializer, RuleSerializer, GuildDataSerializer,
                          GuildMetaSerializer, UserDataSerializer)


class MemberDataView(APIView, ResponseMixin):
    model = Member
    serializers = MemberDataSerializer

    def get(self, request, user_id=None, guild_id=None):
        print(guild_id)
        if guild_id is not None:
            queryset = get_object_or_404(self.model, user__id=user_id, guild__id=guild_id)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.all()
            serializer = self.serializers(queryset, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request, user_id=None):
        # BUG: post does work
        if user_id is not None:
            return self.json_response_405()
        else:
            serializer = MemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return self.json_response_400()

    def put(self, request, user_id=None, guild_id=None):
        if user_id is not None:
            queryset = get_object_or_404(self.model, user__id=user_id, guild__id=guild_id)
            serializer = self.serializers(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return self.json_response_500()
        else:
            return self.json_response_405()

    def delete(self, request, user_id=None, guild_id=None):
        if user_id is not None:
            queryset = get_object_or_404(self.model, user__id=user_id, guild__id=guild_id)
            queryset.delete()
            return self.json_response_204()
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
    serializers = RuleSerializer

    def get(self, request, guild_id):
        queryset = self.model.objects.filter(guild__id=guild_id).order_by("number")
        if not queryset:
            return self.json_response_404()
        serializer = self.serializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class SuggestionDataView(APIView, ResponseMixin):
    model = Suggestions
    serializers = SuggestionSerializer

    def get(self, request, item_id=None, guild_id=None):
        if item_id is not None:
            queryset = get_object_or_404(self.model, message_id=item_id)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.filter(guild__id=guild_id, status="Under Review")
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
            return self.json_response_400()

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


class GuildDataView(APIView, ResponseMixin):
    model = Guild
    serializers = GuildDataSerializer

    def get(self, request, guild_id=None):
        if guild_id is not None:
            queryset = get_object_or_404(self.model, id=guild_id)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.all()
            serializer = self.serializers(queryset, many=True)
            return Response(serializer.data, status=200)

    def post(self, request, guild_id=None):
        if guild_id is not None:
            return self.json_response_405()
        else:
            serializer = self.serializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return self.json_response_400()

    def put(self, request, guild_id):
        queryset = get_object_or_404(self.model, id=guild_id)
        serializer = GuildMetaSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return self.json_response_500()


class UserDataView(APIView, ResponseMixin):
    model = User
    serializers = UserDataSerializer

    def get(self, request, user_id=None):
        if user_id is not None:
            queryset = get_object_or_404(self.model, id=user_id)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            queryset = self.model.objects.filter(member=True).order_by('-perks')[:20]
            serializer = TopMemberSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request, user_id=None):
        if user_id is not None:
            return self.json_response_405()
        else:
            serializer = self.serializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return self.json_response_400()

    def put(self, request, user_id=None):
        if user_id is not None:
            queryset = get_object_or_404(self.model, id=user_id)
            serializer = self.serializers(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return self.json_response_500()

    def delete(self, request, user_id=None):
        if user_id is not None:
            queryset = get_object_or_404(self.model, id=user_id)
            if request.data.get("confirmation_key") == settings.DELETION_CONFIRMATION_KEY:
                queryset.delete()
                return self.json_response_204()
            else:
                return self.json_response_401()
        else:
            return self.json_response_405()




