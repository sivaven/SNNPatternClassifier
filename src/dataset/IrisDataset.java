package dataset;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.StringTokenizer;

import dataset.classes.IrisClass;

public class IrisDataset extends DataSet{
	private static final String FILE_PATH = "input/iris.data";
	private static final int N_ATTR = 4;
	private static final int N_CLASS = 3;
	public IrisDataset(){
		super(FILE_PATH);
	}
	public IrisDataset(String filePath) {
		super(filePath);
	}

	protected Pattern constructPattern(String patternString) {		
		Pattern pattern = new Pattern();
		StringTokenizer st = new StringTokenizer(patternString, ",");
		String token = null;
		int tknCnt=0;
		
		while(st.hasMoreTokens()) {
			token = st.nextToken();
			//System.out.println(token);
			if(tknCnt< N_ATTR) {
				pattern.addAttribute(Float.valueOf(token));		
			}else{
				token = token.replace('-', '_');
				IrisClass _class = IrisClass.valueOf(token);
				pattern.set_class(_class);
			}
			tknCnt++;
		}
		return pattern;
	}
	
	protected ArrayList<Map<Integer, Pattern>> setPatternSetByClass() {
		ArrayList<Map<Integer, Pattern>> patternSetByClass = new ArrayList<>();
		
		Map<Integer, Pattern> _class1 = new HashMap<>();
		Map<Integer, Pattern> _class2 = new HashMap<>();
		Map<Integer, Pattern> _class3 = new HashMap<>();
		
		Iterator it = this.getPatternSet().entrySet().iterator();
	    while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        Integer key = (Integer) pairs.getKey();
	        Pattern pattern = (Pattern) pairs.getValue();
	        
	        if(pattern.get_class().equals(IrisClass.Iris_setosa)){
	        	 _class1.put(key, pattern);
	        }
	        if(pattern.get_class().equals(IrisClass.Iris_versicolor)){
	        	 _class2.put(key, pattern);
	        }
	        if(pattern.get_class().equals(IrisClass.Iris_virginica)){
	        	 _class3.put(key, pattern);
	        }	       
	    }
	    patternSetByClass.add(_class1);
	    patternSetByClass.add(_class2);
	    patternSetByClass.add(_class3);
		
		return patternSetByClass;
	}
	
	public ArrayList<Map<Integer, Pattern>> setPatternSetByClass(Map<Integer, Pattern> patternSet) {
		ArrayList<Map<Integer, Pattern>> patternSetByClass = new ArrayList<>();
		
		Map<Integer, Pattern> _class1 = new HashMap<>();
		Map<Integer, Pattern> _class2 = new HashMap<>();
		Map<Integer, Pattern> _class3 = new HashMap<>();
		
		Iterator it = patternSet.entrySet().iterator();
	    while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        Integer key = (Integer) pairs.getKey();
	        Pattern pattern = (Pattern) pairs.getValue();
	        
	        if(pattern.get_class().equals(IrisClass.Iris_setosa)){
	        	 _class1.put(key, pattern);
	        }
	        if(pattern.get_class().equals(IrisClass.Iris_versicolor)){
	        	 _class2.put(key, pattern);
	        }
	        if(pattern.get_class().equals(IrisClass.Iris_virginica)){
	        	 _class3.put(key, pattern);
	        }	       
	    }
	    patternSetByClass.add(_class1);
	    patternSetByClass.add(_class2);
	    patternSetByClass.add(_class3);
		
		return patternSetByClass;
	}
	
	public Map<Integer, Pattern> getPatternSetByClass(IrisClass _class) {
		return patternSetByClass.get(_class.getNumericClass());
	}	
	
	public Map<Integer, Pattern> samplePatternSetByClass(IrisClass _class, float fraction) {
		return samplePatternSetByClass(_class.getNumericClass(), fraction);
	}
}
