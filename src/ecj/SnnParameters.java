package ecj;

import briansim.BrianSimParameterLabel;
import snn.SNN;

public class SnnParameters {
	private static final float dt_ = 1.0f;
	//private static final float stdp_gmax = 100.0f;
	
	float[] genes;
	
	public SnnParameters(float[] genes){
		this.genes = genes;
	}
	
	public int[] getNwArch() {
		return new int[] {32, (int)genes[0], 3};
	}
	public float getConn1InitWeight() {
		return genes[1];
	}	
	public float getConn2InitWeight() {
		return genes[2];
	}	
	public float getA_1() {
		return genes[3];
	}
	public float getA_2() {
		return genes[4];
	}
	public float tau() {
		return genes[5];
	}
	public float getConn1Prob() {
		return genes[6];
	}
	public float getConn2Prob() {
		return genes[7];
	}
	public float getGmax() {
		return genes[8];
	}
	public SNN constructSnn(){
		/*
		 * add EA parms to SNN
		 */
		SNN snn = new SNN(getNwArch());
		snn.addParameter(BrianSimParameterLabel.conn1_init_weight, getConn1InitWeight());
		snn.addParameter(BrianSimParameterLabel.conn2_init_weight, getConn2InitWeight());
		snn.addParameter(BrianSimParameterLabel.stdp1_a_step, getA_1());
		snn.addParameter(BrianSimParameterLabel.stdp2_a_step, getA_2());
		snn.addParameter(BrianSimParameterLabel.stdp_tau, tau());
		snn.addParameter(BrianSimParameterLabel.conn1_prob, getConn1Prob());
		snn.addParameter(BrianSimParameterLabel.conn2_prob, getConn2Prob());
		snn.addParameter(BrianSimParameterLabel.stdp_gmax, getGmax());
		/*
		 * add constants
		 */
		snn.addParameter(BrianSimParameterLabel.dt_, dt_);
		
		snn.addParameter(BrianSimParameterLabel.sim_dur_stdp, (float)ECJStarter.dataSetManager.getTrainingSet().size()
				*ECJStarter.PATTERN_WINDOW);
		snn.addParameter(BrianSimParameterLabel.sim_dur_ff, ECJStarter.FF_SIM_DUR);
		snn.addParameter(BrianSimParameterLabel.spike_times_iter_stdp, ECJStarter.stdpSpikeTimes);		
		
		return snn;
	}
	
}
