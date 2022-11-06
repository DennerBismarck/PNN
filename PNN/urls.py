from django.contrib import admin
from django.urls import path
from Aplicativo import views as viewsAplicativo
from Localidade import views as viewsLocalidade
from ONG        import views as viewsONG
from Usuario    import views as userView

urlpatterns = [
    # Tela Login e Cadastro
    path('login/', userView.login, name="login"),
    path('cadastro/', userView.cadastro, name="cadastro"),
    path('logout/', userView.logout, name="logout"),
    # Usuário
    path('user/', userView.user , name="user"),
    # Crud de Usuário TELEFONE
    path('user/tel', userView.createTelefone , name="createUserTel"),
    path('user/tel/<int:id_telefone>', userView.updateTelefone , name="updateUserTel"),
    path('user/tel/<int:id_telefone>/delete', userView.deleteTelefone , name="deleteUserTel"),
    # Crud de Usuário EMAIL
    path('user/email', userView.createEmail , name="createUserEmail"),
    path('user/email/<int:id_email>', userView.updateEmail , name="updateUserEmail"),
    path('user/email/<int:id_email>/delete', userView.deleteEmail , name="deleteUserEmail"),
    # Mapeamento
    path('map/', viewsLocalidade.map, name="map"),
    # Admin e Index #
    path('admin/', admin.site.urls),
    path('', viewsAplicativo.index, name='main'),
    # CRUD de NECESSITADOS
    path('necessitado', viewsAplicativo.createNecessitado, name="createNecessitado"),
    path('necessitado/<int:id_necessitado>/delete', viewsAplicativo.deleteNecessitado, name="deleteNecessitado"),
    # CRUD de ATUALIZAÇÕES
    path('necessitado/<int:id_necessitado>', viewsAplicativo.createTimeline, name="createAtualizacao"),
    path('necessitado/<int:id_necessitado>/<int:id_atualizacao>', viewsAplicativo.updateTimeline, name="updateAtualizacao"),
    path('necessitado/<int:id_necessitado>/<int:id_atualizacao>/delete', viewsAplicativo.deleteTimeline, name="deleteAtualizacao"),
    # CRUD de PROFISSÕES
    path('profissao', viewsAplicativo.createProfissao, name="createProfissao"),
    path('profissao/<int:id_profissao>', viewsAplicativo.updateProfissao, name="updateProfissao"),
    path('profissao/<int:id_profissao>/delete', viewsAplicativo.deleteProfissao, name="deleteProfissao"),
    # CRUD de Situação
    path('Situacao', viewsAplicativo.createSituacao, name="createSituacao"),
    path('Situacao/<int:id_Situacao>', viewsAplicativo.updateSituacao, name="updateSituacao"),
    path('Situacao/<int:id_Situacao>/delete', viewsAplicativo.deleteSituacao, name="deleteSituacao"),
    # CRUD de CIDADES
    path('cidade', viewsLocalidade.createCidade, name="createCidade"),
    path('cidade/<int:id_cidade>', viewsLocalidade.updateCidade, name="updateCidade"),
    path('cidade/<int:id_cidade>/delete', viewsLocalidade.deleteCidade, name="deleteCidade"),
    # CRUD de ONGs
    path('ONG', viewsONG.createONG, name="createONG"),
    path('ONG/<int:id_ONG>', viewsONG.updateONG, name="updateONG"),
    path('ONG/<int:id_ONG>/delete', viewsONG.deleteONG, name="deleteONG"),
    # CRUD de TELEFONE DAS ONGS
    path('ONG/<int:id_ONG>/tel', viewsONG.createTelefone, name="createTelefone"),
    path('ONG/<int:id_ONG>/tel/<int:id_telefone>', viewsONG.updateTelefone, name="updateTelefone"),
    path('ONG/<int:id_ONG>/tel/<int:id_telefone>/delete', viewsONG.deleteTelefone, name="deleteTelefone"),
    # CRUD de email das ongs
    path('ONG/<int:id_ONG>/email', viewsONG.createEmail, name="createEmail"),
    path('ONG/<int:id_ONG>/email/<int:id_email>', viewsONG.updateEmail, name="updateEmail"),
    path('ONG/<int:id_ONG>/email/<int:id_email>/delete', viewsONG.deleteEmail, name="deleteEmail"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)