#### DYNAMIC PEAK REFINEMENT NORMS USING EXACT INTEGRATION
import numpy
from numpy import matrix,array
import math
########log( L2_Norma)
L2_1=array([-0.19488134, -0.49565845, -0.69097185, -0.85803807, -0.98188392, -1.12838205])
L2_2=array([-0.32904642, -0.83879389, -1.19705593, -1.49123695, -1.52998575,-1.80111696])
L2_4=array([-0.34148472, -1.01412412, -2.04520492, -2.4106789 , -2.81962691])
L2_8=array([-0.15597721, -1.0884699 , -2.03668025, -2.78970453])
L2_16=array([-1.03212122, -3.32109239])

#########Nop
Nop_1=array([ 2.44715803,  3.03502928,  3.38021124,  3.6249006 ,  3.81504618,3.97349731])
Nop_2=array([ 2.23299611,  2.79934055,  3.14736711,  3.3872118 ,  3.57229061,3.73239376])
Nop_4=array([ 2.24303805,  2.67669361,  3.24303805,  3.44715803,  3.59106461])
Nop_8=array([ 2.51054501,  2.75358306,  3.16375752,  3.18723862])
Nop_16=array([ 3.06295783,  3.30599588])

#########WCT
WCT_1=array([   52.29624891,   191.43673396,   424.69887185,   751.82713795, 1171.80021286,  1678.29351211])
for i in range(6):
    WCT_1[i]=math.log10(WCT_1[i])
WCT_2=array([  20.42459512,   69.42911792,  150.17372584,  263.29202819, 405.95660806,  584.45570493])
for i in range(6):
    WCT_2[i]=math.log10(WCT_2[i])
WCT_4=array([  14.01219702,   34.88989282,  121.35648203,  186.42282605, 263.29734993])
for i in range(5):
    WCT_4[i]=math.log10(WCT_4[i])
WCT_8=array([ 17.29658699,  31.41921902,  57.99922299,  80.59253502])
for i in range(4):
    WCT_8[i]=math.log10(WCT_8[i])
WCT_16=array([ 56.90339303,  97.18765402])
for i in range(2):
    WCT_16[i]=math.log10(WCT_16[i])
print 'dt=1e-3'
import pylab as py

#########PLOTS
L2_1plot=py.plot(10**Nop_1,L2_1,'rD-')
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
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=3)'''
py.title('Inexact Integration')
py.xlabel('Nop')
py.ylabel('log(L2)')

py.show()
#L2_8plot=py.plot(Nop_8,L2_8,color='k')
#L2_16plot=py.plot(Nop_16,L2_16,color='m')
'''
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
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=1)
py.title('Inexact Integration')
py.xlabel('WCT')
py.ylabel('log(L2)')
py.show()
