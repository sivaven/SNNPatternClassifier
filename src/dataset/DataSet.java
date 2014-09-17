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
import java.util.Set;

public class DataSet {
	String filePath = null;
	Map<Integer, Pattern> patternSet;
	protected ArrayList<Map<Integer, Pattern>> patternSetByClass;
	
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
	
	Map<Integer, Pattern> getPatternSetByClass(int classIdx) {
		return patternSetByClass.get(classIdx);
	}	
	
	Map<Integer, Pattern> samplePatternSetByClass(int classIdx, float fraction) {
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
		System.out.println(samplePatternSetByClass.size());
		return samplePatternSetByClass;
	}
}
