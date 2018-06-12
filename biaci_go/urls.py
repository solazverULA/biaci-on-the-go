"""biaci_go URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf.urls import url
from django.urls import include, path

#from libro.views import views


urlpatterns = [
	path('', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')), 
    path('admin/', admin.site.urls),
    path('libro/', include('libro.urls'), name='ver_libro'),
    path('reserva/', include('reserva.urls'), name='reserva'),
    path('perfil/', include('prestamo.urls'), name='prestamo'),
    path('revista/', include('revista.urls'), name='ver_revista'),
    path('tesis/', include('tesis.urls'), name='ver_tesis'),
    path('', include('consulta.urls'), name='consulta'),
    url(r'^reset/password_reset',password_reset,{'template_name':'registration/password_reset_form.html','email_template_name':'registration/password_reset_email.html'},name="password_reset"), 
    url(r'^password_reset_done',password_reset_done,{'template_name':'registration/password_reset_done.html'},name="password_reset_done"), 
    url(r'^reset/(?P<uidb64>[0-94-Za-z_\-]+)/(?P<token>.+)/$',password_reset_confirm,{'template_name':'registration/password_reset_confirm.html'},name="password_reset_confirm"), 
    url(r'^reset/done',password_reset_complete,{'template_name':'registration/password_reset_complete.html'},name="password_reset_complete")
]
