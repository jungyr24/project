from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # ''는 아무것도 없는 것을 의미함 즉 localhost:8000 여기를 의미함
    path('', views.main_page, name='main_page'),

    path('prob-num/', views.get_prob_number, name='get_prob_number'),

    path('tab-page/', views.tab_page, name='tab_page'),



]