from django.contrib import admin

# Register your models here.

from taskgui.models import status
from taskgui.models import ttype
from taskgui.models import location
from taskgui.models import department
from taskgui.models import user_pref


admin.site.register(status)
admin.site.register(ttype)
admin.site.register(location)
admin.site.register(department)
admin.site.register(user_pref)

