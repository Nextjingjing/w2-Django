from django.urls import path
from .views import NoteListView, NoteDetailView

app_name = "note"
urlpatterns = [
    path('', NoteListView.as_view(), name='index'),  # ใช้ ListView
    path('<int:pk>/', NoteDetailView.as_view(), name='detail'),  # ใช้ DetailView
]