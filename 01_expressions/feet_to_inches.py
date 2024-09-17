
def feet_to_inches()->None:
    prompt:str=input("Enter the length in feet : ")
    numb:float=float(prompt)
    to_inches:float=numb*12
    print(f'The value in inches is {to_inches}')
    
def main()->None:
    feet_to_inches()


if __name__=='__main__':
    main()


