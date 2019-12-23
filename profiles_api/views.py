from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Use HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'hello!','an_apiview':an_apiview})
        
