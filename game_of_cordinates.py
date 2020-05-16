T=int(input())
h=[1,1]
def game_of_cordinates(n,h):
    while(n>=1):
        b=list(map(int,input().split()))
        
        if  b == list((h[0]+h[1],h[1])) or b == list((h[0],h[0]+h[1])) :
            print("Yes")
        else:
            print("No")
        h=b
        n=n-1
game_of_cordinates(T,h)
