tem = eval(input("Enter Temperature: "))
if tem <= 0 :
	print("Below freezing")
elif tem >= 1 and tem <= 15 :
	print("Extreme cold temperature")
elif  tem >= 16 and tem <= 30 :
	print("Cold Temperatures")
elif  tem >= 31 and tem <= 38 :
	print("lukewarm temperatures")
elif  tem >= 39 and tem <= 42 :
	print("warm temperatures")
elif  tem >= 43 and tem <= 50 :
	print(" hot temperatures")
elif  tem >= 51 and tem <=60 :
	print(" extremely hot temperatures")
elif  tem >= 61 :
	print("burning temperatures")
else:
	print("invalid input please try again")
