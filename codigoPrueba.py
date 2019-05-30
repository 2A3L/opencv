#original data, two 2x2 images, normalized
x = rand(2,2)
x/=sum(x)
y = rand(2,2)
y/=sum(y)

#initial guess of the flux matrix
# just the product of the image x as row for the image y as column
#This is a working flux, but is not an optimal one
F = (y.flatten()*x.flatten().reshape((y.size,-1))).flatten()

#distance matrix, based on euclidean distance
row_x,col_x = meshgrid(range(x.shape[0]),range(x.shape[1]))
row_y,col_y = meshgrid(range(y.shape[0]),range(y.shape[1]))
rows = ((row_x.flatten().reshape((row_x.size,-1)) - row_y.flatten().reshape((-1,row_x.size)))**2)
cols = ((col_x.flatten().reshape((row_x.size,-1)) - col_y.flatten().reshape((-1,row_x.size)))**2)
D = np.sqrt(rows+cols)

D = D.flatten()
x = x.flatten()
y = y.flatten()
#COST=sum(F*D)

#cost function
fun = lambda F: sum(F*D)
jac = lambda F: D
#array of constraint

#the constraint of sum one is implicit given the later constraints
cons  = []

#each row and columns should sum to the value of the start and destination array
cons += [ {'type': 'eq', 'fun': lambda F:  sum(F.reshape((x.size,y.size))[i,:])-x[i]}     for i in range(x.size) ]
cons += [ {'type': 'eq', 'fun': lambda F:  sum(F.reshape((x.size,y.size))[:,i])-y[i]} for i in range(y.size) ]

#the values of F should be positive
bnds = (0, None)*F.size

from scipy.optimize import minimize
res = minimize(fun=fun, x0=F, method='SLSQP', jac=jac, bounds=bnds, constraints=cons)
