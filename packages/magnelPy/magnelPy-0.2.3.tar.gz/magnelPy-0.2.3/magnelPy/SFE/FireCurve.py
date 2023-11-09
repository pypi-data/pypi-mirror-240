"""Fire definition

Notes
-----
The FireCurve module supports definition of temperature-time curves for SFE.
"""

#############
## IMPORTS ##
#############

import numpy as np
import math as m
from scipy.interpolate import interp1d

############
## MODULE ##
############

def ISO834(time):
	""" Return ISO834 gas temperature at specified times

	Parameters
	----------
	time :	np.array
		array of time instants [min]

	Returns
	-------
	fire :	np.array
		array of gas temperatures for time [C]

	Reference
	---------
	EN 1991-1-2:2002. Eurocode 1: Actions on structures - Part 1-2:
		General actions - Actions on structures exposed to fire, 3.2.1 (p24) 

	Examples
	--------
	>>> import numpy as np
	>>> import magnelPy.SFE as sfe
	>>> time = np.arange(0,120+1,1)
	>>> fire = sfe.FireCurve.ISO834(time)
	>>> print(np.array([time[[0,30,60,90,120]],
		np.around(fire[[0,30,60,90,120]],0)]))
	[[   0.   30.   60.   90.  120.]
 	[  20.  842.  945. 1006. 1049.]]
	"""
	return 20+345*np.log10(8*time+1)


def ASTM(time):
	""" Return ASTM-E119 gas temperature at specified times

	Parameters
	----------
	time :	np.array
		array of time instants [min]

	Returns
	-------
	fire :	np.array
		array of gas temperatures for time [C]

	Reference
	---------
	ASTM E119-00a: Fire Tests of Building Construction and Materials
	via https://www.nrc.gov/docs/ML0516/ML051640380.pdf

	"""
	t_list = np.array([0,5,10,20,30,60,90,120,180,240,300,360,420,480]) # [min]
	T_list = np.array([68,1000,1300,1462,1550,1700,1792,1850,1925,2000,2075,2150,2225,2300]) # [°F]
	T_list = (T_list-32)*5/9 # conversion °F -> °C
	T_data = interp1d(t_list,T_list)
	return T_data(time)


def EuroCodeParametric(time, openingFactor, fireLoadDensity, thermalInertia=1450, length=10, width=10, height=3, t_lim = 20, Reitgruber=False):
	""" Return Eurocode Parametric fire gas temperature at specified times

	Parameters
	----------
	time :	np.array
		array of time instants [min]

	openingFactor : float
		opening factor (typically) between 0.02 and 0.2 [m1/2]

	fireLoadDensity : float
		fire load density related to the surface area [MJ/m2]

	thermalInertia : float
		thermal interia of the compartment, typically between 100 and 2200 [J/m2 s1/2 K] (default = 1450 J/m2 s1/2 K)

	length, width, height : float
		dimensions of a rectangular compartment [m] (default = 10/10/3 m)

	t_lim : float
		factor which indicates the fire growth rate [min] (default = 20 min)
		
	Reitgruber : Boolean
		Take into account correction proposed by Reitguber et al. * (default = False)

	Returns
	-------
	fire :	np.array
		array of gas temperatures for time [C]

	Reference
	---------
	EN 1991-1-2:2002. Eurocode 1: Actions on structures - Part 1-2:
	  Annex A - Parametric temperature-time curves (p30-32)
   *Reitgruber, S., Blasi, C. Di and Franssen, J. (2006) ‘Some Comments on the Parametric Fire Model of Eurocode 1’, 
	    Conference on Fire in Enclosures, (January 2006), pp. 1–25.
	
	Examples
	--------
	>>> import numpy as np
	>>> import magnelPy.SFE as sfe
	>>> time = np.arange(0,120+1,1)
	>>> fire = sfe.FireCurve.EuroCodeParametric(time,0.05,500,1450,10,10,3)
	"""

	# calculation of other parameters required to determine the shape of the heating a cooling phase curves
	A_f = length*width # [m2] floor area
	A_t = 2*A_f + 2*height*(length+width) # [m2] total compartment surface area
	qt_d = fireLoadDensity*A_f/A_t # [MJ/m2] design value of the fire load density related to the total surface area A_t
	Of_lim = 0.0001*qt_d/(t_lim/60) # [m1/2] adjusted opening factor in case of fuel controlled fire
	t_max = max(t_lim/60, 0.0002*qt_d/openingFactor) # [hours] time at which the maximum temperature in the heating phase occurs
	if Reitgruber: 
		Of_lim = 0.00014*qt_d/(t_lim/60)
		t_max = max(t_lim/60, 0.00014*qt_d/openingFactor)
	Lambda = ((openingFactor/thermalInertia)**2)/((0.04/1160)**2) # [-] time scale parameter
	k = 1 + ((openingFactor-0.04)/0.04)*((qt_d-75)/75)*((1160-thermalInertia)/1160) if (openingFactor > 0.04 and qt_d > 75 and thermalInertia <1160) else 1
	Lambda_lim = k*((Of_lim/thermalInertia)**2)/((0.04/1160)**2) # [-] time scale parameter in case of fuel controlled fire
	Lambda_use = Lambda_lim if t_max==t_lim/60 else Lambda
	t_max_st = t_max*Lambda if t_max > t_lim/60 else t_max*Lambda_lim
	theta_max = 20+1325*(1-0.324*m.exp(-0.2*t_max*Lambda_use)-0.204*m.exp(-1.7*t_max*Lambda_use)-0.472*m.exp(-19*t_max*Lambda_use)) # time temperature curve for heating phase (EN 1991-1-2 - Formula A.1)
	x = 1 if t_max>t_lim/60 else t_lim/60*Lambda/(t_max*Lambda_use)
	
	# calcalate tempertures [°C]
	temp_list = []
	for t in time:
		if t/60 <= t_max: # heating phase
			temp_list.append(20+1325*(1 - 0.324*m.exp(-0.2*(t/(60/Lambda_use))) - 0.204*m.exp(-1.7*(t/(60/Lambda_use))) - 0.472*m.exp(-19*(t/(60/Lambda_use)))))
		else: # cooling phase
			if t_max_st < 0.5:
				temp_list.append(max(20,theta_max - 625*(t/60*Lambda - t_max_st*x))) # (EN 1991-1-2 - Formula A.11a)
			else:
				if t_max_st < 2:
					temp_list.append(max(20,theta_max - 250*(3 - t_max_st)*(t/60*Lambda - t_max_st*x))) # (EN 1991-1-2 - Formula A.11b)
				else:
					temp_list.append(max(20,theta_max - 250*(t/60*Lambda - t_max_st*x))) # (EN 1991-1-2 - Formula A.11c)
	return temp_list

def EPFC(time, openingFactor, fireLoadDensity, thermalInertia=1450, length=10, width=10, height=3, t_lim = 20, Reitgruber=False):
	""" Return Eurocode Parametric fire gas temperature at specified times - vectorized function

	Parameters
	----------
	time :	np.array (m,)
		array of time instants [min]

	openingFactor : np.array (n,)
		array of opening factor (typically) between 0.02 and 0.2 [m1/2]

	fireLoadDensity : np.array (n,)
		array of fire load density related to the surface area [MJ/m2]

	thermalInertia : float or np.array (n,)
		thermal interia of the compartment, typically between 100 and 2200 [J/m2 s1/2 K] (default = 1450 J/m2 s1/2 K)

	length, width, height : float or np.array (n,)
		dimensions of a rectangular compartment [m] (default = 10/10/3 m)

	t_lim : float or np.array (n,)
		factor which indicates the fire growth rate [min] (default = 20 min)
		
	Reitgruber : Boolean
		Take into account correction proposed by Reitguber et al. * (default = False)

	Returns
	-------
	fire :	np.array(n,m)
		array of gas temperatures for time [C]

	Reference
	---------
	EN 1991-1-2:2002. Eurocode 1: Actions on structures - Part 1-2:
	  Annex A - Parametric temperature-time curves (p30-32)
	Reitgruber, S., Blasi, C. Di and Franssen, J. (2006) ‘Some Comments on the Parametric Fire Model of Eurocode 1’, 
	    Conference on Fire in Enclosures, (January 2006), pp. 1–25.
	
	Examples
	--------
	import numpy as np
	import magnelPy.SFE as sfe
	time = np.arange(0,120+1,1)
	O=np.array([0.04,0.05])
	qf=np.array([600,700])
	fire = sfe.FireCurve.EPFC(time,O,qf)
	timeprint=[30,60,90,120]
	for t in timeprint:
    	print("At {0:.0f} min, the temperature is {1:.0f} degrees C for curve1 and {2:.0f} degrees for curve2.".format(t,fire[0,t],fire[1,t]))
	>>> At 30 min, the temperature is 784 degrees C for curve1 and 841 degrees for curve2.
	>>> At 60 min, the temperature is 843 degrees C for curve1 and 857 degrees for curve2.
	>>> At 90 min, the temperature is 651 degrees C for curve1 and 592 degrees for curve2.
	>>> At 120 min, the temperature is 459 degrees C for curve1 and 326 degrees for curve2.
	"""	
	## check np.array
	if not isinstance(openingFactor,np.ndarray) or not isinstance(fireLoadDensity,np.ndarray):
		raise NameError("This function requires np.array (n,) for both the opening factor and fire load density.")

	## Preparatory steps
	A_f = length*width # [m2] floor area
	A_t = 2*A_f + 2*height*(length+width) # [m2] total compartment surface area
	qt_d = fireLoadDensity*A_f/A_t # [MJ/m2] design value of the fire load density related to the total surface area A_t
	if Reitgruber:
		Of_lim = 0.00014*qt_d/(t_lim/60)
		t_max = np.maximum(t_lim/60, 0.00014*qt_d/openingFactor)
	else: 
		Of_lim = 0.0001*qt_d/(t_lim/60) # [m1/2] adjusted opening factor in case of fuel controlled fire
		t_max = np.maximum(t_lim/60, 0.0002*qt_d/openingFactor)
	Lambda = ((openingFactor/thermalInertia)**2)/((0.04/1160)**2) # [-] time scale parameter
	k=1+((openingFactor-0.04)/0.04)*((qt_d-75)/75)*((1160-thermalInertia)/1160)*(openingFactor > 0.04)*(qt_d > 75)*(thermalInertia <1160)
	Lambda_lim = k*((Of_lim/thermalInertia)**2)/((0.04/1160)**2) # [-] time scale parameter in case of fuel controlled fire
	Lambda_use = np.where(t_max<=t_lim/60,Lambda_lim,Lambda)
	t_max_st = t_max*Lambda_use
	theta_max = 20+1325*(1-0.324*np.exp(-0.2*t_max_st)-0.204*np.exp(-1.7*t_max_st)-0.472*np.exp(-19*t_max_st)) # time temperature curve for heating phase (EN 1991-1-2 - Formula A.1)
	x = np.where(t_max>t_lim/60,1,t_lim/60*Lambda/(t_max*Lambda_use))
	
	## temperature-time calculation
	n=len(theta_max)
	time=time[np.newaxis,:]
	Lambda_use=Lambda_use[:,np.newaxis]; Lambda=Lambda[:,np.newaxis]; theta_max=theta_max[:,np.newaxis]
	# heating phase curve
	Tgh=20+1325*(1-0.324*np.exp(-0.2*time/60*Lambda_use)-0.204*np.exp(-1.7*time/60*Lambda_use)-0.472*np.exp(-19*time/60*Lambda_use))
	# cooling phase curve
	xi=[0.5,2]; yi=[625,250]; rate=np.reshape(np.interp(t_max_st,xi,yi),(n,1))
	Tgc=theta_max - rate*(time/60*Lambda - np.reshape(t_max_st*x,(n,1)))
	# assign temperatures, with reference (minimum) temperature of 20 degrees
	Tg=np.maximum(np.where(Tgc>theta_max,Tgh,Tgc),20)
	
	return Tg 

#########################
## STAND ALONE - DEBUG ##
#########################

if __name__ == "__main__":

	print("testing")