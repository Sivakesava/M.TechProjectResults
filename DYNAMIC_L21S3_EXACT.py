#### DYNAMIC PEAK REFINEMENT NORMS USING EXACT INTEGRATION
import numpy
from numpy import matrix,array
import math
########log( L2_Norma)
L2_1=array([-0.54082174, -0.87107187, -1.1775333 , -1.46629738, -1.64000789, -1.74204731])
L2_2=array([-0.45197343, -0.9578087 , -1.48990716, -1.92974866, -2.11061728, -2.4031095 ])
L2_4=array([-0.44547129, -1.23800272, -2.37822032, -2.86374106, -3.2244443 ])
L2_8=array([-0.15441694, -1.12404656, -2.35617729, -3.08854449])
L2_16=array([ -1.02783315,  -3.26073694])

########log( NOP )
#Nop_1=array([ 2.40823997,  3.01029996,  3.36248247,  3.61235995,  3.80617997, 3.96454247])
#Nop_2=array([ 2.15836249,  2.76042248,  3.112605  ,  3.36248247,  3.5563025 , 3.71466499])
#Nop_4=array([ 2.        ,  2.60205999,  3.20411998,  3.39794001])
#Nop_8=array([ 1.90848502,  2.51054501,  2.86272753,  3.112605  ])
#Nop_16=array([ 2.46089784,  3.06295783])
Nop_1=array([ 2.44715803,  3.03502928,  3.38021124,  3.6249006 ,  3.81504618,3.97349731])
Nop_2=array([ 2.23299611,  2.79934055,  3.14736711,  3.3872118 ,  3.57229061,3.73239376])
Nop_4=array([ 2.24303805,  2.67669361,  3.24303805,  3.44715803,  3.59106461])
Nop_8=array([ 2.51054501,  2.75358306,  3.16375752,  3.18723862])
Nop_16=array([ 3.06295783,  3.30599588])
########WCT
#WCT_1=array([   53.19979286,   200.6412859 ,   441.08559799,   767.79017591, 1197.16687202,  1719.58901191])
#WCT_2=array([  20.88465309,   70.88935399,  154.07966113,  269.23520112, 431.66837001,  622.10404611])
#WCT_4=array([  15.01597404,   37.78011322,  131.58896399,  203.20119309])
#WCT_8=array([ 18.92670488,  34.31395197,  63.69349313,  88.72508597])
#WCT_16=array([  64.94717002,  110.88217902])
WCT_1=array([   51.42225504,   193.69366693,   426.58717203,   769.94240594, 1173.87319803,  1686.42735195])
for i in range(6):
    WCT_1[i]=math.log10(WCT_1[i])
WCT_2=array([  20.44516182,   69.55468202,  150.84818101,  263.02969599, 405.52999377,  586.10651994])
for i in range(6):
    WCT_2[i]=math.log10(WCT_2[i])
WCT_4=array([  14.01235294,   34.86962795,  121.16120791,  186.79994011, 264.05232   ])
for i in range(5):
    WCT_4[i]=math.log10(WCT_4[i])
WCT_8=array([ 17.17723298,  31.13831615,  57.37526488,  80.3319242 ])
for i in range(4):
    WCT_8[i]=math.log10(WCT_8[i])
WCT_16=array([  56.31972003,   97.41178989])
for i in range(2):
    WCT_16[i]=math.log10(WCT_16[i])
print 'dt=1e-3'
import pylab as py

#########PLOTS
'''L2_1plot=py.plot(10**Nop_1,L2_1,'rD-')
L2_2plot=py.plot(10**Nop_2,L2_2,'b*-')
L2_4plot=py.plot(10**Nop_4,L2_4,'go-')
L2_8plot=py.plot(10**Nop_8,L2_8,'k>-')
L2_16plot=py.plot(10**Nop_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=1)
'''
L2_1plot=py.plot(Nop_1,L2_1,'rD-')
L2_2plot=py.plot(Nop_2,L2_2,'b*-')
L2_4plot=py.plot(Nop_4,L2_4,'go-')
L2_8plot=py.plot(Nop_8,L2_8,'k>-')
L2_16plot=py.plot(Nop_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=3)
py.title('Exact Integration')
py.xlabel('log(Nop)')
py.ylabel('log(L2)')

py.show()
#L2_8plot=py.plot(Nop_8,L2_8,color='k')
#L2_16plot=py.plot(Nop_16,L2_16,color='m')
WCT_1plot=py.plot(WCT_1,L2_1,'rD-')
WCT_2plot=py.plot(WCT_2,L2_2,'b*-')
WCT_4plot=py.plot(WCT_4,L2_4,'go-')
WCT_8plot=py.plot(WCT_8,L2_8,'k>-')
WCT_16plot=py.plot(WCT_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=3)
'''
WCT_1plot=py.plot(10**WCT_1,L2_1,'rD-')
WCT_2plot=py.plot(10**WCT_2,L2_2,'b*-')
WCT_4plot=py.plot(10**WCT_4,L2_4,'go-')
WCT_8plot=py.plot(10**WCT_8,L2_8,'k>-')
WCT_16plot=py.plot(10**WCT_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=1)'''
py.title('Exact Integration')
py.xlabel('log(WCT)')
py.ylabel('log(L2)')
py.show()
