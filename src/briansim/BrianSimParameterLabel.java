package briansim;

/*
 * 3 layered feed-forward architecture
 */
public enum BrianSimParameterLabel {
	dt_, sim_dur_stdp, sim_dur_ff, stdp_gmax,
	//EA parameters
	nw_arch, conn1_init_weight, conn2_init_weight, stdp1_a_step, stdp2_a_step, stdp_tau, conn1_prob, conn2_prob, eta,
	//inputs
	spike_times_iter_stdp, spike_times_iter_ff3d, ip_pattern_idx
}
