from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Paste
from .serializers import PasteSerializer
from core.utils.slug_generator import SlugGenerator
from core.utils.mixins import ResponseMixin  # TODO: REFACTOR


class PasteView(APIView, ResponseMixin):
    model = Paste
    serializers = PasteSerializer
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, slug=None):
        if slug is not None:
            queryset = get_object_or_404(self.model, slug=slug)
            serializer = self.serializers(queryset)
            return Response(serializer.data, status=200)
        else:
            return self.json_response_404()

    def post(self, request):
        data = request.data
        data["slug"] = SlugGenerator.generate()
        serializer = self.serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return self.json_response_400()
