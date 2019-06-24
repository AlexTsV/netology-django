from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    def clean_review(self):
        text = self.cleaned_data.get('text')
        if not text:
            raise forms.ValidationError("Нельзя оставить пустой отзыв")

        return text

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
