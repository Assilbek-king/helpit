"""helpit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main.views import indexHandler, teamHandler , teamitemHandler, studentItemHandler, contactHandler, courseHandler,requestHandler, projectHandler, serviceHandler, serviceitemHandler
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from helpit import settings

urlpatterns = [
    # path('contact', contactHandler),
    # path('blog/', blogHandler),
    # path('blog/<int:post_id>', blogItemHandler),

    path('admin/', admin.site.urls),
    path('team', teamHandler),
    path('team/<int:team_id>', teamitemHandler),
    path('contact', contactHandler),
    path('course', courseHandler),
    path('service', serviceHandler),
    path('project/', projectHandler),
    path('request', requestHandler),
    path('service/<int:serviceitem_id>', serviceitemHandler),
    path('<int:student_id>', studentItemHandler),
    path('', indexHandler),

    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]