#### Assign function to a variable
def square(x):
    return(x*x)

f=square(3)
g=square
print(square)
print(f)
print(g)
print(g(5))


#### Pass a function as a paramter
def exec(func,arg=[]):
    output=[]
    for i in arg:
        output.append(func(i))
    return output

print(exec(square,[1,2,3]))
f=exec
print(f)
print(f(square,[4,5,6,7]))

#### Return function as output
def logger(msg):
    def log_message():
        print ('hello:'+msg)

    return log_message

msg= (logger('world'))
msg()

def html_tag(tag):
    def html_msg(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return html_msg

t1=html_tag('H1')
t1('Hello World')
t2=html_tag('P')
t2('This is awesome')


##### Decorator

def outer_func(func):
    def inner_func():
        print('Function {} was executed inside of inner_func'.format("test_func"))
        return func()
    return inner_func

def test_func(msg):
    print ("This is a test function. write something here")
    print(msg)

test=outer_func(test_func("Execute this code"))
test()
