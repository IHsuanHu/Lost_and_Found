from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lost_Post
from django.urls import reverse_lazy


# Create your views here.
 
def home(request):
    return render(request,"home.html")

def lost(request):
    context={
        'Lost_Posts':Lost_Post.objects.all()
    }
    return render(request,"/lost_post_list.html", context)


class PostListView(ListView):
    model = Lost_Post
    template_name = 'lost_post_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Lost_Posts'
    ordering = ['-date_posted']
    paginate_by = 10
    
class PostDetailView(DetailView):
    model = Lost_Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Lost_Post
    template_name = 'post_form.html'
    fields = ['Lost_item','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Lost_Post
    template_name = 'post_form.html'
    fields = ['Lost_item','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        Lost_Post = self.get_object()
        if self.request.user == Lost_Post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lost_Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('lost_post_list')

    def test_func(self):
        Lost_Post = self.get_object()
        if self.request.user == Lost_Post.author:
            return True
        return False

    

