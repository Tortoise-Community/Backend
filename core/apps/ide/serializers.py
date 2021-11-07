from rest_framework import serializers
from core.apps.ide.models import Paste


class PasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        exclude = ("creation_time",)
