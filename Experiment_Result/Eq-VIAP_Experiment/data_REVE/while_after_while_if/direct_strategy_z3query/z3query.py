import sys
import os
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/setuptools/")
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/z3/python/")
from z3 import *
init(currentdirectory+"/packages/z3")
set_param(proof=True)

try:
	_p1=Int('_p1')
	_p2=Int('_p2')
	_n=Int('_n')
	_bool=Int('_bool')
	arraySort = DeclareSort('arraySort')
	_f=Function('_f',IntSort(),IntSort())
	_ToReal=Function('_ToReal',RealSort(),IntSort())
	_ToInt=Function('_ToInt',IntSort(),RealSort())
	p1c=Int('p1c')
	p2r10=Function('p2r10',IntSort(),IntSort())
	p1t=Int('p1t')
	p1x1=Int('p1x1')
	p2c=Int('p2c')
	p2x8=Function('p2x8',IntSort(),IntSort())
	p2x1=Int('p2x1')
	p1t1=Int('p1t1')
	p2c8=Function('p2c8',IntSort(),IntSort())
	p1c1=Int('p1c1')
	p1c2=Function('p1c2',IntSort(),IntSort())
	p2r1=Int('p2r1')
	p2c1=Int('p2c1')
	p1r5=Function('p1r5',IntSort(),IntSort())
	p2t1=Int('p2t1')
	p1r1=Int('p1r1')
	_N2=Const('_N2',IntSort())
	_N3=Const('_N3',IntSort())
	_N1=Const('_N1',IntSort())
	_N4=Const('_N4',IntSort())
	p2t=Int('p2t')
	p2r=Int('p2r')
	_n2=Int('_n2')
	_n3=Int('_n3')
	_n1=Int('_n1')
	p1r=Int('p1r')
	_n4=Int('_n4')
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p2t1 == p2t)
	_s.add(p1t1 == p1t)
	_s.add(p1c1 == If(0 < p1t,p1c-_N1,p1c))
	_s.add(p2c1 == p2c-_N3)
	_s.add(p1r1 == p1r-_N2)
	_s.add(p2r1 == p2r-_N4)
	_s.add(p1x1 == ((2*_N2)+(If(0 < p1t,_N1,0))))
	_s.add(p2x1 == _N3 + 2*_N4)
	_s.add(0 <= -p1c+_N1)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),0 < p1c-_n1)))
	_s.add(Or(_N1==0,0 < p1c-_N1+1))
	_s.add(0 <= -p1r+_N2)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),p1r-_n2 > 0)))
	_s.add(Or(_N2==0,p1r-_N2 + 1 > 0))
	_s.add(0 <= -p2c+_N3)
	_s.add(ForAll([_n3],Implies(And(_n3 < _N3,_n3>=0),0 < p2c-_n3)))
	_s.add(Or(_N3==0,0 < p2c-_N3 + 1))
	_s.add(0 <= -p2r+_N4)
	_s.add(ForAll([_n4],Implies(And(_n4 < _N4,_n4>=0),p2r-_n4 > 0)))
	_s.add(Or(_N4==0,p2r-_N4 + 1 > 0))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(_N3>=0)
	_s.add(_N4>=0)
	_s.add(And(And(((p1t)==(p2t)),((p1c)==(p2c))),((p1r)==(p2r))))
	_s.add(Not(((((2*_N2)+(If(0 < p1t,_N1,0))))==(If((0<p2t),(_N3),0) + 2*_N4))))

except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()

	sys.exit(1)

try:
	result=_s.check()
	if sat==result:
		print "Counter Example"
		print _s.model()
	elif unsat==result:
		result
		try:
			if os.path.isfile('j2llogs.logs'):
				file = open('j2llogs.logs', 'a')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
			else:
				file = open('j2llogs.logs', 'w')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
		except Exception as e:
			file = open('j2llogs.logs', 'a')
			file.write("\n**************\nProof Details\n**************\n"+"Error"+"\n")
			file.close()
		print "Successfully Proved"
	else:
		print "Failed To Prove"
except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()
