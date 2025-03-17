# Read a File and Handle Errors
try:
    
    file = open("sample.txt", "r")
    print("Reading file content: ")
    # for line in files:
    #     print(line)
    print("Line 1:", file.readline())
    print("Line 2:", file.readline())
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")   
