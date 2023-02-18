from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.index,name='home'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('register',views.register,name='registerd'),
    path('view',views.files,name='fileview'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
