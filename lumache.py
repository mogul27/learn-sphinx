def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings

    :param kind: Optional "kind" of ingredients
    :type kind: list[str] or None
    :return: The ingredients list
    :raise lumache.InvalidKindError: If the kind is invalid.
    :rtype: list[str]
    
    """
    return ["shells", "gorgonzola", "parsley"]

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

# Changes made for re-push