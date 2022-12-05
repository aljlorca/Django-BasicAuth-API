from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .basic_auth import request_auth


#Creation of the view 
class Test(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        auth_response = request_auth(request)
        try:
            auth_response[0]
            return JsonResponse(auth_response,status=200,safe=False)
        except:
            if auth_response['message-error']=='You have to authenticate':
                return JsonResponse(auth_response,status=500,safe=False)
            else:
                return JsonResponse(auth_response,status=404,safe=False)
