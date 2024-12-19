# zoho_integration/api/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Middleware function to verify the signature
def verify_signature(request):
    expected_signature = "some-secret-key-would-be-from-vault"  # Replace with actual secure key
    provided_signature = request.headers.get("X-Signature")
    if provided_signature != expected_signature:
        return JsonResponse({"error": "Invalid signature"}, status=403)
    return None  # Signature is valid


@csrf_exempt  # Disable CSRF check for these API endpoints (ensure to handle this securely in production)
def create_child_account(request):
    signature_check = verify_signature(request)
    if signature_check:
        return signature_check  # Return error response if signature is invalid

    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            # Process the payload and create the child account
            return JsonResponse({"message": "Child account created successfully!"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


@csrf_exempt
def update_customer(request):
    signature_check = verify_signature(request)
    if signature_check:
        return signature_check

    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            # Handle updating customer logic here
            return JsonResponse({"message": "Customer updated successfully!"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


@csrf_exempt
def update_invoice(request):
    signature_check = verify_signature(request)
    if signature_check:
        return signature_check

    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            # Handle updating invoice logic here
            return JsonResponse({"message": "Invoice updated successfully!"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


@csrf_exempt
def update_products(request):
    signature_check = verify_signature(request)
    if signature_check:
        return signature_check

    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            # Handle updating products logic here
            return JsonResponse({"message": "Products updated successfully!"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)
