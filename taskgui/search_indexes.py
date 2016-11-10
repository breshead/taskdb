import datetime
from haystack import indexes
from taskgui.models import task
from taskgui.models import note
from django.contrib.auth.models import User


class TaskIndex(indexes.SearchIndex, indexes.Indexable):
    text      = indexes.CharField(document=True, use_template=True)
    #owner     = indexes.CharField(model_attr=User)  -- cannot deal with user
    ttype     = indexes.CharField(model_attr='ttype')
    #role      = indexes.CharField(model_attr='role') -- cannot deal with null values
    created   = indexes.DateTimeField(model_attr='created')
    due       = indexes.DateTimeField(model_attr='due', null=True)
    completed = indexes.DateTimeField(model_attr='completed', null=True)
    progress  = indexes.IntegerField(model_attr='progress', null=True)
    status    = indexes.CharField(model_attr='status', null=True)
    priority  = indexes.IntegerField(model_attr='priority', null=True)

    def get_model(self):
        return task



class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text      = indexes.CharField(document=True, use_template=True)
    #user     = indexes.CharField(model_attr=User)  -- cannot deal with user
    stamp     = indexes.DateTimeField(model_attr='stamp')

    def get_model(self):
        return note 

