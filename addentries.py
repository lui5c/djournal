import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'journal.settings')

import django
django.setup()
from journalentries.models import Entry

def parse_entry_from_txtfile(file):
    title = ""
    date = ""
    text = ""
    for line in file:
        if "title: " in line and title == "":
            line = line[:-1] # truncate newline
            title = line[7:]
        elif "date: " in line and date == "":
            line = line[:-1] # truncate newline
            date = line[6:]
        elif date != "" and title != "":
            text += line
    returner = {
        'entry_title': title,
        'entry_date': date,
        'entry_text': text
    }
    return returner


for filename in os.listdir('entries'):
    f = os.path.join('entries', filename)
    if os.path.isfile(f):
        tempfile = open(f, 'r')
        tempdict = parse_entry_from_txtfile(tempfile)
        print(f'found: {tempdict["entry_title"]} from {tempdict["entry_date"]} with length {len(tempdict["entry_text"])}')
        Entry.objects.create(**tempdict)
        tempfile.close()

