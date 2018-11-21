x = input ( "What's your name: " )
y = float ( input ( " What time is it?: " ))
if  y >= 22.00 :
    y = " Night "
elif y >= 17.30 :
    y = " Evening "
elif y >= 15.30 :
    y = " Afternoon "
elif y >= 13.00 :
    y = " Noon "
elif y >= 05.00 :
    y = " Morning "
print ( " Selamat " + y + "  " + x)