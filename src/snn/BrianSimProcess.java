package snn;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class BrianSimProcess {
	
	private static final int Py_OP_SpikeTime_idx = 2;
	
	private ArrayList<String> outputFromBrian;	
	private String pyModule;
	SNN snn;
	
	public BrianSimProcess(String pyModule, SNN snn) {
		this.pyModule = pyModule;
		outputFromBrian = new ArrayList<>();
		this.snn = snn;
	}
	public void runBrianSimSNN(){
		
		List<String> command = new ArrayList<String>();
		command.add("python");
		command.add(pyModule);		
		
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
		finalizeSNN();
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
	
	public void finalizeSNN(){
		int outputLayer = snn.nNeurons.length-1;
		SpikeTimes[] neuronSpikeTimes = new SpikeTimes[snn.nNeurons[outputLayer]];
		String[] olST = getOutputLayerSpikeTimesString();		
		for(int i=0;i<neuronSpikeTimes.length;i++) {
			neuronSpikeTimes[i] = new SpikeTimes(olST[i]);
		}				
		snn.layers[outputLayer].setNeuronSpikeTimes(neuronSpikeTimes );
	}
	
	public static void main(String[] args) {
		String pyModule = "C:\\Anaconda\\Lib\\site-packages\\brian\\snnClassifier\\snn.py";
		//String pyModuleTest = "C:\\Anaconda\\Lib\\site-packages\\brian\\aSamples\\SimulateSNN.py";
		int[] nNeurons = new int[] {7, 4, 4};		
		SNN snn = new SNN(nNeurons);
		
		BrianSimProcess bSimProcess = new BrianSimProcess(pyModule, snn);
		bSimProcess.runBrianSimSNN();
		//bSimProcess.displayBrianOutput();
		
		
		int outputLayer = snn.nNeurons.length-1;
		snn.layers[outputLayer].displaySpikeTimes();
	}

}
