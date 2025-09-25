from django.urls import path
from . import views


urlpatterns = [
    path('', views.quiz_home ),
    path('quiz/',views.quiz_view),
    path('result/', views.result_view,name='result' ),
]