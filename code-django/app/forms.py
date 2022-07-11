from django import forms
from django.forms import ModelForm
from .models import file


# create a file form
class fileForm(ModelForm):
    class Meta:
        model = file
        # fields = ('nameOfFile', 'nameOfLectures',
        #           'fields', 'usedFor', 'difficultyLevel', 'comment', 'sourceOfProblem', 'author', 'typeOfProblem', 'intendedLearningOutcome', 'purposeOfFile', 'grading')
        fields = ("__all__")

        labels = {
            'nameOfFile': '',
            'nameOfLectures': '',
            'fields': '',
            'file_upload': '',
            'usedFor': '',
            'difficultyLevel': '',
            'comment': '',
            'sourceOfProblem': '',
            'author': '',
            'typeOfProblem': '',
            'intendedLearningOutcome': '',
            'purposeOfFile': '',
            'grading': '',
        }

        widgets = {
            'nameOfFile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the file name'}),
            'nameOfLectures': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the lecture name'}),
            'fields': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the field name'}),
            'usedFor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is this file used for?'}),
            'difficultyLevel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the difficulty level'}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Any comment for the file'}),
            'sourceOfProblem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Where is the source of the problem taken from?'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author of the file'}),
            'typeOfProblem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type of problem ex. Numerical/Theoretical'}),
            'intendedLearningOutcome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Learning Outcome'}),
            'purposeOfFile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purpose of the file ex. Exams, Homeworks'}),
            'grading':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Grading'})
        }
