def slice_me(family: list, start: int, end: int) -> list:
    """
    A function that takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments.

    Args:
    - family: a 2D array
    - start: an integer
    - end: an integer

    Returns:
    - a truncated version of the array
    """
    if family.__class__ != list:
        raise TypeError("The input should be a list")

    for i in family:
        if i.__class__ != list:
            raise TypeError("The input should be a 2D list")
        if len(i) != len(family[0]):
            raise ValueError("The lists should have the same length")

    print(f"My shape is : ({len(family)},{len(family[0])})")
    print(f"My new shape is : ({len(family[start:end])},{len(family[0])})")
    
    return family[start:end]