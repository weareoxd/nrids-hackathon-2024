from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheck(APIView):
    """
    Returns 200 OK response code
    """

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK, data={"status": "OK"})
