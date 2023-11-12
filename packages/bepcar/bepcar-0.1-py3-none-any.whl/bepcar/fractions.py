def gcd(a, b):
   while b:
       a, b = b, a % b
   return a


class Fractions(object):
    """A class for mathematics fractions.
    
    Args:
        a: the top of the fraction
        b: the bottom of the fraction
        
        
    Functions:
        add: fractional addition
        subtract: fractional subtraction
        multiply: fractional multiplication
        divide: fractional division
    """
    @staticmethod
    def __all__():
        return [
            "__init__",
            "__add__",
            "__sub__",
            "__mul__",
            "__truediv__"
        ]
        
    def __init__(self, a:int, b:int, simplify=True):
        """Initializes the fraction.
        
        Args:
            a: the top of the fraction
            b: the bottom of the fraction
            simply: 
                If you want to simplify the fraction, such as it was give `Fraction(4,6)`, you will get `2/3`.
                Else, you will just get `4/6`.
                
        Self:
            a,b: a,b
            z: 
                if the fraction is positive, z is 1.
                else z is 0.
        """
        if b == 0:
            raise ZeroDivisionError("You just input a fraction with a zero-denominator.")
        if a*b > 0:
            self.a, self.b = abs(a), abs(b)
        else:
            self.a, self.b = -abs(a), abs(b)
        if simplify:
            g = gcd(a, b)
            self.a, self.b = self.a // g, self.b // g
        
    def __add__(self, other, simplify=True):
        """Adds two fractions together.
        
        Args:
            other: the fraction to add to this one
            
        Returns:
            The sum of the two fractions.
        """
        return Fractions(self.a * other.b + other.a * self.b, self.b * other.b, simplify=simplify)
        
    def __sub__(self, other, simplify=True):
        """Subtracts two fractions together.
        
        Args:
            other: the fraction to subtract from this one
            
        Returns:
            The difference of the two fractions.
        """
        return Fractions(self.a * other.b - other.a * self.b, self.b * other.b, simplify=simplify)
    
    def __mul__(self, other, simplify=True):
        """Multiplies two fractions together.

        Args:
            other: the fraction to multiply this one by

        Returns:
            The product of the two fractions.
        """
        return Fractions(self.a * other.a, self.b * other.b, simplify=simplify)

    def __truediv__(self, other, simplify=True):
        """Divide the first fraction by the second one.

        Args:
            other (Fraction): the fraction to divide the other.
            
        Returns:
            The division of the two fraction.
        """
        t = self * Fractions(other.b, other.a)
        return Fractions(t.a, t.b, simplify=simplify)
    
    def __str__(self, mod=1) -> str:
        """Make an output for the fraction.

        Args:
            mod (int, optional): 
                If 1, the return will be like: `1/2`.
                Otherwise, the return will be like `
                6 
                -
                7
                `.
            Defaults to 1.

        Returns:
            str: _description_
        """
        if self.a == self.b:
            return "1"
        if self.a == 0:
            return "0"
        if mod == 1:
            return str(self.a)+"/"+str(self.b)
        else:
            return str(self.b)+"\n-\n"+str(self.a)
    
    