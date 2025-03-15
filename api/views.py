from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def health_check(request):
    return Response({'Status': 'Working'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def hello_world(request):
    return Response({'Message': 'Hello world!'}, status=status.HTTP_200_OK)

