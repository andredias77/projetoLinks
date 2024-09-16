from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import AmazonLink
from .models import PaginaProduto
from .models import Link

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "bio")


class AmazonLinkForm(forms.ModelForm):
    class Meta:
        model = AmazonLink
        fields = ['product_name', 'amazon_link']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'amazon_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

class PaginaProdutoForm(forms.ModelForm):
    class Meta:
        model = PaginaProduto
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['nome_produto', 'url']  