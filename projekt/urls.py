from django.contrib import admin
from django.urls import path
from api import views
# do działania obrazków
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', views.user_registration, name='user-register'),
    path('api/groups/', views.get_groups, name='get-groups'),
]

# do obrazków
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
