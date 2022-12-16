from django.urls import path
from . import views

app_name = 'makam_app'

urlpatterns = [
    path('', views.HomeView, name='HomeView'),
    # path('first_data_entry/', views.FirstDataEntryView, name='FirstDataEntryView'),
    # path('makam_list/', MakamListView.as_view(), name='MakamDataEntryView'),
    path('create_piece/', views.CreatePieceView, name='CreatePieceView'),
]
