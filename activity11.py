class myclass:
    __privatevar=22

    def __pr(self):
        print("This is a private method")

    def d(self):
        print("this is not a private method",self.__privatevar)

obj=myclass()
obj.d()
obj.__pr()

