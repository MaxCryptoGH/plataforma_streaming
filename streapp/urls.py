from django.urls import path
from streapp import views
from streapp.views import inicio, peliculas, series, documentales, buscar, form_series, form_peliculas, form_documentales, buscar_serie


urlpatterns = [
    
    path ('', views.inicio, name="inicio"), 
    
    # urls de Peliculas
    path ('peliculas/', views.peliculas, name="peliculas"), 
    path ('form_peliculas/', views.form_peliculas,  name="form_peliculas"), 
    path ('buscar_pelicula/', views.buscar_pelicula,  name="buscar_pelicula"),
    path ('buscar_p/', views.buscar_p, name="buscar_p"), 

    # urls de Series
    path ('series/', views.series,  name="series"), 
    path ('form_series/', views.form_series,  name="form_series"),
    path ('buscar_serie/', views.buscar_serie,  name="buscar_serie"),
    path ('buscar/', views.buscar, name="buscar"), 

    # urls de Documentales
    path ('documentales/', views.documentales,  name="documentales"), 
    path ('form_documentales/', views.form_documentales,  name="form_documentales"), 
    path ('buscar_documentales/', views.buscar_documentales,  name="buscar_documentales"),
    path ('buscar_d/', views.buscar_d, name="buscar_d"), 
    # Otras urls
    
]