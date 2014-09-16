package dataset;

import java.util.StringTokenizer;

import dataset.classes.IrisClass;

public class IrisDataset extends DataSet{
	private static final String FILE_PATH = "input/iris.data";
	private static final int CLASS_ATTR_IDX = 4;
	
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
			if(tknCnt!=CLASS_ATTR_IDX) {
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
	
}
