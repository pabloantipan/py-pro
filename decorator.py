def decorator(func):
    def reaper():
        print("This is added by the decorator")
        func()

    return reaper


def say_hi():
    print("Hi!!")


@decorator
def say_hello():
    print("I say hello!")


hello = decorator(say_hi)
hello()
say_hello()


def upperDecorator(func):
    def reaper(text):
        try:
            return func(text).upper()
        except:
            print("Tried, but I could not")
            return func(text)

    return reaper


@upperDecorator
def say_hi2(text):
    return f"I said hi!, {text}"


print(say_hi2("Pablo"))
