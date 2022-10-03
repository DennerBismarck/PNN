from django.contrib import admin
from django.urls import path
from Aplicativo import views

urlpatterns = [
    # Tela Login e Cadastro
    path('login/', views.login),
    path('cadastro/', views.cadastro),
    #-----------  -----------#
    path('admin/', admin.site.urls),
    path('', views.index, name= 'main'),
    # CRUD de NECESSITADOS
    path('necessitado', views.createNecessitado, name="createNecessitado"),
    path('necessitado/<int:id_necessitado>', views.updateNecessitado, name="updateNecessitado"),
    path('necessitado/<int:id_necessitado>/delete', views.deleteNecessitado, name="deleteNecessitado"),
    # CRUD de CIDADES
    path('cidade', views.createCidade, name="createCidade"),
    path('cidade/<int:id_cidade>', views.updateCidade, name="updateCidade"),
    path('cidade/<int:id_cidade>/delete', views.deleteCidade, name="deleteCidade"),
    # CRUD de PROFISSÕES
    path('profissao', views.createProfissao, name="createProfissao"),
    path('profissao/<int:id_profissao>', views.updateProfissao, name="updateProfissao"),
    path('profissao/<int:id_profissao>/delete', views.deleteProfissao, name="deleteProfissao"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)