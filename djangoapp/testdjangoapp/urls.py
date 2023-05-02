from django.urls import path
from . import views
app_name = 'testdjangoapp'
urlpatterns = [
    # menu view
    path('base', views.menu, name='base'),
    
]