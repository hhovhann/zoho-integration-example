# zoho_integration/middleware.py

from django.http import JsonResponse


class SignatureVerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        expected_signature = "some-secret-key-would-be-from-vault"
        provided_signature = request.headers.get("X-Signature")
        if provided_signature != expected_signature:
            return JsonResponse({"error": "Invalid signature"}, status=403)

        response = self.get_response(request)
        return response
