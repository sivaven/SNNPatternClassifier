from brian import *
from time import time
stdp_tau=95.0
conn2_prob=0.9458033
conn2_init_weight=3.0
stdp1_a_step=1.0
dt_=0.1
eta=4.825826
spike_times_iter_ff3d=[[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[18.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[12.0],[10.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[9.0],[15.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[13.0],[9.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[10.0],[13.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[15.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[8.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[13.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[12.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[8.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[14.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[18.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[11.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[15.0],[15.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[9.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[10.0],[13.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[16.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[9.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[14.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[12.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[9.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[12.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[18.0],[13.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[9.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[15.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[9.0],[17.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[8.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[13.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[18.0],[13.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[9.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[18.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[13.0],[13.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[12.0],[10.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[9.0],[15.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[13.0],[9.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[13.0],[13.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[9.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[9.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[15.0],[15.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[18.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[9.0],[15.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[10.0],[13.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[10.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[4000.0],[18.0],[18.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[16.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[8.0],[16.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[15.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[16.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[9.0],[17.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[9.0],[17.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[9.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[16.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[13.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[8.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[8.0],[16.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[11.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[16.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[12.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[18.0],[18.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[12.0],[10.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[11.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]]]
stdp2_a_step=1.0
conn1_prob=0.26869082
sim_dur_ff=50.0
ip_pattern_idx=[0,136,2,138,3,141,143,6,142,7,129,128,9,131,130,11,12,14,17,19,18,20,22,146,29,28,31,35,32,33,38,37,41,46,44,51,55,54,52,58,62,61,68,70,71,64,65,67,77,72,73,75,84,87,83,92,94,89,88,102,103,100,101,96,111,108,104,105,119,118,115,113,126,125,123]
conn1_init_weight=9.0
sim_dur_stdp=1500.0
spike_times_iter_stdp=[[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,858.0,4860.0,4880.0,918.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,1258.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,34.0,4040.0,74.0,94.0,4100.0,136.0,4140.0,177.0,4180.0,217.0,237.0,4240.0,274.0,297.0,4300.0,4320.0,356.0,374.0,398.0,414.0,436.0,457.0,478.0,4480.0,518.0,536.0,4540.0,574.0,594.0,4600.0,636.0,655.0,4660.0,4680.0,715.0,736.0,754.0,4760.0,798.0,814.0,838.0,853.0,874.0,4880.0,913.0,936.0,955.0,976.0,994.0,1016.0,1034.0,5040.0,5060.0,1098.0,1116.0,5120.0,1153.0,1174.0,1198.0,5200.0,1234.0,1253.0,5260.0,1294.0,1314.0,1337.0,1354.0,5360.0,5380.0,1417.0,1434.0,5440.0,1478.0,1496.0],[4000.0,34.0,4040.0,74.0,94.0,4100.0,136.0,4140.0,177.0,4180.0,217.0,237.0,4240.0,274.0,297.0,4300.0,4320.0,356.0,374.0,398.0,414.0,436.0,457.0,478.0,4480.0,518.0,536.0,4540.0,574.0,594.0,4600.0,636.0,655.0,4660.0,4680.0,715.0,736.0,754.0,4760.0,798.0,814.0,838.0,853.0,874.0,4880.0,913.0,936.0,955.0,976.0,994.0,1016.0,1034.0,5040.0,5060.0,1098.0,1116.0,5120.0,1153.0,1174.0,1198.0,5200.0,1234.0,1253.0,5260.0,1294.0,1314.0,1337.0,1354.0,5360.0,5380.0,1417.0,1434.0,5440.0,1478.0,1496.0],[18.0,36.0,57.0,75.0,96.0,113.0,133.0,154.0,173.0,195.0,213.0,233.0,253.0,275.0,293.0,313.0,334.0,353.0,375.0,393.0,415.0,433.0,453.0,473.0,493.0,513.0,533.0,558.0,575.0,595.0,614.0,633.0,654.0,674.0,698.0,714.0,733.0,755.0,775.0,793.0,815.0,833.0,857.0,875.0,894.0,917.0,933.0,954.0,973.0,995.0,1014.0,1035.0,1054.0,1074.0,1093.0,1114.0,1135.0,1157.0,1176.0,1193.0,1215.0,1235.0,1258.0,1275.0,1295.0,1315.0,1333.0,1355.0,1374.0,1393.0,1413.0,1435.0,1456.0,1473.0,1494.0],[13.0,4020.0,53.0,4060.0,4080.0,117.0,4120.0,155.0,178.0,195.0,218.0,238.0,256.0,4260.0,298.0,316.0,335.0,4340.0,4360.0,397.0,4400.0,4420.0,458.0,477.0,497.0,517.0,4520.0,553.0,4560.0,4580.0,615.0,4620.0,4640.0,675.0,693.0,4700.0,4720.0,4740.0,775.0,798.0,4800.0,837.0,4840.0,4860.0,895.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,1056.0,1076.0,1097.0,5100.0,1134.0,5140.0,5160.0,1197.0,1214.0,5220.0,5240.0,1274.0,5280.0,5300.0,1338.0,5340.0,1376.0,1396.0,1418.0,5420.0,1453.0,1478.0,5480.0],[17.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,557.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,697.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,1358.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[16.0,36.0,56.0,76.0,96.0,116.0,135.0,156.0,176.0,196.0,216.0,236.0,256.0,276.0,298.0,316.0,336.0,356.0,375.0,396.0,416.0,436.0,456.0,476.0,496.0,516.0,535.0,557.0,577.0,597.0,616.0,635.0,657.0,676.0,696.0,717.0,735.0,755.0,776.0,796.0,815.0,836.0,856.0,876.0,896.0,916.0,936.0,956.0,977.0,996.0,1018.0,1035.0,1056.0,1076.0,1096.0,1117.0,1136.0,1156.0,1177.0,1197.0,1216.0,1237.0,1256.0,1276.0,1297.0,1317.0,1336.0,1355.0,1376.0,1396.0,1416.0,1437.0,1457.0,1477.0,1498.0],[16.0,36.0,56.0,76.0,96.0,116.0,135.0,156.0,176.0,196.0,216.0,236.0,256.0,276.0,298.0,316.0,336.0,356.0,375.0,396.0,416.0,436.0,456.0,476.0,496.0,516.0,535.0,557.0,577.0,597.0,616.0,635.0,657.0,676.0,696.0,717.0,735.0,755.0,776.0,796.0,815.0,836.0,856.0,876.0,896.0,916.0,936.0,956.0,977.0,996.0,1018.0,1035.0,1056.0,1076.0,1096.0,1117.0,1136.0,1156.0,1177.0,1197.0,1216.0,1237.0,1256.0,1276.0,1297.0,1317.0,1336.0,1355.0,1376.0,1396.0,1416.0,1437.0,1457.0,1477.0,1498.0],[17.0,37.0,57.0,76.0,97.0,116.0,138.0,157.0,178.0,197.0,217.0,237.0,257.0,277.0,295.0,317.0,336.0,358.0,378.0,398.0,417.0,437.0,457.0,477.0,497.0,517.0,538.0,556.0,576.0,596.0,616.0,638.0,656.0,677.0,697.0,716.0,738.0,758.0,777.0,797.0,818.0,837.0,857.0,877.0,897.0,916.0,937.0,957.0,976.0,996.0,1016.0,1038.0,1057.0,1076.0,1097.0,1116.0,1137.0,1156.0,1176.0,1196.0,1216.0,1236.0,1257.0,1276.0,1296.0,1316.0,1337.0,1358.0,1377.0,1397.0,1417.0,1436.0,1456.0,1476.0,1496.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,918.0,4920.0,4940.0,978.0,4980.0,1018.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,1238.0,1257.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,30.0,4040.0,70.0,92.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,270.0,291.0,4300.0,4320.0,4340.0,4360.0,4380.0,412.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,572.0,592.0,4600.0,4620.0,651.0,4660.0,4680.0,711.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,850.0,871.0,4880.0,909.0,4920.0,4940.0,969.0,993.0,1009.0,5020.0,5040.0,5060.0,5080.0,1111.0,5120.0,1150.0,1175.0,5180.0,5200.0,1229.0,1248.0,5260.0,1291.0,1310.0,5320.0,5340.0,5360.0,5380.0,5400.0,1431.0,5440.0,5460.0,1493.0],[4000.0,30.0,4040.0,70.0,92.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,270.0,291.0,4300.0,4320.0,4340.0,4360.0,4380.0,412.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,572.0,592.0,4600.0,4620.0,651.0,4660.0,4680.0,711.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,850.0,871.0,4880.0,909.0,4920.0,4940.0,969.0,993.0,1009.0,5020.0,5040.0,5060.0,5080.0,1111.0,5120.0,1150.0,1175.0,5180.0,5200.0,1229.0,1248.0,5260.0,1291.0,1310.0,5320.0,5340.0,5360.0,5380.0,5400.0,1431.0,5440.0,5460.0,1493.0],[4000.0,32.0,4040.0,72.0,90.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,272.0,291.0,4300.0,4320.0,4340.0,378.0,4380.0,410.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,570.0,590.0,4600.0,4620.0,651.0,4660.0,4680.0,711.0,4720.0,4740.0,4760.0,4780.0,816.0,4820.0,852.0,871.0,4880.0,913.0,4920.0,4940.0,973.0,989.0,1013.0,1038.0,5040.0,5060.0,5080.0,1111.0,5120.0,1152.0,1168.0,5180.0,5200.0,1233.0,1255.0,5260.0,1291.0,1312.0,5320.0,5340.0,5360.0,5380.0,5400.0,1431.0,5440.0,5460.0,1489.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,136.0,4140.0,171.0,4180.0,217.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,358.0,369.0,4380.0,4400.0,4420.0,457.0,4460.0,4480.0,518.0,534.0,4540.0,4560.0,4580.0,4600.0,635.0,4640.0,4660.0,4680.0,4700.0,733.0,4740.0,4760.0,4780.0,808.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,955.0,4960.0,998.0,5000.0,1029.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,1177.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,1335.0,1351.0,5360.0,1398.0,5400.0,5420.0,5440.0,5460.0,1498.0],[4000.0,4020.0,4040.0,4060.0,4080.0,113.0,128.0,153.0,172.0,4180.0,209.0,236.0,4240.0,4260.0,4280.0,4300.0,4320.0,350.0,374.0,4380.0,4400.0,431.0,448.0,473.0,496.0,509.0,529.0,4540.0,4560.0,4580.0,4600.0,629.0,4640.0,4660.0,4680.0,4700.0,730.0,751.0,774.0,791.0,816.0,832.0,4840.0,4860.0,897.0,4900.0,935.0,949.0,4960.0,4980.0,5000.0,1034.0,1057.0,1076.0,1095.0,5100.0,1138.0,5140.0,5160.0,1198.0,1213.0,5220.0,5240.0,5260.0,5280.0,5300.0,1329.0,1352.0,5360.0,1389.0,1416.0,5420.0,5440.0,1471.0,5480.0],[16.0,4020.0,58.0,4060.0,4080.0,110.0,137.0,150.0,4160.0,190.0,215.0,228.0,250.0,4260.0,4280.0,311.0,332.0,353.0,4360.0,391.0,4400.0,432.0,456.0,470.0,488.0,514.0,538.0,4540.0,4560.0,4580.0,612.0,637.0,4640.0,671.0,4680.0,4700.0,738.0,752.0,769.0,792.0,4800.0,831.0,4840.0,4860.0,888.0,4900.0,929.0,957.0,4960.0,4980.0,5000.0,5020.0,1048.0,1068.0,1089.0,5100.0,1130.0,5140.0,5160.0,1190.0,1210.0,5220.0,5240.0,1272.0,5280.0,5300.0,1337.0,5340.0,1370.0,1394.0,1408.0,5420.0,1456.0,1472.0,5480.0],[8.0,4020.0,49.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,192.0,4200.0,236.0,252.0,4260.0,4280.0,311.0,330.0,4340.0,4360.0,391.0,4400.0,4420.0,4440.0,4460.0,496.0,4500.0,4520.0,552.0,4560.0,4580.0,610.0,4620.0,4640.0,671.0,692.0,4700.0,4720.0,4740.0,778.0,4780.0,4800.0,4820.0,4840.0,4860.0,895.0,4900.0,937.0,4940.0,4960.0,4980.0,5000.0,5020.0,1055.0,1076.0,1097.0,5100.0,1133.0,5140.0,5160.0,1193.0,5200.0,5220.0,5240.0,1270.0,5280.0,5300.0,5320.0,5340.0,1372.0,5380.0,1416.0,5420.0,1448.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,878.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,1258.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[18.0,35.0,57.0,75.0,95.0,117.0,136.0,157.0,176.0,198.0,216.0,237.0,257.0,275.0,295.0,318.0,338.0,356.0,376.0,396.0,415.0,437.0,456.0,476.0,497.0,516.0,536.0,558.0,575.0,595.0,618.0,636.0,655.0,678.0,698.0,715.0,736.0,757.0,776.0,797.0,816.0,836.0,855.0,875.0,898.0,915.0,938.0,956.0,975.0,995.0,1015.0,1036.0,1058.0,1078.0,1097.0,1115.0,1138.0,1155.0,1175.0,1198.0,1216.0,1235.0,1255.0,1278.0,1295.0,1315.0,1336.0,1356.0,1377.0,1396.0,1418.0,1435.0,1458.0,1477.0,1495.0],[18.0,35.0,57.0,75.0,95.0,117.0,136.0,157.0,176.0,198.0,216.0,237.0,257.0,275.0,295.0,318.0,338.0,356.0,376.0,396.0,415.0,437.0,456.0,476.0,497.0,516.0,536.0,558.0,575.0,595.0,618.0,636.0,655.0,678.0,698.0,715.0,736.0,757.0,776.0,797.0,816.0,836.0,855.0,875.0,898.0,915.0,938.0,956.0,975.0,995.0,1015.0,1036.0,1058.0,1078.0,1097.0,1115.0,1138.0,1155.0,1175.0,1198.0,1216.0,1235.0,1255.0,1278.0,1295.0,1315.0,1336.0,1356.0,1377.0,1396.0,1418.0,1435.0,1458.0,1477.0,1495.0],[15.0,38.0,56.0,78.0,98.0,116.0,136.0,156.0,177.0,195.0,217.0,236.0,256.0,278.0,298.0,315.0,335.0,357.0,377.0,396.0,418.0,436.0,456.0,476.0,496.0,516.0,537.0,555.0,578.0,598.0,615.0,637.0,658.0,675.0,696.0,718.0,737.0,756.0,776.0,796.0,817.0,836.0,858.0,878.0,895.0,918.0,936.0,956.0,978.0,998.0,1018.0,1037.0,1056.0,1076.0,1096.0,1118.0,1135.0,1158.0,1178.0,1195.0,1216.0,1238.0,1258.0,1275.0,1298.0,1318.0,1337.0,1357.0,1376.0,1396.0,1415.0,1438.0,1455.0,1476.0,1498.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0]]
nw_arch=[32,75,69]
stdp_gmax=18.0
#
#

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

model9pEqs= Equations('''
		dV/dt=(k*((V-vR)*(V-vT))-U+I)/(C) : volt
		dU/dt=a*((b*(V-vR)/ms/ms)-(U/ms)) : volt/second
		I : mV/ms
		''')

eqs_stdp='''
dA_pre/dt=-A_pre/tau : 1
dA_post/dt=-A_post/tau : 1
'''

simclock = Clock(dt=dt_*ms)
spikeTimes = [(i, t*ms) for i in xrange(len(spike_times_iter_stdp)) for t in spike_times_iter_stdp[i]]

inputLayer = SpikeGeneratorGroup(nw_arch[0], spikeTimes, clock=simclock)
hiddenLayer = NeuronGroup(nw_arch[1], model=model9pEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
outputLayer = NeuronGroup(nw_arch[2], model=model9pEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
hiddenLayer.V = vR 
hiddenLayer.U =0
outputLayer.V = vR 
outputLayer.U =0

conn1 = Connection(inputLayer, hiddenLayer, 'V', weight=conn1_init_weight*mV, sparseness=conn1_prob)
conn2 = Connection(hiddenLayer, outputLayer, 'V', weight=conn2_init_weight*mV, sparseness=conn2_prob)
tau = stdp_tau*ms
stdp1=STDP(conn1,eqs=eqs_stdp,pre='A_pre+=stdp1_a_step*mV;w+=A_post*eta',post='A_post+=stdp1_a_step*mV;w+=A_pre*eta',wmax=stdp_gmax*mV, clock=simclock)
stdp2=STDP(conn2,eqs=eqs_stdp,pre='A_pre+=stdp2_a_step*mV;w+=A_post*eta',post='A_post+=stdp2_a_step*mV;w+=A_pre*eta',wmax=stdp_gmax*mV, clock=simclock)
Mpr = PopulationRateMonitor(outputLayer, bin=dt_*ms)

run(sim_dur_stdp*ms)

#
#
def feed_forward(spikeTimesIterList, ipPatternIdx):
	reinit(states=False)
	spikeTimes = [(i, t*ms) for i in xrange(len(spikeTimesIterList)) for t in spikeTimesIterList[i]]
	inputLayer.spiketimes=spikeTimes
	t1 = time()
	run(sim_dur_ff*ms)
	t2 = time()
	print "#$ip_pattern_idx:", ipPatternIdx
	print "$sim_time:", t2 - t1, "s"
	print "$op_layer_pop_rates:"," ".join(str(p) for p in Mpr.rate)


stdp1 = None
stdp2=None
hiddenLayer.V = vR 
hiddenLayer.U =0
outputLayer.V = vR 
outputLayer.U =0
for i in xrange(0, len(spike_times_iter_ff3d)):
	feed_forward(spikeTimesIterList = spike_times_iter_ff3d[i], ipPatternIdx = ip_pattern_idx[i])