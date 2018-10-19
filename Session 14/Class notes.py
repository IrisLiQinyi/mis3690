import os
print(os.getcwd())
# fout = open('session14/output.txt','a') #a is append

# line1 = 'How many roads must a man walk down\n'
# fout.write(line1)
# line2 = "before you call him a man?\n"
# fout.write(line2)
# fout.close()

# print(os.path.abspath('session14/output.txt')) #give where exactly this file is, whether this file eists or not

# print(os.path.exists('session14/output.txt'))
# print(os.path.exists('session14/input.txt'))

def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

fin = open('bad_file')
try:    
    fin = open('bad_file')
except:
    print('Something went wrong.')


# f = open('save.p', 'w')
# s = pickle.dump(t1,f) 
# f.close()

t2 = pickle.load(open('save.p', 'rb'))
print(t2)