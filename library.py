#!/usr/bin/env python3

import sys
from pwn import *

def main():
    menu = """ 
       z                                                    
      zz        z   zzzzz             zz     zzzz    zz    z
      z        zz   z  zz   zzzzzz   zz z   zz  zz    zz  zz
     zz        z  zzzzzz    zz  zz zzz  z   z  zz      zzzz 
     z        zz zz   zzz   zzzzz zzzzzzz  zzzzz       zzz  
     z        z zz      z  zz zzz  z   z   z zz        z    
    zzzzzzzz zz z       z zz    z  z   z  z   zz      z     
           z z  zzzzzzzzz z    z       z  z    zz    z      
                                                z  zz       
                                                   z     
[1] Get a book
[2] Add a book
[3] Show books
    """
    print(menu)
    
    option = int(input("Select an option: "))
    print("\r")

    if option == 1:
        get_book()
    elif option == 2:
        add_book()
    elif option == 3:
        show_books()
    else:
        log.failure("That option doesn't exist")
        sys.exit(1)

def options():
    menu = "\n[1] Get a book\n[2] Add a book\n[3] Show books"
    print(menu)
    
    option = int(input("Select an option: "))
    print("\r")

    if option == 1:
        get_book()
    elif option == 2:
        add_book()
    elif option == 3:
        show_books()
    else:
        log.failure("That option doesn't exist")
        sys.exit(1)

def get_book():
    log.success("You've selected option 1\n")
    book_name = input("\nWhat's the name of the book you want to get?: ")
    book_name = book_name.lower()
    book_found = False
    
    with open("books", "r") as f:
        lines = f.readlines()
    
    with open("books", "w") as f:
        for line in lines:
            if line.rstrip() != book_name:
                f.write(line.lower())
            else:
                book_found = True
                
    if book_found:
        log.success(f"Here is your book {book_name.title()}")
    else:
        log.failure("We couldn't find that book")

def add_book():
    log.success("You've selected option 2\n")
    book_name = input("What's the name of the book you want to add?: ")
    book_name = book_name.lower()
    with open("books", "a") as f:
        f.write(f"{book_name}\n")

def show_books():
    log.success("Available Books:\r\r")
    with open("books", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "books:" not in line:
                print(line.title().strip())
    options()

if __name__ == '__main__':
   main()
