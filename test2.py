from brian import *
from time import time
dt_ =1.0
simclock = Clock(dt=dt_*ms)
monclock = Clock(dt=dt_* ms)
n=[32,800,200,3]
connProb=[0.45870978,0.37947842,0.50685066,0.81756854,0.912884,0.6225655,0.87712395]
connWeight=[4.325525,4.1846164,1.9306312,1.0532838,2.7184972,2.5971072,0.7932462]
spikeTimesIter = [[100.0],[7.0],[7.0],[8.0],[100.0],[100.0],[100.0],[100.0],[100.0],[8.0],[8.0],[8.0],[100.0],[100.0],[100.0],[100.0],[9.0],[4.0],[4.0],[7.0],[100.0],[100.0],[100.0],[100.0],[9.0],[8.0],[8.0],[9.0],[100.0],[100.0],[100.0],[100.0]]
spikeTimes = [(i, t*ms) for i in xrange(len(spikeTimesIter)) for t in spikeTimesIter[i]]

k=0.571/ms/mV
a=0.13
b=-2.714
d=111.506
C=81.2
vR=-60.5*mV
vT=-34.8*mV
vPeak=42.4*mV
c=-60.0*mV
Is=0
dur=99
simDur=99

model9pEqs= Equations('''
        dV/dt=(k*((V-vR)*(V-vT))-U+I)/(C) : volt
        dU/dt=a*((b*(V-vR)/ms/ms)-(U/ms)) : volt/second
        I : mV/ms
        ''')

inputLayer = SpikeGeneratorGroup(n[0], spikeTimes, clock=simclock)
hiddenLayer = NeuronGroup(n[1]+n[2], model=model9pEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
hiddenExc = hiddenLayer.subgroup(n[1])
hiddenInh = hiddenLayer.subgroup(n[2])
outputLayer = NeuronGroup(n[3], model=model9pEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
output1 = outputLayer.subgroup(1)
output2 = outputLayer.subgroup(1)
output3 = outputLayer.subgroup(1)

conn0 = Connection(inputLayer, hiddenExc, 'V', sparseness=connProb[0], weight=connWeight[0]*mV)
conn1 = Connection(hiddenExc, hiddenExc, 'V', sparseness=connProb[1], weight=connWeight[1]*mV)
conn2 = Connection(hiddenExc, hiddenInh, 'V', sparseness=connProb[2], weight=connWeight[2]*mV)
conn3 = Connection(hiddenInh, hiddenExc, 'V', sparseness=connProb[3], weight=-connWeight[3]*mV)
conn4 = Connection(hiddenExc, output1, 'V', sparseness=connProb[4], weight=connWeight[4]*mV)
conn5 = Connection(hiddenExc, output2, 'V', sparseness=connProb[5], weight=connWeight[5]*mV)
conn6 = Connection(hiddenExc, output3, 'V', sparseness=connProb[6], weight=connWeight[6]*mV)
SMO = SpikeMonitor(outputLayer)

SM = SpikeMonitor(hiddenLayer)
VM = StateMonitor(outputLayer, 'V', record=True, clock=monclock)      

hiddenLayer.V = vR 
hiddenLayer.U =0
outputLayer.V = vR 
outputLayer.U =0

t1 = time()
run(simDur*ms)
t2 = time()
print "Simulation time:", t2 - t1, "s"
print "Output Layer Spike times:"
for i in xrange(0, n[len(n)-1]):
    print str(SMO[i])
 
colors=     [0,0,0]   
if True:
    subplot(211)
    raster_plot(SM, title='Network Activity')
    subplot(234)
    plot(VM.times / ms, VM[0] / mV, lw=1.0, color=colors)
    subplot(235)
    plot(VM.times / ms, VM[1] / mV, lw=1.0, color=colors)
    subplot(236)
    plot(VM.times / ms, VM[2] / mV, lw=1.0, color=colors)
xlabel('Time (ms)')
ylabel('V (mV)')
    
show()
