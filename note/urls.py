from django.urls import path
from .views import NoteListView, NoteDetailView, current_time, list_directory

app_name = "note"
urlpatterns = [
    path('', NoteListView.as_view(), name='index'),  # ใช้ ListView
    path('<int:pk>/', NoteDetailView.as_view(), name='detail'),  # ใช้ DetailView
    path('time/', current_time, name='time'),
    path('dir/', list_directory , name='dir')
]