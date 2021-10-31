from django import forms

class AddForm(forms.Form):
    reps = forms.IntegerField()
    tasksn = forms.IntegerField()
 #   tasks = forms.CheckboxSelectMultiple()
    worktime = forms.IntegerField()
    resttime = forms.IntegerField()
