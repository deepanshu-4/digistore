from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from . import util
from django.contrib.auth.decorators import login_required
import markdown2
import random as rd
@login_required
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
@login_required
def createpage(request):
    if request.method=='POST':
        title=request.POST.get('inpt')
        content=request.POST.get('area')
        # print(title,content)
        if(len(title)==0 or len(content)==0):
            return redirect('/create')
        if(title not in util.list_entries()):
            util.save_entry(title,content)
            return redirect('wiki/'+title)
        else:
            messages.error(request, 'Title exists')
            return render(request, "encyclopedia/create.html", {
                "entries": util.list_entries(),
                "message":messages
            })

    return render(request, "encyclopedia/create.html", {
        "entries": util.list_entries()
    }) 
@login_required    
def editpage(request):
    if request.method=='POST':
        title=request.POST.get('inpt')
        content=request.POST.get('area')
        # print(title,content)
        if(len(title)==0 or len(content)==0):
            return redirect('/editpage')
        util.save_entry(title,content)
        return redirect('wiki/'+title)
    return render(request, "encyclopedia/create.html", {
        "entries": util.list_entries()
    }) 
@login_required
def random(request):
    x=util.list_entries()
    y=rd.choice(x)
    return redirect('wiki/'+y)
@login_required
def wiki(request,title):
    x=util.get_entry(title)
    if(title not in util.list_entries()):
        return HttpResponse("<h1>Page not exist</h1>")
    html=markdown2.markdown(x)
    # print(html)
    return render(request, "encyclopedia/wiki.html", {
        "get":html,
        "entries": util.list_entries(),
        "title":title
    })
@login_required    
def edit(request,title):
    x=util.get_entry(title)
    return render(request, "encyclopedia/editpage.html", {
        "get":x,
        "entries": util.list_entries(),
        "title":title
    })
@login_required
def search(request):
    title = request.GET.get('q')
    x=util.list_entries()
    # print(x)
    a=[]
    for i in x:
        if(title==i):
            return redirect('/wiki/'+title)
            break
        elif title in i:
            a.append(i)
    if(len(a)==0):
        return HttpResponse("<h1>Result not  found</h1>")

    return render(request,"encyclopedia/random.html",{
        "a":a
        })    
            


