from django.shortcuts import render
from django.http import HttpResponse

from .models import Entry

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the journalentries index.")

def single_entry_view(request, date):
    try:
        found = Entry.objects.filter(entry_date=date).first()
        context = {
            'date': found.entry_date,
            'text': found.entry_text,
            'title': found.entry_title,
            }
        return render(request, 'journalentries/index.html', context)
    except:
        return HttpResponse("You fucked up")
    