####AMR NORMS USING EXACT INTEGRATION
import numpy
from numpy import matrix,array
import math
#AMR ERROR NOMRS AND WCT FOR DT=1E-3
########log( L2_Norma)
L2_1=array([-0.54679319, -0.8580572 , -1.18841452, -1.50305915, -1.72427754, -1.89169007])
L2_2=array([-0.45197327, -0.94598443, -1.42051563, -1.83582831, -2.08435875, -2.29199694])
L2_4=array([-0.44547135, -1.23800278, -2.4222988 , -2.71533895, -3.14830528])
L2_8=array([-0.15441695, -1.12404666, -2.30501108, -3.08854439, -3.71050404, -4.02427739])
L2_16=array([-1.02783314, -3.26073697])
########log( NOP )
Nop_1=array([ 2.42813479,  3.01535976,  3.36473856,  3.61363043,  3.80699351, 3.96510759])
Nop_2=array([ 2.23299611,  2.78031731,  3.12155984,  3.36754227,  3.55954756, 3.71692107])
Nop_4=array([ 2.24303805,  2.67669361,  3.22401481,  3.41077723,  3.56525734])
Nop_8=array([ 2.51054501,  2.75358306,  2.98766626,  3.18723862,  3.35564305, 3.49954963])
Nop_16=array([ 3.06295783,  3.30599588])
########WCT
WCT_1=array([   50.98099995,   189.9734509 ,   424.116786  ,   752.25574708, 1171.34021401,  1697.48880792])
for i in range(6):
    WCT_1[i]=math.log10(WCT_1[i])
WCT_2=array([  20.48453093,   68.33993602,  149.11365485,  261.46964598, 405.33344698,  583.64703989])
for i in range(6):
    WCT_2[i]=math.log10(WCT_2[i])
WCT_4=array([  13.99198198,   35.11728621,  119.4230659 ,  182.61577582, 260.57227707])
for i in range(5):
    WCT_4[i]=math.log10(WCT_4[i])
WCT_8=array([  16.89583707,   31.16567278,   52.05392694,   81.47087502, 119.54263902,  165.46921206])
for i in range(6):
    WCT_8[i]=math.log10(WCT_8[i])
WCT_16=array([ 56.22001195,  98.04714298])
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
