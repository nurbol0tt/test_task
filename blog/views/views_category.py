from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CategoryForm
from blog.models import Article, Category


class CategoryView(generic.ListView):
    model = Category
    template_name = "category/category.html"


class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/category_create.html"


def CategoryDetailView(request, id):
    category = get_object_or_404(Category, id=id)
    category_article = Article.objects.filter(category_id=category)
    return render(request, 'category/category_detail.html', {'articles': category_article})


class CategoryUpdateView(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/category_update.html"


class CategoryDeleteView(generic.DeleteView):
    model = Category
    template_name = "article/article_delete.html"
    success_url = reverse_lazy("home")
