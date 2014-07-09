####AMR NORMS USING INEXACT INTEGRATION
import numpy
from numpy import matrix,array
import math
#AMR ERROR NOMRS AND WCT FOR DT=1E-3
########log( L2_Norma)
L2_1=array([-0.23063703, -0.48451075, -0.66173529, -0.83217076, -0.96684679, -1.09024427])
L2_2=array([-0.32904641, -0.83674479, -1.15116915, -1.4242082 , -1.65037226, -1.82822562])
L2_4=array([-0.34148476, -1.01412413, -2.01121519, -2.49295869, -2.64873158])
L2_8=array([-0.15597721, -1.08847032, -2.09327491, -2.78970493, -3.50324317, -3.82918702])
L2_16=array([-1.03212122, -3.3210925 ])

#######Nop
Nop_1=array([ 2.42813479,  3.01535976,  3.36473856,  3.61363043,  3.80699351, 3.96510759])
Nop_2=array([ 2.23299611,  2.78031731,  3.12155984,  3.36754227,  3.55954756, 3.71692107])
Nop_4=array([ 2.24303805,  2.67669361,  3.22401481,  3.41077723,  3.56525734])
Nop_8=array([ 2.51054501,  2.75358306,  2.98766626,  3.18723862,  3.35564305, 3.49954963])
Nop_16=array([ 3.06295783,  3.30599588])

#####WCT
WCT_1=array([   53.68983698,   195.53828287,   429.42695093,   761.22626901, 1189.91134   ,  1714.66943812])
for i in range(6):
    WCT_1[i]=math.log10(WCT_1[i])
WCT_2=array([  20.89557695,   69.70300817,  151.47372603,  267.20976686, 412.11786795,  597.35743904])
for i in range(6):
    WCT_2[i]=math.log10(WCT_2[i])
WCT_4=array([  14.42751718,   36.18101406,  123.43810105,  189.102844  , 272.63265204])
for i in range(5):
    WCT_4[i]=math.log10(WCT_4[i])
WCT_8=array([  17.96821594,   32.91668892,   55.06757808,   85.98865199, 124.35620618,  173.42373896])
for i in range(6):
    WCT_8[i]=math.log10(WCT_8[i])
WCT_16=array([  59.09440804,  103.10671687])
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
