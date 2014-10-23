package utils;

import java.util.ArrayList;
import java.util.StringTokenizer;

public class Utils {
	public static void displayArray(float[] array){
		for(float f: array)
			System.out.print(f+"\t");
		System.out.println();
	}
	public static String convertToString(float[] array){
		String str = "";
		for(float f: array)
			str+=f;
		return str;
	}
	public static boolean isCloseEnough(float val1, float val2, float threshold){
		if(Math.abs(val2-val1) <= threshold)
			return true;
		else
			return false;
	}
	public static ArrayList<Float> getFloatedList(String stringList) {
		ArrayList<Float> floatedList = new ArrayList<>();		
		StringTokenizer st = new StringTokenizer(stringList, " ");
		String token = null;		
		while(st.hasMoreTokens()) {
			token = st.nextToken();
			floatedList.add(Float.parseFloat(token));
		}
		return floatedList;
	}
}
