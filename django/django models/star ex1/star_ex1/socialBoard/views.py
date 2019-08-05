from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    messages = ["post:"]
    for post in Post.objects.all():
        messages.append(str(post))
        return HttpResponse("<br>".join(messages));