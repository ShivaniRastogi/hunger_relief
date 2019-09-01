from hunger_app.model.restaurant import Restaurant
from hunger_app import ma
from hunger_app.schema.base import safe_execute


class RestaurantSchema(ma.ModelSchema):
    class Meta:
        model = Restaurant
        exclude = ('updated_at', 'created_at')