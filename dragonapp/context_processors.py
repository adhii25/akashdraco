from dragonapp.models import Categories


def MovieCategories(request):
    categories=Categories.objects.all()
    return dict(movie_cat=categories)
