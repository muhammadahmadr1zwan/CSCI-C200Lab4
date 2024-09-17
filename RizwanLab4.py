# This lab was made by Muhammad Ahmad Rizwan on 9/14/2023 for the COMPUTING 1 Lab 4 assignment. This lab will be currency-conversion program where users will be able to enter
# a number in US dollars and have a choice of output among different currencies such as Chinese yuan, Pakistani rupees, Turkish lira, and Euros.

def mainheadings(): # defining main headings of the program description
    print('    '); # blank space
    print('    '); # blank space
    print('     This is a currency conversion calculator, in which you have six different currencies to convert from'); # heading describing what the program is
    print('     These currencies include: Chinese Yuan, Turkish Lira, Pakistani Rupees, Jordanian Dinar, Somali Shilling, Euros'); # heading describing what the program is
    print('     Saudi Riyals, Great British Pounds, Russian Rubles, and Afghan Afghanis'); # heading describing what the program is

def menu(): # defining menu of the program where the different currencies can be chosen from
    print('    '); # blank space
    print(" What would you like to convert?"); # Text asking what would the user like to convert
    print(""); # blank space
    print(" 1) Chinese Yuan (¥)"); # number one option is Chinese Yuan
    print(" 2) Turkish Lira (₺)"); # number two option is Turkish Lira
    print(" 3) Pakistani Rupees (₨)"); # number three option is Pakistani Rupees
    print(" 4) Jordanian Dinar (JD)"); # number four option is Jordanian Dinar
    print(" 5) Somali Shillings (Sh.so.)"); # number five option is Somali Shillings
    print(" 6) Euros (€)"); # number six option is Euros
    print(" 7) Saudi Riyal (﷼‎)");#number seven option is Saudi Riyals
    print(" 8) Great British Pound (£)"); # number eight option is Great British Pounds
    print(" 9) Russian Ruble (₽)"); # number nine option is Russian Ruble
    print(" 10) Afghan Afghani (؋)"); # number ten option is Afghan Afghani
    print('   '); # blank space
    return get_choice(); # return value to ouput the get_choice function, which is called inside of the return value

def main(): # defining main function of the code where all the different functions are put called and put together in
    mainheadings(); # mainheadings function called
    menuselected = menu(); # menuselected variable defined as the menu function is called
    print(menuselected); # print the menuselected variable
    #conversion= input('Please enter what currency to convert to:\n') # input currency (string)
    numberofusds= input('Please enter USD amount for conversion:\n') # USD value (integer)
    print('     '); # blank space
    currencycalculations(menuselected, numberofusds); # currency calculations left with menuselected and numberofusds as paramaters

def get_choice(): # defining get_choice of the program where the choice inputted by the user is filtered to be only numerical
    while True: # while true, part of the if-else sequence
        choice= input('What is your choice? [1-10]'); # defining the choice variable
        if choice.isnumeric() and 1<= int(choice) <= 10: # if the choice is numeric and between 0-10, then:
            return choice; # return the choice
        else: # otherwise
            print('Invalid entry, please try again'); # error message pops up, saying 'Invalid entry, please try again'

from RizwanLab4UtilityFile import currencyvalues, currencysymbols, currencycalculations

main(); # calling the main function so the program runs






