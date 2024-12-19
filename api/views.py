from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import SecretKeyAuthentication
from rest_framework.permissions import IsAuthenticated

class ZohoCreateChildAccount(APIView):
    authentication_classes = [SecretKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Handle creating the account
        return Response({"message": "Child account created"}, status=status.HTTP_201_CREATED)

class ZohoUpdateCustomer(APIView):
    def post(self, request, *args, **kwargs):
        # Handle updating the customer
        return Response({"message": "Customer updated"}, status=status.HTTP_200_OK)

class ZohoUpdateInvoice(APIView):
    def post(self, request, *args, **kwargs):
        # Handle updating the invoice
        return Response({"message": "Invoice updated"}, status=status.HTTP_200_OK)

class ZohoUpdateProducts(APIView):
    def post(self, request, *args, **kwargs):
        # Handle updating the products
        return Response({"message": "Products updated"}, status=status.HTTP_200_OK)
