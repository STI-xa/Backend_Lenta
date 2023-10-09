from rest_framework import mixins


class CreateRetrieveMixin(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin
):
    """Кастомный миксин - create / retrieve."""
    pass
