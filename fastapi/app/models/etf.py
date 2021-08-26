from py2neo import Model

class ETF(Model):
    __primarykey__ = "symbol"

    symbol = Property()
    description = Property()
