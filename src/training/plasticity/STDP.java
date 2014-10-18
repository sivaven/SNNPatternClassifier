package training.plasticity;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

import briansim.BrianSimParameter;
import briansim.BrianSimProcess;
import briansim.BriansimPythonBuilder;
import snn.SNN;
import snn.SpikeTimes;
import training.DataSetManager;
import classifier.Classifier;
import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import encode.Encoder;

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
		DataSet dataSet = new IrisDataset();
		DataSetManager dm = new DataSetManager(dataSet);
		dm.setDataSetPartitions(0.5f, 1);
		Map<Integer, Pattern> trainingSet = dm.getTrainingSet();
		Map<Integer, Pattern> evalSet = dm.getEvaluationSet();
		
		Map<Integer, Pattern> sampleTrainingSet = dataSet.samplePatternSet(trainingSet, 1f);
		Map<Integer, Pattern> sampleEvalSet = dataSet.samplePatternSet(evalSet, 0.02f);
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
		
		int[] nNeurons = new int[] {32, 20, 3};
		
		
		Map<BrianSimParameter, Object> parms = new HashMap<BrianSimParameter, Object>();
		parms.put(BrianSimParameter.dt_, 1.0f);
		parms.put(BrianSimParameter.nw_arch, nNeurons);
		parms.put(BrianSimParameter.sim_dur_stdp, DURATION);
		parms.put(BrianSimParameter.sim_dur_ff, 500f);
		parms.put(BrianSimParameter.conn1_init_weight, 3.0f);
		parms.put(BrianSimParameter.conn2_init_weight, 5.0f);
		parms.put(BrianSimParameter.stdp1_a_step, 0.1f);
		parms.put(BrianSimParameter.stdp2_a_step, 0.1f);
		parms.put(BrianSimParameter.stdp_tau, 10f);
		parms.put(BrianSimParameter.stdp_gmax, 100.0f);
		parms.put(BrianSimParameter.spike_times_iter_stdp, stdpSpikeTimes);
		parms.put(BrianSimParameter.spike_times_iter_ff3d, ffSpikeTimes);
		parms.put(BrianSimParameter.ip_pattern_idx, ipPatternIdx);
		
		BriansimPythonBuilder builder = new BriansimPythonBuilder("testing.py", parms, true);
		builder.build();
		
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

	public static void run1(){
		DataSet dataSet = new IrisDataset();
		
		Map<Integer, Pattern> allClass0 = dataSet.samplePatternSetByClass(0, 1);
		Map<Integer, Pattern> allClass1 = dataSet.samplePatternSetByClass(1, 1);
		Map<Integer, Pattern> allClass2 = dataSet.samplePatternSetByClass(2, 1);
		
		Map<Integer, Pattern> trainingSet0 = dataSet.samplePatternSet(allClass0, 0.5f);
		Map<Integer, Pattern> trainingSet1 = dataSet.samplePatternSet(allClass1, 0.5f);
		Map<Integer, Pattern> trainingSet2 = dataSet.samplePatternSet(allClass2, 0.5f);
		
		Map<Integer, Pattern> evalSet0 = dataSet.getExclusive(allClass0, trainingSet0);
		Map<Integer, Pattern> evalSet1 = dataSet.getExclusive(allClass1, trainingSet1);
		Map<Integer, Pattern> evalSet2 = dataSet.getExclusive(allClass2, trainingSet2);
		
		Map<Integer, Pattern> trianingSetAll = new HashMap<Integer, Pattern>();			
		trianingSetAll.putAll(trainingSet0);
		trianingSetAll.putAll(trainingSet1);
		trianingSetAll.putAll(trainingSet2);
		TreeMap<Integer, Pattern> trainingSetOrdered = dataSet.getOrderedMapWCustomKey(trianingSetAll, 0);		
		dataSet.shuffleMap(trainingSetOrdered);		
		
		TreeMap<Integer, Pattern> evalSetOrdered0 = dataSet.getOrderedMapWCustomKey(evalSet0, trainingSetOrdered.size());
		TreeMap<Integer, Pattern> evalSetOrdered1 = dataSet.getOrderedMapWCustomKey(evalSet1, trainingSetOrdered.size()+evalSetOrdered0.size());
		TreeMap<Integer, Pattern> evalSetOrdered2 = dataSet.getOrderedMapWCustomKey(evalSet2, trainingSetOrdered.size()+evalSetOrdered0.size()+evalSetOrdered1.size());
				
		TreeMap<Integer, Pattern> allInputPatterns = new TreeMap<>(trainingSetOrdered);
		allInputPatterns.putAll(evalSetOrdered0);
	//	allInputPatterns.putAll(evalSetOrdered1);
	//	allInputPatterns.putAll(evalSetOrdered2);
		
		
	//	dataSet.displayDataSet(allInputPatterns);
		
		
		Encoder encoder = new Encoder(dataSet, 8);
		SpikeTimes[] ipLayerSpikeTimes = encoder.encode(allInputPatterns, 20);
	
		
		int[] nNeurons = new int[] {32, 50, 3};
		SNN snn = new SNN(nNeurons);
		//snn.randomizeWeights(5);
		snn.setInputLayerSpikeTimes(ipLayerSpikeTimes);
		
		BrianSimProcess bsm = new BrianSimProcess(snn);
		//bsm.setDebug(true);
		for(int i=0; i<1;i++)
		bsm.runBrianSimSNNArch1(true);
	
	//	bsm.displayBrianOutput();
	}
}
