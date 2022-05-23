if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    results=[]
    for i in range(x+1):
        if 0<=i<=x:
            for j in range(y+1):
                if 0<=j<=y:
                    for k in range(z+1):
                        if 0<=k<=z and i+j+k!=n:
                            results.append([i,j,k])
    print(results)