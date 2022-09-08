from django import forms

# Lista de generos para películas, series y documentales -----------------
genero= [
    ('Fantasía', 'Fantasía'),
    ('Misterio', 'Misterio'),
    ('Acción', 'Acción'),
    ('Infantil', 'Infantil'),
    ('Comedia', 'Comedia'),
    ('Historia', 'Historia'),
    ('Ciencia', 'Ciencia'),
    ('Ficción', 'Ficción'),
    ]

# Clases películas, series y documentales -----------------
 # name = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Please enter your name'}))

class PrimerFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la película")
    genero = forms.CharField(label="Género", widget=forms.Select(choices=genero))
    fecha = forms.DateField(label="Fecha", widget=forms.TextInput(attrs={'placeholder': 'aaaa/mm/dd'}))
    aptoPara = forms.IntegerField(label="Edad requerida")

class SeriesFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la serie")
    genero = forms.CharField(label="Género", widget=forms.Select(choices=genero))
    fecha = forms.DateField(label="Fecha", widget=forms.TextInput(attrs={'placeholder': 'aaaa/mm/dd'}))
    aptoPara = forms.IntegerField(label="Edad requerida")

class DocumentalesFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la documental")
    genero = forms.CharField(label="Género", widget=forms.Select(choices=genero))
    fecha = forms.DateField(label="Fecha", widget=forms.TextInput(attrs={'placeholder': 'aaaa/mm/dd'}))
    aptoPara = forms.IntegerField(label="Edad requerida")
