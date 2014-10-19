package ecj;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import dataset.classes.IrisClass;

public class DataSetManager {
	
	public DataSet dataSet;
	private Map<Integer, Pattern> trainingSet;
	private Map<Integer, Pattern> evaluationSet;
	ArrayList<Map<Integer, Pattern>> trainingSetByClass;
	private float fitSetFrac;
	
	public DataSetManager(DataSet dataSet){
		this.dataSet = dataSet;
	}
		
	public void setDataSetPartitions(float tSetFrac, float fitSetFrac){
		this.fitSetFrac = fitSetFrac;
		trainingSet = new HashMap<Integer, Pattern>();
		evaluationSet = new HashMap<Integer, Pattern>();
		
		for(IrisClass _class: IrisClass.values()){		
			Map<Integer, Pattern> patternSetAll = ((IrisDataset)dataSet).getPatternSetByClass(_class);	
			Map<Integer, Pattern> patternSetSub = ((IrisDataset)dataSet).samplePatternSetByClass(_class, tSetFrac);		
			Map<Integer, Pattern> patternSetExcl = (dataSet).getExclusive(patternSetAll, patternSetSub);		
			trainingSet.putAll(patternSetSub);
			evaluationSet.putAll(patternSetExcl);
		}
		trainingSetByClass = ((IrisDataset)dataSet).setPatternSetByClass(trainingSet);
	}
	
	public Map<Integer, Pattern> getTrainingSet(){
		return this.trainingSet;
	}
	public Map<Integer, Pattern> sampleFitEvalSet(){
		Map<Integer, Pattern> fitEvalSet = new HashMap<Integer, Pattern>();
		
		for(int i=0; i<IrisClass.values().length;i++)
			fitEvalSet.putAll((dataSet).samplePatternSet(trainingSetByClass.get(i), fitSetFrac));
		
		return fitEvalSet;
	}
	public Map<Integer, Pattern> getEvaluationSet(){
		return this.evaluationSet;
	}
	public Map<Integer, Pattern> getSampleEvaluationSet(float frac){
		return dataSet.samplePatternSet(evaluationSet, frac);
	}
}
