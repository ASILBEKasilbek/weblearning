from django.contrib import admin
from .models import Video,Category

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file')

admin.site.register(Category)