class Visitor():
  def visitSomaExp(self, somaExp):
    somaExp.exp1.accept(self)
    print('+')
    somaExp.exp2.accept(self)

  def visitMultExp(self, mulExp):
    mulExp.exp1.accept(self)
    print('*')
    mulExp.exp2.accept(self)

  def visitPotExp(self, potExp):
    potExp.exp1.accept(self)
    print('^')
    potExp.exp2.accept(self)

  def visitCallExp(self, callExp):
    callExp.call.accept(self)

  def visitAssignExp(self, assignExp):
    assignExp.assign.accept(self)

  def visitNumExp(self, numExp):
    numExp.num.accept(self)
    print(num)

  def visitIDExp(self, idExp):
    idExp.Id.accept(self)
    print(Id)
  
  def visitParamsCall(self,paramsCall):
    paramsCall.Id.accept(self)
    print(Id)
    paramsCall.Params.accept(self)
    print(Params)
  
  def visitSimpleCall(self,simpleCall):
    simpleCall.Id.accept(self)
    print(Id)
  
  def visitCompoundParams(self, compoundParams):
    compoundParams.Id.accept(self)
    print(Id)
    compoundParams.Params.accept(self)
    print(Params)

  def visitSingleParam(self,singleParam):
    singleParam.Id.accept(self)
    print(Id)

  def visitAssignExp(self,assignExp):
    assignExp.Id.accept(self)
    print(Id)
    assignExp.exp.accept(self)
    print(exp)
    

    