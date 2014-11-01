package briansim;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.concurrent.atomic.AtomicLong;

import snn.SNN;
import snn.SpikeTimes;
import snn.constants.LayerLabel;

public class BrianSimProcess {
	private static final String FF_PATTERN_DELIM = "#";	
	Map<Integer, BrianSimOutput> brianPatternKeyOutputMap;
	
	private boolean debug = false;
	private boolean processDebug = false;
	
	private static AtomicLong ID_COUNTER = new AtomicLong();

	public static String createID()	{
	    return String.valueOf(ID_COUNTER.getAndIncrement());
	}
	public BrianSimProcess(){
		this(false);
	}
	public BrianSimProcess(boolean debug) {
		brianPatternKeyOutputMap = new HashMap<Integer, BrianSimOutput>();
		this.debug = debug;
	}
	
	public void runBrianSimSNN(String moduleName, boolean deleteModuleAfterRun){
		
		List<String> command = new ArrayList<String>();
		command.add("python");
		command.add(moduleName);		
		
		String brianOutputAsString = "";
		if(debug) System.out.println(command);
			
		ProcessBuilder pb = new ProcessBuilder(command);//"python", pyModule );
		try {
			Process p = pb.start();	
			if(processDebug){
				System.out.println("Process exit value: "+p.exitValue());
				BufferedReader in = new BufferedReader(new InputStreamReader(p.getErrorStream()));
				System.out.println("ErrorStream.\t"+in.readLine());			
			}			
			BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));	
			int idx = 0;
			while(true){
				String retVal = in.readLine();				
				if(retVal!=null) {
					brianOutputAsString+=retVal;	
				}else{
					break;
				}	
			}
			if(deleteModuleAfterRun)
				new File(moduleName).delete();
		} catch (IOException e) {
			e.printStackTrace();
		}	
		processOutput(brianOutputAsString);
	}

	private void processOutput(String brianOutputAsString) {
		StringTokenizer st = new StringTokenizer(brianOutputAsString, FF_PATTERN_DELIM);
		while(st.hasMoreTokens()){
			BrianSimOutput brianOutput = new BrianSimOutput(st.nextToken());			
			brianPatternKeyOutputMap.put(brianOutput.processOutput(), brianOutput);
		}		
	}

	public void displayBrianOutput() {
		Iterator it = brianPatternKeyOutputMap.entrySet().iterator();
		while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        ((BrianSimOutput)pairs.getValue()).displayItems();
		}
	}
	
	public String buildPythonModule(Map<BrianSimParameterLabel, Object> parms){
		return buildPythonModule(parms, false);
	}
	public String buildPythonModule(Map<BrianSimParameterLabel, Object> parms,
			boolean doPlot){		
		String fileName = createID() +".py";		
		BriansimPythonBuilder builder = new BriansimPythonBuilder(fileName, parms, doPlot);
		builder.build();
		return fileName;
	}

	public ArrayList<SpikeTimes> getOutputLayerSpikeTimesForPattern(Integer patternKey) {
		if(!brianPatternKeyOutputMap.containsKey(patternKey)){
			System.out.println("<getOutputLayerSpikeTimesForPattern> \tPattern key not returned from brianSim.\t"+patternKey);
			System.exit(-1);
		}
		return (ArrayList<SpikeTimes>) brianPatternKeyOutputMap.get(patternKey).getItems().get(BrianOutputLabel.op_layer_spike_times);
	}
	
	public ArrayList<Float> getOutputLayerPopRatesForPattern(Integer patternKey) {
		if(!brianPatternKeyOutputMap.containsKey(patternKey)){
			System.out.println("<getOutputLayerPopRatesForPattern> \tPattern key not returned from brianSim.\t"+patternKey);
			displayBrianOutput();
			System.exit(-1);
		}
		return (ArrayList<Float>) brianPatternKeyOutputMap.get(patternKey).getItems().get(BrianOutputLabel.op_layer_pop_rates);
	}
	
	public boolean isProcessDebug() {
		return processDebug;
	}

	public void setProcessDebug(boolean processDebug) {
		this.processDebug = processDebug;
	}
	
}
