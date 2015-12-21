def answer(population, x, y, strength):
    if population[y][x]== -1:
        return
    if population[y][x] > strength:
        return population
    else:
        population[y][x] = -1
        if x > 0:
            answer(population, x-1, y, strength)
        if x < len(population[0])-1:
            answer(population, x+1, y, strength)
        if y > 0:
            answer(population, x, y-1, strength)
        if y < len(population)-1:
            answer(population, x, y+1, strength)
    return population

print answer([[2,2],[2,2]], 0, 0, 1)
print answer([[2,2],[2,2]], 0, 0, 3)
print answer([[1,2,3],[2,3,4],[3,2,1]], 0,0,2)




    # if population[y][x]== -1:
    #     return
    # if population[y][x] > strength:
    #     return population
    # else:
    #     population[y][x] = -1
    #     if x > 0:
    #         answer(population, x-1, y, strength)
    #     if x < len(population[0])-1:
    #         answer(population, x+1, y, strength)
    #     if y > 0:
    #         answer(population, x, y-1, strength)
    #     if y < len(population)-1:
    #         answer(population, x, y+1, strength)
    # return population
