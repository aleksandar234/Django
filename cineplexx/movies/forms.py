from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField()

    choice1 = forms.CharField(required=False)
    choice2 = forms.CharField(required=False)
    choice3 = forms.CharField(required=False)
