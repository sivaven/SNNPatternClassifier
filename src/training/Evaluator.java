package training;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import classifier.Classifier;
import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import dataset.classes.IrisClass;

public class Evaluator {
	
	private Map<Integer, Pattern> trainingSet;
	private Map<Integer, Pattern> evaluationSet;
	ArrayList<Map<Integer, Pattern>> trainingSetByClass;
	private float fitSetFrac;
	
	Classifier classifier;
	
	public Evaluator(Classifier classifier_){
		this.classifier = classifier_;		
	}
	
	public float evaluate(){
		return classifier.evaluate(sampleFitEvalSet());
	}
	
	public void setDataSetPartitions(float tSetFrac, float fitSetFrac){
		this.fitSetFrac = fitSetFrac;
		trainingSet = new HashMap<Integer, Pattern>();
		evaluationSet = new HashMap<Integer, Pattern>();		
		DataSet dataSet = classifier.getEncoderDataSet();
		
		for(IrisClass _class: IrisClass.values()){		
			Map<Integer, Pattern> patternSetAll = ((IrisDataset)dataSet).getPatternSetByClass(_class);	
			Map<Integer, Pattern> patternSetSub = ((IrisDataset)dataSet).samplePatternSetByClass(_class, tSetFrac);		
			Map<Integer, Pattern> patternSetExcl = dataSet.getExclusive(patternSetAll, patternSetSub);		
			trainingSet.putAll(patternSetSub);
			evaluationSet.putAll(patternSetExcl);
		}
		trainingSetByClass = ((IrisDataset)dataSet).setPatternSetByClass(trainingSet);
	}
	
	public Map<Integer, Pattern> getTrainingSet(){
		return this.trainingSet;
	}
	public Map<Integer, Pattern> sampleFitEvalSet(){
		DataSet dataSet = classifier.getEncoderDataSet();
		Map<Integer, Pattern> fitEvalSet = new HashMap<Integer, Pattern>();
		
		for(int i=0; i<IrisClass.values().length;i++)
			fitEvalSet.putAll(dataSet.samplePatternSet(trainingSetByClass.get(i), fitSetFrac));
		
		return fitEvalSet;
	}
	public Map<Integer, Pattern> getEvaluationSet(){
		return this.evaluationSet;
	}
}
