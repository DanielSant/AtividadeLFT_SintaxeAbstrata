from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

# FuncDecl Abstrata
class FuncDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class FuncDeclConcrete(FuncDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body

    def accept(self, Visitor):
        return Visitor.visitFuncDeclConcrete(self)

# Signature Abstrata
class Signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class SignatureConcrete(Signature):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams

    def accept(self, Visitor):
        return Visitor.visitSignatureConcrete(self)

# SigParams Abstrata
class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class SingleSigParams(SigParams):
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def accept(self, Visitor):
        return Visitor.visitSingleSigParams(self)

class CompoundSigParams(SigParams):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams

    def accept(self, Visitor):
        return Visitor.visitCompoundSigParams(self)

# Body Abstrata
class Body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class BodyConcrete(Body):
    def __init__(self, stms):
        self.stms = stms

    def accept(self, Visitor):
        return Visitor.visitBodyConcrete(self)

# Stms Abstrata
class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class SingleStm(Stms):
    def __init__(self, stm):
        self.stm = stm

    def accept(self, Visitor):
        return Visitor.visitSingleStm(self)

class CompoundStm(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms

    def accept(self, Visitor):
        return Visitor.visitCompoundStm(self)

# Stm Abstrata
class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class StmExp(Stm):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, Visitor):
        return Visitor.visitStmExp(self)

class StmWhile(Stm):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block

    def accept(self, Visitor):
        return Visitor.visitStmWhile(self)

class StmReturn(Stm):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, Visitor):
        return Visitor.visitStmReturn(self)

# Exp Abstrata
class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class AssignExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, Visitor):
        return Visitor.visitAssignExp(self)

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, Visitor):
        return Visitor.visitSomaExp(self)

class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        
    def accept(self, Visitor):
        return Visitor.visitMulExp(self)

class PotExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, Visitor):
        return Visitor.visitPotExp(self)


class CallExp(Exp, Stm):
    def __init__(self, call):
        self.call = call

    def accept(self, Visitor):
        return Visitor.visitCallExp(self)

class NumExp(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, Visitor):
        return Visitor.visitNumExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, Visitor):
        return Visitor.visitIdExp(self)

class BooleanExp(Exp):
    def __init__(self, boolValue):
        self.boolValue = boolValue
    def accept(self, Visitor):
        return Visitor.visitBooleanExp(self)

# Call Abstrata
class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class ParamsCall(Call):
    def __init__ (self, id, params):
        self.id = id
        self.params = params
    def accept(self, Visitor):
        return Visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id
    def accept(self, Visitor):
        return Visitor.visitNoParamsCall(self)

# Params Abstrata
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, Visitor):
        return Visitor.visitCompoundParams(self)

class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, Visitor):
        return Visitor.visitSingleParam(self)