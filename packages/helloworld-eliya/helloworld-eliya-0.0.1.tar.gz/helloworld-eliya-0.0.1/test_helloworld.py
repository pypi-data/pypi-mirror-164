from helloworldtal1948 import say_hello
import rsa


def test_helloworld_no_params():
    assert say_hello() == "Hello, World!"


def test_helloworld_with_params():
    assert say_hello("Tal") == "Hello, Tal!"
