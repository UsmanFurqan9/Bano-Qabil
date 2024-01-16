#unit converter
#this program can convert english units into metric unit or metric units into english units
#this program can convert:
#Liters Into Gallons And Vice Versa
#Kilograms Into Pounds And Vice Versa
#Kilometers Into Miles And Vice Versa
#Inches Into Centimeter And Vice Versa
#Foot Into Centimeter And Vice Versa
#This Program Was Made By Usman Furqan
print("Unit Convertor")
given_unit=input("What Unit Do You Want To Convert?: ")
convert_into=input("What Unit Do You Want To Convert To?: ")
if given_unit=="kilogram" and convert_into=="pound" or given_unit=="kilograms" and convert_into=="pounds":
   X= input("Enter The Kilogram Value: ")
   X=int(X)
   B= X*2.20462
   B=float(B)
   print(X,"Kilograms =",B,"Pounds")
elif given_unit=="pound" and convert_into=="kilogram" or given_unit=="pounds" and convert_into=="kilograms":
   X= input("Enter The Pound Value: ")
   X=int(X)
   B= X*0.453592
   B=float(B)
   print(X,"Pounds =",B,"Kilograms")
elif given_unit=="liter" and convert_into=="gallon" or given_unit=="liters" and convert_into=="gallons":
   X= input("Enter The Value In Liters: ")
   X=int(X)
   B= X*0.2641
   B=float(B)
   print(X,"Liters =",B,"Gallons")
elif given_unit=="gallon" and convert_into=="liter" or given_unit=="gallons" and convert_into=="liters":
   X= input("Enter The Value In Gallons: ")
   X=int(X)
   B= X*3.78541
   B=float(B)
   print(X,"Gallons =",B,"Liters")
elif given_unit=="kilometer" and convert_into=="mile" or given_unit=="kilometers" and convert_into=="miles":
   X= input("Enter The Value In Kilometers: ")
   X=int(X)
   B= X*0.621371
   B=float(B)
   print(X,"Kilometers =",B,"Miles")
elif given_unit=="mile" and convert_into=="kilometer" or given_unit=="miles" and convert_into=="kilometers":
   X= input("Enter The Value In Miles: ")
   X=int(X)
   B= X*1.60934
   B=float(B)
   print(X,"Miles =",B,"Kilometers")
elif given_unit=="inch" and convert_into=="centimeter" or given_unit=="inches" and convert_into=="centimeters":
   X= input("Enter The Value In Inches: ")
   X=int(X)
   B= X*2.54
   B=float(B)
   print(X,"Inches =",B,"Centimeters")
elif given_unit=="centimeter" and convert_into=="inch" or given_unit=="centimeters" and convert_into=="inches":
   X= input("Enter The Value In Centimeters: ")
   X=int(X)
   B= X*0.393701
   B=float(B)
   print(X,"Centimeters =",B,"Inches")
elif given_unit=="foot" and convert_into=="centimeter" or given_unit=="foots" and convert_into=="centimeters":
   X= input("Enter The Value In Foots: ")
   X=int(X)
   B= X*30.48
   B=float(B)
   print(X,"Foots =",B,"Centimeters")
elif given_unit=="centimeter" and convert_into=="foot" or given_unit=="centimeters" and convert_into=="foots":
   X= input("Enter The Value In Centimeters: ")
   X=int(X)
   B= X*0.0328084
   B=float(B)
   print(X,"Centimeters =",B,"Foot")
print()
print ("This Program Was Made By Usman Furqan")