# isect July 23, 2022
# calucurate intersection between two line segments
# p1(x0, y0), p1(x1, y1), p3(x2, y2), p4(x3, y3)
# segment1(p1, p2), segment2(p3, p4)
# return value: (x, y) or False
def intersect(x0, y0, x1, y1, x2, y2, x3, y3):
    d0x = x1 - x0; d0y = y1 - y0
    d2x = x3 - x2; d2y = y3 - y2

    d = d0x * d2y - d2x * d0y
    if d == 0: # Two line seguments are paralell.
        return False
    sn = d2y * (x2 - x0) - d2x * (y2 - y0)
    tn = d0y * (x2 - x0) - d0x * (y2 - y0)
    s = sn / d
    t = tn / d
    if 0 <= s <= 1 and 0 <= t <= 1: # on the line seguments
        return x0 + d0x * sn / d, y0 + d0y * sn / d
    else: 
        return False
