from django.http import JsonResponse, HttpResponse


class ResponseMixin(object):

    @staticmethod
    def json_response_204():
        return JsonResponse({"response": "Not Content"}, status=204)

    @staticmethod
    def json_response_400():
        return JsonResponse({"response": "Bad Request"}, status=400)

    @staticmethod
    def json_response_401():
        return JsonResponse({"response": "Unauthorized"}, status=401)

    @staticmethod
    def json_response_404():
        return JsonResponse({"response": "Not Found"}, status=404)

    @staticmethod
    def json_response_405():
        return JsonResponse({"response": "Method Not Allowed"}, status=405)

    @staticmethod
    def json_response_500():
        return JsonResponse({"response": "Internal Server Error"}, status=500)

    @staticmethod
    def json_response_501():
        return JsonResponse({"response": "Not Implemented"}, status=501)

    @staticmethod
    def json_response_502():
        return JsonResponse({"response": "Bad Gateway"}, status=502)

    @staticmethod
    def json_response_503():
        return JsonResponse({"response": "Internal Server Error"}, status=503)

    @staticmethod
    def json_response_504():
        return JsonResponse({"response": "Gateway Timeout"}, status=504)
