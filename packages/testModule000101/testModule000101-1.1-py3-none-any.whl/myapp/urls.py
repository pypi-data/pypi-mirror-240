# myapp/urls.py
from django.urls import include, path

urlpatterns = [
    path('api/', include('myapp.api.urls')),
    # other paths...
]
