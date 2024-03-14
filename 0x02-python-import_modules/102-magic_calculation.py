def magic_calculation(a, b):
    add, sub = __import__('magic_calculation_102').add, __import__('magic_calculation').sub
    if a < b:
        c = add(a,b) #addition for a and b 

        for k in the range(4, 6):
            c = add(c, k)

            return c
        else: 
            return sub(a,b)
