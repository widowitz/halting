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


def make_selection_based_on_sampling(numbers, sample_size):
    """
    makes a selection by sampling,
    i.e. look at the first <sample_size> numbers,
    then pick the next larger one

    params:
        numbers: list of integers
        sample_size: how many of these will be looked at before making decision

    return value:
        an integer value, the ultimately selected number
    """
    length = len(numbers)
    assert length > 1, "Need to have at least two cards for this game to make sense"
    assert sample_size < length, "Training sample must be smaller than number of cards"
    if (length == 2): # just stop at the very first card, it's 50:50 anyway
        return(numbers[0])
    training_sample = numbers[:sample_size]
    remainder = numbers[sample_size:]
    threshold = max(training_sample)
    filtered_list = list(filter(lambda x: x > threshold, remainder))
    selection = filtered_list[0] if filtered_list else remainder[-1] 
    return(selection)
    

if __name__ == "__main__":
    NUMBER_OF_CARDS = 100
    MAXIMUM_VALUE = 100000
    MINIMUM_VALUE = 1
    ITERATIONS = 5000
    optimum_sample_size = None
    optimum_result_achieved = 0
    for sample_size in range(1, NUMBER_OF_CARDS):
        attempts = 0
        successes = 0
        print(f"Sample size: {sample_size}:")
        for _ in range(ITERATIONS):
            attempts = attempts + 1
            cards = generate_random_cards(NUMBER_OF_CARDS, MINIMUM_VALUE, MAXIMUM_VALUE)
            selected = make_selection_based_on_sampling(cards, sample_size)
            optimum = max(cards)
            if (selected == optimum):
                successes = successes + 1
        success_rate = successes / attempts
        print(f' Success rate {success_rate:.3f} ({attempts} attempts, {successes} successful)')
        if (success_rate > optimum_result_achieved):
            optimum_result_achieved = success_rate
            optimum_sample_size = sample_size
    print(f"Optimum sample size: {optimum_sample_size}, achieved success rate: {optimum_result_achieved:.3f}")

