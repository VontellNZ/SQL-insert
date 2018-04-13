checker = 1
dbName = input("What is the name of the databse? ")

while checker != "n":
	statement = "INSERT INTO " + dbName + " VALUES("
	
	pname = input("Enter player name: ")
	pcountry = input("Enter country: ")
	gdpnom = input("Nominal gdp = ")
	val1 = input("mil/bil/tril: ")
	gdpppp = input("PPP gdp = ")
	val2 = input("mil/bil/tril: ")
	
	count = 0
	gdpgrowth = 0
	growthlast = 0
	print("Enter values for growth: ")
	while count != 10:
		value = float(input())
		growthlast = value
		gdpgrowth += value
		count += 1
	gdpgrowth = gdpgrowth / 10
	print(gdpgrowth)
	
	statement += "'" + pname + "', '" + pcountry + "', " + gdpnom + ", '" + val1 + "', " + gdpppp + ", '" +val2 + "', " + str(gdpgrowth) + ", " + str(growthlast) + ");"
	print(statement)
	
	checker = input("continue(y/n)? ")
	print()
	
