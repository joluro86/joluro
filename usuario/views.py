# usuarios/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def list_users(request):
    users = User.objects.all()
    return render(request, 'usuario/list_users.html', {'users': users})

@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('list_users')
    else:
        form = UserCreationForm()
    return render(request, 'usuario/create_user.html', {'form': form})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('list_users')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'usuario/edit_user.html', {'form': form, 'user': user})

@login_required
def change_user_status(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    messages.success(request, f'User {user.username} is now {"active" if user.is_active else "inactive"}.')
    return redirect('list_users')

