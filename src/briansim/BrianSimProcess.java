package briansim;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

import dataset.DataSet;
import dataset.IrisDataset;
import encode.Encoder;
import snn.SNN;
import snn.SpikeTimes;
import snn.constants.LayerLabel;

public class BrianSimProcess {
		
	private static final int Py_OP_SpikeTime_idx = 2;	
	private ArrayList<String> outputFromBrian;	
	SNN snn;
	
	private boolean debug = false;
	
	private static AtomicLong ID_COUNTER = new AtomicLong();

	public static String createID()
	{
	    return String.valueOf(ID_COUNTER.getAndIncrement());
	}
	
	public BrianSimProcess(SNN snn) {
		outputFromBrian = new ArrayList<>();
		this.snn = snn;
	}
	
	public void runBrianSimSNNArch1(boolean plot){		
		int[] nwArch = snn.getArch();
		float[][] ipLW = snn.getLayer(LayerLabel.INPUT).getWeightsToNextLayer();
		float[][] hLW = snn.getLayer(LayerLabel.HIDDEN).getWeightsToNextLayer();		
		SpikeTimes[] spikeTimes = snn.getLayer(LayerLabel.INPUT).getNeuronSpikeTimes();		
		
		String moduleName = buildPythonModule("1.0", nwArch, ipLW, hLW,  spikeTimes, plot);
		runBrianSimSNN(moduleName);
	}
	
	public void runBrianSimSNNArch1(){		
		int[] nwArch = snn.getArch();
		float[][] ipLW = snn.getLayer(LayerLabel.INPUT).getWeightsToNextLayer();
		float[][] hLW = snn.getLayer(LayerLabel.HIDDEN).getWeightsToNextLayer();		
		SpikeTimes[] spikeTimes = snn.getLayer(LayerLabel.INPUT).getNeuronSpikeTimes();		
		
		String moduleName = buildPythonModule("1.0", nwArch, ipLW, hLW,  spikeTimes, false);
		runBrianSimSNN(moduleName);
	}
	
	public void runBrianSimSNNArch2(){					
		SpikeTimes[] spikeTimes = snn.getLayer(LayerLabel.INPUT).getNeuronSpikeTimes();			
		String moduleName = buildPythonModule("1.0", snn.getArch(), snn.getConnProb(), snn.getConnWeight(),  spikeTimes, false);
		runBrianSimSNN(moduleName);
	}
	
	public void runBrianSimSNN(String moduleName){
		
		List<String> command = new ArrayList<String>();
		command.add("python");
		command.add(moduleName);		
		
		//initializeFromSNN(command);
		
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
			//new File(moduleName).delete();
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
		int outputLayer = snn.getArch().length-1;
		SpikeTimes[] neuronSpikeTimes = new SpikeTimes[snn.getArch()[outputLayer]];
		String[] olST = getOutputLayerSpikeTimesString();		
		for(int i=0;i<neuronSpikeTimes.length;i++) {
			neuronSpikeTimes[i] = new SpikeTimes(olST[i]);
		}				
		snn.getLayer(LayerLabel.OUTPUT).setNeuronSpikeTimes(neuronSpikeTimes );
	}
	
	private String buildPythonModule(String dt,
			int[] nwArch, float[][] ipLW, float[][] hLW,
			SpikeTimes[] spikeTimes,
			boolean doPlot){	
		
		String fileName = createID() +".py";		
		BriansimPythonBuilder builder = new BriansimPythonBuilder(fileName);
		builder.build(dt, nwArch, ipLW, hLW, spikeTimes, doPlot);		
		return fileName;
	}
	
	private String buildPythonModule(String dt,
			int[] nwArch, float[] connProb, float[] connWeights,
			SpikeTimes[] spikeTimes,
			boolean doPlot){	
		
		String fileName = createID() +".py";		
		BriansimPythonBuilder builder = new BriansimPythonBuilder(fileName);
		builder.build(dt, nwArch, connProb, connWeights, spikeTimes, doPlot);		
		return fileName;
	}
	public static void main(String[] args) {
		int[] arch = new int[]{32,800,200,3};		
		float[] cProb = new float[] {0.8f, 0.2f, 0.05f, 0.02f, 0.01f, 0.01f, 0.01f };
		float[] cW = new float[] {2, 2, 2, 2, 2, 2, 2};
		
		SNN snn = new SNN(arch, cProb, cW);
		
		DataSet dataSet = new IrisDataset();		
		Encoder encoder = new Encoder(dataSet, 8);	
		SpikeTimes[] times = encoder.encode(dataSet.getPatternSet().get(0).getAttributes());				
		snn.setInputLayerSpikeTimes(times );
		
		BrianSimProcess bsm = new BrianSimProcess(snn);		
		
		SpikeTimes[] spikeTimes = snn.getLayer(LayerLabel.INPUT).getNeuronSpikeTimes();		
		
		bsm.runBrianSimSNNArch2();
		System.out.println(bsm.outputFromBrian);
	}

	
	public boolean isDebug() {
		return debug;
	}

	public void setDebug(boolean debug) {
		this.debug = debug;
	}
}
