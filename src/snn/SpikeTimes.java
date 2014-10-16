package snn;

import java.util.ArrayList;
import java.util.StringTokenizer;

/*
 * Neuron level info: currently only spike times
 */
public class SpikeTimes {
	private static final char[] STOP_CHARS = {'[',']'}; // if adding, update removeStopChars method!!
	
	ArrayList<Float> spikeTimes;
	
	public SpikeTimes(){
		spikeTimes = new ArrayList<>();
	}
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
	
	public void addSpikeTime(Float spikeTime){
		this.spikeTimes.add(spikeTime);
	}
	private String removeStopChars(String str){
		return str.replace(STOP_CHARS[0], ' ').replace(STOP_CHARS[1], ' ');		
	}
	public ArrayList<Float> getSpikeTimes() {
		return this.spikeTimes;
	}
	public void display(){
		/*for(int i=0;i<spikeTimes.size();i++){
			if(i==0) System.out.print("[");
			System.out.print(Math.round(spikeTimes.get(i).floatValue()));
			if(i!=spikeTimes.size()-1)
			System.out.print(",");
		}
		System.out.print("]\n");*/
		System.out.println(spikeTimes);
	}
}