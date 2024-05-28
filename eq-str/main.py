from os import system
import string
from string_funcs import eq_string


def main():
    while True:
        eq_string(input("First str: "), input("Second str: "))
    

if __name__ == "__main__":
    main()
