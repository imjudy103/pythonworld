import math

width = 200
length = 80

print(math.gcd(width, length))

print((width/math.gcd(width, length)) * (length/math.gcd(width, length)))