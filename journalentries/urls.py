from django.urls import path

from . import views

urlpatterns = [
    # ex: /journalentries/
    path('', views.index, name='index'), # this maps the empty path to the index view.
    # ex: /journalentries/01-02-2020/
    path('<date>/', views.single_entry_view, name='single entry')
]