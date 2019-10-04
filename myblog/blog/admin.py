from django.contrib import admin
from .models import BlogPost,Profile
# Register your models here.
admin.site.register(Profile)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','date_posted','author','slug')


admin.site.register(BlogPost,BlogAdmin)
