def answer(total_lambs):
	# find gen_max
	gen_max = 0
	next_cost = 2
	total_cost = 1
	while total_cost <= total_lambs:

        	gen_max += 1

        	total_cost += next_cost

        	next_cost *= 2

    
    # check leftover LAMBs
	remaining = total_cost - (next_cost/2)
	if((total_lambs - remaining) >= ((next_cost/4) + (next_cost/8))):

        	gen_max += 1

	# find stin_max
	a, b = 1, 1

	stin_max = 1
	current_cost = 2
	while current_cost <= total_lambs:

        	stin_max += 1

        	a, b = b, b+a

        	current_cost += b



    return stin_max - gen_max