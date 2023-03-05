from django import forms


class AskForm(forms.Form):
    ask_gpt = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}))

    class Meta:
        fields = ('ask_gpt',)
