import numpy
from numpy import matrix,array
import math
########log( L2_Norma)
L2_1=array([-0.42652486, -0.88049465, -1.25444948, -1.52987059, -1.74162135, -1.91189307])
L2_2=array([-0.31981155, -0.99372432, -1.36521641, -1.75117917, -2.02957373, -2.26312785])
L2_4=array([-0.10827674, -0.90984774, -2.16823396, -2.64059537, -3.15152472])
L2_8=array([-0.84096622, -0.83988245, -2.12274861, -2.77687445])
L2_16=array([-3.19126309, -3.18896246, -4.24501011])


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
Nop_8=array([  324.,   567.,  1458.,  1539.])
for i in range(3):
    Nop_8[i]=math.log10(Nop_8[i])
Nop_16=array([ 1156.,  2023.,  5202.])
for i in range(3):
    Nop_16[i]=math.log10(Nop_16[i])

########WCT
WCT_1=array([   535.18766904,   2006.53841901,   4416.59984398,   7742.84705591, 11958.09760308,  17201.292696  ])
for i in range(6):
    WCT_1[i]=math.log10(WCT_1[i])
WCT_2=array([  207.96543884,   727.06528783,  1605.92239785,  2765.94084215, 4198.02916002,  6065.1500361 ])
for i in range(6):
    WCT_2[i]=math.log10(WCT_2[i])
WCT_4=array([  142.93469   ,   355.62488008,  1282.89590693,  2125.11188698, 2916.69829583])
for i in range(5):
    WCT_4[i]=math.log10(WCT_4[i])
WCT_8=array([ 189.52523112,  339.52007198,  859.13998985,  871.58323193])
for i in range(3):
    WCT_8[i]=math.log10(WCT_8[i])
WCT_16=array([  600.53741884,   997.25596905,  2481.72711015])
for i in range(2):
    WCT_16[i]=math.log10(WCT_16[i])
print 'dt=1e-3'
import pylab as py

#########PLOTS
L2_1plot=py.plot(10**Nop_1,L2_1,color='r')
L2_2plot=py.plot(10**Nop_2,L2_2,color='b')
L2_4plot=py.plot(10**Nop_4,L2_4,color='g')
L2_8plot=py.plot(10**Nop_8,L2_8,color='k')
'''
L2_1plot=py.plot(Nop_1,L2_1,color='r')
L2_2plot=py.plot(Nop_2,L2_2,color='b')
L2_4plot=py.plot(Nop_4,L2_4,color='g')
L2_8plot=py.plot(Nop_8,L2_8,color='k')'''
#L2_16plot=py.plot(Nop_16,L2_16,color='m')
py.title('Normalized L2 Error')
py.xlabel('Nop')
py.ylabel('log(L2)')
#py.legend(('N=4'),loc=1)
py.legend(('N=1','N=2','N=4','N=8'),loc=1)
py.show()
#L2_8plot=py.plot(Nop_8,L2_8,color='k')
#L2_16plot=py.plot(Nop_16,L2_16,color='m')
py.title('Normalized L2 Error')
WCT_1plot=py.plot(10**WCT_1,L2_1,color='r')
WCT_2plot=py.plot(10**WCT_2,L2_2,color='b')
WCT_4plot=py.plot(10**WCT_4,L2_4,color='g')
WCT_8plot=py.plot(10**WCT_8,L2_8,color='k')
'''
WCT_1plot=py.plot(WCT_1,L2_1,color='r')
WCT_2plot=py.plot(WCT_2,L2_2,color='b')
WCT_4plot=py.plot(WCT_4,L2_4,color='g')
WCT_8plot=py.plot(WCT_8,L2_8,color='k')'''
#WCT_16plot=py.plot(WCT_16,L2_16,color='m')
py.title('Wall Clock Time ')
py.xlabel('WCT')
py.ylabel('log(L2)')
py.legend(('N=1','N=2','N=4','N=8'),loc=1)
py.show()
