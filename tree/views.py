from django.shortcuts import render, get_object_or_404, redirect
from .models import Tree, Branch
from .forms import TreeForm
from django.urls import reverse


# Create your views here.


def tree_list(request):
    trees = Tree.objects.filter(public=True)[:5]
    return render(request,
                  'forest/tree/list.html',
                  {'trees': trees})


def tree_detail(request, title, unique_id):
    tree = get_object_or_404(Tree, unique_id=unique_id, title=title)
    return render(request, 'forest/tree/tree_detail.html', {'tree': tree})


def create_tree(request):
    if request.method == 'POST':
        tree_form = TreeForm(request.POST)
        if tree_form.is_valid():
            new_tree = tree_form.save()
            return redirect(new_tree.get_unique_id())
    else:
        tree_form = TreeForm()
    return render(request, 'forest/tree/create_tree.html', {'tree_form': tree_form})
