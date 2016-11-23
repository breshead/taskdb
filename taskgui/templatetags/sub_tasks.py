from taskgui.models import task
from django import template
register = template.Library()
 
@register.inclusion_tag('sub_task_list.html')
def sub_tasks(parent, indent):
    #tasks = task.objects.filter(parent_id=parent).order_by('priority')
    try:
        tasks = parent.children
    except AttributeError:
        tasks = None
        
    indentpx = indent * 20
    indent = indent + 1
    return { 'tasks': tasks, 'indent': indent, 'indentpx': indentpx }


