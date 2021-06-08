# recipes/urls.py
from django.urls import path

from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('', RecipeListView.as_view(), name='recipe_list'),
]
