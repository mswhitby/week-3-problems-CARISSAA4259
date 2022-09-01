def dis(price, discount):
	pay_pct = 100 - discount
	price = (pay_pct / 100) * price
	
	return price
