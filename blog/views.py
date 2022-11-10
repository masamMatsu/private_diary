from django.views import generic

from .forms import PostForm

class TopView(generic.TemplateView):
    template_name = "top.html"


class PostView(generic.FormView):
    template_name = "post.html"
    form_class = PostForm

