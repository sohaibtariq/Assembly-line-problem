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

def calculate(lines,e,x,n,line):
	t1=0
	t2=0
	t3=0
	global path
	if n==0:
		path.append(())
		return e[line] + lines[0][0].f
		
	if line == 0:
		t1=min(calculate(lines,e,x,n-1,0)+lines[0][n].f,
			   calculate(lines,e,x,n-1,1) + lines[1][n].t[0] + lines[0][n].f,
			   calculate(lines,e,x,n-1,2) + lines[2][n].t[0] + lines[0][n].f)
	elif line == 1:
	 	t2=min(calculate(lines,e,x,n-1,1)+lines[1][n].f,
			   calculate(lines,e,x,n-1,0) + lines[0][n].t[1] + lines[1][n].f,
			   calculate(lines,e,x,n-1,2) + lines[2][n].t[1] + lines[1][n].f)
	elif line == 2:
	 	t3=min(calculate(lines,e,x,n-1,1)+lines[2][n].f,
			   calculate(lines,e,x,n-1,0) + lines[0][n].t[2] + lines[2][n].f,
			   calculate(lines,e,x,n-1,2) + lines[1][n].t[2] + lines[2][n].f)
	 
	return min(t1,t2,t3)


	

	# l1=calculate(lines,0,station-1)
	# l2=calculate(lines,1,station-1)
	# l3=calculate(lines,2,station-1)



	# time += min(l1,l2,l3)
	
	# if min(l1,l2,l3) == l1:
	# 	path.append((0,station))
	# elif min(l1,l2,l3) == l2:
	# 	path.append((1,station))
	# elif min(l1,l2,l3) == l3:
	# 	path.append((2,station))

	# return time;	
	 


lines=[ [node(5,0,1,2),node(6,0,2,3),node(7,0,0,0),node(3,0,0,0)], 
		[node(8,3,0,2),node(8,1,0,3),node(7,0,0,0),node(4,0,0,0)],
		[node(2,3,2,0),node(3,1,2,0),node(7,0,0,0),node(5,0,0,0)] ]
e=[2,3,4]
x=[4,5,4]

print calculate(lines,e,x,2,2)
print path