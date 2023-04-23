from django.shortcuts import render
from forum.models import Post
from forum.forms import PostForm
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def show_forum(request):
    post_data = Post.objects.all()
    #answer_data = Answer.objects.all()
    user = request.user

    context = {
        'list_of_post': post_data,
        #'list_of_answers': answer_data,
        'username': user.username,
    }
    
    return render(request, 'forum.html', context)

@csrf_exempt
def create_forum_ajax(request):
    form = PostForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        data = Post.objects.last()

        result = {
            'username' : data.user.username,
            'id': data.id, 
            'date': data.date,
            'title': data.title,
            'content': data.content 
            }
        
        return JsonResponse(result)
    
    context = {'form': form}
    return render(request, "create_post.html", context)
    
def delete_forum(request, id):
    post = Post.objects.get(pk=id)
    post.delete()

    return HttpResponseRedirect(reverse('forum:show_forum'))

def get_post_json(request):
    data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
