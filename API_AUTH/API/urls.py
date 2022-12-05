from .views import Test
from django.urls import path


urlpatterns = [
    #url of the api http://127.0.0.1:8000/API/test/
    path('test/',Test.as_view(),name='test'),
    
]
