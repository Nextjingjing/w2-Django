from django.views.generic import ListView, DetailView

from .models import Note

class NoteListView(ListView):
    model = Note
    template_name = 'note/index.html'  # ชื่อไฟล์ Template
    context_object_name = 'notes'     # ชื่อ Context ที่ส่งไป Template (default: 'object_list')

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detail.html' 
    context_object_name = 'note'       