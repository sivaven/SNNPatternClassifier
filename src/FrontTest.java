import java.util.ArrayList;
import java.util.Map;

import snn.SNN;
import snn.SpikeTimes;
import training.DataSetManager;
import classifier.Classifier;
import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import encode.Encoder;


public class FrontTest {

	public static void EvaluatorTest(){
		
		DataSet dataSet = new IrisDataset();	
		Encoder encoder = new Encoder(dataSet, 8);	
		Classifier cl = new Classifier(encoder);
		
		int[] arch = new int[]{32,800,200,3};		
		float[] cProb = new float[] {0.8f, 0.2f, 0.05f, 0.02f, 0.01f, 0.01f, 0.01f };
		float[] cW = new float[] {2, 2, 2, 2, 2, 2, 2};		
		SNN snn = new SNN(arch, cProb, cW);
		cl.setSNN(snn);
		
		DataSetManager eval = new DataSetManager(dataSet);
		float tSet = 0.1f;
		float fitSet = 0.4f;
		eval.setDataSetPartitions(tSet, fitSet);
		dataSet.displayDataSet(eval.getTrainingSet());
		System.out.println("<><><><><>");
		Map<Integer, Pattern> fitEvalset = eval.sampleFitEvalSet();
		dataSet.displayDataSet(fitEvalset);
		System.out.println("Training size:" + eval.getTrainingSet().size());
		System.out.println("Fit size:" + fitEvalset.size());
		fitEvalset = eval.sampleFitEvalSet();
		dataSet.displayDataSet(fitEvalset);
		System.out.println("Training size:" + eval.getTrainingSet().size());
		System.out.println("Fit size:" + fitEvalset.size());
	}
	public static void main(String[] args) {
		
		DataSet dataSet = new IrisDataset();	
		Encoder encoder = new Encoder(dataSet, 8);	
		Classifier cl = new Classifier(encoder);
		
		int[] arch = new int[]{32,800,200,3};		
		float[] cProb = new float[] {0.8f, 0.2f, 0.05f, 0.02f, 0.01f, 0.01f, 0.01f };
		float[] cW = new float[] {2, 2, 2, 2, 2, 2, 2};		
		SNN snn = new SNN(arch, cProb, cW);
		cl.setSNN(snn);
				
		cl.evalStatDisplay = false;
		cl.evalStatDetailDisplay = false;
		cl.setDebug(false);
		/*
		 * setup evaluator
		 */
		float tSetFrac = 0.1f;  //n=15
		float fitSetFrac = 0.4f; //n=6
		DataSetManager dm = new DataSetManager(dataSet);
		dm.setDataSetPartitions(tSetFrac, fitSetFrac);
		
		//ArrayList<Float> attributes = dm.getTrainingSet().get(0).getAttributes();
		//SpikeTimes[] spikeTimes = encoder.encode(attributes );
		//cl.setInputLayerSpikeTimes(spikeTimes);
		
		//System.out.println(cl.classify(attributes));
		
		float hit = cl.evaluate(dm.sampleFitEvalSet());
		
		System.out.println("hit: \t" + hit);
		
	}
}
