def Decorator (function):
    def modifiedFunction():
        print("Start")
        function()
        print("End")
    return modifiedFunction

@Decorator
def greet():
    for n in range(20):
        print("Hello world")
        
greet()