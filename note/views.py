from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Note
from django.http import HttpResponse
from django.conf import settings
import os
from django.shortcuts import render
import os


class NoteListView(ListView):
    model = Note
    template_name = 'note/index.html'  
    context_object_name = 'notes'     

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detail.html' 
    context_object_name = 'note'

def current_time(request):
    now = timezone.now()
    return HttpResponse(f"Current time: {now.strftime('%H:%M:%S')}")

def list_directory(request):
    directory_path = request.GET.get('directory_path', '.')
    try:
        files_and_folders = os.listdir(directory_path)

        items = [
            {
                "name": item,
                "is_dir": os.path.isdir(os.path.join(directory_path, item)),
                "path": os.path.join(directory_path, item),
            }
            for item in files_and_folders
        ]
        return render(request, 'note/dir.html', {
            "directory": directory_path,
            "contents": items,
        })
    except FileNotFoundError:
        return HttpResponse('error')

