# djournal
journal app that uses a local django server as a backend to write, read, and search journal entries

## how to use
create a directory in djournal called "entries" full of .txt files of the form:
```
---
title: entry title
date: mm-dd-yyyy
---
today was a good day
```
then run addentries.py. this imports/syncs your journal entries, then you can use the web interface to add more

run the server, and either write more or browse your existing entries