import django_redis.cache
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tree, Branch
from .forms import TreeForm, BranchForm
from django.core.cache import cache
from django_redis import get_redis_connection


# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def tree_list(request):
    trees = Tree.objects.filter(public=True)[:5]
    return render(request,
                  'forest/tree/list.html',
                  {'trees': trees})


def tree_detail(request, title, unique_id):
    tree = get_object_or_404(Tree, unique_id=unique_id, title=title)
    return render(request, 'forest/tree/tree_detail.html', {'tree': tree})


def tree_detail_edit(request, title, unique_id):
    tree = get_object_or_404(Tree, unique_id=unique_id, title=title)
    branches = tree.branches
    user = get_client_ip(request)
    if cache.get(tree.unique_id) != user:
        return redirect(tree.get_unique_id())
    else:
        if request.method == 'POST':
            branch_form = BranchForm(data=request.POST)
            if branch_form.is_valid():
                new_branch = branch_form.save(commit=False)
                new_branch.tree = tree
                new_branch.save()
        else:
            branch_form = BranchForm()
        return render(request, 'forest/tree/tree_detail_edit.html',
                      {'tree': tree, 'branches': branches, 'branch_form': branch_form})


def create_tree(request):
    if request.method == 'POST':
        tree_form = TreeForm(request.POST)
        if tree_form.is_valid():
            new_tree = tree_form.save()
            user = get_client_ip(request)
            cache.set(new_tree.unique_id, user)
            return redirect(new_tree.get_unique_id())
    else:
        tree_form = TreeForm()
    return render(request, 'forest/tree/create_tree.html', {'tree_form': tree_form})
