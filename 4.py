def lucky_number(n):
    m = str(n)
    sum_ = 0
    k = 0
    while k < 10000:
        if int(m)**2 == 1:
            print('This number lucky')
            break
        else:
            for i in m:
                sum_ +=  int(i) ** 2
        m = str(sum_)
        sum_ = 0
        k+=1
        if k == 9999:
            print('This number is not lucky')



lucky_number(120)