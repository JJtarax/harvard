import sys #docs.python.org/3/library/sys.html

if len(sys.argv) < 2:
   sys.exit("Too few arguments")

for arg in sys.argv[1:]:
   print("Hello my name is," , arg)
'''
if len(sys.argv) < 2:
   sys.exit("Too few arguments")
elif len(sys.argv) > 4:
    sys.exit("Too many arguments")
else:
    print("Hello my name is" , sys.argv[1] , sys.argv[2] , sys.argv[3])
'''
# When you run this you need to write your name 
# EX. name.py Carlos
# Then it will print "Hello my name is Carlos"