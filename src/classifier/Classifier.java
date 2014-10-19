package classifier;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import briansim.BrianSimParameterLabel;
import briansim.BrianSimProcess;
import outputwriter.FileUtils;
import snn.SNN;
import snn.SpikeTimes;
import dataset.DataSet;
import dataset.Pattern;
import ecj.ECJStarter;
import encode.Encoder;

public class Classifier {

	private SNN snn;	
	private Encoder encoder;
	
	private boolean debug = false;
	public boolean evalStatDisplay = false;
	public boolean evalStatDetailDisplay = false;
	
	public Classifier(int[] arch, Encoder encoder_) {
		snn = new SNN(arch);
		this.encoder = encoder_;
	}
	public Classifier(SNN snn, Encoder encoder_) {
		this.snn = snn;
		this.encoder = encoder_;
	}
	
	public Classifier(Encoder encoder_) {
		this.snn = null;
		this.encoder = encoder_;
	}
	
	public void randomizeWeights(int magFactor) {
		snn.randomizeWeights(magFactor);
	}
	public void setWeights(float[] weights){
		if(snn.getNWeights() != weights.length) {
			System.out.println("Expected length: "+snn.getNWeights() +"\tReceived: "+weights.length);
			System.exit(-1);
		}
		snn.setWeights(weights);
	}
	public void setInputLayerSpikeTimes(SpikeTimes[] spikeTimes) {
		snn.setInputLayerSpikeTimes(spikeTimes);
	}
	
	
	public SNN getSNN(){
		return this.snn;
	}
	
	public void setSNN(SNN snn){
		this.snn = snn;
	}
	public float doStdpThenevaluate(Map<Integer, Pattern> ffSet) {
		/*
		 * add remaining parms to snn, related to dataset
		 */
		SpikeTimes[][] ffSpikeTimes = new SpikeTimes[ffSet.size()][];
		int[] ipPatternIdx = new int[ffSet.size()];
		
		Iterator it = ffSet.entrySet().iterator();
		int i=0;
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        Integer key = (Integer) pairs.getKey();
	        Pattern pattern = (Pattern) pairs.getValue();	       
	        ffSpikeTimes[i] = encoder.encode(pattern.getAttributes());
	        ipPatternIdx[i++] = key;
		}				
		snn.addParameter(BrianSimParameterLabel.spike_times_iter_ff3d, ffSpikeTimes);
		snn.addParameter(BrianSimParameterLabel.ip_pattern_idx, ipPatternIdx);
		/*
		 * run brian sim process		
		 */
		BrianSimProcess bsm = new BrianSimProcess();
		String moduleName = bsm.buildPythonModule(snn.getParms());		
		bsm.runBrianSimSNN(moduleName, true);	
		//bsm.displayBrianOutput();
		/*
		 * evaluate
		 */
		Iterator it2 = ffSet.entrySet().iterator();
		float score = 0;
		while (it2.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it2.next();
	        Integer key = (Integer) pairs.getKey();
	        Pattern pattern = (Pattern) pairs.getValue();	        
	        int classBySnn = encoder.decode(bsm.getOutputLayerSpikeTimesForPattern(key));
	        if(pattern.get_class().getNumericClass() == classBySnn){
	        	score += 1;
	        }
	        if(evalStatDisplay) {
	        	System.out.println("PatternKey\tClass\tClassBySNN.\t"+key+"\t"+pattern.get_class().getNumericClass()+"\t"+classBySnn);
	        }
		}	
		return (1.0f*score)/(1.0f*ffSet.size());
	}
	
	public float evaluate(Map<Integer, Pattern> patternSet){
		float hit = 0;
		Iterator it = patternSet.entrySet().iterator();
		int score = 0;	
		int itmCnt = 0;
		double time = System.currentTimeMillis();
		if(evalStatDisplay) {
			System.out.println("Eval starting.. with nPattenrs : " +patternSet.size());
		}
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	       // Integer key = (Integer) pairs.getKey();
	        Pattern pattern = (Pattern) pairs.getValue();
	        int classBySNN = classify(pattern.getAttributes());
	       
			if(evalStatDetailDisplay) {
				snn.displayOutputLayerSpikeTimes();
				System.out.println("Actual Class : "+ pattern.get_class().getNumericClass());
			}
	        if(pattern.get_class().getNumericClass() == classBySNN){
	        	score += 1;
	        }
	        itmCnt+=1;
	        if(itmCnt%5==0) FileUtils.writeEvalStat(""+itmCnt);
	        if(evalStatDisplay && itmCnt%1==0) System.out.println("Eval done for nPattenrs : " +itmCnt);
		}
		FileUtils.writeEvalStat("\n");
        if(evalStatDisplay) System.out.println("Eval Completed in : "+(System.currentTimeMillis() -time)/1000+" s.");
		return (1.0f*score)/(1.0f*patternSet.size());
	}
	
	public int classify(ArrayList<Float> attributes){		
		setInputLayerSpikeTimes(encoder.encode(attributes));		
		ArrayList<SpikeTimes> opLayerSpikeTimes = null;//runSNNArch1();		
		return encoder.decode(opLayerSpikeTimes);
	}
	
	public DataSet getEncoderDataSet(){
		return this.encoder.getDataSet();
	}
	
	public void setDebug(boolean debug) {
		this.debug = debug;
	}

}
