import time

class Foo:
    def __init__(self):
        self.flag=0
        
    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.flag=1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.flag!=1:
            time.sleep(0.01)
        printSecond()
        self.flag=2


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.flag!=2:
            time.sleep(0.01)
        printThird()
        self.flag=3
