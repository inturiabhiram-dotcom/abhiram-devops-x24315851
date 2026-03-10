"""Filters for food search functionality."""
from .models import Food
import django_filters
from django_filters import CharFilter

class FoodFilter(django_filters.FilterSet):
    """Filter class for searching food items."""

    food_name = CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label="search food items"
    )

    class Meta:
        """Meta configuration for FoodFilter."""

        model = Food
        fields = ["food_name"]
        