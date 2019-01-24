from interval import Interval
from decimal import *

# r1_top = Decimal('0').quantize(Decimal('0.00'))
# r1_bottom = Decimal('10').quantize(Decimal('0.00'))
# r2_top = Decimal('10').quantize(Decimal('0.00'))
# r2_bottom = Decimal('20').quantize(Decimal('0.00'))
# r1 = Interval(r1_top, r1_bottom)
# r2 = Interval(r2_top, r2_bottom)

r1 = Interval(0, 10)
r2 = Interval(10, 20, lower_closed=False)

# print(r1.overlaps(r2))
# print(type(r1_top))
# print(r1_top, r1_bottom, r2_top, r2_bottom)
print(r1.adjacent_to(r2))
