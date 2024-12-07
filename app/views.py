from django.shortcuts import render, get_object_or_404
from .models import Video, Category

def home(request):
    videos = Video.objects.all()
    categories = Category.objects.all()
    return render(request, 'base.html', {'videos': videos, 'categories': categories})

def category_videos(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    videos = Video.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'base.html', {
        'videos': videos,
        'categories': categories,
        'selected_category': category
    })
