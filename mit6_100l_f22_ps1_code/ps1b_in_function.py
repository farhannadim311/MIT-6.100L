def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0
	r = 0.05
	months = 0
	monthly_salary = yearly_salary / 12 
	down_payment = cost_of_dream_home * portion_down_payment
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while (amount_saved <= down_payment):
	    amount_saved = amount_saved + amount_saved * (r/12) + (monthly_salary * portion_saved)
	    months = months + 1
	    if(months % 6 == 0):
	        yearly_salary = yearly_salary + (semi_annual_raise * yearly_salary)
	        monthly_salary = yearly_salary / 12
	print(f"Number of months: {months}")
	return months