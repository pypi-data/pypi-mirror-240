#File type: Object: pData
#By Junxiang H., 2023/07/01
#wacmk.com/cn Tech. Supp.

import numpy as np 
class pData: #this is a sample version of Data Object
	def __init__(self, grid, quantities):
		self.grid=grid
		self.quantities=quantities
	def update(self,quantities):
		self.quantities.update(quantities)
grids=(512,280,128)
ppt=((2,200),
	(np.pi/20,np.pi-np.pi/20),
	(0,2*np.pi))
grid={}
for i in range(3):
	try:
		grid.update({"x"+str(i+1):np.arange(ppt[i][0],ppt[i][1],(ppt[i][1]-ppt[i][0])/grids[i])})
	except:
		continue

quantities={
	"gamma":4/3,
	"c":3e8,
	"mu":1/2,
	"k":1.38e-23,
	"mp":1.6726231e-27,
	"geometry":"SPHERICAL"
}
try:
	quantities.update({"rho":np.random.random((len(grid["x1"]),len(grid["x2"])),len(grid["x3"])),
		"prs":np.random.random((len(grid["x1"]),len(grid["x2"])),len(grid["x3"])),
		"vx1":np.random.random((len(grid["x1"]),len(grid["x2"])),len(grid["x3"])),
		"vx2":np.random.random((len(grid["x1"]),len(grid["x2"])),len(grid["x3"])),
		"vx3":np.random.random((len(grid["x1"]),len(grid["x2"])),len(grid["x3"]))})
except:
	try:
		quantities.update({"rho":np.random.random((len(grid["x1"]),len(grid["x2"]))),
			"prs":np.random.random((len(grid["x1"]),len(grid["x2"]))),
			"vx1":np.random.random((len(grid["x1"]),len(grid["x2"]))),
			"vx2":np.random.random((len(grid["x1"]),len(grid["x2"]))),
			"vx3":np.random.random((len(grid["x1"]),len(grid["x2"])))})
	except:
		quantities.update({"rho":np.random.random((len(grid["x1"]))),
			"prs":np.random.random((len(grid["x1"]))),
			"vx1":np.random.random((len(grid["x1"]))),
			"vx2":np.random.random((len(grid["x1"]))),
			"vx3":np.random.random((len(grid["x1"])))})

try:
	import ShockFinder.Data as Data
	cla=Data.Data
except:
	cla=pData

TestData=cla(grid,quantities)
def get(num):
	return [cla(grid,quantities) for i in range(num)]

if __name__=="__main__":
	print(quantities)