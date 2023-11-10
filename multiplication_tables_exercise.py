# multiplication tables

#(1, 11) -> 1 - 10
for i in range(1, 11): # for each 1 - 10

    for j in range(1, 11): # multiply by j, 1 - 10

        print("{} * {} = {}".format(i, j, i * j)) # print multiplication table results
