from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', IndexPage, name="Index"),
  path('blog/', BlogHome, name="Blog"),
  path('blog-details/<str:slug>/', PostDetails, name="post_details"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)