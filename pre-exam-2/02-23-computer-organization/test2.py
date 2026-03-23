def predator_prey(moose_pop, wolf_pop, num_months, steps_per_month):
    """ Write a docstring here.

    """
    birth_rate_moose = 0.5      # b_M
    death_rate_moose = 0.02     # d_M
    birth_rate_wolves = 0.005   # b_W = d_M * efficiency 0.25
    death_rate_wolves = 0.75    # d_W

    # The rest of the function goes here...
    time_list = [0]
    moose_list = [moose_pop]
    wolf_list = [wolf_pop]
    for i in range(1,num_months*steps_per_month+1):
        time_list.append(round(i/steps_per_month,2))
        temp = moose_pop
        moose_pop = moose_pop + (birth_rate_moose/steps_per_month)*moose_pop - (death_rate_moose/steps_per_month)*(moose_pop*wolf_pop)
        wolf_pop = wolf_pop + (birth_rate_wolves/steps_per_month)*temp*wolf_pop - (death_rate_wolves/steps_per_month)*wolf_pop
        moose_list.append(round(moose_pop))
        wolf_list.append(round(wolf_pop))
    # Uncomment the following line when you are ready to test your function.
    return time_list, moose_list, wolf_list
