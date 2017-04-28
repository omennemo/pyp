#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:55:26 2017

@author: nimeshvellera
"""
lstWeeklyPay = ["Weekly Pay"]
lstName = ["Name"]

while True:
    name = input("Enter Employee Name : ")
    if name=="":
        print("End of Loop")
        break
    
    lstName.append(name)
    
    hoursWorked = input("Enter the Hours Worked : ")
    try:
        hoursWorked = float(hoursWorked)
    except:
        hoursWorked = 40

    if hoursWorked > 40:
        ratePerHour = 150.00
    else:
        ratePerHour = 100.00

    weeklyPay = hoursWorked * ratePerHour
    lstWeeklyPay.append(weeklyPay)
    
for (name,pay) in zip(lstName, lstWeeklyPay):
    print(str(name).ljust(10,' ')+" "+str(pay).rjust(10,' '))

#    print("Employee Name : " + name + " | " + "Weekly Pay : " + str(weeklyPay))