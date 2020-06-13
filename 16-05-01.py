N = int(input(''))
list_in = list()
for i in range(0, N):
    S = input('')
    list_in.append(S)
#print(list_in)
var_j = 0
for j in list_in:
    var_j += 1
    #print('j=',j)
    x = 0
    var_k = 0
    for k in j:
        var_k += 1
        if k == '1':
            #print('k=',k)
            if x == -1:
                break
            else:
                for l in list_in:
                    #print('l=',l)
                    if list_in.index(j) != list_in.index(l):
                        var_m = 0
                        for m in l:
                            var_m += 1
                            if m == '1':
                                #print('m=',m)
                                if var_k == var_m and var_j == len(list_in):
                                    x = -1
                                    print(-1)
                                    break
                                elif var_k == var_m:
                                    continue
                                elif len(l) == var_m:
                                    print(1)
                                    x = -1
                                    break
                                else:
                                    continue
                            else:
                                continue
                    else:
                        continue
        else:
            continue
