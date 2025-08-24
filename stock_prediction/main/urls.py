from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('predictions/', views.predictions, name='predictions'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('insights/', views.insights, name='insights'),
    path('about/', views.about, name='about'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
