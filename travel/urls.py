from django.urls import path

from . import views


app_name = 'travel'
urlpatterns = [
    # example /polls/
    path('', views.index, name='index'),
    #/polls/5/
    path('<int:destination_id>', views.detail, name='detail'),
    #/polls/3/results/
    path('<int:destination_id>/dates/', views.dates, name='dates'),
    #/polls/3/results/final/
    path('<int:destination_id>/dates/final/', views.final, name='final'),



]