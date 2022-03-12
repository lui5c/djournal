from django.db import models

# Create your models here.

class EntryManager(models.Manager):
    def create_entry(self, title, date, text):
        new_entry = self.create(entry_title=title, entry_date=date, entry_text=text)
        print(self)
        return new_entry


class Entry(models.Model):
    entry_text = models.TextField(default="empty text")
    entry_date = models.TextField(default="empty date")
    entry_title = models.TextField(default="empty title")
    objects = EntryManager()

    def __repr__(self):
        return f'{self.entry_title} from {self.entry_date} ({len(self.entry_text)} chars)'