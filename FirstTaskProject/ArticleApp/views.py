from ast import Return
from django.shortcuts import render
from .forms import Article
from .models import Articles
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date


def index(request):
    if request.method == "POST":
        article = Articles()
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.dateOfCreation = date.today()
        article.save()
        return HttpResponseRedirect("/")
    else:
        articles = Articles.objects.all().filter(isArchive=False)
        articleForm = Article()
        return render(request, "index.html", {"form": articleForm, "articles": articles})

def delete(request, id):
    try:
        article = Articles.objects.get(id=id)
        article.delete()
        return HttpResponseRedirect("/")
    except Articles.DoesNotExist:
        return  HttpResponseRedirect("/")

def edit(request, id, title, content):
    articleForm = Article(initial={"title": title, "content": content}) 
    if request.method == "POST":
        try:
            article = Articles.objects.get(id=id)
            article.title = request.POST.get("title")
            article.content = request.POST.get("content")
            article.save() 
        except:
            pass           
    else:      
        return render(request, "edit.html", {"form": articleForm})
    return HttpResponseRedirect("/")

def archive(request, id=0):
    if request.method == "POST":
        article = Articles.objects.get(id=id)
        article.isArchive = True
        article.save()
        return HttpResponseRedirect("/")
    else:
        articles = Articles.objects.all().filter(isArchive=True)
        articleForm = Article()
        return render(request, "archives.html", {"form": articleForm, "articles": articles})