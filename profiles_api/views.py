from rest_framework.views import APIView
from rest_framework.response import Response


class APIProject(APIView):

    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP methods as function (Get, Put, Post, Pacth, Delete)',
        'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!!', 'an_apiview': an_apiview})
