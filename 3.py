from brian import *
from time import time
stdp_tau=500.0
ip_pattern_idx=[137,0,136,1,138,3,141,4,140,143,7,129,128,10,13,135,14,19,18,20,22,145,24,146,26,31,30,34,35,32,36,41,46,47,44,50,49,53,52,56,63,62,61,68,69,70,65,76,77,78,74,75,85,84,81,95,89,91,102,100,101,98,99,97,108,106,107,104,118,113,112,125,124,122,121]
stdp_gmax=10.0
nw_arch=[32,61,99]
stdp2_a_step=1.0
conn1_init_weight=9.0
conn1_prob=0.5762958
eta=2.076338
stdp1_a_step=1.0
spike_times_iter_ff3d=[[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[8.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[13.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[9.0],[15.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[14.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[12.0],[10.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[9.0],[17.0],[4000.0],[18.0],[18.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[10.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[18.0],[18.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[18.0],[13.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[9.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[13.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[18.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[15.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[12.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[15.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[9.0],[17.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[8.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[13.0],[9.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[15.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[15.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[16.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[10.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[14.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[16.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[9.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[16.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[13.0],[9.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[12.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[8.0],[15.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[9.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[12.0],[10.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[8.0],[16.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[10.0],[13.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[9.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[15.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[18.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[12.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[9.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[10.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[17.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[15.0],[15.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[10.0],[18.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[13.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[8.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[12.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[12.0],[10.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[8.0],[16.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[12.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[9.0],[17.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[10.0],[10.0],[12.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[11.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[16.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[9.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[9.0],[15.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[14.0],[9.0],[18.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[8.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[12.0],[4000.0],[18.0],[18.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[10.0],[13.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[12.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[18.0],[13.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[8.0],[8.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[17.0],[13.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[16.0],[16.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[13.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[8.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[17.0],[17.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[18.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[9.0],[9.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[18.0],[18.0],[13.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[12.0],[4000.0],[4000.0],[17.0],[17.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[14.0],[14.0],[15.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[17.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[11.0],[11.0],[11.0],[4000.0],[4000.0],[4000.0],[4000.0],[18.0],[15.0],[15.0],[18.0],[4000.0],[4000.0],[4000.0],[4000.0]],[[4000.0],[4000.0],[4000.0],[15.0],[14.0],[4000.0],[4000.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[4000.0],[13.0],[10.0],[4000.0],[4000.0],[16.0],[16.0],[16.0],[4000.0],[4000.0],[4000.0],[4000.0]]]
sim_dur_stdp=1500.0
conn2_init_weight=8.0
dt_=0.1
spike_times_iter_stdp=[[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,158.0,4160.0,4180.0,4200.0,4220.0,4240.0,278.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,1158.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,34.0,4040.0,74.0,97.0,118.0,134.0,153.0,178.0,4180.0,214.0,235.0,254.0,273.0,4280.0,4300.0,337.0,356.0,4360.0,4380.0,4400.0,434.0,456.0,477.0,4480.0,517.0,4520.0,556.0,574.0,598.0,615.0,635.0,656.0,677.0,693.0,717.0,4720.0,4740.0,778.0,4780.0,814.0,838.0,855.0,874.0,896.0,914.0,4920.0,956.0,974.0,996.0,1014.0,5020.0,1057.0,1076.0,1097.0,1114.0,1134.0,1153.0,1177.0,5180.0,5200.0,5220.0,1258.0,5260.0,1294.0,1317.0,5320.0,1358.0,1373.0,5380.0,5400.0,5420.0,1456.0,1473.0,1498.0],[4000.0,34.0,4040.0,74.0,97.0,118.0,134.0,153.0,178.0,4180.0,214.0,235.0,254.0,273.0,4280.0,4300.0,337.0,356.0,4360.0,4380.0,4400.0,434.0,456.0,477.0,4480.0,517.0,4520.0,556.0,574.0,598.0,615.0,635.0,656.0,677.0,693.0,717.0,4720.0,4740.0,778.0,4780.0,814.0,838.0,855.0,874.0,896.0,914.0,4920.0,956.0,974.0,996.0,1014.0,5020.0,1057.0,1076.0,1097.0,1114.0,1134.0,1153.0,1177.0,5180.0,5200.0,5220.0,1258.0,5260.0,1294.0,1317.0,5320.0,1358.0,1373.0,5380.0,5400.0,5420.0,1456.0,1473.0,1498.0],[13.0,36.0,58.0,75.0,93.0,113.0,135.0,157.0,173.0,193.0,216.0,234.0,255.0,277.0,298.0,314.0,333.0,353.0,373.0,395.0,415.0,435.0,453.0,473.0,494.0,513.0,533.0,554.0,575.0,593.0,614.0,634.0,653.0,673.0,697.0,713.0,733.0,753.0,773.0,794.0,815.0,833.0,854.0,875.0,893.0,915.0,933.0,954.0,975.0,993.0,1015.0,1034.0,1053.0,1073.0,1093.0,1116.0,1135.0,1157.0,1173.0,1194.0,1216.0,1234.0,1253.0,1278.0,1295.0,1313.0,1334.0,1353.0,1376.0,1397.0,1413.0,1433.0,1453.0,1476.0,1493.0],[17.0,4020.0,53.0,4060.0,98.0,117.0,4120.0,4140.0,177.0,197.0,4200.0,4220.0,4240.0,4260.0,293.0,316.0,338.0,4340.0,376.0,394.0,414.0,4420.0,4440.0,478.0,495.0,518.0,537.0,4540.0,4560.0,597.0,4600.0,4620.0,4640.0,678.0,4680.0,718.0,737.0,756.0,777.0,795.0,4800.0,838.0,4840.0,4860.0,4880.0,4900.0,937.0,4940.0,4960.0,4980.0,5000.0,1035.0,1058.0,5060.0,1098.0,5100.0,5120.0,5140.0,1178.0,1196.0,1213.0,1236.0,1257.0,1273.0,5280.0,1318.0,1336.0,1358.0,5360.0,1393.0,1416.0,1436.0,5440.0,5460.0,1497.0],[4000.0,4020.0,57.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,298.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,1277.0,5280.0,5300.0,5320.0,5340.0,5360.0,1398.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,1138.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[16.0,36.0,57.0,77.0,96.0,116.0,136.0,156.0,176.0,195.0,216.0,236.0,257.0,276.0,296.0,316.0,336.0,356.0,376.0,396.0,416.0,437.0,456.0,478.0,496.0,516.0,536.0,558.0,575.0,596.0,617.0,637.0,658.0,676.0,697.0,716.0,736.0,756.0,776.0,796.0,816.0,836.0,857.0,877.0,896.0,915.0,935.0,958.0,976.0,996.0,1016.0,1036.0,1056.0,1076.0,1096.0,1117.0,1135.0,1156.0,1176.0,1196.0,1217.0,1236.0,1257.0,1277.0,1297.0,1316.0,1336.0,1355.0,1376.0,1396.0,1416.0,1436.0,1455.0,1476.0,1496.0],[16.0,36.0,57.0,77.0,96.0,116.0,136.0,156.0,176.0,195.0,216.0,236.0,257.0,276.0,296.0,316.0,336.0,356.0,376.0,396.0,416.0,437.0,456.0,478.0,496.0,516.0,536.0,558.0,575.0,596.0,617.0,637.0,658.0,676.0,697.0,716.0,736.0,756.0,776.0,796.0,816.0,836.0,857.0,877.0,896.0,915.0,935.0,958.0,976.0,996.0,1016.0,1036.0,1056.0,1076.0,1096.0,1117.0,1135.0,1156.0,1176.0,1196.0,1217.0,1236.0,1257.0,1277.0,1297.0,1316.0,1336.0,1355.0,1376.0,1396.0,1416.0,1436.0,1455.0,1476.0,1496.0],[17.0,37.0,56.0,76.0,97.0,118.0,137.0,156.0,177.0,198.0,217.0,237.0,256.0,277.0,297.0,317.0,337.0,357.0,376.0,396.0,417.0,436.0,457.0,475.0,497.0,517.0,537.0,556.0,578.0,597.0,616.0,636.0,655.0,678.0,696.0,718.0,737.0,756.0,777.0,796.0,816.0,837.0,856.0,876.0,897.0,918.0,938.0,956.0,977.0,998.0,1017.0,1037.0,1057.0,1077.0,1097.0,1116.0,1138.0,1157.0,1177.0,1197.0,1216.0,1237.0,1256.0,1276.0,1296.0,1317.0,1336.0,1358.0,1376.0,1397.0,1417.0,1437.0,1458.0,1476.0,1497.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,158.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,558.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,1158.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,1298.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,1478.0,5480.0],[4000.0,30.0,4040.0,70.0,4080.0,4100.0,131.0,149.0,4160.0,4180.0,210.0,4220.0,251.0,270.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,432.0,4440.0,471.0,4480.0,4500.0,4520.0,549.0,4560.0,4580.0,611.0,630.0,650.0,4660.0,690.0,4700.0,4720.0,4740.0,4760.0,4780.0,813.0,4820.0,851.0,871.0,4880.0,4900.0,4920.0,953.0,972.0,4980.0,1011.0,5020.0,5040.0,5060.0,5080.0,1112.0,5120.0,1149.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,1289.0,5300.0,5320.0,5340.0,1372.0,5380.0,5400.0,5420.0,5440.0,1469.0,5480.0],[4000.0,30.0,4040.0,70.0,4080.0,4100.0,131.0,149.0,4160.0,4180.0,210.0,4220.0,251.0,270.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,432.0,4440.0,471.0,4480.0,4500.0,4520.0,549.0,4560.0,4580.0,611.0,630.0,650.0,4660.0,690.0,4700.0,4720.0,4740.0,4760.0,4780.0,813.0,4820.0,851.0,871.0,4880.0,4900.0,4920.0,953.0,972.0,4980.0,1011.0,5020.0,5040.0,5060.0,5080.0,1112.0,5120.0,1149.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,1289.0,5300.0,5320.0,5340.0,1372.0,5380.0,5400.0,5420.0,5440.0,1469.0,5480.0],[4000.0,32.0,4040.0,72.0,4080.0,4100.0,131.0,153.0,4160.0,4180.0,212.0,4220.0,251.0,272.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,430.0,4440.0,471.0,4480.0,4500.0,4520.0,553.0,578.0,4580.0,611.0,632.0,652.0,4660.0,692.0,4700.0,4720.0,4740.0,4760.0,4780.0,809.0,4820.0,851.0,871.0,4880.0,918.0,4920.0,949.0,970.0,4980.0,1011.0,5020.0,5040.0,5060.0,5080.0,1110.0,5120.0,1153.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,1293.0,5300.0,5320.0,5340.0,1370.0,5380.0,5400.0,5420.0,5440.0,1473.0,5480.0],[4000.0,4020.0,4040.0,4060.0,97.0,4100.0,4120.0,4140.0,4160.0,198.0,4200.0,235.0,4240.0,4260.0,4280.0,4300.0,335.0,4340.0,4360.0,4380.0,4400.0,4420.0,457.0,4460.0,4480.0,4500.0,4520.0,4540.0,569.0,4580.0,4600.0,4620.0,4640.0,676.0,4680.0,711.0,4720.0,4740.0,4760.0,4780.0,818.0,4820.0,4840.0,4860.0,897.0,909.0,4920.0,958.0,4960.0,998.0,5000.0,5020.0,5040.0,1072.0,5080.0,5100.0,1131.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,1317.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,1454.0,5460.0,1496.0],[4000.0,4020.0,4040.0,4060.0,89.0,4100.0,4120.0,4140.0,174.0,190.0,4200.0,229.0,4240.0,4260.0,4280.0,4300.0,329.0,351.0,371.0,4380.0,418.0,4420.0,449.0,4460.0,492.0,516.0,536.0,4540.0,574.0,593.0,4600.0,4620.0,4640.0,668.0,4680.0,712.0,735.0,758.0,775.0,4780.0,4800.0,836.0,4840.0,4860.0,888.0,914.0,935.0,4940.0,4960.0,990.0,5000.0,1033.0,1056.0,1071.0,1096.0,5100.0,1132.0,5140.0,1171.0,1192.0,5200.0,1237.0,1258.0,5260.0,5280.0,1308.0,1336.0,1356.0,5360.0,5380.0,1418.0,5420.0,1449.0,5460.0,1488.0],[11.0,4020.0,4040.0,4060.0,95.0,111.0,4120.0,4140.0,169.0,193.0,4200.0,237.0,4240.0,4260.0,4280.0,310.0,337.0,352.0,372.0,392.0,410.0,4420.0,455.0,4460.0,491.0,508.0,528.0,4540.0,4560.0,590.0,4600.0,4620.0,4640.0,677.0,4680.0,4700.0,729.0,749.0,769.0,792.0,4800.0,828.0,4840.0,4860.0,896.0,4900.0,929.0,4940.0,4960.0,993.0,5000.0,1030.0,1048.0,5060.0,1088.0,5100.0,5120.0,5140.0,1172.0,1191.0,1216.0,1228.0,1250.0,1278.0,5280.0,1316.0,1328.0,1348.0,5360.0,1396.0,1409.0,1431.0,1458.0,5460.0,1497.0],[11.0,4020.0,52.0,4060.0,4080.0,111.0,4120.0,4140.0,178.0,4180.0,4200.0,4220.0,4240.0,4260.0,291.0,312.0,4320.0,4340.0,4360.0,390.0,413.0,4420.0,4440.0,4460.0,4480.0,516.0,536.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,737.0,754.0,777.0,790.0,4800.0,836.0,4840.0,4860.0,4880.0,4900.0,937.0,4940.0,4960.0,4980.0,5000.0,5020.0,1056.0,5060.0,1096.0,5100.0,5120.0,5140.0,5160.0,5180.0,1208.0,1235.0,1253.0,1269.0,5280.0,5300.0,1336.0,1357.0,5360.0,1388.0,1414.0,1431.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,138.0,4140.0,4160.0,4180.0,218.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,1018.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[17.0,35.0,58.0,75.0,96.0,116.0,135.0,155.0,177.0,196.0,215.0,236.0,255.0,275.0,298.0,317.0,336.0,357.0,377.0,398.0,418.0,435.0,456.0,475.0,496.0,517.0,537.0,555.0,576.0,596.0,615.0,635.0,655.0,676.0,695.0,716.0,737.0,758.0,777.0,798.0,815.0,837.0,855.0,875.0,896.0,916.0,937.0,955.0,975.0,996.0,1015.0,1037.0,1057.0,1076.0,1098.0,1115.0,1136.0,1155.0,1176.0,1197.0,1218.0,1238.0,1258.0,1278.0,1295.0,1316.0,1338.0,1357.0,1375.0,1397.0,1417.0,1438.0,1456.0,1475.0,1496.0],[17.0,35.0,58.0,75.0,96.0,116.0,135.0,155.0,177.0,196.0,215.0,236.0,255.0,275.0,298.0,317.0,336.0,357.0,377.0,398.0,418.0,435.0,456.0,475.0,496.0,517.0,537.0,555.0,576.0,596.0,615.0,635.0,655.0,676.0,695.0,716.0,737.0,758.0,777.0,798.0,815.0,837.0,855.0,875.0,896.0,916.0,937.0,955.0,975.0,996.0,1015.0,1037.0,1057.0,1076.0,1098.0,1115.0,1136.0,1155.0,1176.0,1197.0,1218.0,1238.0,1258.0,1278.0,1295.0,1316.0,1338.0,1357.0,1375.0,1397.0,1417.0,1438.0,1456.0,1475.0,1496.0],[16.0,38.0,55.0,78.0,96.0,116.0,138.0,158.0,176.0,196.0,218.0,236.0,258.0,278.0,295.0,316.0,337.0,356.0,376.0,395.0,415.0,438.0,456.0,478.0,496.0,516.0,536.0,558.0,577.0,597.0,618.0,638.0,658.0,677.0,698.0,717.0,736.0,755.0,776.0,795.0,818.0,836.0,858.0,878.0,896.0,917.0,936.0,958.0,978.0,997.0,1018.0,1036.0,1056.0,1076.0,1095.0,1118.0,1137.0,1158.0,1176.0,1196.0,1215.0,1236.0,1255.0,1276.0,1298.0,1317.0,1336.0,1356.0,1378.0,1396.0,1416.0,1435.0,1457.0,1478.0,1496.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0],[4000.0,4020.0,4040.0,4060.0,4080.0,4100.0,4120.0,4140.0,4160.0,4180.0,4200.0,4220.0,4240.0,4260.0,4280.0,4300.0,4320.0,4340.0,4360.0,4380.0,4400.0,4420.0,4440.0,4460.0,4480.0,4500.0,4520.0,4540.0,4560.0,4580.0,4600.0,4620.0,4640.0,4660.0,4680.0,4700.0,4720.0,4740.0,4760.0,4780.0,4800.0,4820.0,4840.0,4860.0,4880.0,4900.0,4920.0,4940.0,4960.0,4980.0,5000.0,5020.0,5040.0,5060.0,5080.0,5100.0,5120.0,5140.0,5160.0,5180.0,5200.0,5220.0,5240.0,5260.0,5280.0,5300.0,5320.0,5340.0,5360.0,5380.0,5400.0,5420.0,5440.0,5460.0,5480.0]]
sim_dur_ff=50.0
conn2_prob=0.3920475
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
Mpr = PopulationRateMonitor(outputLayer, bin=1*ms)

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
