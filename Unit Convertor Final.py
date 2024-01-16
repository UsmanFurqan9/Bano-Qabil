#unit converter
#this program can convert english units into metric unit or metric units into english units
#this program can convert:
#Liters Into Gallons And Vice Versa
#Kilograms Into Pounds And Vice Versa
#Kilometers Into Miles And Vice Versa
#Inches Into Centimeter And Vice Versa
#Foot Into Centimeter And Vice Versa
#This Program Was Made By Usman Furqan
from time import sleep

print("\033[1mUnit Convertor")
print()
sleep(1)
print("Units Available For Conversion:")
units_list = [["\033[0m1)Liters Into","2)Kilograms Into","3)Kilometers Into","4)Inches Into","5)Foot Into"], ["Gallons And Vice Versa","Pounds And Vice Versa", "Miles And Vice Versa","Centimeters And Vice Versa","Centimeters And Vice Versa"]]
for y, z in zip(*units_list):
    print (y, z)
given_unit=input("What Unit Do You Want To Convert?: ")
convert_into=input("What Unit Do You Want To Convert To?: ")
if given_unit=="kilogram" and convert_into=="pound" or given_unit=="kilograms" and convert_into=="pounds" or given_unit=="kg" and convert_into=="lb":
   X= input("Enter The Kilogram Value: ")
   X=float(X)
   B= X*2.20462
   B=float(B)
   print(X,"Kilograms =",B,"Pounds")
elif given_unit=="pound" and convert_into=="kilogram" or given_unit=="pounds" and convert_into=="kilograms" or given_unit=="lb" and convert_into=="kg":
   X= input("Enter The Pound Value: ")
   X=float(X)
   B= X*0.453592
   B=float(B)
   print(X,"Pounds =",B,"Kilograms")
elif given_unit=="liter" and convert_into=="gallon" or given_unit=="liters" and convert_into=="gallons":
   X= input("Enter The Value In Liters: ")
   X=float(X)
   B= X*0.2641
   B=float(B)
   print(X,"Liters =",B,"Gallons")
elif given_unit=="gallon" and convert_into=="liter" or given_unit=="gallons" and convert_into=="liters":
   X= input("Enter The Value In Gallons: ")
   X=float(X)
   B= X*3.78541
   B=float(B)
   print(X,"Gallons =",B,"Liters")
elif given_unit=="kilometer" and convert_into=="mile" or given_unit=="kilometers" and convert_into=="miles" or given_unit=="km" and convert_into=="mi":
   X= input("Enter The Value In Kilometers: ")
   X=float(X)
   B= X*0.621371
   B=float(B)
   print(X,"Kilometers =",B,"Miles")
elif given_unit=="mile" and convert_into=="kilometer" or given_unit=="miles" and convert_into=="kilometers" or given_unit=="mi" and convert_into=="km":
   X= input("Enter The Value In Miles: ")
   X=float(X)
   B= X*1.60934
   B=float(B)
   print(X,"Miles =",B,"Kilometers")
elif given_unit=="inch" and convert_into=="centimeter" or given_unit=="inches" and convert_into=="centimeters" or given_unit=="inch" and convert_into=="cm":
   X= input("Enter The Value In Inches: ")
   X=float(X)
   B= X*2.54
   B=float(B)
   print(X,"Inches =",B,"Centimeters")
elif given_unit=="centimeter" and convert_into=="inch" or given_unit=="centimeters" and convert_into=="inches" or given_unit=="cm" and convert_into=="inch":
   X= input("Enter The Value In Centimeters: ")
   X=float(X)
   B= X*0.393701
   B=float(B)
   print(X,"Centimeters =",B,"Inches")
elif given_unit=="foot" and convert_into=="centimeter" or given_unit=="foots" and convert_into=="centimeters" or given_unit=="ft" and convert_into=="cm":
   X= input("Enter The Value In Foots: ")
   X=float(X)
   B= X*30.48
   B=float(B)
   print(X,"Foots =",B,"Centimeters")
elif given_unit=="centimeter" and convert_into=="foot" or given_unit=="centimeters" and convert_into=="foots" or given_unit=="cm" and convert_into=="ft":
   X= input("Enter The Value In Centimeters: ")
   X=float(X)
   B= X*0.0328084
   B=float(B)
   print(X,"Centimeters =",B,"Foot")
else: 
   print("\033[1mError: **Spelling Mistake**")
print()
sleep(1)
print ("\033[1mThis Program Was Made By Usman Furqan")