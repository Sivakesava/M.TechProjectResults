import numpy
from numpy import matrix,array
import math
########log( L2_Norma)
L2_1=array([-0.42652467, -0.88049173, -1.25444867, -1.5298765 , -1.74163667, -1.91191911])
L2_2=array([-0.31981094, -0.9937115 , -1.36518562, -1.75108068, -2.02936888, -2.26277648])
L2_4=array([-0.10827526, -0.90984621, -2.168276  , -2.64067897, -3.14964635])
L2_8=array([-0.83987684, -2.12272456, -2.77641257])#1#-0.84096   , 
L2_16=array([-3.19114058, -3.18883338])

########log( NOP )
Nop_1=array([  280.,  1084.,  2400.,  4216.,  6532.,  9408.])
for i in range(6):
    Nop_1[i]=math.log10(Nop_1[i])
Nop_2=array([  171.,   630.,  1404.,  2439.,  3735.,  5400.])
for i in range(6):
    Nop_2[i]=math.log10(Nop_2[i])
Nop_4=array([  175.,   475.,  1750.,  2800.,  3900.])
for i in range(5):
    Nop_4[i]=math.log10(Nop_4[i])
Nop_8=array([ 567.,  1458.,  1539.])#1# 324.,   
for i in range(3):
    Nop_8[i]=math.log10(Nop_8[i])
Nop_16=array([ 1156.,  2023.])
for i in range(2):
    Nop_16[i]=math.log10(Nop_16[i])

########WCT
WCT_1=array([   54.60607195,   205.45761681,   452.28267884,   784.71112394, 1188.11847687,  1679.86016202])
for i in range(6):
    WCT_1[i]=math.log10(WCT_1[i])
WCT_2=array([  20.25134611,   70.62777519,  156.23432302,  270.19963908,  408.779212  ,  593.80398798])
for i in range(6):
    WCT_2[i]=math.log10(WCT_2[i])
WCT_4=array([  13.96261716,   34.61423492,  123.33704305,  197.37765002, 273.37155795])
for i in range(5):
    WCT_4[i]=math.log10(WCT_4[i])
WCT_8=array([  31.10647702,  78.53359008,  80.06485796])#1#17.14396787, 
for i in range(3):
    WCT_8[i]=math.log10(WCT_8[i])
WCT_16=array([ 56.37746501,  97.04683805])
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
#WCT_16plot=py.plot(10**WCT_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8'),loc=1)'''
py.title('Exact Integration')
py.xlabel('log(WCT)')
py.ylabel('log(L2)')
py.show()
