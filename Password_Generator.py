####################################################################################################################################
# Password Generator 
# Created By: Gabbierutt
# System Version 1.0

# Note: Anyone who wants to change the code for his reference is allowed. Make sure to credit me for the friendly permission as well. 
# Thank you.
####################################################################################################################################

### IMPORTING MODULES ###

from logging import raiseExceptions
import sys
from typing import ParamSpecKwargs
from rich import console
from rich.console import Console
from time import sleep
import random
import os


console = Console()

os.system('cls')

def main():
    
    with open('pass_log.txt.txt', 'r') as file: # Read a ascii character thru text format and display to console
        ascii = "".join(file.readlines())
        console.print(ascii)
    
    console.print("=============================================================================================", style = 'cyan')
    console.print("(C) 2021 Gabbierutt. All rights reserved. System Version 1.0. January Python project", style = 'cyan')
    console.print("=============================================================================================", style = 'cyan')
    console.print()
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$&*=+,"
    
    
    while True:
        try:
            console.print()
            console.print("=============================================================================================", style = 'cyan')
            console.print("Enter password length", style = 'cyan')
            password_length = int(input(">> "))
            console.print("=============================================================================================", style = 'cyan')
    
            console.print()
    
            with console.status("[green]Generating password please wait...") as status:
                for index in range(3):
                    sleep(1)
            console.print()
            console.print("=============================================================================================", style = 'cyan')
            console.print("These are your passwords. You can choose from the following:", style = 'cyan')
            console.print()
    
            for i in range(3): # Gives a 3 list of passwords
                for generate in range(password_length): # loops that generates length of password according to user inputs
                    _rnd = random.choice(characters)
                    console.print(_rnd, end = "", style = 'cyan')
                console.print()
            console.print("=============================================================================================", style = 'cyan')
    
            console.print()
        
            while True:
                console.print()
                console.print("Do you want to generate again [y/n] ? ", style = 'cyan')
                response = input(">> ")
                response = response.lower()
        
                if response == 'y':
                    os.system('cls')
                    main()
                    break
                elif response == 'n':
                    quit()
                else:
                    console.print("Invalid input! Please try again!", style = 'red')
                    console.print()
                console.print("=============================================================================================", style = 'cyan')
        
        except ValueError:
            console.print("Please enter number only! Strings or other characters are not supported", style = 'red')
    
        console.print()

main()