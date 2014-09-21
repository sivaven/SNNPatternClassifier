package training;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import snn.SNN;
import dataset.DataSet;
import dataset.IrisDataset;
import ec.EvolutionState;
import ec.Evolve;
import ec.util.Output;
import ec.util.Parameter;
import ec.util.ParameterDatabase;
import encode.Encoder;

public class ECJStarter {
	public static  DataSetManager dataSetManager;
	public static Encoder encoder;
	public static int[] nNeurons = new int[] {32, 4, 3};
	
	public static void main(String[] args) {
		String parmsFile = "input/ecj.params";
		float tSetFrac = 0.1f;  //(.1, .4) => n=15, 6
		float fitSetFrac = 0.4f; 
				
		DataSet dataSet = new IrisDataset();
		dataSetManager = new DataSetManager(dataSet);		
		dataSetManager.setDataSetPartitions(tSetFrac, fitSetFrac);
		encoder = new Encoder(dataSet, 8);	
		
		try {	
			ParameterDatabase parameterDB = new ParameterDatabase(new File(parmsFile));			
			int nJobs = parameterDB.getInt(new Parameter("jobs"), new Parameter("jobs"));	
			parameterDB.set(new Parameter("pop.subpop.0.species.genome-size"), 
					""+(new SNN(nNeurons).getNWeights()));
			
			for(int i=0; i<nJobs; i++)				{
					Output output = Evolve.buildOutput();
					output.setFilePrefix("output/job."+i+".");
					final EvolutionState state = Evolve.initialize(parameterDB, i+1, output );	
					state.run(EvolutionState.C_STARTED_FRESH);
				}	    
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
	}
}


