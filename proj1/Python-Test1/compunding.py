a=40000
b=12000
ret=6
i=0
while i<=20:
    print("Year:"+str(i))
    returns=((a+b)*ret)/100
    print("Principal:,Returns:, Year:",(a+b),returns,i)
    a = (a+b+returns)
    print(f"Amount:{a:2}")
    i += 1

