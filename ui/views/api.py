
import time
import uuid

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from asgiref.sync import async_to_sync

from ..models import Gameslist
from ..serializers import GetGamesListSerializer, SearchSerializer

from AgentService.connector import AgentConnector
from AgentService.connector.types import AgentResponse


class GamesListView(APIView):

    def get(self, request: Request):
        serializer = GetGamesListSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        time.sleep(1)

        try:
            games_list = Gameslist.objects.get(key=data['key'].lower())
            games = games_list.games.values()

        except Exception as err:
            games = []

        return Response({
            "games": list(games),
        }, status=status.HTTP_200_OK)


class SearchView(APIView):
    def get(self, request):
        serializer = SearchSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        agent = AgentConnector(endpoint="https://bots.innova.ua/agents/agent59")
        answer: AgentResponse = async_to_sync(agent.send)(
            chat_id=uuid.uuid4().hex,
            text=data["query"]
        )
        tags = answer.content.replace(" ", "").split(",")

        return Response({
            "tags": tags,
        }, status=status.HTTP_200_OK)
