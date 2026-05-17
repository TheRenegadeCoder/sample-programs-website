def select(count: int, singular: str, plural: str) -> str:
    """Return the correct word form based on count.

    Args:
        count: Number used to determine grammatical number.
        singular: Form used when count == 1.
        plural: Form used when count != 1.

    Returns:
        `singular` if count == 1, otherwise `plural`.

    """
    return singular if count == 1 else plural


def pluralize(count: int, singular: str, plural: str | None = None) -> str:
    """Return the appropriate singular or plural form based on a count.

    If `plural` is not provided, it defaults to the singular form plus "s".

    Args:
        count: Number of items used to determine grammatical form.
        singular: Singular form of the word.
        plural: Optional explicit plural form of the word. If None,
            defaults to `singular + "s"`.

    Returns:
        The correct form (singular or plural) based on `count`.

    """
    return select(count, singular, plural or f"{singular}s")


def is_are(count: int) -> str:
    """Return the correct form of the verb "to be" based on count.

    Args:
        count: Number used to determine grammatical number.

    Returns:
        "is" if count is 1, otherwise "are".

    """
    return select(count, "is", "are")
