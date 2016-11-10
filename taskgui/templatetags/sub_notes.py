from taskgui.models import note
from django import template
register = template.Library()
 
@register.inclusion_tag('note_view.html')
def sub_notes(parent, indent):
    notes = note.objects.filter(parent_id=parent).order_by('-stamp')
    indentpx = indent * 40
    indent = indent + 1
    return { 'notes': notes, 'indent': indent, 'indentpx': indentpx }


