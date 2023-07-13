
import sys,random

def guess(a,b):
    try:
        if(0<int(a)<10):
            if(int(a)==int(b)):
                print("You are a genius ")
                return True
            else:
                return False
        else:
            return "number between 0,10"
    except ValueError as err:
        return err