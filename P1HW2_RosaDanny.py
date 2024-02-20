#DANNYROSA
#2-20-2024
#P1HW2
#This program calculates and displays travel expenses


budget = int(input('Enter Budget: '))
#input user budget
destin = input('Enter your travel destination: ')
#input user destination
gas = int(input('How much do you think you will spend on gas? '))
#input user gas expense
balance = budget - gas
#subtract from budget
accom = int(input('Approximately, how much will you need for accomodation/hotel? '))
#input user hotel expense
balance = budget - accom
#subtract from budget
food = int(input('Last, how much do you need for food? '))
balance = budget - food
#subtract from budget

print('------------Travel Expenses------------')
print('Location:', destin)
print('Initial Budget:', budget)
print()
print('Fuel:', gas)
print('Accomodation:', accom)
print('Food:', food)
print()
print('Remaining Balance:', balance)

