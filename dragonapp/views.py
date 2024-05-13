from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from  django.contrib import messages
from django.views import generic
from django.views.decorators.http import require_POST
from .forms import EditProfileForm


from dragonapp.models import Movies, Categories
from django.http import HttpResponse
from dragonapp.forms import CategoryForm, MoviesForm


# Create your views here.
@login_required(login_url='login/')
def ShowAllProducts(request):
    products = Movies.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

@login_required(login_url='/')
def Addmovie(request):
    if request.method=="POST":
        movie_name=request.POST['movie']
        date=request.POST['r_date']
        actor=request.POST['actors']
        about=request.POST['desc']
        image=request.FILES['poster']
        movie_cat=request.POST['category']
        category=Categories.objects.get(id=movie_cat)
        m_link=slugify(movie_name)
        website=request.POST['websites']
        movie=Movies(movie=movie_name,release_date=date,actors=actor,description=about,poster=image,category=category,links=m_link,websites=website)
        movie.save()
        return redirect("dragonapp:all_movies")
    return render(request,'add-movie.html')

@login_required(login_url='/')
def AllMovies(request,c_link=None):
    if c_link!=None:
        cat=Categories.objects.get(slug=c_link)
        my_movies=Movies.objects.filter(category=cat)
    else:
      my_movies=Movies.objects.all()
    return render(request,"all-movies.html",{"movies":my_movies})

def Category(request):
    form=CategoryForm()
    return render(request,"category.html",{'form':form})

def ProductDetail(request,id):
    prod = Movies.objects.filter(id=id)
    return render(request,'productDetail.html',{'prod': prod})

def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Movies.objects.filter(movie__icontains=query)
            return render(request,'searchbar.html',{'products':products})
        else:
            print("No information")
            return request(request,'searchbar.html',{})



def Update(request, id, current_user=None):
    movie=Movies.objects.get(id=id)
    form=MoviesForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()

        fd = current_user.id
        if fd == movie:
            movie.delete()
        else:
            return redirect('/')
    return render(request,'update.html',{'form':form,'prod': movie})



@login_required
def Delete(request,id):
    if request.method == 'POST':
     event = Movies.objects.get(id=id)
     event.delete()
     return redirect('/')
    return render(request,'delete.html')





def register(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password= request.POST['password']

        if password == password:
            if User.objects.filter(username=username).exists():
                print('User Name Is Already Exist')
                return redirect('dragonapp:register')
            else:
                if User.objects.filter(email=email).exists():
                    print('Email Is Already Exist')
                    return redirect('dragonapp:register')
                else:
                    user =User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                    user.save()
                    messages.info(request, "Registration successfully")
                    return redirect('dragonapp:login')
        else:
            print('password did not match')
            return redirect('dragonapp:register')
    else:
        return render(request,'register.html')



def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print('Login successfully')
            return redirect('/')
        else:
            print('invalid credentials')
            return redirect('dragonapp:login')
    else:
        return render(request,'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logged out from websites....')
        return redirect('dragonapp:login')



def review_page(request):

    id = request.GET.get('id')
    item_details = item.objects.get(id=int(id))
    user = request.session['email']
    user_detail = username.objects.get(email=user)
    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        item_review = request.POST.get('item_review')

        item_reviews = review(user=user_detail, item=item_details, rating=star_rating, review_desp = item_review)
        item_reviews.save()

        rating_details = review.objects.filter(item=item_details)
        context = {'reviews': rating_details}
        return render(request, 'productDetail.html', context)

    rating_details = review.objects.filter(item=item_details)
    context = {'reviews': rating_details}
    return render(request, 'productDetail.html', context)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponse('Your profile is updated')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request,'edit_profile.html',{'form':form})



def categories(request):
    c=Movies.objects.all()
    return render(request,"categories.html",{'c':c})

# def update_user(request,id):
#     user = user.objects.get(id=id)
#     form = MoviesForm(instance=user)
#     if request.method == 'POST':
#         form = MoviesForm(request.POST,request.FILES,instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         context = {
#             "form":form
#         }
#         return render(request,'edit_profile.html',context)



# def c_update(request,id):
#     movie=Movies.objects.get(id=id)
#     if request.user == movie.id:
#         movie.update()
#         messages.success(request,"movie deleted")
#         return redirect('/')
#     else:
#         messages.success(request,'You cant access')
#         return redirect('/')
#     return render(requests,'c_page.html',{'movie':movie})
#


    # movie = Movies.objects.get(id=id)
    # if request.user == movie.category:
    #     movie.update()
    #     messages.success(request, "movie deleted")
    #     return redirect('/')
    # else:
    #     messages.success(request, 'You cant access')
    #     return redirect('/')

    # @login_required
    # def Delete(request, id):
    #     current_user = request.User.id
    #     post = Movies.objects.filter(id=id)
    #     if request.method == 'POST':
    #         all = current_user == post
    #         all.delete()
    #
    #         return HttpResponse("post edited successfully")
    #     else:
    #         # return HttpResponse("you are not authorised")
    #         return render(request, 'delete.html')

    # def Delete(request, id):
    #     post = get_object_or_404(Movies, id=id)
    #     if request.GET[Movies.category] == Movies.category:
    #         post.delete()
    #         return redirect('/')
    #     else:
    #         return render(request, 'delete.html')
