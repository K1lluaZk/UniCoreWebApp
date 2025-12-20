from django.contrib import admin
from Modules.AppAcademic.models import *

admin.site.register(Career)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)

admin.site.site_header = "UniCore Admin"
admin.site.site_title = "UniCore"
admin.site.index_title = "Gestión Académica"
