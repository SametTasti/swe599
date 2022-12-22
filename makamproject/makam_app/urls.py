from django.urls import path
from . import views

app_name = 'makam_app'

urlpatterns = [
    path('', views.HomeView, name='HomeView'),
    path('create_piece/', views.CreatePieceView, name='CreatePieceView'),
    path('find_piece/', views.FindPieceView, name='FindPieceView'),
    path('query_results/', views.QueryResultsView, name='QueryResultsView'),
    path('analysis/', views.AnalysisView, name='AnalysisView'),
]
