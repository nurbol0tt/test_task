from django.urls import path
from blog.views import views_article
from blog.views import views_category


urlpatterns = [
    path("", views_article.HomeView.as_view(), name="home"),
    path("create_post/", views_article.ArticleCreateView.as_view(), name="article_create"),
    path("<int:pk>/detail/", views_article.ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/update/", views_article.ArticleUpdateView.as_view(), name="article_update"),
    path("<int:pk>/delete/", views_article.ArticleDeleteView.as_view(), name="article_delete"),

    path("categories/", views_category.CategoryView.as_view(), name="categories"),
    path("create_category/", views_category.CategoryCreateView.as_view(), name="category_create"),
    path("category/<int:id>/detail/", views_category.CategoryDetailView, name="category_detail"),
    path("category/<int:pk>/update/", views_category.CategoryUpdateView.as_view(), name="category_update"),
    path("category/<int:pk>/delete/", views_category.CategoryDeleteView.as_view(), name="category_delete"),

]