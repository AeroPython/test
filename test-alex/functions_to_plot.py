import matplotlib.pyplot as plt

def foo(x):
    global a
    plt.plot(a, x, 'o')

def foo2(x):
    plt.plot(x, x, 'o')

def foo_global(x):
    global a
    plt.plot(a, x, 'o')