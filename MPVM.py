# http://www.instantiations.com/PDFs/papers/avmarch.pdf

            # registers
R = None    ## Receiver/Result
A = None    ## Argument
X = None    ## indeX

S = []      # Stack
Sp = None   ## Stack Pointer
Fp = None   ## Frame Pointer

PC = None   # Program Counter


  
# import Queue
# from numbers import Number
# 
# Q = Queue.Queue()   # sys.queue
# 
# def nop(): pass
# def bye(): Q.queue.clear()  # drop system queue
# def add(): pass
# 
# R = {'+':add}
# 
# Q.put(nop)
# # Q.put(bye)
# Q.put('+')
# Q.put(1)
# Q.put(2.3)
# 
# class Prim:
#     def __repr__(self): return '%s:%s'%(self.__class__.__name__.lower(),self.val)
# class Num(Prim):
#     def __init__(self,N): self.val = N 
# 
# while not Q.empty():
#     C = Q.get() ; print C.__class__,C,
#     if callable(C): print 'fn',C(), # functions must be executed as VM commands
#     elif isinstance(C, Number): print 'num', ; Q.put(Num(C)) # numbers must we wrapped
#     elif C in R: print 'R',R[C],R[C](),
#     print
