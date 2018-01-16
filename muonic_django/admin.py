from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Run)
admin.site.register(Analyzer)
admin.site.register(Decay)
admin.site.register(Pulse)
admin.site.register(Velocity)
admin.site.register(Rate)