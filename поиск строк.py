# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
a = 0
c = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue    
    data = line
    first = data.find(":")
    number = line[first:]
    b = float(number.strip(": "))
    print(b)
    a = float(a + 1)
    c += b
    d = c/a
print("Done")
print("Average spam confidence: ", d)
print(c)
