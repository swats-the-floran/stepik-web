from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('question/<int:id>/', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.new, name='new'),
]