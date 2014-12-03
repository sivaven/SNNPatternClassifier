package utils;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Utils {
	public static float calculateMean(float[] numbers){
		 
        float sum = 0;
        for(float number : numbers) {
            sum = sum + number;
        }         
        return sum / numbers.length;
	}
	public static float calculateStdDev(float[] numbers){
		 
		List<Float> listOfDifferences = new ArrayList<Float>();
        float average = calculateMean(numbers);
        for(float number : numbers) {
        	float difference = number - average;
            listOfDifferences.add(difference);
        }
 
        List<Float> squares = new ArrayList<Float>();         
        for(float difference : listOfDifferences) {
        	float square = difference * difference;
            squares.add(square);
        }
        float sum = 0;        
        for(float number : squares) {
            sum = sum + number;
        }
        float result = sum / (numbers.length - 1);
       return (float) Math.sqrt(result);
	}
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
