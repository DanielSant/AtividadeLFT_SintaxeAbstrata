class Visitor():
  def visitSomaExp(self, somaExp):
    somaExp.exp1.accept(self)
    print('+', end = ' ')
    somaExp.exp2.accept(self)

  def visitMulExp(self, mulExp):
    mulExp.exp1.accept(self)
    print('*', end = ' ')
    mulExp.exp2.accept(self)

  def visitPotExp(self, potExp):
    potExp.exp1.accept(self)
    print('^', end = ' ')
    potExp.exp2.accept(self)

  def visitCallExp(self, callExp):
    callExp.call.accept(self)

  def visitAssignExp(self, assignExp):
    assignExp.assign.accept(self)

  def visitNumExp(self, numExp):
    print(numExp.num, end = ' ')

  def visitIDExp(self, idExp):
    print(idExp.Id, end = ' ')
  
  def visitParamsCall(self,paramsCall):
    print(paramsCall.Id, end = ' ')
    print('(', end =' ')
    paramsCall.Params.accept(self)
    print(')', end =' ')
  
  def visitSimpleCall(self,simpleCall):
    simpleCall.Id.accept(self)
    print('(', end = ' ')
    print(simpleCall.Id, end = ' ')

  def visitCompoundParams(self, compoundParams):
    print(compoundParams.Id, end = ', ')
    compoundParams.params.accept(self)

  def visitSingleParam(self,singleParam):
    singleParam.Id.accept(self)
    print(singleParam.Id, end =' ')

  def visitAssignC(self,assignExp):
    print(assignExp.Id, end =' ')
    print('=', end = ' ')
    assignExp.exp.accept(self)