a=7500000
b=200000
ret=10
i=0
while i<=30:
    print("Year:"+str(i))
    returns=((a+b)*ret)/100
    print("Principal:,Returns:, Year:",(a+b),returns,i)
    a = (a+b+returns)
    print(f"Amount:{a:2}")
    i += 1

##  31,054,217 - 7500000 FD
##  27,326,327 -  200000  SIP (15%)
## 141,161,385 - 7500000 15%

141,161,385
55,501,874
143,957,568
