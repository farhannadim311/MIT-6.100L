def part_c(initial_deposit):
	#########################################################################
	cost_of_house = 800000
	down_payment_percentage = 0.25
	down_payment = cost_of_house * down_payment_percentage
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	low = 0
	high = 1
	r = (low + high) / 2
	epsilon = 100
	amount_saved = initial_deposit * (1+ r/12)**36
	steps = 0
	if (initial_deposit > (down_payment - epsilon)):
	    r = 0
	    print(f"Best savings rate: {r}")
	    print(f"Steps in bisection search: {steps}")
	elif (initial_deposit * (1 + 1/12)**36 < (down_payment - epsilon)):
	    r = None
	    print(f"Best savings rate: {r}")
	    print(f"Steps in bisection search: {steps}")
	else:
	    while(abs(amount_saved - down_payment) >= epsilon):
	        if (amount_saved > down_payment):
	            high = r
	        else:
	            low = r
	        r = (low + high) / 2
	        amount_saved = initial_deposit * (1 + r/12)**36
	        steps = steps + 1
	    print(f"Best Savings rate: {r}")
	    print(f"Steps in bisection search: {steps}")
	return r, steps