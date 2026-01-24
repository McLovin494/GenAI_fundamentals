class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare_chai(self):
        print(f"Preparing {self.type} chai ...")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("adding cardaomom, ginger and cloves")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        # holds a object of class basechai
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"serving {self.chai.type} chai in the shop")
        self.chai.prepare_chai()


class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai
