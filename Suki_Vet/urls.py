from django.urls import path, include

urlpatterns = [
    path('', include('admin_app.urls')),
    path('', include('gestion_pacientes.urls')),
    path('', include('consulta_app.urls')),

]
