from django.contrib import admin
from django.urls import path, include
from main.views.views import UserMatchView

urlpatterns = [
    path('account/', include('main.urls')),
    path('usermedia/', include('usermedia.urls')),
    path('admin/', admin.site.urls),
    path('match', UserMatchView.as_view()),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)