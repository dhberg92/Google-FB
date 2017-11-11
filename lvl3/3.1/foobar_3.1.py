def answer(n):
    count = 0
    n = int(n)
    while n > 1:
        # if n is even, always divide by 2
        if n%2 == 0:
            n /= 2
            count += 1
        # if n is odd
        else:
            # if n is 1 greater than a power of 2, subtract
            if ((n-1) & (n-2)) == 0:
                n -= 1
                count += 1
            # else check n-1 and n+1 to see which one will divide into an odd number
            else:
                # if n+1 divided by 2 is even, add
                if ((n+1)/2)%2 == 0:
                    n += 1
                    count += 1
                # else n-1 divided by 2 must be even, so subtract
                else:
                    n -= 1
                    count += 1
            
    return count