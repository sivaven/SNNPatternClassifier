from brian import *
simclock = Clock(dt=1*ms)
eqs = '''
dv/dt = ((-60.*mV-v)+(I_synE+I_synI+I_b)/(10.*nS))/(20*ms) : volt
I_synE = 3.*nS*ge*( 0.*mV-v) : amp
I_synI = 30.*nS*gi*(-80.*mV-v) : amp
I_b : amp
dge/dt = -ge/( 5.*ms) : 1
dgi/dt = -gi/(10.*ms) : 1
'''
P = NeuronGroup(1000, eqs, threshold=-50.*mV, refractory=5.*ms, reset=-60.*mV, clock=simclock)
Pe1 = P.subgroup(500)
Pe2 = P.subgroup(500)
Ce = Connection(Pe1, Pe2, 'ge', weight=1., sparseness=1)
eqs_stdp = '''
dpre/dt = -pre/(20.*ms) : 1.0
dpost/dt = -post/(20.*ms) : 1.0
'''
nu = 0.1 # learning rate
alpha = 0.12 # controls the firing rate
stdp = STDP(Ce, eqs=eqs_stdp, pre='pre+= 1.; w+= nu*(post-alpha)',
post='post+= 1.; w+= nu*pre', wmin=0., wmax= 10.)
M1 = SpikeMonitor(Pe1)
M2 = SpikeMonitor(Pe2)
#P.I_b = 200.*pA #set the input current
run(100*ms)

subplot(2,1,1)
raster_plot(M1)
axis([0, 100, 0, 500])
subplot(2,1,2)
raster_plot(M2)
axis([0, 100, 0, 500])
show()