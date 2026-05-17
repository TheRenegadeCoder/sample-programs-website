def pluralize(count: int, singular: str, plural: str | None = None) -> str:
    """Pluralize an item

    :param count: Count of number of items
    :param singular: Singular form of item
    :param plural: Plural form of item. If None, use singular plus an "s"
    :return: Pluralized item
    """
    if plural is None:
        plural = f"{singular}s"

    return singular if count == 1 else plural
