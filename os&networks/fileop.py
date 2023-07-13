import shutil
import os


def q1_create(filename):
    fs = open(filename, 'w+')
    fs.close()


def q2_open(filename, msg):
    fs = open(filename, 'a+')
    fs.write(msg)
    print(fs.read())
    fs.close()


def q3_seek(filename, pointer):
    try:
        fs = open(filename, 'r')
        fs.seek(pointer)
        print(fs.read())
        print(f"FileSize  {(os.stat(filename)).st_size}")
        fs.close()
    except FileNotFoundError:
        print("File does Not exist")
    except:
        print('Error')

def q4_dup(filename,msg):
    try:

        fd = os.open(filename, os.O_RDWR|os.O_CREAT )

        dupFd = os.dup( fd )
        line = f"Descriptor{fd}\nCopy Descriptor {dupFd}\nMessage {msg}" 

        b = str.encode(line)
        os.write(dupFd, b)
        os.closerange( fd, dupFd)
        print ("Done")
    except FileNotFoundError:
        print("File does Not exist")
    except:
        print('Error')
#   if fd<0:
#         print("Error opening the file")
    
#     up = os.dup(fd)
#     os.write(up,'Hello')
#     os.write(fd,'Hello there')



def q5_link(filename1,filename2):
    file_exists = os.path.exists(filename2)
    if not file_exists:
        fd = os.open(filename1, os.O_RDWR | os.O_CREAT)
        os.close(fd)
    if os.link(filename1, filename2)==-1:
        print('File is already link')
    else:
        print(f'File is linked')


def q6_unlink(filename):
    os.unlink(filename)


def q7_create4k(filename):
    fs = open(filename, 'wb')
    fs.seek(4000-1)
    fs.write(b"\b")
    fs.close()
    print(os.stat(filename).st_size)


def q8_copy(filename1, filename2):
    shutil.copy(filename1, filename2)


def q9_Content(path):
    o = os.listdir(path)
    for i in o:
        print(os.path.splitext(i))


if __name__ == '__main__':
    op = 0
    while True:
        op = int(input(' 1. Create\n 2. Open\n 3. Seek\n 4. Dup\n 5. Link\n 6. Unlink\n 7. Create 4k\n 8. Copy\n 9. Directories \n10. Exit\n'))
        if op == 1:
            a = input('filename ')
            q1_create(a)
        elif op == 2:
            a = input('filename ')
            msg = input('message ')
            q2_open(a, msg)
        elif op == 3:
            a = input('filename ')
            pointer = int(input('pointer '))
            q3_seek(a, pointer)
        elif op == 4:
            f = input('filename ')
            msg=input('message ')
            q4_dup(f,msg)
        elif op == 5:
            f = input('filename 1 ')
            s = input('filename 2 ')

            q5_link(f,s)
        elif op == 6:
            f = input('filename ')
            q6_unlink(f)
        elif op == 7:
            f = input('filename ')
            q7_create4k(f)
        elif op == 8:
            f = input('filename ')
            g = input('copy destination ')
            q8_copy(f, g)
        elif op == 9:
            f = input('path ')
            q9_Content(f)
        else:
            break
