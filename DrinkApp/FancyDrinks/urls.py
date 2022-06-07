from django.urls import path
from . import views

app_name = 'FancyDrinks'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/detail', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    # # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:pk>/vote/', views.VoteView.as_view(), name='vote'),
    # path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    # path('admin_choice/', views.AdminChoiceView.as_view(), name='admin_choice'),
    path('add_drink/', views.AddDrinkView.as_view(), name='add_drink'),

]
