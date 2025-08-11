from django.contrib import admin
from api.models import Daily_task, Long_term_goals, CustomUser

admin.site.register(Daily_task)
admin.site.register(Long_term_goals)
admin.site.register(CustomUser)
