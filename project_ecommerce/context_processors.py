from items.models import Category

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}