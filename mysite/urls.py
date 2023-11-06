from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


#direct, simple way
def home(request):
    return HttpResponse('Hello Word!')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls'), name='index'),
    # path('apps/', include('apps.urls'), name ='given_name'),
    # path('apps/', def_view, name='given_name'),
    path('', home),
]
