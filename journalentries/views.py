from django.shortcuts import render
from django.http import HttpResponse

from .models import Entry

# Create your views here.
def index(request):
    found = Entry.objects.all()
    entries = []
    for e in found:
        temp_context = {
            'date': e.entry_date,
            'preview': e.entry_text.split("\n"),
            'title': e.entry_title,
            }
        entries.append(temp_context)
    context = {'entries':entries}
    return render(request, 'journalentries/index.html', context)

def single_entry_view(request, date):
    found = Entry.objects.filter(entry_date=date).first()
    context = {}
    if not found:
        return render(request, 'journalentries/404.html', context)
    #plist is a list of paragraphs
    plist = found.entry_text.split("\n")
    context = {
        'date': found.entry_date,
        'text': plist,
        'title': found.entry_title,
        }
    return render(request, 'journalentries/singleentry.html', context)
