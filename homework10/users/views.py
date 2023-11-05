from django.shortcuts import render, redirect

from .forms import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:index')
        else:
            return render(request, 'registration/register.html', context={"form": form})

    return render(request, 'registration/register.html', context={"form": RegisterForm()})