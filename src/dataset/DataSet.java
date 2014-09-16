package dataset;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class DataSet {
	String filePath = null;
	ArrayList<Pattern> patternSet;
	public DataSet(String filePath) {
		this.filePath = filePath;
		readDataSet();
	}
	private void  readDataSet() {
		patternSet = new ArrayList<>();		
		try {
			BufferedReader br = new BufferedReader(new FileReader(filePath));
			String str = null;
			while(true){
				str = br.readLine();				
				if(str!=null) {
					patternSet.add(constructPattern(str));
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
	
	public void displayDataSet() {
		for(Pattern pattern: patternSet)
			pattern.displayPattern();
	}

}
