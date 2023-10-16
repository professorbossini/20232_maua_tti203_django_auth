from django.urls import path
from autenticacao_autorizacao_app.views import CadastroNovoUsuarioView
urlpatterns = [
  path('signup/', CadastroNovoUsuarioView.as_view(), name="signup")
]