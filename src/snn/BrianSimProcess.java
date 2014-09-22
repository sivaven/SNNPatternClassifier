package snn;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import snn.constants.LayerLabel;

public class BrianSimProcess {
	
	//public static final String PY_Module = "C:\\Anaconda\\Lib\\site-packages\\brian\\snnClassifier\\snn.py";
	public static final String PY_Module = "snn.py";
	private static final int Py_OP_SpikeTime_idx = 2;
	
	private ArrayList<String> outputFromBrian;	
	private String pyModule;
	SNN snn;
	
	private boolean debug = false;
	
	public BrianSimProcess(SNN snn) {
		this.pyModule = PY_Module;
		outputFromBrian = new ArrayList<>();
		this.snn = snn;
	}
	
	public BrianSimProcess(String pyModule, SNN snn) {
		this.pyModule = pyModule;
		outputFromBrian = new ArrayList<>();
		this.snn = snn;
	}
	
	private void initializeFromSNN(List<String> command) {
		//set layer/Neuron
		for(int n:snn.nNeurons){
			command.add(""+n);
		}			
		//set conn weights
		for(Layer layer:snn.layers){
			if(!layer.getLabel().equals(LayerLabel.OUTPUT)){
				float[][] weights = layer.getWeightsToNextLayer();
				for(float[] weight: weights)
					for(float w: weight)
						command.add(""+w);				
			}
		}
		// set ip layer spike times
		//first, set nspikeTimes for each ip neuron
		SpikeTimes[] neuronSpikeTimes = snn.getLayer(LayerLabel.INPUT).getNeuronSpikeTimes();
		for(int i=0;i<snn.nNeurons[0];i++){
			command.add(""+neuronSpikeTimes[i].spikeTimes.size());
		}
		//next, add spike times:
		for(SpikeTimes spikeTimes: neuronSpikeTimes) {
			for(float st: spikeTimes.spikeTimes)
				command.add(""+st);
		}
	}
	public void runBrianSimSNN(){
		
		List<String> command = new ArrayList<String>();
		command.add("python");
		command.add(pyModule);		
		
		initializeFromSNN(command);
		
		if(debug) System.out.println(command);
			
		ProcessBuilder pb = new ProcessBuilder(command);//"python", pyModule );
		try {
			Process p = pb.start();	
			//p.destroy();
			//System.out.println("Process exit value: "+p.exitValue());
			//BufferedReader in = new BufferedReader(new InputStreamReader(p.getErrorStream()));
			//System.out.println(in.readLine());			
			BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));	
			int idx = 0;
			while(true){
				String retVal = in.readLine();				
				if(retVal!=null) {
					outputFromBrian.add(retVal);	
				}else{
					break;
				}	
			}
		} catch (IOException e) {
			e.printStackTrace();
		}	
		if(!debug)
		finalizeToSNN();
	}
	
	public void displayBrianOutput() {
		System.out.println("BrianSim Output****");
		for(String str: outputFromBrian) 
			System.out.println(str);
		System.out.println("*******");
	}
	
	private String[] getOutputLayerSpikeTimesString(){
		String[] olST = new String[outputFromBrian.size() - Py_OP_SpikeTime_idx];
		for(int i=0; i<olST.length; i++) {
			olST[i] = outputFromBrian.get(i + Py_OP_SpikeTime_idx);
		}
		return olST;		
	}
	
	private void finalizeToSNN(){
		int outputLayer = snn.nNeurons.length-1;
		SpikeTimes[] neuronSpikeTimes = new SpikeTimes[snn.nNeurons[outputLayer]];
		String[] olST = getOutputLayerSpikeTimesString();		
		for(int i=0;i<neuronSpikeTimes.length;i++) {
			neuronSpikeTimes[i] = new SpikeTimes(olST[i]);
		}				
		snn.getLayer(LayerLabel.OUTPUT).setNeuronSpikeTimes(neuronSpikeTimes );
	}
	
	public static void main(String[] args) {
		
		//String pyModuleTest = "C:\\Anaconda\\Lib\\site-packages\\brian\\aSamples\\SimulateSNN.py";
		
		//snn.getLayer(LayerLabel.OUTPUT).displaySpikeTimes();
	}

	
	public boolean isDebug() {
		return debug;
	}

	public void setDebug(boolean debug) {
		this.debug = debug;
	}
}
