package utils;

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
}
