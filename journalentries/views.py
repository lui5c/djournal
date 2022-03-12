from django.shortcuts import render
from django.http import HttpResponse

from .models import Entry

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the journalentries index.")

def single_entry_view(request, date):
    found = Entry.objects.filter(entry_date=date).first()
    #plist is a list of paragraphs
    plist = found.entry_text.split("\n")
    context = {
        'date': found.entry_date,
        'text': plist,
        'title': found.entry_title,
        }
    return render(request, 'journalentries/singleentry.html', context)
