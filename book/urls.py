from django.urls import path
from .views import SuperVillain


urlpatterns = [
    path('hello-su/<str:name>/', SuperVillain.as_view()),
    path('hello-su/', SuperVillain.as_view()),
]
