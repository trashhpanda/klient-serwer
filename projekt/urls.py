from django.contrib import admin
from django.urls import path
from api import views
# do działania obrazków
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', views.user_registration, name='user-register'),
    path('api/user/login/', views.login_view, name='user-login'),
    path('api/user/logout/', views.logout_view, name='user-logout'),
    path('api/user/', views.user_view, name='user-view'),
    path('api/groups/', views.get_groups, name='get-groups'),
    path('api/client/', views.client_view, name='client-view'),
    path('api/instructors/', views.instructors_view, name='instructors-view'),
    path('api/schools/', views.schools_view, name='schools-view'),
    path('api/calendar/', views.calendar_view, name='calendar-view'),
    path('api/booking/', views.booking_view, name='booking-view'),
    path('api/student/', views.student_view, name='student-view'),
    path('api/class_type/', views.class_type_view, name='class-type-view'),
    path('api/address/', views.address_view, name='address-view'),
    path('api/language/', views.language_view, name='language-view'),
    path('api/qualification/', views.qualification_view, name='qualification-view'),
]

# do obrazków
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
