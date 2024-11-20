def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate the BMI for each weight-height pair.

    Args:
    - weights (list of float or int): List of weights in kilograms or pounds.
    - heights (list of float or int): List of heights in meters or inches.

    Returns:
    - list of float: List of calculated BMI values.
    """
    if (len(height) != len(weight)):
        raise ValueError("The length of the height and weight lists should be the same.")
    
    if not all(isinstance(h, (int, float)) for h in height):
        raise ValueError("The elements of the height list should be integers or floats.")
    
    if not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("The elements of the weight list should be integers or floats.")

    if (type(height) != list or type(weight) != list):
        raise ValueError("The input should be a list.")
    
    if (len(height) == 0):
        raise ValueError("The list should not be empty.")

    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / height[i] ** 2)
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    A function that accepts a list of integers or floats and an integer representing a limit as parameters.

    Args:
    - bmi (list of float or int): List of BMI values.
    - limit (int): A limit to compare the BMI values with.

    Returns:
    - list of bool: A list of boolean values indicating whether the BMI values are greater than the limit.
    """
    if type(bmi) != list:
        raise ValueError("The input should be a list.")

    if type(limit) != int:
        raise ValueError("The limit should be an integer.")

    if (len(bmi) == 0):
        raise ValueError("The list should not be empty.")

    result = []
    for i in range(len(bmi)):
        if bmi[i] > limit:
            result.append(True)
        else:
            result.append(False)
    return result
