from django_filters import AllValuesMultipleFilter, rest_framework
from django_filters.widgets import BooleanWidget
from recipes.models import Recipe
from rest_framework.filters import SearchFilter


class IngredientSearchFilter(SearchFilter):
    search_param = 'name'


class RecipeFilter(rest_framework.FilterSet):
    is_in_shopping_cart = rest_framework.BooleanFilter(widget=BooleanWidget())
    is_favorited = rest_framework.BooleanFilter(widget=BooleanWidget())
    tags = AllValuesMultipleFilter(field_name='tags__slug')
    author = AllValuesMultipleFilter(field_name='author__id')

    class Meta:
        model = Recipe
        fields = ['author__id', 'tags__slug']
