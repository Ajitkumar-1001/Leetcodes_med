## reverse an integer 

class ReverseInt:
    def __init__(self, x : int) -> int:
        
        x = str(x) ## converts the int to string to use the string methods and instances 

        is_negative = False #boolean sign 

        if x[0] == "-":
            x = x[1:]
            is_negative = True
        
        x = int(x[::-1])

        if is_negative:
            x = 0 - x 
        
        #now implement the constraints 
        if x > 2**31 - 1 or x < 2 **31:
            return 0

        else:
            return x 

