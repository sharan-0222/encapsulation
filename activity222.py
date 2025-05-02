class s:
    def __init__(self):
        self.__price=900

    def sell(self):
        print(f"selling price of computer= {self.__price}")

    def maxprice(self,mprice):
        self.__price=mprice

comp=s()
comp.sell()
comp.__price=1000
comp.sell()
comp.maxprice(2000000000)
comp.sell()
