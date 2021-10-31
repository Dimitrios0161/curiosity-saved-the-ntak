def find_product3(inputs: List[int]) -> int:
    """
    Find the two elements that add up to 2020
    and return their product
    """
    needs = {2020 - i - j: (i, j)
             for i in inputs
             for j in inputs
             if i != j}

    for i in inputs:
        if i in needs:
            j, k = needs[i]
            return i * j * k

assert find_product3(INPUTS) == 241861950