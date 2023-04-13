from django import forms

from blog.models import Article, Category


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = (
            'title',
            'description',
            'image',
            'user_id',
            'category_id'
        )

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'This is Title Placeholder'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'This is Title Description'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'user_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': '',
                    'id': 'elder',
                    'type': 'hidden'
                }
            ),
            'category_id': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class ArticleUpdateForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = (
            'title',
            'description',
            'category_id',
            'image'
        )

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'This is Title Placeholder'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'This is Title Description'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category_id': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title',)

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'This is Title Placeholder'
                }
            ),
            }