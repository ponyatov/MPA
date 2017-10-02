# http://www.instantiations.com/PDFs/papers/avmarch.pdf
from numbers import Number

import ply.lex  as lex
import ply.yacc as yacc

class VM:
    def __init__(self,Node,M=[]):
        self.PC=0 
        if type(M)==type([]): self.M = M    # ready to use list
        else: raise TypeError(M)
        self.Node=Node # computing node name
        self.CMD = {
            'nop':self.nop,'bye':self.bye,
            '+':self.add,'*':self.mul
            }
                        # registers
        self.R = None   ## Receiver/Result
        self.A = None   ## Argument
        self.X = None   ## indeX

        self.S = []     # Stack
        self.Sp = None  ## Stack Pointer
        self.Fp = None  ## Frame Pointer

        self.M = M      # bytecode program Memory
        self.PC = 0     # Program Counter
    
    def __repr__(self):
        return '[%s] R:%s A:%s X:%s S: %s Sp:%s Fp:%s PC:%s M:%s'%(self.Node,\
            self.R,self.A,self.X,self.S,self.Sp,self.Fp,self.PC,self.M)
    def run(self):
        N=0 ; yield self
        while self.PC is not None and N<0x7: self.tick() ; N += 1 ; yield self
    def tick(self):                                 # FETCH/DECODE/EXECUTE
        C = self.M[self.PC] ; self.PC += 1          ## FETCH
        if C in self.CMD: self.CMD[C]()             ## string-encoded opcode
        elif callable(C): C(self)                   ## can be fn(VM):return None
        elif isinstance(C, Number): self.push(C)    ## numbers as is
        else: raise BaseException(C)                ## unsupported command
    # stack/memory/io
    def push(self,X): self.S.append(X)
    def pop(self): return self.S.pop()
    # command set
    ## control flow
    def nop(self): pass
    def bye(self): self.PC=None # stop VM
    ## math
    def add(self): B=self.pop() ; A=self.pop() ; self.push(A.add(B))
    def mul(self): B=self.pop() ; A=self.pop() ; self.push(A.mul(B))
    
S1 = VM('S1','nop 1+2.3*4e-05 bye')
for i in S1.run(): print i
