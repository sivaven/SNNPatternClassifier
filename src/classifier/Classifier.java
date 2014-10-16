package classifier;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Map;

import briansim.BrianSimProcess;
import outputwriter.FileUtils;
import snn.SNN;
import snn.SpikeTimes;
import dataset.DataSet;
import dataset.Pattern;
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
	public SpikeTimes[] runSNNArch1(){		
		BrianSimProcess bSimProcess = new BrianSimProcess(snn);
		bSimProcess.setDebug(debug);
		bSimProcess.runBrianSimSNNArch1();
		if(debug)
			bSimProcess.displayBrianOutput();	
		return snn.getOutputLayerSpikeTimes();
	}
	
	public SpikeTimes[] runSNNArch2(){		
		BrianSimProcess bSimProcess = new BrianSimProcess(snn);
		bSimProcess.setDebug(debug);
		bSimProcess.runBrianSimSNNArch2();
		if(debug)
			bSimProcess.displayBrianOutput();	
		return snn.getOutputLayerSpikeTimes();
	}
	
	public SNN getSNN(){
		return this.snn;
	}
	
	public void setSNN(SNN snn){
		this.snn = snn;
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
		SpikeTimes[] opLayerSpikeTimes = runSNNArch1();		
		return encoder.decode(opLayerSpikeTimes);
	}
	
	public DataSet getEncoderDataSet(){
		return this.encoder.getDataSet();
	}
	
	public void setDebug(boolean debug) {
		this.debug = debug;
	}

}
