
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from blog.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('author/<name>', getauthor, name='author'), 
    path('single/<int:id>', getsingle, name='single'),
    path('gettopic/<str:catagory_name>/', gettopic, name='gettopic'),
    path('login/', getlogin, name='login'),
    path('logout/', getLogout, name='logout'),
    path('create/', getcreate, name='create'),
    path('profile/', getprofile, name='profile'),
    path('update/<int:pid>', getUpdate, name='update'),
    path('delete/<int:pid>', getDelete, name='delete'),
    path('signup/', signUp, name='signup'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)