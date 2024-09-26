from django.shortcuts import render

from .models import Post

# Create your views here.
def homeView(request):
    post_list = Post.objects.all()
   
    # for post in post_list:
    #     print(post.body)
    

    return render(request, 'index.html', {
        'post': post_list,
        'test': 'this is the testing message'
    })