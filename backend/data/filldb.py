import json

from django.db import transaction

from recipes.models import Ingredient

json_file_path = ('data/ingredients.json')

with open(json_file_path, encoding='utf-8') as f:
    data = json.load(f)

    with transaction.atomic():
        for item in data:
            ingredient = Ingredient.objects.get_or_create(
                name=item['name'],
                measurement_unit=item['measurement_unit']
            )
