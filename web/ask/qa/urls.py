from django.urls import path
from . import views

urlpatterns = [
    # path('', views.root, name='root'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('question/<int:pk>/', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('', views.new, name='new'),
]