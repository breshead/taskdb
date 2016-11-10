from django.db import models
from django.contrib.auth.models import User

class ttype(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=20, null=False)

    # This '__unicode__' function is required for django to follow foriegn keys to the result.
    def __unicode__(self):
        return self.name

class status(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=20, null=False)

    def __unicode__(self):
        return self.name


class tag(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=100, null=False)

    def __unicode__(self):
        return self.name
    
class role(models.Model):
    id        = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=False)

    def __unicode__(self):
        return self.name

class context(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=100, null=False)

    def __unicode__(self):
        return self.name

class user_pref(models.Model):
    id        = models.AutoField(primary_key=True)
    user_id   = models.ForeignKey(User, on_delete=models.CASCADE)
    key       = models.CharField(max_length=100, null=False)
    value     = models.TextField(null=False)

class task(models.Model):
    id        = models.AutoField(primary_key=True)
    parent    = models.ForeignKey('task', on_delete=models.CASCADE, null=True, blank=True)
    context   = models.ForeignKey('context', on_delete=models.CASCADE, null=True)
    owner     = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(User, related_name='requested_by', on_delete=models.CASCADE , null=True, blank=True)
    ttype     = models.ForeignKey('ttype', on_delete=models.CASCADE)
    role      = models.ForeignKey('role', on_delete=models.CASCADE, null=True, blank=True)
    name      = models.CharField(max_length=100, null=False)
    created   = models.DateTimeField(null=False)
    due       = models.DateTimeField(null=True, blank=True)
    completed = models.DateTimeField(null=True, blank=True)
    overview  = models.TextField(null=True)
    progress  = models.IntegerField(null=True, blank=True)
    status    = models.ForeignKey('status', on_delete=models.CASCADE, null=True)
    storage   = models.CharField(max_length=100, null=True, blank=True)
    priority  = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name

    def text_name(self):
        return self.name


    def get_absolute_url(self):
        return "/taskgui/task/%s" % self.id



class note(models.Model):
    id       = models.AutoField(primary_key=True)
    task     = models.ForeignKey('task', on_delete=models.CASCADE, null=True)
    parent   = models.ForeignKey('note', on_delete=models.CASCADE, null=True, blank=True)
    stamp    = models.DateTimeField(null=False)
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    title    = models.CharField(max_length=70, null=False)
    text     = models.TextField(null=True)

    def __unicode__(self):
        return self.title

    def text_name(self):
        myTask = task.objects.get(pk=self.task_id)
        return "{}/{}".format(myTask.text_name(), self.title)

    def get_absolute_url(self):
        return "/taskgui/task/%s" % self.task_id




class comment(models.Model):
    id       = models.AutoField(primary_key=True)
    note     = models.ForeignKey('note', on_delete=models.CASCADE, null=True)
    stamp    = models.DateTimeField(null=False)
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    text     = models.TextField(null=True)

    def __unicode__(self):
        return self.text


class checkup(models.Model):
    id        = models.AutoField(primary_key=True)
    note_id  = models.ForeignKey('task', on_delete=models.CASCADE, null=True)
    checkdate= models.DateTimeField(null=False)


