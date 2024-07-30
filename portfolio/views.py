from django.shortcuts import render
from .models import Contact,Gallery,Blog,Books,PortfolioItem,About
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.views.generic.edit import FormView
from .bot import send_message


class ContactFormView(FormView):
    template_name = "contact.html"
    form_class =ContactForm
    success_url = "/"
 
    def form_valid(self,form):
      name = form.cleaned_data.get('name')
      email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      text = f"Name: {name}\nEmail: {email}\ntext: {content}"
      send_message(text)
      form.save()
      return super().form_valid(form)


def index_view(request):
 return render(request,'index.html')







def About_view(request):
    about =About.objects.all()
    context = {
       "about" :about,
    }
    return render(request,'about.html', {'about': about})





def Gallery_view(request):
    gallery = Gallery.objects.all()
    context = {
        "gallery":gallery,
    }

    return render(request, 'Gallery.html',context)


def blog_view(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
    }
    return render(request, 'blog.html', context)

def books_view(request):
    books = Books.objects.all()
    context = {
        "books" : books,
    }
    return render(request, 'books.html',context=context)

def portfolio_view(request):
    portfolio_item = PortfolioItem.objects.all()
    # context = {
    #   "portfolio" : portfolio,
    # }
    return render(request, 'portfolio_item.html', {'portfolio': portfolio_item})
