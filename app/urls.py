from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('yessem2020', views.yessem2020, name='yessem2020')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

