from django.shortcuts import render
from django.db.models import Q


from .models import Article


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def article_list(request):
    template_name = 'core/article_list.html'
    object_list = Article.objects.all()

    search = request.GET.get('search')

    if search:
        object_list = object_list.filter(
            Q(title__unaccent__icontains=search) |
            Q(subtitle__unaccent__icontains=search)
        )

    context = {'object_list': object_list}
    return render(request, template_name, context)
