from django.contrib import admin
from django.urls import path,include
from notes import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Notes API Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', views.NotesListCreateAPIView.as_view()),
    path('notes/<int:id>/', views.NotesRetrieveUpdateDestroyAPIView.as_view()),
    path('api/doc/', schema_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
