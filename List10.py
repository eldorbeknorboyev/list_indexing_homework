def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    largest=list_num[0]
    if largest<list_num[-1]:
        largest=list_num[-1]
    return largest
print(main([5, 32, 1, 4, 3]))
print(main([12, 2, 5, 2, 7, 9, 1]))