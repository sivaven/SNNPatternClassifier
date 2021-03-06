package ecj;

import briansim.BrianSimParameterLabel;
import snn.SNN;

public class SnnParameters {
	public static final float dt_ = 0.1f;
	//private static final float stdp_gmax = 100.0f;
	
	float[] genes;
	
	public SnnParameters(float[] genes){
		this.genes = genes;
	}
	
	public int[] getNwArch() {
		return new int[] {ECJStarter.nRF*ECJStarter.dataSetManager.dataSet.getnAttr(), (int)genes[0], (int)genes[1]};
	}
	public float getConn1InitWeight() {
		return genes[2];
	}	
	public float getConn2InitWeight() {
		return genes[3];
	}	
	public float getA_1() {
		return 1;
	}
	public float getA_2() {
		return 1;
	}
	public float tau() {
		return genes[6];
	}
	public float getGmax() {
		return genes[7];
	}
	
	public float getConn1Prob() {
		return genes[8];
	}
	public float getConn2Prob() {
		return genes[9];
	}
	
	public float getPopRateThresh(){
		return genes[10];
	}
	
	public float[] getClassTimesToThresh() {
		float timeOffsetForClasses = 1;//genes[12];
		return new float[] {
							genes[11]+(0*timeOffsetForClasses),  
							genes[11]+(1*timeOffsetForClasses), 
							genes[11]+(2*timeOffsetForClasses)
							};
	}
	
	public float getEta(){
		return genes[13];
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
		snn.addParameter(BrianSimParameterLabel.eta, getEta());
		snn.addParameter(BrianSimParameterLabel.stdp_tau, tau());
		snn.addParameter(BrianSimParameterLabel.conn1_prob, getConn1Prob());
		snn.addParameter(BrianSimParameterLabel.conn2_prob, getConn2Prob());
		snn.addParameter(BrianSimParameterLabel.stdp_gmax, getGmax());
		/*
		 * add constants
		 */
		snn.addParameter(BrianSimParameterLabel.dt_, dt_);
		
		snn.addParameter(BrianSimParameterLabel.sim_dur_stdp, (float)ECJStarter.dataSetManager.getTrainingSet().size()
				*ECJStarter.PATTERN_WINDOW*ECJStarter.stdp_iter);
		snn.addParameter(BrianSimParameterLabel.sim_dur_ff, ECJStarter.FF_SIM_DUR);
		
		return snn;
	}
	
}
