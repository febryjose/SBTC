from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Please Enter Your Name'}))
    contactno = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please Enter Your Contact Number'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please Enter Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Please enter your message here'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'textbox'})
        self.fields['contactno'].widget.attrs.update({'class' : 'textbox'})
        self.fields['email'].widget.attrs.update({'class' : 'textbox'})
        self.fields['message'].widget.attrs.update({'class' : 'textarea'})
