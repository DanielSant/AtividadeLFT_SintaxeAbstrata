from abc import abstractmethod
from abc import ABCMeta

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

    class SomaExp(Exp):
        def __init__(self, exp1, exp2):
            self.exp1 = exp1
            self.exp2 = exp2
        def accept(self, Visitor):
            Visitor.visitSomaExp(self)

    class MulExp(Exp):
        def __init__(self, exp1, exp2):
            self.exp1 = exp1
            self.exp2 = exp2
        def accept(self, Visitor):
            Visitor.visitMulExp(self)

    class PotExp(Exp):
        def __init__(self, exp1, exp2):
            self.exp1 = exp1
            self.exp2 = exp2
        def accept(self, Visitor):
            Visitor.visitPotExp(self)

    class CallExp(Exp):
        def __init__(self, call):
            self.call = call
        def accept(self, Visitor):
            Visitor.visitCallExp(self)
    
    class AssignExp(Exp):
        def __init__(self, assign):
            self.assign = assign
        def accept(self, Visitor):
            Visitor.visitAssignExp(self)

    class NumExp(Exp):
        def __init__(self, num):
            self.num = num
        def accept(self, Visitor):
            Visitor.visitNumExp(self)

    class IDExp(Exp):
        def __init__(self, Id):
            self.Id = Id
        def accept(self, Visitor):
            Visitor.visitIDExp(self)

class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

    class ParamsCall(Exp):
        def __init__(self, Id, Params):
            self.Id = Id
            self.Parms = Params
        def accept(self, Visitor):
            Visitor.visitParamsCall(self)