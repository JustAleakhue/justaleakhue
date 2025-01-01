from .models import SaveToDatabase
from django.shortcuts import render, redirect  # Fix the import statement
from gallery.models import Category, Gallery
from .forms import ContactForm
from django.contrib import messages  # Fix the import statement
from .models import Photo
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    photos = Gallery.objects.all()
    categories = Category.objects.all()

    return render(request, 'photography/index.html', {
        'categories': categories,
        'photos': photos,
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                'Photography',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                settings.DEFAULT_FROM_EMAIL,
                ['shotbyjustaleakhue@gmail.com'], 
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('photography:contact')  
        else:
            messages.error(request, 'Message not sent. Please check the form and try again.')
    else:
        form = ContactForm()

    return render(request, 'photography/contact.html', {
        'form': form,
    })

def gallery(request):
    return render(request, 'photography/gallery.html')

def about(request):
    return render(request, 'photography/about.html')

def Photogallery(request):
    photos = Photo.objects.all()
    return render(request, 'photography/Photogallery.html', {'photos': photos})
