package briansim;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.StringTokenizer;

import snn.SpikeTimes;
import utils.Utils;

public class BrianSimOutput {
	private static final String ITEM_DELIM = "$";
	private static final String LABEL_DELIM = ":";
	private static final String LINE_DELIM = ",";
	
	private String outputFromBrian;
	private Map<BrianOutputLabel, Object> items;
	
	public BrianSimOutput(String outputFromBrian) {
		this.outputFromBrian = outputFromBrian;
	}
	public BrianSimOutput() {
		outputFromBrian = "";
	}
	public void addOutputLn(String outputLn){
		outputFromBrian += outputLn;
	}
	public Integer processOutput(){
		Integer patternKey = null;
		items = new HashMap<>();		
		StringTokenizer st = new StringTokenizer(outputFromBrian, ITEM_DELIM);
		while(st.hasMoreTokens()) {
			String item = st.nextToken();
			mapItem(item);
		}
		patternKey = (Integer)items.get(BrianOutputLabel.ip_pattern_idx);
		return patternKey;
	}
	private void mapItem(String item){
		StringTokenizer st = new StringTokenizer(item, LABEL_DELIM);
		String label = st.nextToken();
		String value = st.nextToken();
		
		if(BrianOutputLabel.ip_pattern_idx.toString().equals(label)){
			items.put(BrianOutputLabel.ip_pattern_idx, Integer.valueOf(value.trim()));			
		}
		if(BrianOutputLabel.sim_time.toString().equals(label)){
			items.put(BrianOutputLabel.sim_time, value);			
		}
		if(BrianOutputLabel.op_layer_spike_times.toString().equals(label)){
			mapOpLayerSpikeTimes(value);			
		}
		if(BrianOutputLabel.op_layer_pop_rates.toString().equals(label)){
			items.put(BrianOutputLabel.op_layer_pop_rates, Utils.getFloatedList(value));	
		}
	}
	private void mapOpLayerSpikeTimes(String values){
		StringTokenizer st = new StringTokenizer(values, LINE_DELIM);
		ArrayList<SpikeTimes> spikeTimesList = new ArrayList<>();		
		while(st.hasMoreTokens()) {
			String item = st.nextToken();
			spikeTimesList.add(new SpikeTimes(item));
		}
		items.put(BrianOutputLabel.op_layer_spike_times, spikeTimesList);
	}
	
	
	
	public void displayItems(){
		System.out.println("***Output From BrianSim***");
		Iterator it = items.entrySet().iterator();
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        BrianOutputLabel key = (BrianOutputLabel) pairs.getKey();
	        Object object = pairs.getValue();
	        if(BrianOutputLabel.op_layer_spike_times.equals(key)){
	        	displayOpLayerSpikeTimes(object);
	        }else{
	        	displayString(key.name(), object);
	        }	        
		}
		System.out.println("*************************");
	}
	
	public Map<BrianOutputLabel, Object> getItems(){
		return this.items;
	}
	private void displayString(String itemLabel, Object item) {
		System.out.println(itemLabel+".\t"+item);
	}
	
	private void displayOpLayerSpikeTimes(Object object) {
		ArrayList<SpikeTimes> spikeTimesList = (ArrayList<SpikeTimes>)object;
		System.out.println(BrianOutputLabel.op_layer_spike_times+".");
		for(SpikeTimes spikeTimes: spikeTimesList){
			spikeTimes.display();
		}		
	}
	public static void main(String[] args) {		
		BrianSimOutput output = new BrianSimOutput();
		
		File file = new File("temp.txt");
		FileInputStream fis;
		try {
			fis = new FileInputStream(file);					
			BufferedReader in = new BufferedReader(new InputStreamReader(fis));	
			int idx = 0;
			while(true){
				String retVal = in.readLine();				
				if(retVal!=null) {
					output.addOutputLn(retVal);	
				}else{
					break;
				}	
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		catch (IOException e) {
			e.printStackTrace();
		}
	
		output.processOutput();
		output.displayItems();

	}

}

enum BrianOutputLabel {
	sim_time, op_layer_spike_times, ip_pattern_idx, op_layer_pop_rates
}