

from rest_framework import serializers


class GetGamesListSerializer(serializers.Serializer):
    key = serializers.CharField()


class SearchSerializer(serializers.Serializer):
    query = serializers.CharField()
