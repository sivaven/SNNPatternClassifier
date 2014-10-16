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

import dataset.Pattern;
import snn.SpikeTimes;

public class BrianSimOutput {
	private static final String ITEM_DELIM = "$";
	private static final String LABEL_DELIM = ":";
	private static final String LINE_DELIM = ",";
	
	private String outputFromBrian;
	private Map<BrianOutputLabel, Object> items;
	
	public BrianSimOutput() {
		outputFromBrian = "";
	}
	public void addOutputLn(String outputLn){
		outputFromBrian += outputLn;
	}
	public void processOutput(){
		items = new HashMap<>();		
		StringTokenizer st = new StringTokenizer(outputFromBrian, ITEM_DELIM);
		while(st.hasMoreTokens()) {
			String item = st.nextToken();
			mapItem(item);
		}		
	}
	private void mapItem(String item){
		StringTokenizer st = new StringTokenizer(item, LABEL_DELIM);
		String label = st.nextToken();
		String value = st.nextToken();
		
		if(BrianOutputLabel.sim_time.toString().equals(label)){
			items.put(BrianOutputLabel.sim_time, value);			
		}
		if(BrianOutputLabel.op_layer_spike_times.toString().equals(label)){
			mapOpLayerSpikeTimes(value);			
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
		Iterator it = items.entrySet().iterator();
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        BrianOutputLabel key = (BrianOutputLabel) pairs.getKey();
	        Object object = pairs.getValue();
	        if(BrianOutputLabel.op_layer_spike_times.equals(key)){
	        	displayOpLayerSpikeTimes(object);
	        }
	        if(BrianOutputLabel.sim_time.equals(key)){
	        	displaySimTime(object);
	        }
		}		
	}
	
	private void displaySimTime(Object object) {
		System.out.println("SimTime.\t"+object);
	}
	
	private void displayOpLayerSpikeTimes(Object object) {
		ArrayList<SpikeTimes> spikeTimesList = (ArrayList<SpikeTimes>)object;
		for(SpikeTimes spikeTimes: spikeTimesList){
			spikeTimes.display();
			System.out.println();
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
	sim_time, op_layer_spike_times, conn_weight_matrix
}