# import extension - named defined in setup.py, bind.c
import _hello

def helloworld():
    return _hello.helloworld()

def greeting(name: str, number: int):
    return _hello.greeting(name, number)
