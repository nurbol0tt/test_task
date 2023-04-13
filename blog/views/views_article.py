from django.urls import reverse_lazy
from django.views import generic

from blog.forms import ArticleForm, ArticleUpdateForm
from blog.models import Article


class HomeView(generic.ListView):
    model = Article
    template_name = "home.html"


class ArticleCreateView(generic.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/create_post.html"

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Save the image
        form.instance.image = form.cleaned_data['image']

        return super().form_valid(form)


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "article/article_detail.html"


class ArticleUpdateView(generic.UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = "article/article_update.html"


class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = "article/article_delete.html"
    success_url = reverse_lazy("home")


