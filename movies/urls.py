
from django.urls import path
from . import views

# movies
urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.details, name='movies_details')
]
