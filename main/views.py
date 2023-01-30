from django.shortcuts import render
from .models import Chapter, Theme
from django.shortcuts import get_object_or_404

def index(request):
    themes  = Theme.objects.all().order_by("chapter__number").order_by("number")
    chapters  = Chapter.objects.all().order_by("number")
    return render(request, 'index.html', {"themes" : themes, "chapters" : chapters})

def theme_view(request, slug, option=""):
    print(option)
    main_theme = get_object_or_404(Theme, slug=slug)
    themes  = Theme.objects.all().order_by("chapter__number").order_by("number")
    chapters  = Chapter.objects.all().order_by("number")
    return render(request, "theme.html", {"main_theme" : main_theme, "themes" : themes, "chapters" : chapters})