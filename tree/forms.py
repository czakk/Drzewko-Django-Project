from django import forms
from .models import Tree, Branch


class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ('creator', 'title', 'public')


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('title', 'url',)
