package classifier;

import snn.BrianSimProcess;
import snn.SNN;
import snn.SpikeTimes;

public class Classifier {

	private SNN snn;
	private boolean debug = false;
	public Classifier(int[] arch) {
		snn = new SNN(arch);
	}
	public void randomizeWeights() {
		snn.randomizeWeights();
	}
	public void setWeights(float[] weights){
		snn.setWeights(weights);
	}
	public void setInputLayerSpikeTimes(float[][] spikeTimes) {
		snn.setInputLayerSpikeTimes(spikeTimes);
	}
	public SpikeTimes[] runSNN(){		
		BrianSimProcess bSimProcess = new BrianSimProcess(snn);
		bSimProcess.setDebug(debug);
		bSimProcess.runBrianSimSNN();
		if(debug)
			bSimProcess.displayBrianOutput();	
		return snn.getOutputLayerSpikeTimes();
	}
	
	public SNN getSNN(){
		return this.snn;
	}
	
	public static void main(String[] args) {
		int[] nNeurons = new int[] {3, 4, 3};
		float[][] _spikeTimes = new float[][] {{100.0f, 200f, 300f}, {300f, 400f, 500f}, {}};
		
		Classifier cl = new Classifier(nNeurons);
		float[] weights = new float[cl.snn.getNWeights()+1];
		weights[0] =100f;
		weights[4] = 100f;
		cl.setWeights(weights);
		//cl.randomizeWeights();		
		cl.setInputLayerSpikeTimes(_spikeTimes);
		//cl.debug = true;
		SpikeTimes[] opLayerSpikeTimes = cl.runSNN();
		for(SpikeTimes spikeTimes: opLayerSpikeTimes)
			spikeTimes.display();
	}	
	public void setDebug(boolean debug) {
		this.debug = debug;
	}

}
