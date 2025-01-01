from django.shortcuts import render, get_object_or_404, redirect
from .models import Gallery,Category
from random import shuffle

def detail(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    related_photos = Gallery.objects.filter(category=gallery.category,).exclude(pk=pk)

    return render(request, 'gallery/detail.html',{
        'gallery': gallery,
        'related_photos': related_photos
    })

def category_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    photos_in_category = list(Gallery.objects.filter(category=category))
    shuffle(photos_in_category)


    return render(request, 'gallery/category.html', {
        'category': category,
        'photos_in_category': photos_in_category,
    })

def photo_detail(request, pk):
    photo = get_object_or_404(Gallery, pk=pk)
    photos = Gallery.objects.all()

    return render(request, 'photography/photo_detail.html', {
        'photo': photo,
        'photos': photos,
    })

