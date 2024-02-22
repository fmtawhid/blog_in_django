from django.shortcuts import render,get_object_or_404, redirect     
from django.contrib.auth import authenticate, login, logout     # Account Releted Package   
from django.contrib.auth.models import User     # Account Package Import
from .models import *   # Custom Models Impost
from django.core.paginator import Paginator     # Pagination Package Import
from django.db.models import Q      # Query Package Import
from .form import createAuthor, createForm,Usercreate
from django.contrib import messages
 
# Homa page Function
def index(request):
    post = article.objects.all()
    cat = catagory.objects.all()

    #search function
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
            
        )

    # Paginator function
    paginator = Paginator(post, 2)  
    page_number = request.GET.get("page")
    total_article = paginator.get_page(page_number)
    context = {
        'post':total_article,
        'cat':cat,
        'search':search
    }
    return render(request, 'index.html', context)

# author function
def getauthor(request, name):
    post_author = get_object_or_404(User, username = name)
    author = get_object_or_404(auth, name=post_author.id)
    post = article.objects.filter(article_auth = author)
    ccoo = post.count()
    
    # Paginator function
    paginator = Paginator(post, 2)  
    page_number = request.GET.get("page")
    total_article = paginator.get_page(page_number)
    
    context = {
        "author":author,
        "post":total_article,
        'ccoo':ccoo
    }
    return render(request, 'profile.html' , context)


# Single Post Function
def getsingle(request, id):
    post = get_object_or_404(article, pk = id)
    fast = article.objects.first()
    last = article.objects.last()
    releted = article.objects.filter(catagory=post.catagory). exclude(id=id)[:4]
    context = {
        'post':post,
        'fast':fast,
        'last':last,
        'releted':releted, 
    }
    return render(request, 'single.html', context)


# Catagory Function
def gettopic(request, catagory_name):
    cat = get_object_or_404(catagory, catagory_name=catagory_name)
    post = article.objects.filter(catagory=cat.id)

    # Paginator function
    paginator = Paginator(post, 2)  
    page_number = request.GET.get("page")
    total_article = paginator.get_page(page_number)
    context = {
        'post':total_article,
    }
    return render(request, 'catagory.html', context )


# login Function
def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect(index)
            else:
                messages.add_message(request, messages.INFO, "Hello world.")
                return render(request, 'login.html')
    return render(request, 'login.html')

# logout Function
def getLogout(request):
    logout(request)
    return redirect(index)



def getcreate(request):
    if request.user.is_authenticated:
        u=get_object_or_404(auth, name=request.user.id)  # Get the currently logged-in user
        form = createForm(request.POST or None, request.FILES or None) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_auth = u
            instance.save()
            return redirect("index")
        
        context = {
            'form': form
        }
        return render(request, "create.html", context)
    else:
        return redirect("login")
    
# Update Post
def getUpdate(request, pid):
    if request.user.is_authenticated:
        u=get_object_or_404(auth, name=request.user.id)  # Get the currently logged-in user
        post = get_object_or_404(article, id=pid)
        form = createForm(request.POST or None, request.FILES or None, instance=post ) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_auth = u
            instance.save()
            messages.success(request, 'Article is updated')
            return redirect("profile")
        context = {
            'form': form
        }
        return render(request, "create.html", context)

    else:
        return redirect("login")
    


# Delete Post
def getDelete(request, pid):
    if request.user.is_authenticated:
        post = get_object_or_404(article, id=pid)
        post.delete()
        return redirect("profile")
       
    else:
        return redirect("login")
    




def getProfile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        author_profile = auth.objects.filter(name=user.id)
        if author_profile:
            authorUser = get_object_or_404(auth, name=request.user.id)
            post = article.objects.filter(article_author=authorUser.id)
            return render(request, 'logged_in_profile.html', {"post": post, "user": authorUser})
        else:
            form = createAuthor(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.name = user
                instance.save()
                messages.success(request, 'Author profile is created successfully')
                return redirect('profile')
            return render(request, 'createauthor.html', {"form": form})

    else:
        return redirect('login')






def getprofile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(auth, name=request.user.id)
        post = article.objects.filter(article_auth=request.user.id)
        context={
            'post':post,
            'user':user,
        }
        return render(request, 'log_profile.html', context)
    else:
        return redirect('login')
    

def signUp(request):
    form = Usercreate(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Registration successfully completed')
        return redirect('login')
    return render(request, 'sign_up.html', {"form": form})
