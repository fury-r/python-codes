import sys,requests,hashlib



def get_api_data(data):
    url=f'https://api.pwnedpasswords.com/range/{data}' #give first 5 hash and it returns the rest of the hash without the first 5 hash
    res=requests.get(url)
    
    if(res.status_code==400):
        raise RuntimeError(f"Error: {res.status_code}")
    return res #has response without the first 5 or the head hash
    
def read_res(res,hash):
    a=(line.split(":") for line in res.text.splitlines()) 
    c=0
    for h,count in a:
        if(hash[5:]==h): #comparing tail hashes whether  your_password hash==response hash
            return count
    return 0
def check_file_for_password(): #reading password from file and then checking 
    r=open("./a.txt" ,'r')
    p=(r.read()).splitlines()
    for i in p: 
        hash=hashlib.sha1(i.encode('utf-8')).hexdigest().upper() #by default encode is utf-8
        data=hash[:5] #for the api sending only the first 5 letters of the hash
        res=get_api_data(data)
        ans=read_res(res,hash)
        if(ans):
            print(f"{i} password has been breached  {ans} times .Change it!" )
        else:
            print(f"{i} as password is secure." )
    return "Finished Checking!"          
""" def check_hash(l):
    for i in l:
        hash=hashlib.sha1(iencode('utf-8')).hexdigest().upper()
        data=hash[:5] #for the api sending only the first 5 letters of the hash
        res=get_api_data(data)
        ans=read_res(res,hash)
        if(ans):
            print(f"{i} password has been breached  {ans} times .Change it!" )
        else:
            print(f"{i} as password is secure." )
    return "Finished Checking!"          

l=sys.argv[1:] """


if __name__=='__main__':
    sys.exit(check_file_for_password()) #systemcall exits  