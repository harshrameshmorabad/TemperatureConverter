celcius = float(input("What is the temperature which you would like to insert in celcius ?"))
farenheit = (celcius*1.8 + 32)
print( " %0.1f degree celcius = %0.1f farenheit "  %(celcius,farenheit) )

if farenheit>+104 :
    print(" It is too hot !!!!")

elif farenheit<=50 :
    print(" It is too cold !!! ")

else :
    print(" It is a moderatre Temperature . :) ")
