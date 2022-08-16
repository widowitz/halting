import math
import random


def generate_random_cards(n, minimum, maximum):
    """
    returns a list of n random numbers
    """
    return_value = random.sample(range(minimum, maximum + 1), n)
    return(return_value)


def make_selection(numbers, strategy = 1):
    """
    applies a given strategy to the passed numbers;
    returns the number selected as a result

    params:
        numbers: list of integers
        strategy: numerical id of the strategy to be applied
            strategy == 1: 
                sample the first (n / e) numbers, then select the next
                number that is higher than that
                (e.g., if there are 100 numbers, 100/e == 100/2.7 == 37)
            so far no other strategies implemented

    return value:
        an integer value, the ultimately selected number
    """
    assert strategy in [1, 2], "Strategy not implemented" 
    length = len(numbers)
    assert length > 1, "Need to have at least two cards for this game to make sense"
    if (strategy == 1):
        if (length == 2): # just stop at the very first card, it's 50:50 anyway
            return(numbers[0])
        sample_size = round(length / math.e)
        training_sample = numbers[:sample_size]
        remainder = numbers[sample_size:]
        threshold = max(training_sample)
        filtered_list = list(filter(lambda x: x > threshold, remainder))
        selection = filtered_list[0] if filtered_list else remainder[-1] 
        return(selection)
    if (strategy == 2):
        if (length == 2): # just stop at the very first card, it's 50:50 anyway
            return(numbers[0])
        sample_size = round(length / 2)
        training_sample = numbers[:sample_size]
        remainder = numbers[sample_size:]
        threshold = max(training_sample)
        filtered_list = list(filter(lambda x: x > threshold, remainder))
        selection = filtered_list[0] if filtered_list else remainder[-1] 
        return(selection)
    return # should never be reached


if __name__ == "__main__":
    NUMBER_OF_CARDS = 100
    MAXIMUM_VALUE = 100000
    MINIMUM_VALUE = 1
    ITERATIONS = 100000
    META_ITERATIONS = 500
    for _ in range(META_ITERATIONS):
        attempts = 0
        successes = 0
        for _ in range(ITERATIONS):
            attempts = attempts + 1
            cards = generate_random_cards(NUMBER_OF_CARDS, MINIMUM_VALUE, MAXIMUM_VALUE)
            selected = make_selection(cards, 2)
            optimum = max(cards)
            if (selected == optimum):
                successes = successes + 1
        print(f'Success rate {successes / attempts:.3f} ({attempts} attempts, {successes} successful)')

