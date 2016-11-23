from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tasks$', login_required(views.ListTaskView.as_view()), name='task-list'),
    url(r'^task/(?P<pk>[0-9]+)$', views.TaskView.as_view(), name='task-view'),
    url(r'^task/new$', views.TaskNew.as_view(), name='task-new'),
    url(r'^task/new_child/(?P<pTaskid>[0-9]+)$', views.TaskNewChild.as_view(), name='task-new'),
    url(r'^task_edit/(?P<pk>[0-9]+)$', views.TaskEdit.as_view(), name='task-edit'),
    url(r'^task/delete/(?P<pk>[0-9]+)$', views.TaskDelete.as_view(), name='task-edit'),
    url(r'^task/complete/(?P<pk>[0-9]+)$', views.TaskComplete.as_view(), name='task-edit'),
    url(r'^note/(?P<pk>[0-9]+)$', views.NoteEdit.as_view(), name='note_edit'),
    url(r'^note/new/(?P<taskid>[0-9]+)$', views.NoteNew.as_view(), name='note-new'),
    url(r'^note/comment/(?P<noteid>[0-9]+)$', views.NoteComment.as_view(), name='note-new'),
    url(r'^note/delete/(?P<pk>[0-9]+)$', views.NoteDelete.as_view(), name='note-delete'),
    url(r'^search/', include('haystack.urls')),
]
