package snn;

import java.util.ArrayList;
import java.util.StringTokenizer;

/*
 * Neuron level info: currently only spike times
 */
public class SpikeTimes {
	private static final char[] STOP_CHARS = {'[',']'}; // if adding, update removeStopChars method!!
	
	ArrayList<Float> spikeTimes;
	
	public SpikeTimes(ArrayList<Float> spikeTimes){
		this.spikeTimes = spikeTimes;
	}
	
	public SpikeTimes(float[] spikeTimesArray){
		spikeTimes = new ArrayList<>();
		for(float t: spikeTimesArray)
			spikeTimes.add(t);
	}
	
	public SpikeTimes(String spikeTimesStringList) {
		spikeTimes = new ArrayList<>();
		spikeTimesStringList = removeStopChars(spikeTimesStringList);
		
		StringTokenizer st = new StringTokenizer(spikeTimesStringList, " ");
		String token = null;		
		while(st.hasMoreTokens()) {
			token = st.nextToken();
			spikeTimes.add(Float.parseFloat(token)*1000);
		}
	}
	private String removeStopChars(String str){
		return str.replace(STOP_CHARS[0], ' ').replace(STOP_CHARS[1], ' ');		
	}
	
	public void display(){
		System.out.println(spikeTimes);
	}
}