def zero_count_sorted2(sorted_numbers): # TODO
    step = 0
    total = 0

    for number in sorted_numbers:
        step = step + 1

        if number > 0:
            return total, step

        if number == 0:
            total = total + 1

    return total, step
