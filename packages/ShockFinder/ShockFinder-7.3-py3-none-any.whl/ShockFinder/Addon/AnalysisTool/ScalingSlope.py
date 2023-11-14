#File BlackHoleMassFlux
#Only for 2D data, support SPHERICAL, POLAR, XOY
#	edge: fall into black hole, match accretion rate.
# 		plus : escape from black hole, minor: fall into black hole
#	inj: injet flow
#		plus : accreted into system, minor: escape from system
#	wind: wind
#		plus: back to system, minor: escape from system
#	outflow:
#		plus: back to system, minor: escape from system	
#   jet:
#		plus: escape from bh,....
#in each case, positive flux means material go to accretion region
#ac_begin and ac_end are size of accretion region (Escapt Polar coordinate)

try:
	from ShockFinder.Addon.AnalysisTool.Basic import *
	import ShockFinder.Addon.AnalysisTool.Differential as Differential
	#if AvgTh_CAL is True
	#import ShockFinder.Addon.AnalysisTool.Mean as Mean
	#import ShockFinder.Addon.AnalysisTool.<packages name> as <packages name>
except Exception as err:
	print(err)
	from Basic import *
	import Differential
	#import Mean #debug
	#import <packages name>

need=[]
#args will be inserted into Data Object
#vargs will not be inserted into Data Object
import numpy as np,math
def get(Dataobj,quantity_name,args={},vargs={}):
	if type(quantity_name) in (np.ndarray,list,tuple):
		for i in quantity_name:
			Dataobj=get(Dataobj,i,args,vargs)
		return Dataobj
	Dataobj.quantities.update(args)
	rho_0=get_par(Dataobj,vargs,"rho_0",1)
	need=[quantity_name,"Gradient_"+quantity_name+"_x1"]
	for i in need:
		if i not in Dataobj.quantities.keys() and i not in vargs.keys():
			print("Warning: args:",i,"is needed")
			return Dataobj
	quantities={
		"ScalingSlope_"+quantity_name:Dataobj.grid["x1"]/Dataobj.quantities[quantity_name]*Dataobj.quantities["Gradient_"+quantity_name+"_x1"]
	}
	Dataobj.quantities.update(quantities)
	return Dataobj
def result(quantity_name=None,anafname=None):
	return ["ScalingSlope_"+i for i in quantity_name.split(",")] #this function will return result types shown in GUI

if __name__=="__main__":
	pass