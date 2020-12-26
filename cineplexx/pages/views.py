from django.shortcuts import render
from .forms import SnippetForm


def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()

    form = SnippetForm()
    return render(request, 'pages/index.html', {'form': form})
