from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
    # MODEL
class DateInput(forms.DateInput):
    input_type = 'date'
    
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "User Name ..."
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Password..."
            })
    )

class SignupForm(UserCreationForm):
    firstname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "First Name......."
        }))
    lastname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Last Name............."
        }))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "User Name ..."
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Email....."
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Password...."
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Confirm Password..."
        }
    ))
    dept = forms.CharField(
        widget=forms.Select(
            choices=Dept,
            attrs={
                'class': 'form-control'
            }
            ))
    year = forms.CharField(
        widget=forms.Select(
            choices=Year,
            attrs={
                'class': 'form-control'
            }
            ))
    semester = forms.CharField(
        widget=forms.Select(
            choices=Sem,
            attrs={
                'class': 'form-control'
            }
            ))
    enrollment = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enrollment Number.."
            }
            ))

    profilepic = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                # 'class': 'custom-file-input',
                'id': "customFile",
                'onchange': "readURL(this);",
                'style': "display: none;",
            }
        ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'dept', 'year', 'semester',
                  'enrollment', 'profilepic', 'status', 'is_cdc', 'is_teacher', 'is_student')
        """ widgets = {
            'password1': forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Password"})),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Email"}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Debasish"}),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Confirm Passowrd"}),
        } """

class CategoryManagement(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Category Name..."
            }))

    class Meta:
        model = QuestionCategory
        fields = ('name', 'owner', 'status')


class QuestionManagement(forms.ModelForm):
    question = forms.Textarea()

    class Meta:
        model = Question
        fields = ('question', 'questioncategory',
                  'owner', 'status', 'postedtime')


class AnswerManagement(forms.ModelForm):
    answer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': "Provide your Answers Here..................and press Enter button on your Device"
            }))

    class Meta:
        model = Answer
        fields = ('answer', 'questionid',
                  'solver', 'answertime', 'status')

