from django import forms
from cards.models import Card


class CardForm(forms.ModelForm):
	description = forms.CharField(label='', max_length=140, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
	image = forms.ImageField(label='', required=True)

	class Meta:
		model = Card
		fields = ['description', 'image']
