"""URL Routing for the API Backend."""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from polls import views

api_router = routers.DefaultRouter()
api_router.register(r'polls', views.PollView, "polls")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/polls/<int:poll_id>/question_result/", views.question_result_list),
    path("api/", include(api_router.urls))
]
