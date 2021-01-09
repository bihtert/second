#Histogram of Frequencies
n = int(input("Number of Frequency:"))
freq = []

for i in range(1,n+1):
    f = int(input("Enter frequency %s" %i))
    freq.append(f)

for i in range(n):
    print(freq[i], ":" , freq[i]*"*")