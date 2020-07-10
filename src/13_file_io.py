"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
guys = {"Frank Zappa":"Weasels rip my Flesh", "Les Claypool": "Primus","Nioh": "Samurai"}

for k, v in guys.items():
    print(k, v)


for i, v in enumerate(['shnowlie', 'molwie','fowlie']):
    print(i,v)

    q= ['name','mission','favorite food']
    a=['Lt Frankie', 'Killin Nazis','Enchiladas']

    for q, a in zip(q, a):
        print('What is your{0}? It is {1}'.format(q,a))

for i in reversed(range(0,100,20)):
    print( i)


# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# f = open('foo.txt','r')

# for i in f:
#     print(i)
    
# f.read()
# f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
b = open('bar.txt','w+')

for i in range(10):
    b.write(f'this is line {i}')
 
for i in b:
    print(i)
b.closed   

b= open('bar.txt',"r")

for i in b:
    print(i)

b.read()
b.closed