package training.plasticity;

import java.util.ArrayList;
import java.util.Map;

import snn.SNN;
import snn.SpikeTimes;
import classifier.Classifier;
import code.Decoder;
import dataset.Pattern;
import ecj.ECJStarter;
import ecj.SnnParameters;

public class STDP {
	public static final float TIME_INTERVAL_BW_IP_PATTERNS = 20;
	public static float N_INPUT_PATTERNS ;
	
	public static float DURATION; //ms
	public static final float tau_stdp = 10f; //ms
	public static final int gmax = 10;
	public static final float conn1_init_weight = 3.0f;
	public static final float weight_step = 1.0f;
	
	public static final float conn1Prob = 1.0f;
	public static final float conn2Prob = 1.0f;
	public static final float conn2_init_weight = 5.0f;
	
	public static void main(String[] args) {
		
		ECJStarter.init();		
		
		float[] genes = new float[] {499.0f, 453.0f,
				11.0f, 5.0f,
				1.3580258f, 8.058138f, 
				101.0f, 
				7.0f, 
				0.88080144f, 0.5963614f,
				152.0f, 18.0f, 1.0f
		};
		genes = new float[] {72.0f, 83.0f,
				5.0f, 8.0f,
				3.7924376f, 2.8046827f,
				10.0f,
				20.0f,
				0.25669977f, 0.24825996f, 
				142.0f, 17.0f, 1.0f

		}; 
		genes = new float[] {26, 99, 
			22, 7,
			9.600343f, 13.661923f,
			188.0f,
			14.0f,
			0.53445536f, 0.24563898f,
			150.0f, 18.0f, 1.0f, 10
};
		genes = new float[] {61.0f, 99.0f,
		9.0f, 8.0f, 1.9465299f, -2.9970865f, 500.0f, 10.0f, 0.5762958f, 0.3920475f, 1500.0f, 16.0f, 1.0f, 2.076338f};

		
       	
		double time = System.currentTimeMillis();
		Map<Integer, Pattern> trainingSet = ECJStarter.dataSetManager.getTrainingSet();
		
		SpikeTimes[] spikeTimes = ECJStarter.encoder.encode(trainingSet, ECJStarter.PATTERN_WINDOW, ECJStarter.stdp_iter);
		
		for(int i=0;i<spikeTimes.length;i++){
			if(i==0) System.out.print("[");
			spikeTimes[i].display();
			if(i==spikeTimes.length-1) System.out.print("]");
			else System.out.print(",");
			
		}
		System.out.println();
		for(int i=0;i<1;i++){
		//	ECJStarter.resampleDataSets();
			SnnParameters snnParms = new SnnParameters(genes);		
			Decoder decoder = new Decoder(snnParms.getPopRateThresh(), SnnParameters.dt_, snnParms.getClassTimesToThresh());	       
	        Classifier cl = new Classifier(ECJStarter.encoder, decoder);			
			cl.setSNN(snnParms.constructSnn());
			cl.evalStatDisplay= false;
			
	        float score = cl.twoFoldEvaluate();
	        		//cl.doStdpThenevaluate(ECJStarter.dataSetManager.getSampleEvaluationSet(ECJStarter.sampleEvalSetFrac)
	        			//						, true,
	        			//						false);
	        System.out.println("Accuracy.\t"+score);
    	
		}
		time = System.currentTimeMillis() - time;
	//	System.out.println("Time taken.\t"+(time/1000)+" s.");

	}
	
	public static void other(){
		/*DataSet dataSet = new IrisDataset();
		DataSetManager dm = new DataSetManager(dataSet);
		dm.setDataSetPartitions(0.5f, 1);
		Map<Integer, Pattern> trainingSet = dm.getTrainingSet();
		Map<Integer, Pattern> evalSet = dm.getEvaluationSet();
		
		Map<Integer, Pattern> sampleTrainingSet = dataSet.samplePatternSet(trainingSet, 1f);
		Map<Integer, Pattern> sampleEvalSet = dataSet.samplePatternSet(evalSet, 0.1f);
		System.out.println("sample T set size.\t"+sampleTrainingSet.size());
		System.out.println("sample E set size.\t"+sampleEvalSet.size());		
		N_INPUT_PATTERNS = sampleTrainingSet.size();
		DURATION = N_INPUT_PATTERNS * TIME_INTERVAL_BW_IP_PATTERNS;
		
		Encoder encoder = new Encoder(dataSet, 8);
		SpikeTimes[] stdpSpikeTimes = encoder.encode(sampleTrainingSet, TIME_INTERVAL_BW_IP_PATTERNS);
		SpikeTimes[][] ffSpikeTimes = new SpikeTimes[sampleEvalSet.size()][];
		int[] ipPatternIdx = new int[sampleEvalSet.size()];
		
		Iterator it = sampleEvalSet.entrySet().iterator();
		int i=0;
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        Integer key = (Integer) pairs.getKey();
	        Pattern pattern = (Pattern) pairs.getValue();	       
	        ffSpikeTimes[i] = encoder.encode(pattern.getAttributes());
	        ipPatternIdx[i++] = key;
		}		
		*/
		
		
		
		/*	BrianSimProcess bsm = new BrianSimProcess(snn);
		double time = System.currentTimeMillis();
		bsm.runBrianSimSNNArch1(true);
		bsm.displayBrianOutput();
		time = System.currentTimeMillis() - time;
		System.out.println("Time taken for "+DURATION+" ms Sim .\t"+time/1000);
		
		N_INPUT_PATTERNS = sampleEvalSet.size();
		DURATION = N_INPUT_PATTERNS * TIME_INTERVAL_BW_IP_PATTERNS;
		Classifier classifier = new Classifier(snn, encoder);
		time = System.currentTimeMillis();
		float hits = 0;//classifier.evaluate(sampleEvalSet);	
		time = System.currentTimeMillis() - time;
		System.out.println("Time taken for "+DURATION+" ms Sim .\t"+time/1000);
		
		System.out.println("Hits.\t"+hits);*/
	}

}
