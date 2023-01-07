from django.urls import path, include
from . import views

app_name = 'makam_app'

urlpatterns = [
    path('', views.HomeView, name='HomeView'),
    path('create_piece/', views.CreatePieceView, name='CreatePieceView'),
    path('find_piece/', views.FindPieceView, name='FindPieceView'),
    path('query_results/', views.QueryResultsView, name='QueryResultsView'),
    path('analysis/', views.AnalysisView, name='AnalysisView'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.UserPieceView.as_view(), name='profile'),
    path('edit/<int:pk>', views.EditPieceView, name='EditPieceView'),
]
