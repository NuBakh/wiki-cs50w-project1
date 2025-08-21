from django.shortcuts import render, redirect
import markdown2
from . import util
import random
from django import forms

page=[]

class NewPageForm(forms.Form):
    title=forms.CharField(label="Title")
    body = forms.CharField(widget=forms.Textarea)
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, title):
    
    content= util.get_entry(title)
    if content is None:
        
        return render(request,"encyclopedia/not_found.html", {
            "title": title
        }) 
        
    html_content= markdown2.markdown(content)   
    return render(request, "encyclopedia/entry.html",{
        "title":title,
        'html_content':html_content
    })





def random_page(request):
    entries = util.list_entries()
    choice = random.choice(entries)
    return redirect("entry", title=choice)


def search(request):
    entries = util.list_entries()
    if request.method== "GET":
        param=request.GET.get("q")
        if param:
            for entry in entries:
                if param.lower()== entry.lower():
                     return redirect("entry", title=entry)
            result=[entry for entry in entries if param.lower() in entry.lower()]
            print(result)

            if result:
                return render(request, "encyclopedia/search.html",{
                           "results": result,
                           "param": param
                        })
    return render(request, "encyclopedia/not_found.html", {
        "title": param
    })
    
    
    
def new_page (request):
    if request.method=="POST":
        form=NewPageForm(request.POST)
        if  form.is_valid():
            body=form.cleaned_data["body"]
            title=form.cleaned_data["title"]
            
            request.session["title"]= title
            request.session["body"]= body
                
            
            if title in util.list_entries():
                return render(request, "encyclopedia/new_page.html", {
                    "form": form,
                    "error": "This title already exists."
                })
            
            else:
                util.save_entry(title, body)
            
                return redirect("entry", title=title)
        else:

            return render(request, "encyclopedia/new_page.html", {
                "form": form
            })
        
    
    return render(request, "encyclopedia/new_page.html",{
            "form": NewPageForm()
        })
    
    
    
def edit(request, title):
    existing_data = util.get_entry(title)

    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data["body"]
            util.save_entry(title, body)  # title və body göndərilir
            return redirect("entry", title=title)
    else:
        form = NewPageForm(initial={'title': title, 'body': existing_data})

    return render(request, "encyclopedia/new_page.html", {"form": form})

        
    
      
    
            
        
   
            
            
        
       
    
