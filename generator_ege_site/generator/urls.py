from django.urls import path
from . import views

app_name = 'generator'


urlpatterns = [
    path('', views.generator, name='generator'),
    path('generate/<int:variant_id>/', views.generate_variant, name='generate_variant')
]