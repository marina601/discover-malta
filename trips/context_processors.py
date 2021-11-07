# pylint: disable=no-member
from .models import Category


def menu_links(request):
    """Get links to all categories"""
    links = Category.objects.all()
    return dict(links=links)
