import sys 
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 10 # it will set the desire prcision of the decimal value , 28 is default precision

current_humidity = 67
ideal_humidity = 55

print(f"Ideal humidity {ideal_humidity}")
print(f"Current humidity {current_humidity}")

print(f"differece in huimidity {ideal_humidity - current_humidity}")

frac = Fraction(ideal_humidity,current_humidity)
print(f"fraction {frac}")

deci= Decimal(frac.numerator) / Decimal(frac.denominator)
print(f"In decimal {deci}")