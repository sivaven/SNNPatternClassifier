import java.util.Map;

import training.Evaluator;
import classifier.Classifier;
import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import encode.Encoder;


public class FrontTest {

	public static void EvaluatorTest(){
		int[] nNeurons = new int[] {32, 4, 3};	
		DataSet dataSet = new IrisDataset();	
		Encoder encoder = new Encoder(dataSet, 8);	
		Classifier cl = new Classifier(nNeurons, encoder);
		Evaluator eval = new Evaluator(cl);
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
		
		/*
		 * setup classifier
		 */
		int[] nNeurons = new int[] {32, 4, 3};	
		DataSet dataSet = new IrisDataset();	
		Encoder encoder = new Encoder(dataSet, 8);	
		
		Classifier cl = new Classifier(nNeurons, encoder);			
		//float[] weights = new float[cl.snn.getNWeights()+1];
		//weights[0] =10f;
		//weights[4] = 10f;
		//cl.setWeights(weights);
		cl.randomizeWeights(10);
		cl.evalStatDisplay = true;
		cl.evalStatDetailDisplay = true;
		/*
		 * setup evaluator
		 */
		float tSetFrac = 0.1f;  //n=15
		float fitSetFrac = 0.4f; //n=6
		Evaluator eval = new Evaluator(cl);
		eval.setDataSetPartitions(tSetFrac, fitSetFrac);
		
		float hit = eval.evaluate();
		
		System.out.println("hit: \t" + hit);
		
	}
}
