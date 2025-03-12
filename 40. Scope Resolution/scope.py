# Variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Here vaiables are enclosed inside functions itself. It cannot 
# be called from outside or with another function

# Local Scope
def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()

# Enclosed Scope
def fun1():
    x = 1
    def fun2():
        print(x)
    fun2()

fun1()

# Global scope
def fun1():
    print(x)
def fun2():
    print(x)

x = 3

fun1()
fun2()

# Built in
from math import e

def fun1():
    print(e)

fun1()