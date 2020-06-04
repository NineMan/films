from django.urls import path
# from .views import FilmView
# from .views import SingleFilmView
from .views import FilmView, GhibliFilmView


app_name = 'filmtitle'

urlpatterns = [
    # path('film/', SingleFilmView.as_view()),
    # path('film/<int:pk>', SingleFilmView.as_view()),
    # path('film/<int:origid>', SingleFilmView.as_view()),
    # path('film/<int:pk>', FilmView.as_view()),
    path('film/<uuid:uuid>', GhibliFilmView.as_view()),
    path('film/<str>', FilmView.as_view()),
]
