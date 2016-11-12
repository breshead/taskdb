from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model


from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView
from taskgui.models import task
from taskgui.models import note
from taskgui.models import status
from taskgui.models import ttype
from taskgui.models import location 
from taskgui.models import department
from django.db.models import Q
import sys
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import time
from django.shortcuts import redirect


#@method_decorator(login_required)
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return redirect('/taskgui/tasks')

#class ListTaskView(ListView):
class ListTaskView(TemplateView):
    template_name = "task_list.html"
    #model = task

    def users(self):
        User = get_user_model()
        return User.objects.all()

    def statii(self):
        return status.objects.all()

    def types(self):
        return ttype.objects.all()

    def departments(self):
        return department.objects.all()

    def locations(self):
        return location.objects.all()




    # Implement the view.tlist call in the template.
    # Using the "view" object frm here..
    # http://reinout.vanrees.org/weblog/2014/05/19/context.html
    def x_unused_tlist(self):
        # Get the checkbox filter data
        user_filter = self.request.GET.get('User', None)
        status_filter = self.request.GET.get('Status', '0')


        # Create a Q object filter and set it up.
        my_filter_qs = Q()

        if status_filter != "0":
            my_filter_qs = my_filter_qs & Q(status=status_filter)
            print >>sys.stderr, "Using STATUS FILTER :" + status_filter + ":"
        

        if user_filter != "0":
            my_filter_qs = my_filter_qs & Q(owner=user_filter)
            print >>sys.stderr, "Using USER FILTER :" + user_filter + ":"


        #print >>sys.stderr, "IN tasklist :" + f + ":"
        #https://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects 

        tasklist = task.objects.filter(my_filter_qs)
        
        return tasklist

        
    

    def get_context_data(self, **kwargs):
        context = super(ListTaskView, self).get_context_data(**kwargs)
        user_filter = self.request.GET.get('User', None)
        status_filter = self.request.GET.get('Status', None)
        type_filter = self.request.GET.get('Type', None)
        pri_filter = self.request.GET.get('Priority', None)
        location_filter = self.request.GET.get('Location', None)
        w_dept_filter = self.request.GET.get('W_DEPT', None)
        for_dept_filter = self.request.GET.get('FOR_DEPT', None)


        if pri_filter == None:
            pri_filter = "1"
            print >>sys.stderr, "Using DEF PRI FILTER :" + pri_filter + ":"


        if type_filter == None:
            type_filter = "1"
            print >>sys.stderr, "Using DEF TYPE FILTER :" + type_filter + ":"

        # If there is no selections then grab the user ID and set that to be a filter.
        if user_filter == None:
            user_filter = str(self.request.user.id)
            print >>sys.stderr, "Using DEF USER FILTER :" + user_filter + ":"

        # If there is no status selection then set it to "In Progress"
        if status_filter == None:
            status_filter = "A" # In Progress
            print >>sys.stderr, "Using DEF STAUTS FILTER :" + status_filter + ":"


        # Create a Q object filter and set it up.
        my_filter_qs = Q()


        if pri_filter != "0":
            my_filter_qs = my_filter_qs & Q(priority=pri_filter)
            print >>sys.stderr, "Using pri FILTER :" + pri_filter + ":"


        if status_filter == "A":
            my_filter_qs = my_filter_qs & ~Q(status="4") &  ~Q(status="5")

        if status_filter != "0" and status_filter != "A":
            my_filter_qs = my_filter_qs & Q(status=status_filter)
            print >>sys.stderr, "Using STATUS FILTER :" + status_filter + ":"

        if user_filter != "0":
            my_filter_qs = my_filter_qs & Q(owner=user_filter)
            print >>sys.stderr, "Using USER FILTER :" + user_filter + ":"

        if type_filter and type_filter != "0":
            my_filter_qs = my_filter_qs & Q(ttype=type_filter)
            print >>sys.stderr, "Using USER FILTER :" + type_filter + ":"

        if location_filter and location_filter != "0":
            my_filter_qs = my_filter_qs & Q(location=location_filter)
            print >>sys.stderr, "Using LOCATION FILTER :" + location_filter + ":"

        if w_dept_filter and w_dept_filter != "0":
            my_filter_qs = my_filter_qs & Q(w_dept=w_dept_filter)
            print >>sys.stderr, "Using W_DEPT FILTER :" + w_dept_filter + ":"

        if for_dept_filter and for_dept_filter != "0":
            my_filter_qs = my_filter_qs & Q(for_dept=for_dept_filter)
            print >>sys.stderr, "Using FOR_DEPT FILTER :" + for_dept_filter + ":"


        #https://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects 
        tasklist = task.objects.filter(my_filter_qs).order_by('priority')

        # Populate the context with our custom data.
        context['task_list'] = tasklist
        context['user_filter'] = user_filter
        context['status_filter'] = status_filter
        context['type_filter'] = type_filter
        context['pri_filter'] = pri_filter
        context['pri_list'] = range(1,5)

        context['location_filter'] = location_filter
        context['w_dept_filter'] = w_dept_filter
        context['for_dept_filter'] = for_dept_filter

        return context



# DetailView uses TemplateView class and does what we have done in the get_context for us.
# So all we have to define here is what model, template and name to use.
# In the urls.py we have changed the parameter name from "id" to "pk" so that it knows what to do with it.
class xTaskView(DetailView):
    model = task
    template_name = "task_view.html"
    context_object_name = 'task'




# Using the templateview as it allows us access to get_context_data 
# so that we can add the 'notes' data element.
class TaskView(TemplateView):
    model = task
    template_name = "task_view.html"

    def get_context_data(self, **kwargs):
        taskid = self.kwargs.get('pk', None)
        context = super(TaskView, self).get_context_data(**kwargs)
        context['task'] = task.objects.get(pk=taskid)
        context['notes'] = note.objects.filter(task_id=taskid,
                parent_id=None).order_by('-stamp')
        context['subtasks'] = task.objects.filter(parent_id=taskid).order_by('created')
        return context
   
class TaskEdit(UpdateView):
    model = task
    template_name = 'task_edit.html'
    fields = '__all__'
    #fields = ['title', 'text']
    #success_url = "/taskgui/tasks"

    print >>sys.stderr, "Task Edit :" + template_name + ":"
    
    def get_success_url(self):
        taskid = self.kwargs.get('pk', None)
        print >>sys.stderr, "SUCCESSURL TASKID:" + str(taskid) + ":"
        success_url = "/taskgui/task/" + str(taskid)
        return success_url
        
    
    def get_context_data(self, **kwargs):
        taskid = self.kwargs.get('pk', None)
        print >>sys.stderr, "CTXT TASKID:" + str(taskid) + ":"
        context = super(TaskEdit, self).get_context_data(**kwargs)
        myTask = task.objects.get(pk=taskid)
        parid = myTask.parent

        if parid == None:
            context['parentname'] = "NONE"
        else:
            context['parentname'] = myTask.parent.name
        
        context['taskname'] = myTask.name

        return context

class TaskNewChild(TemplateView):
    model = task

    def get(self, request, pTaskid):
        userid = str(self.request.user.id)
        UserMdl = get_user_model()
        user =  UserMdl.objects.get(pk=userid)
        myTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        myTask = task.objects.create(context_id=1, owner_id=user.id,
                requested_by_id=user.id,
                name='Name Here', created=myTime, due=myTime,
                ttype_id = 1, overview='Overview Here', status_id=1, 
                priority=1, parent_id=pTaskid)
        myID = myTask.id
        return redirect('/taskgui/task_edit/' + str(myTask.id))



class TaskNew(TemplateView):
    model = task

    def get(self, request):
        userid = str(self.request.user.id)
        UserMdl = get_user_model()
        user =  UserMdl.objects.get(pk=userid)
        myTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        myTask = task.objects.create(context_id=1, owner_id=user.id,
                requested_by_id=user.id,
                name='Name Here', created=myTime, due=myTime,
                ttype_id = 1, overview='Overview Here', status_id=1, priority=1)
        myID = myTask.id
        return redirect('/taskgui/task_edit/' + str(myTask.id))


class TaskDelete(TemplateView):
    model = task
    def get(self, request, pk):
        myTask = task.objects.get(pk=pk)

        res = myTask.delete()
        #####################################################
        # Replacing the above line with the below code..
        #task_cplt = status.objects.get(name="Completed")
        #tstamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        #res = myTask.status = task_cplt
        #res = myTask.completed = tstamp
        #myTask.save()

        #userid  = str(self.request.user.id)
        #UserMdl = get_user_model()
        #user    =  UserMdl.objects.get(pk=userid)
        #myNote  = note.objects.create( task=myTask, stamp=tstamp, 
        #          user_id=userid, title='Deleting Task', text='Automated Reason')
        ######################################################


        return redirect('/taskgui/tasks')
 
    def post(self, request, pk):
        return self.get(request, pk)


class TaskComplete(TemplateView):
    model = task
    def get(self, request, pk):
        myTask = task.objects.get(pk=pk)
        task_cplt = status.objects.get(name="Completed")
        res = myTask.status = task_cplt
        tstamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        res = myTask.completed = tstamp
        myTask.save()

        # Now that we have updated the task, we need to create a new note
        # and drop the user into it..
        userid  = str(self.request.user.id)
        UserMdl = get_user_model()
        user    =  UserMdl.objects.get(pk=userid)
        myNote  = note.objects.create( task=myTask, stamp=tstamp, 
                  user_id=userid, title='Status = Complete', text='Marking complete because..')

        return redirect('/taskgui/note/' + str(myNote.id))

 
    def post(self, request, pk):
        return self.get(request, pk)


 

class NoteEdit(UpdateView):
    model = note
    template_name = "note_edit.html"
    #fields = ['title', 'text']
    fields = '__all__'
    #success_url = "/taskgui/tasks"

    def get_context_data(self, **kwargs):

        # Get the note data and put it in the context.
        noteid = self.kwargs.get('pk', None)
        context = super(NoteEdit, self).get_context_data(**kwargs)
        myNote = note.objects.get(pk=noteid)
        context['note'] = myNote
        
        # Get the task name and put it inthe context
        taskid = myNote.task_id
        myTask = task.objects.get(pk=taskid)
        context['taskname'] = myTask.name

        # Get the user name and put in context..
        userid = str(self.request.user.id)
        UserMdl = get_user_model()
        user =  UserMdl.objects.get(pk=userid)
        context['username'] = user.username
        return context



        
    def get_success_url(self):
        noteid = self.kwargs.get('pk', None)
        print "NOTEID:" + str(noteid) + ":"
        myNote = note.objects.get(pk=noteid)
        taskid = myNote.task_id
        print "TASKID:" + str(taskid) + ":"
        success_url = "/taskgui/task/" + str(taskid)
        return success_url
        



class NoteNew(TemplateView):
    model = note 

    def get(self, request, taskid):
        userid  = str(self.request.user.id)
        UserMdl = get_user_model()
        user    =  UserMdl.objects.get(pk=userid)
        tstamp  = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        myNote  = note.objects.create( task_id=taskid, stamp=tstamp, 
                                user_id=userid, title=' ', text=' ')

        return redirect('/taskgui/note/' + str(myNote.id))



class NoteDelete(TemplateView):
    model = note

    def get(self, request, pk):
        myNote = note.objects.get(pk=pk)
        taskid = myNote.task.id
        res = myNote.delete()
        return redirect('/taskgui/task/' + str(taskid))
 
    def post(self, request, pk):
        return self.get(request, pk)


class NoteComment(TemplateView):
    model = note 

    def get(self, request, noteid):
        userid  = str(self.request.user.id)
        UserMdl = get_user_model()
        user    =  UserMdl.objects.get(pk=userid)
        tstamp  = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        orignote = note.objects.get(pk=noteid)


        myNote  = note.objects.create( task_id=orignote.task.id, parent_id=noteid, stamp=tstamp, 
                                user_id=userid, title=' ', text=' ')

        return redirect('/taskgui/note/' + str(myNote.id))


