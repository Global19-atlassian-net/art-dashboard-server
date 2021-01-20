from rest_framework import generics
from .serializer import BuildSerializer
from rest_framework.response import Response
import json
from .request_dispatcher import handle_build_post_request

# Create your views here.


class BuildView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):

        post_data = dict()

        if isinstance(request.data, dict):
            post_data = request.data
        elif isinstance(request.data, str):

            if request.data == "":
                post_data = {}
            else:
                try:
                    post_data = json.loads(request.data)
                except ValueError as e:
                    return Response(
                        data={"status": "error", "message": "Invalid request format.", "data": [], "error": str(e)})
        response = handle_build_post_request(post_data)

        return Response(data=response)
