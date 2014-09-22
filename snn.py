from brian import *
from time import time

dt_ = 0.5
simclock = Clock(dt=dt_*ms)
monclock = Clock(dt=dt_* ms)

doPlot = False
#
#Argument structure (w/ indices) passed from Java
#[1, 2, 3] - layer/nNeuron 
#[[[4,5,6,..], [...,..]] ||| [[], []] ]   - 2, 2D array for 2 layer weights
#[nForneuron1, nForneuron2,...] - nSpike times for input layer neurons
#[[neuron1 spike times], [n2 spike times], []] - 2d array for ip layer spike times
#NW parms
# 
idx=1
n = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
maxN = max(n)
idx+=3
#
nConns = (n[0] * n[1])
ipLayerConnWeights = [float(sys.argv[idx+i]) for i in xrange(nConns)]
idx+=nConns
#
nConns = (n[1] * n[2])
hdLayerConnWeights = [float(sys.argv[idx+i]) for i in xrange(nConns)]
idx+=nConns
#
#connProb = [0.5, 0]
#connWeight = [10.0, 100.0]
#
nSpikeTimes = [int(sys.argv[idx+i]) for i in xrange(0, n[0])]
idx+=n[0]
#
spikeTimesIter = [[0 for j in xrange(0, nSpikeTimes[i])] for i in xrange(0, n[0])]
for i in xrange(0, n[0]):
    spikeTimesIter[i] = [float(sys.argv[idx+j]) for j in xrange(0, nSpikeTimes[i])]
    idx+=nSpikeTimes[i]    
spikeTimes = [(i, t*ms) for i in xrange(len(spikeTimesIter)) for t in spikeTimesIter[i]]

#
#Neuron parms
#
k=0.571/ms/mV
a=0.130
b=-2.714
d=111.506
C=81.2
vR=-60.5*mV
vT=-34.8*mV
vPeak=42.4*mV
c=-60*mV

Is=0
dur=40
#Plot&Sim
colors=     [0,0,0]
simDur = dur

model9pEqs= Equations('''
        dV/dt=(k*((V-vR)*(V-vT))-U+I)/(C) : volt
        dU/dt=a*((b*(V-vR)/ms/ms)-(U/ms)) : volt/second                                      
        I : mV/ms                                                                                  
        ''')

#inputLayer = NeuronGroup(n[0], model=modelEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
inputLayer = SpikeGeneratorGroup(n[0], spikeTimes, clock=simclock)
hiddenLayer = NeuronGroup(n[1], model=model9pEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
outputLayer = NeuronGroup(n[2], model=model9pEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)

conn1 = Connection(inputLayer, hiddenLayer, 'V')
conn2 = Connection(hiddenLayer, outputLayer, 'V')

#conn1.connect_full(weight=connWeight[0]*mV)
#conn2.connect_full(weight=connWeight[1]*mV)

for i in xrange(0, n[0]):
    for j in xrange(0, n[1]):
        conn1[i, j] =  ipLayerConnWeights[(i*n[1])+j]*mV
        
for i in xrange(0, n[1]):
    for j in xrange(0, n[2]):
        conn2[i, j] =  hdLayerConnWeights[(i*n[2])+j]*mV        
#
SM = [SpikeMonitor(inputLayer), 
      SpikeMonitor(hiddenLayer), 
      SpikeMonitor(outputLayer)]
VM = [
#StateMonitor(hiddenLayer, 'V', record=True, clock=monclock),
      StateMonitor(hiddenLayer, 'V', record=True, clock=monclock),
      StateMonitor(outputLayer, 'V', record=True, clock=monclock),
      ]

if doPlot:
    ipLayerV = [[vR for i in arange(0,simDur,dt_)] for i in xrange(n[0])]  
    ipLayerT = [i for i in arange(0,simDur,dt_)]  
    for i in xrange(0, len(spikeTimesIter)):
        for j in xrange(0, len(spikeTimesIter[i])):
            ipLayerV[i][int(spikeTimesIter[i][j]/dt_)] = vPeak
        

hiddenLayer.V = vR 
hiddenLayer.U =0
outputLayer.V = vR 
outputLayer.U =0
    
#Start simulation
t1 = time()
run(simDur*ms)
#((timeMax-timeMin)+200 )* msecond)
t2 = time()
print "Simulation time:", t2 - t1, "s"

#Throw output
print "Output Layer Spike times:"
for i in xrange(0, n[len(n)-1]):
    print str(SM[len(n)-1][i])
    
if doPlot:    
    cnt = -maxN
    for i in xrange(0, len(n)):
        cnt+=maxN
        for j in xrange(0, n[i]):
            subplot(len(n),n[i], (n[i]*i)+j+1)
            if i > 0:
                plot(VM[i-1].times / ms, VM[i-1][j] / mV, lw=1.0, color=colors)
            else:
                plot(ipLayerT, ipLayerV[j], lw=1.0, color=colors)

    xlabel('Time (ms)')
    ylabel('V (mV)')
    show()