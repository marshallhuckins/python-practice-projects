#with open("test.txt","w") as outfile:
#    outfile.write("Now, this is another file.\n")
#    outfile.write("It has more content.\n")
#    outfile.write("And, it will also appear in IDLE at the prompt>>>.\n")


with open("numbers.txt","w") as outfile:
    for number in range(0, 10):
        outfile.write( str( number )+ "\n")

with open("numbers.txt") as infile:
    for line in infile:
        print( line, end="" )
    print("\n\n\n")


