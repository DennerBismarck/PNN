from django.contrib import admin
from django.urls import path
from Aplicativo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'main'),
    # URLs de CRUD dos Necessitados.
    path('necessitado', views.createNecessitado, name="createNecessitado"),
    path('necessitado/<int:id_necessitado>', views.updateNecessitado, name="updateNecessitado"),
    path('necessitado/<int:id_necessitado>/delete', views.deleteNecessitado, name="deleteNecessitado"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)