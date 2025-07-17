from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(
        max_length=200,
        label="Nom",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre nom'
        })
    )
    
    prenom = forms.CharField(
        max_length=200,
        label="Prénom",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre prénom'
        })
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'exemple@email.com'
        })
    )

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Votre message ici...'
        })
    )
