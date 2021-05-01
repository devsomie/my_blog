from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post, Prediction


# Create your views here.
def index(request):
    posts = Post.objects.all( )
    return render(request, 'main/index.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post', slug=post.slug)
    else:
        form = CommentForm()
      
    return render(request, 'main/post.html', {'post': post,'form': form})

def predictions(request):
    predictions = Post.objects.all( )
    return render(request, 'main/predictions.html',{'predictions': predictions})

# def comments(request):
#     return redirect('post_detail')

# def (request):
#     movies = Movie.objects.all() #queryset containing all movies we just created
# 	paginator = Paginator(movies, 3)
# 	page_number = request.GET.get('page')
# 	page_obj = paginator.get_page(page_number)
# 	return render(request=request, template_name="main/movies.html", context={'movies':page_obj})
