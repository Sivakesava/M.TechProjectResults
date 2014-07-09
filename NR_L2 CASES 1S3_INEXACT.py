#dt=1e-3,NORMAL REFINEMENT NORMS WITH INEXACT INTEGRATION
import numpy
from numpy import matrix,array
import math
########log( L2_Norma)
L2_1=array([-0.11252299, -0.40972025, -0.6133166 , -0.78528126, -0.9334686 , -1.06314386])
L2_2=array([-0.15505087, -0.72948977, -1.05127013, -1.40996824, -1.68134193, -1.90673596])
L2_4=array([-0.0415694 , -0.72098532, -1.89377704, -2.32563467, -2.7625019 ])
L2_8=array([-0.13106951, -0.77754917, -2.00522236, -2.4478199 , -3.35494819, -3.83432342])
L2_16=array([-0.84467527, -3.07997309, -4.30750168])

########log( NOP )
Nop_1=array([ 2.40823997,  3.01029996,  3.36248247,  3.61235995,  3.80617997, 3.96454247])
Nop_2=array([ 2.15836249,  2.76042248,  3.112605  ,  3.36248247,  3.5563025 , 3.71466499])
Nop_4=array([ 2.        ,  2.60205999,  3.20411998,  3.39794001,  3.5563025 ])
Nop_8=array([ 1.90848502,  2.51054501,  2.86272753,  3.112605  ,  3.30642503,3.46478752])
Nop_16=array([ 2.46089784,  3.06295783,  3.41514035])

######WCT
WCT_1=array([  22.9302001 ,   87.78433704,  199.36750507,  354.74526095, 553.9921    ,  799.02598715])
for i in range(6):
    WCT_1[i]=math.log10(WCT_1[i])
WCT_2=array([   7.57329297,   28.47949815,   63.41481304,  111.52294683, 176.49934292,  251.93656898])
for i in range(6):
    WCT_2[i]=math.log10(WCT_2[i])
WCT_4=array([  3.83424497,  11.66106701,  43.06940198,  66.81088495,  94.57506323])
for i in range(5):
   WCT_4[i]=math.log10(WCT_4[i])
WCT_8=array([  4.69503403,   8.34787393,  14.35065699,  22.82677889, 33.5558331 ,  46.65770411])
for i in range(6):
    WCT_8[i]=math.log10(WCT_8[i])
WCT_16=array([ 17.03612804,  26.60572195,  42.6389401 ])
for i in range(3):
   WCT_16[i]=math.log10(WCT_16[i])

print 'dt=1e-3'
import pylab as py

#########PLOTS
L2_1plot=py.plot(10**Nop_1,L2_1,'rD-')
L2_2plot=py.plot(10**Nop_2,L2_2,'b*-')
L2_4plot=py.plot(10**Nop_4,L2_4,'go-')
L2_8plot=py.plot(10**Nop_8,L2_8,'k>-')
L2_16plot=py.plot(10**Nop_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=4)
'''
L2_1plot=py.plot(Nop_1,L2_1,'rD-')
L2_2plot=py.plot(Nop_2,L2_2,'b*-')
L2_4plot=py.plot(Nop_4,L2_4,'go-')
L2_8plot=py.plot(Nop_8,L2_8,'k>-')
L2_16plot=py.plot(Nop_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=3)'''
py.title('Inxact Integration')
py.xlabel('Nop')
py.ylabel('log(L2)')

py.show()
#L2_8plot=py.plot(Nop_8,L2_8,color='k')
#L2_16plot=py.plot(Nop_16,L2_16,color='m')
'''WCT_1plot=py.plot(WCT_1,L2_1,'rD-')
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
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=4)
py.title('Inxact Integration')
py.xlabel('WCT')
py.ylabel('log(L2)')
py.show()
