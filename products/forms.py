from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, UserReview
from django.forms import Textarea

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-4'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = UserReview
        fields = ['title', 'content']
        widgets = {
            'content': Textarea(attrs={'cols': 40, 'rows': 10})
        }
