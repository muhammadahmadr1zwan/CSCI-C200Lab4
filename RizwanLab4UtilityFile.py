

def currencyvalues(menuselected): # define currencyvalues function with menuselected as a paramater
    if int(menuselected) == 1:return 7.27; # if choice is 1, then return 7.27 [exchange rate for Yuan]
    if int(menuselected) == 2:return 26.99; # if choice is 2, then return 26.99 [exchange rate for Lira]
    if int(menuselected) == 3:return 296.42;# if choice is 3, then return 296.42 [exchange rate for Rupees]
    if int(menuselected) == 4:return 0.71; # if choice is 4, then return 0.71 [exchange rate for Dinar]
    if int(menuselected) == 5:return 569.50; # if choice is 5, then return 596.50 [exchange rate for Shillings]
    if int(menuselected) == 6:return 0.94; # if choice is 6, then return 0.94 [exchange rate for Euros]
    if int(menuselected) == 7:return 3.75; # if choice is 7, then return 3.75 [exchange rate for Riyal]
    if int(menuselected) == 8:return 1.24; # if choice is 8, then return 1.24 [exchange rate for Pound]
    if int(menuselected) == 9:return 96.80; # if choice is 9, then return 96.80 [exchange rate for Ruble]
    if int(menuselected) == 10:return 78.93; # if choice is 10 then return 78.93 [exchange rate for Afghani]
    if int(menuselected) == 11:return 1;

def currencysymbols(menuselected): # define currencysymbols function with menuselected as a parameter
    if int(menuselected) == 1:return ('¥'); # if choice is 1, then return yuan symbol
    if int(menuselected) == 2:return ('₺'); # if choice is 2, then return lira symbol
    if int(menuselected) == 3:return ('₨'); # if choice is 3, then return rupee symbol
    if int(menuselected) == 4:return ('JD'); # if choice is 4, then return dinar symbol
    if int(menuselected) == 5:return ('Sh.so.'); # if choice is 5, then return shilling symbol
    if int(menuselected) == 6:return ('€'); # if choice is 6, then return euro symbol
    if int(menuselected) == 7:return ('﷼‎');# if choice is 7, then return riyal symbol
    if int(menuselected) == 8:return('£'); # if choice is 8, then return GBP symbol
    if int(menuselected) == 9:return('₽'); # if choice is 9, then return ruble symbol
    if int(menuselected) == 10:return('؋'); # if choice is 10, then return Afghani symbol

def currencycalculations(currencymenu, usdamount): # define currencycalculations function with currencymenu and usdamount as parameters
    print("Inputted amount: " + usdamount + '$'); # print Inputted amount + usdamount inputted + dollar symbol
    conversion_rate = currencyvalues(int(currencymenu)); # conversion_rate is equal to currencyvalues times currencymenu
    symbol = currencysymbols(int(currencymenu)); # symbol is equal to currencyvalues times currencymenu
    convertedvalue= float(usdamount) * conversion_rate; #convertedvalue is equal go float of usdamount times conversion_rate
    print("Converted amount: " + str(convertedvalue)+ "" + symbol); # print the converted amount + string of converted value + blank space + symbol of currency