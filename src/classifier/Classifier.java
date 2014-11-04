package classifier;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Map;

import outputwriter.FileUtils;
import snn.SNN;
import snn.SpikeTimes;
import briansim.BrianSimParameterLabel;
import briansim.BrianSimProcess;
import code.Decoder;
import code.Encoder;
import dataset.DataSet;
import dataset.Pattern;
import ecj.ECJStarter;

public class Classifier {

	private SNN snn;	
	private Encoder encoder;
	private Decoder decoder;
	
	private boolean debug = false;
	public boolean evalStatDisplay = false;
	public boolean evalStatDetailDisplay = false;
	
	public Classifier(SNN snn, Encoder encoder_, Decoder decoder_) {
		this.snn = snn;
		this.encoder = encoder_;
		this.decoder = decoder_;
	}
	public Classifier(int[] arch, Encoder encoder_, Decoder decoder_) {
		this(new SNN(arch), encoder_, decoder_);
	}	
	
	public Classifier(Encoder encoder_, Decoder _decoder) {
		this.snn = null;
		this.encoder = encoder_;
		this.decoder = _decoder;
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
	/*
	 * version 1
	 */
	public float doStdpThenevaluate(Map<Integer, Pattern> ffSet, boolean deleteModuleAfterRun, boolean doPlot) {
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
		String moduleName = bsm.buildPythonModule(snn.getParms(), doPlot);		
		bsm.runBrianSimSNN(moduleName);	
		if(bsm.isBrianOutputEmpty()) {
			System.out.println("Brian output empty for module.\t"+moduleName);				
			System.exit(-1);			
		}
		if(deleteModuleAfterRun) {
			bsm.deleteModule(moduleName);
		}
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
	    //    int classBySnn = encoder.decode(bsm.getOutputLayerSpikeTimesForPattern(key));
	        int classBySnn = decoder.decode(bsm.getOutputLayerPopRatesForPattern(key));
	        if(pattern.get_class().getNumericClass() == classBySnn){
	        	score += 1;
	        }
	        if(evalStatDisplay) {
	        	System.out.println("PatternKey\tClass\tClassBySNN.\t"+key+"\t"+pattern.get_class().getNumericClass()+"\t"+classBySnn);
	        }
		}	
		return (1.0f*score)/(1.0f*ffSet.size());
	}
	
	public float doStdpThenevaluate(Map<Integer, Pattern> ffSet) {
		return doStdpThenevaluate(ffSet, true, false);
	}
	
	/*
	 * version 2
	 */
	public float doStdpThenevaluate(SpikeTimes[] stdpSpikeTimes, 
			SpikeTimes[][] ffSpikeTimes, int[] ipPatternIdx, int[] patternClasses){
		return doStdpThenevaluate(stdpSpikeTimes, 
				ffSpikeTimes, ipPatternIdx, patternClasses,
				true, false);
	}
	public float doStdpThenevaluate(SpikeTimes[] stdpSpikeTimes, 
									SpikeTimes[][] ffSpikeTimes, int[] ipPatternIdx, int[] patternClasses,
									boolean deleteModuleAfterRun, boolean doPlot) {
		/*
		 * add remaining parms to snn, related to dataset
		 */
		//System.out.println(stdpSpikeTimes.length);
		snn.addParameter(BrianSimParameterLabel.spike_times_iter_stdp, stdpSpikeTimes);			
		snn.addParameter(BrianSimParameterLabel.spike_times_iter_ff3d, ffSpikeTimes);
		snn.addParameter(BrianSimParameterLabel.ip_pattern_idx, ipPatternIdx);
		/*
		 * run brian sim process		
		 */
		BrianSimProcess bsm = new BrianSimProcess();
		String moduleName = bsm.buildPythonModule(snn.getParms(), doPlot);		
		bsm.runBrianSimSNN(moduleName);	
		if(bsm.isBrianOutputEmpty()) {
			System.out.println("Brian output empty for module.\t"+moduleName);				
			System.exit(-1);			
		}
		if(deleteModuleAfterRun) {
			bsm.deleteModule(moduleName);
		}
		//bsm.displayBrianOutput();
		/*
		 * evaluate
		 */		
		float score = 0;
		for(int i=0;i<ipPatternIdx.length;i++){	        
	        int classBySnn = decoder.decode(bsm.getOutputLayerPopRatesForPattern(ipPatternIdx[i]));	        
	        if(patternClasses[i] == classBySnn){
	        	score += 1;
	        }
	        if(evalStatDisplay) {
	        	System.out.println("PatternKey\tClass\tClassBySNN.\t"+ipPatternIdx[i]+"\t"+patternClasses[i]+"\t"+classBySnn);
	        }
		}	
		return (1.0f*score)/(1.0f*ipPatternIdx.length);
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
	
	public float twoFoldEvaluate() {
		float acc0 = doStdpThenevaluate(ECJStarter.stdpSpikeTimes[0], 
				ECJStarter.ffSpikeTimes[1], ECJStarter.ipPatternIdx[1], ECJStarter.patternClasses[1]);
		float acc1 = doStdpThenevaluate(ECJStarter.stdpSpikeTimes[1], 
				ECJStarter.ffSpikeTimes[0], ECJStarter.ipPatternIdx[0], ECJStarter.patternClasses[0]);
		
		return (acc0+acc1)/2.0f;
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
