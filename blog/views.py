from django.shortcuts import render


def blog_view(request):
    return render(request, 'light/blog-post.html')
