from django.contrib import admin
from django.urls import path
from Aplicativo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'main'),
    # CRUD de CIDADES
    path('cidade', views.createCidade, name="createCidade"),
    path('cidade/<int:id_cidade>', views.updateCidade, name="updateCidade"),
    path('cidade/<int:id_cidade>/delete', views.deleteCidade, name="deleteCidade"),
    # CRUD de PROFISSÕES
    path('profissao', views.createProfissao, name="createProfissao"),
    path('profissao/<int:id_profissao>', views.updateProfissao, name="updateProfissao"),
    path('profissao/<int:id_profissao>/delete', views.deleteProfissao, name="deleteProfissao"),
    # CRUD de SITUAÇÕES
    path('situacao', views.createSituacao, name="createSituacao"),
    path('situacao/<int:id_situacao>', views.updateSituacao, name="updateSituacao"),
    path('situacao/<int:id_situacao>/delete', views.deleteSituacao, name="deleteSituacao"),
    # CRUD de GÊNEROS
    path('genero', views.createGenero, name="createGenero"),
    path('genero/<int:id_genero>', views.updateGenero, name="updateGenero"),
    path('genero/<int:id_genero>/delete', views.deleteGenero, name="deleteGenero"),
    # CRUD de NECESSITADOS
    path('necessitado', views.createNecessitado, name="createNecessitado"),
    path('necessitado/<int:id_necessitado>', views.updateNecessitado, name="updateNecessitado"),
    path('necessitado/<int:id_necessitado>/delete', views.deleteNecessitado, name="deleteNecessitado"),
    # CRUD de ATUALIZAÇAÕES
    path('atualizacao', views.createAtualizacao, name="createAtualizacao"),
    path('atualizacao/<int:id_atualizacao>', views.updateAtualizacao, name="updateAtualizacao"),
    path('atualizacao/<int:id_atualizacao>/delete', views.deleteAtualizacao, name="deleteAtualizacao"),
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)