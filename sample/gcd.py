import functools
import fractions

values = [290021904, 927964716, 826824516, 817140688]
gcd = functools.reduce(fractions.gcd, values)
print(gcd)
# =>92
