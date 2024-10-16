# library/forms.py
from django import forms
from .models import Book
from .models import Transaction
from django.contrib.auth.forms import AuthenticationForm

# library/forms.py



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'serial_no', 'book_type']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter book title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control', 
                'readonly': 'readonly'  # To make it non-editable
            }),
            'serial_no': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter serial number'
            }),
            'book_type': forms.Select(attrs={
                'class': 'form-control'
            })
        }

    def clean_serial_no(self):
        serial_no = self.cleaned_data.get('serial_no')
        if not serial_no.isdigit():
            raise forms.ValidationError("Serial number must be numeric.")
        return serial_no


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)



# library/forms.py



class IssueBookForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['book', 'issue_date', 'return_date']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }
