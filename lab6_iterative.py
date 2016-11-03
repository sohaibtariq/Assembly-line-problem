"""
-	Create a node class that contains an integer variable ‘f’ that represents the amount of time a
	 chassis spends on a station and a list ‘ t’ that contains the time it would take to shift the
	  chassis from the current station to the next station in a different assembly line.
-   lines represents the 3 assembly lines 
-   For example, If we were to shift the chassis from the current position of lines[1][1] to lines[0][2] we would require time=lines[1][1].t[0]
-	An assembly line is represented by a list that contains objects of the node class
-	The time required to initially load a chassis onto an assembly line is represented by  list ‘e’
-	The  time required to unload a chassis from an assembly line is represented by list ‘x’

"""
path=[]
class node:
	def __init__(self, stationTime, transferTime1, transferTime2, transferTime3):
		self.f=stationTime
		self.t=[transferTime1,transferTime2,transferTime3]

def calculate(lines, e, x):
	t1=[]
	t2=[]
	t3=[]
	global path
	t1.append(e[0] + lines[0][0].f)
	t2.append(e[1] +lines[1][0].f)
	t3.append(e[2] +lines[2][0].f)

	if min(t1,t2,t3) == t1:
			path.append((0,0))
	elif min(t1,t2,t3) == t2:
			path.append((1,0))
	elif min(t1,t2,t3) == t3:
			path.append((2,0))
	
	for i in range(1,len(lines)):
		t1.append(min(t1[i-1]+lines[0][i].f, 
					  t2[i-1]+lines[1][i-1].t[0]+lines[0][i].f, 
					  t3[i-1]+lines[2][i-1].t[0]+lines[0][i].f))
		
		t2.append(min(t2[i-1]+lines[1][i].f,
				      t1[i-1]+lines[0][i-1].t[1]+ lines[1][i].f, 
				      t3[i-1]+lines[2][i-1].t[1]+ lines[1][i].f))


		t3.append(min(t3[i-1]+lines[2][i].f,
				      t1[i-1]+lines[0][i-1].t[2]+ lines[2][i].f, 
				      t2[i-1]+lines[1][i-1].t[2]+ lines[2][i].f))


		if min(t1,t2,t3) == t1:
			path.append((0,i))
		elif min(t1,t2,t3) == t2:
			path.append((1,i))
		elif min(t1,t2,t3) == t3:
			path.append((2,i))

	return min(t1[-1]+x[0],t2[-1]+x[1],t3[-1]+x[2])




lines=[ [node(5,0,1,2),node(6,0,2,3),node(7,0,0,0)], 
		[node(8,3,0,2),node(8,1,0,3),node(7,0,0,0)],
		[node(2,3,2,0),node(3,1,2,0),node(7,0,0,0)] ]
e=[2,3,4]
x=[4,5,4]
print calculate(lines,e,x)
print path
print min(e,x)
