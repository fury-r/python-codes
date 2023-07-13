with open("test.txt",mode="a") as myfile: #mode r is for read ,w is for write,a is for append
    text=myfile.write(" sup")
 
    print(myfile.read())
