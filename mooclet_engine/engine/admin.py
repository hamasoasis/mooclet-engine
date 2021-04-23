from django.contrib import admin
from .models import *

# Register your models here.

class PolicyParameterHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_time',)
admin.site.register(Environment)
admin.site.register(Mooclet)
admin.site.register(Version)
admin.site.register(Variable)
admin.site.register(Value)
admin.site.register(Policy)
admin.site.register(Learner)
admin.site.register(PolicyParameters)
admin.site.register(PolicyParametersHistory, PolicyParameterHistoryAdmin)