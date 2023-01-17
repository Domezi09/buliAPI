from django.urls import path
from Bundesliga import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('signup/', accounts_views.signup, name='signup'),
        path('results', views.get_last_results, name='results'),
    ]
