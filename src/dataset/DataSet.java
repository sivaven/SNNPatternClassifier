package dataset;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Random;

public class DataSet {
	String filePath = null;
	private Map<Integer, Pattern> patternSet;
	protected ArrayList<Map<Integer, Pattern>> patternSetByClass;
	private int nAttr;
	private float[] patternAttrMin;
	private float[] patternAttrMax;
	
	public DataSet(String filePath) {
		this.filePath = filePath;
		readDataSet();
		patternSetByClass = setPatternSetByClass();
	}
	private void  readDataSet() {
		patternSet = new HashMap<Integer, Pattern>();		
		try {
			BufferedReader br = new BufferedReader(new FileReader(filePath));
			String str = null;
			int idx = 0;
			while(true){
				str = br.readLine();				
				if(str!=null) {
					patternSet.put(idx, constructPattern(str));
					idx+=1;
				}else{
					break;
				}
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		nAttr = patternSet.get(0).getAttributes().size();
		setMinMaxPatternAttributes();
	}
	
	private void setMinMaxPatternAttributes(){
		patternAttrMin = new float[nAttr];
		patternAttrMax = new float[patternAttrMin.length];
		for(int i=0;i<patternAttrMin.length;i++){
			patternAttrMin[i] = Float.MAX_VALUE;
			patternAttrMax[i] = -Float.MAX_VALUE;
        }
		Iterator it = this.patternSet.entrySet().iterator();
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        Pattern pattern = (Pattern) pairs.getValue();
	        for(int i=0;i<patternAttrMin.length;i++){
	        	if(pattern.getAttributes().get(i) < patternAttrMin[i])
	        		patternAttrMin[i] = pattern.getAttributes().get(i);
	        	if(pattern.getAttributes().get(i) > patternAttrMax[i])
	        		patternAttrMax[i] = pattern.getAttributes().get(i);
	        }
		}	
	}
	/*
	 * must override
	 */
	protected Pattern constructPattern(String patternString) {
		return null;
	}
	
	protected ArrayList<Map<Integer, Pattern>> setPatternSetByClass() {
		return null;
	}
	
	protected ArrayList<Map<Integer, Pattern>> setPatternSetByClass(Map<Integer, Pattern> patternSet) {
		return null;
	}
	/*
	 * 
	 */
	public void displayDataSet() {
		Iterator it = this.patternSet.entrySet().iterator();
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        Integer key = (Integer) pairs.getKey();
	        Pattern pattern = (Pattern) pairs.getValue();
	        pattern.displayPattern();
		}		
	}
	public void displayDataSet(Map<Integer, Pattern> patternSet) {
		Iterator it = patternSet.entrySet().iterator();
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        Integer key = (Integer) pairs.getKey();
	        Pattern pattern = (Pattern) pairs.getValue();
	        System.out.print(key+"\t");
	        pattern.displayPattern();
		}
	}
	
	public Map<Integer, Pattern> getPatternSetByClass(int classIdx) {
		return patternSetByClass.get(classIdx);
	}	
	
	public Map<Integer, Pattern> getPatternSetByClass(Map<Integer, Pattern> patternSet, int classIdx) {
		return patternSetByClass.get(classIdx);
	}
	
	public Map<Integer, Pattern> samplePatternSetByClass(int classIdx, float fraction) {
		Map<Integer, Pattern> allPatternSetByClass = getPatternSetByClass(classIdx);
		
		Map<Integer, Pattern> samplePatternSetByClass = new HashMap<>();		
		int nSamples = (int) (allPatternSetByClass.size() * fraction);
		
		int count=0;
		Random random = new Random();
		Object[] keySet = allPatternSetByClass.keySet().toArray();

		while(count < nSamples){			
			int keyIdx = random.nextInt(keySet.length);
			Integer key = (Integer)keySet[keyIdx];
			if(!samplePatternSetByClass.containsKey(key)) {	
				Pattern value = allPatternSetByClass.get(key);			
				samplePatternSetByClass.put(key, value);
				count++;		
			}
		}			
		return samplePatternSetByClass;
	}
	
	public Map<Integer, Pattern> samplePatternSet(Map<Integer, Pattern> patternSet, float fraction) {			
		Map<Integer, Pattern> samplePatternSet = new HashMap<>();		
		int nSamples = (int) (patternSet.size() * fraction);
		
		int count=0;
		Random random = new Random();
		Object[] keySet = patternSet.keySet().toArray();

		while(count < nSamples){			
			int keyIdx = random.nextInt(keySet.length);
			Integer key = (Integer)keySet[keyIdx];
			if(!samplePatternSet.containsKey(key)) {	
				Pattern value = patternSet.get(key);			
				samplePatternSet.put(key, value);
				count++;		
			}
		}			
		return samplePatternSet;
	}
	
	public Map<Integer, Pattern> getExclusive(Map<Integer, Pattern> patternSetAll, Map<Integer, Pattern> patternSetSub) {
		Map<Integer, Pattern> patternSetExcl = new HashMap<>();		
		Iterator it = patternSetAll.entrySet().iterator();
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        Integer key = (Integer) pairs.getKey();
	        if(!patternSetSub.containsKey(key)){
	        	patternSetExcl.put(key, (Pattern)pairs.getValue());
	        }
		}	
		return patternSetExcl;
	}
	public float[] getPatternAttrMin(){
		return this.patternAttrMin;
	}
	public float[] getPatternAttrMax(){
		return this.patternAttrMax;
	}
	public int getnAttr() {
		return nAttr;
	}	
	public Map<Integer, Pattern> getPatternSet(){
		return this.patternSet;
	}
}
