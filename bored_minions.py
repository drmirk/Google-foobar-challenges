def answer(rolls, blocks):
    #t is number of rolls
    #n is number of tile
    #three sided die, L R and Stay
    #return number of trials modulo 123454321
    #token starts on left most tile
    # must get to right most tile and stay there
    #once it reaches either the finishing tile it must stay there
    #find the possible solutions
    valid_combos = 0
    if rolls == blocks -1:
        return 1
    # for i in range(0, rolls - blocks + 1):
    #     valid_combos += 2**i
    invalids = 0
    max_valid_combos = rolls ** (rolls - blocks) %123454321
    for i in range(1, rolls - blocks):
        # invalids += 3 ** (2*i) % 123454321
        # invalids +=
        print invalids
    valid_combos = max_valid_combos - invalids
    # print valid_combos


    return valid_combos #% 123454321


## maybe the better question is to check how many possible rolls and discover which ones are valid from there
print answer(1,2) #== 1 # combos == 6 valid combos == 1
print "***"
print answer(3,2) #== 3
print "***"
print answer(5,3)
# print answer(1000,10)
