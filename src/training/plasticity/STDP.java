package training.plasticity;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

import briansim.BrianSimParameterLabel;
import briansim.BrianSimProcess;
import briansim.BriansimPythonBuilder;
import snn.SNN;
import snn.SpikeTimes;
import classifier.Classifier;
import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import ecj.DataSetManager;
import ecj.ECJStarter;
import ecj.SnnParameters;
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
		
		ECJStarter.init();
		ECJStarter.resampleDataSets();
		
		float[] genes = new float[] {20, 3, 5, 0.1f, 0.1f, 10, 0.5f, 0.5f, 99};
		SnnParameters snnParms = new SnnParameters(genes);
		SNN snn = snnParms.constructSnn();
		
		Classifier cl = new Classifier(ECJStarter.encoder);			
		cl.setSNN(snn);
		cl.evalStatDisplay= true;
        /*
         * 
         */		
        float score = cl.doStdpThenevaluate(ECJStarter.dataSetManager.getSampleEvaluationSet(ECJStarter.sampleEvalSetFrac));
        System.out.println("\n**Accuracy.\t"+score);
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
