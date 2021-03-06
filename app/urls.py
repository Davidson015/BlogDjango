from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from app.views import *

urlpatterns = [
  path('', IndexPage, name="Index"),
  path('blog/category/<str:slug>/', BlogHome, name="Blog"),
  path('blog/<str:slug>/', PostDetails, name="post_details"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)