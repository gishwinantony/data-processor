from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WellData
from .serializers import WellDataSerializer
import logging
logger = logging.getLogger(__name__)



class AnnualDataView(APIView):
    """
    API view to retrieve annual well data by API well number.

    Handles GET requests to retrieve annual well data based on the provided 'well' query parameter.
    
    Query Parameters:
        - well (str): The API well number for which the annual data is to be retrieved.
    
    Responses:
        - 200 OK: Returns the annual data if found.
        - 400 Bad Request: If the 'well' query parameter is not provided.
        - 404 Not Found: If no annual data is found for the provided API well number.

    Error Handling:
        - Returns an error message if the 'well' query parameter is missing.
        - Returns an error message if no data is found for the provided API well number.
        - Handles any other exceptions that may occur during data retrieval.
    """
    
    def get(self, request):
        # Retrieve the 'well' query parameter
        well = request.query_params.get('well', None)
        if not well:
            logger.warning({"error": "The 'well' query parameter is required."})
            return Response({"error": "The 'well' query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            annual_data = WellData.objects.filter(api_well_number=well).first()
            if annual_data is None:
                logger.error({"error": "No annual data found for the specified API well number."})
                return Response({"error": "No annual data found for the specified API well number."}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = WellDataSerializer(annual_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            logger.error({"error": f"An unexpected error occurred: {e}"})
            return Response({"error": f"An unexpected error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
