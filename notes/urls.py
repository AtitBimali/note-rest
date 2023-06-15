
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from main.views import NoteViewSet,ShareNoteViewSet
router = DefaultRouter()

router.register("notes", NoteViewSet)
router.register("shared-notes",ShareNoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls