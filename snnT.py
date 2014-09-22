#import brian_no_units
from brian import *
#from clock import defaultclock
from time import time

simclock = Clock(dt=1.0 * ms)
monclock = Clock(dt=1.0 * ms)
inputclock = Clock(dt=1.0 * ms)

doPlot = False                      
#
#NW parms
# 
n = [10, 5, 3]
#connProb = [0.5, 0]
connWeight = [1.0, 1.0]
maxN = max(n)

spikeTimesIter = [[1, 100, 500, 550] for i in range(0, n[0])]
spikeTimes = [(i, t*ms) for i in xrange(len(spikeTimesIter)) for t in spikeTimesIter[i]]
#
#Neuron parms
#
a=0.02
b=0.2
c=-65*mV
d=8
vPeak=30*mV
vR = -70*mV
Is=0
dur=1000

#Plot&Sim
colors=     [0,0,0]
timeMin=100.0
timeMax=timeMin+dur
simDur = dur

modelEqs = Equations('''
        dV/dt=(0.04/ms/mV)*(V*V)+(5/ms)*V+(140*mV/ms)-U+(I) : volt
        dU/dt=a*((b*V/ms/ms)-U/ms) : volt/second    
        I : mV/ms    
        ''')

#inputLayer = NeuronGroup(n[0], model=modelEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
inputLayer = SpikeGeneratorGroup(n[0], spikeTimes, clock=simclock)
hiddenLayer = NeuronGroup(n[1], model=modelEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
outputLayer = NeuronGroup(n[2], model=modelEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)

conn1 = Connection(inputLayer, hiddenLayer, 'V')
conn2 = Connection(hiddenLayer, outputLayer, 'V')

conn1.connect_full(weight=connWeight[0]*mV)
conn2.connect_full(weight=connWeight[1]*mV)
#probabilistic connection
#conn1.connect_random(sparseness=connProb[0], weight=connWeight[0]*mV)
#conn2.connect_random(sparseness=connProb[1], weight=connWeight[1]*mV)
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
    ipLayerV = [[vR for i in range(simDur)] for i in range(n[0])]    
    for i in range(0, len(spikeTimesIter)):
        for j in range(0, len(spikeTimesIter[i])):
            ipLayerV[i][spikeTimesIter[i][j]] = vPeak
        
#inputLayer.V = vR 
#inputLayer.U =0
hiddenLayer.V = vR 
hiddenLayer.U =0
outputLayer.V = vR 
outputLayer.U =0

#@network_operation(inputclock)
#def stimulate():
#    if inputclock.t < timeMax*ms:
#        if inputclock.t > timeMin*ms: 
#            for i in range(0, n[0]):
#                inputLayer.I[i] = Is*mV/ms                
#        else: inputLayer.I = 0
#    else: inputLayer.I = 0
    
#Start simulation
t1 = time()
run(simDur*ms)
#((timeMax-timeMin)+200 )* msecond)
t2 = time()
print "Simulation time:", t2 - t1, "s"

#Throw output
for i in range(0, len(n)):
    print "layer "+str(i)+" spikes: "+str(SM[i].nspikes)

if doPlot:    
    cnt = -maxN
    for i in range(0, len(n)):
        cnt+=maxN
        for j in range(0, n[i]):
            subplot(len(n),n[i], (n[i]*i)+j+1)
            if i > 0:
                plot(VM[i-1].times / ms, VM[i-1][j] / mV, lw=1.0, color=colors)
            else:
                plot(VM[i].times / ms, ipLayerV[j], lw=1.0, color=colors)

    xlabel('Time (ms)')
    ylabel('V (mV)')
    show()