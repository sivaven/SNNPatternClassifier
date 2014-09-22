package outputwriter;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class FileUtils {
	private static final String summaryFile = "output/summary.txt";
	private static final String evalStatFile = "output/evalStat.txt";
	
	private static FileWriter fw = null;
	private static FileWriter fw2 = null;
	static {
		try {
				fw = new FileWriter(new File(summaryFile));	
				fw2 = new FileWriter(new File(evalStatFile));	
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static void writeSummaryln(String str){		
		try {			
			fw.write(str+"\n");
			fw.flush();			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static void writeEvalStat(String str){		
		try {			
			fw2.write(str+",");
			fw2.flush();			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static void closeSummaryFile(){		
		try {
			fw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static void closeStatFile(){		
		try {
			fw2.close();			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static float readBestFitness(String fileName, int lineNo) {
		float fitness = Float.MAX_VALUE;
		try {
			BufferedReader br = new BufferedReader(new FileReader(fileName));
			String str = null;
			for(int i=0;i<lineNo;i++) {
				str = br.readLine();
			}
			StringTokenizer st = new StringTokenizer(str);
			String token = null;
			while(st.hasMoreTokens()) {
				token = st.nextToken();
				token = st.nextToken();
				fitness = Float.parseFloat(token);
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return fitness;
	}
	/*
	 * reads best solution from _full output of ECJ
	 */
	public static float[] readBestSolution(String fileName, int lineNo, int nParms) {
		float[] parms = new float[nParms];
		try {
			BufferedReader br = new BufferedReader(new FileReader(fileName));
			String str = null;
			for(int i=0;i<lineNo;i++) {
				str = br.readLine();
			}
			StringTokenizer st = new StringTokenizer(str);
			String token = null;
			int i=0;
			while(st.hasMoreTokens()) {
				token = st.nextToken();
				parms[i++] = Float.parseFloat(token);
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return parms;
	}
	
	public static void main(String[] args) {
		FileUtils.writeSummaryln("12");		
		FileUtils.closeSummaryFile();
		FileUtils.writeSummaryln("1200");
	}
	
}
