# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.

def fun_nearestbusstop(street):
    f = street%8
    s = 8 - f
    if(f<=s):
        return street - f
    else:
        return street + s
print(fun_nearestbusstop(13))