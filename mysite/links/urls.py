# links/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('criar_pagina_produto/', views.criar_pagina_produto, name='criar_pagina_produto'),
    path('editar_pagina_produto/', views.editar_pagina_produto, name='editar_pagina_produto'),
    path('pagina_produto/<int:pagina_id>/', views.visualizar_pagina_produto, name='visualizar_pagina_produto'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
