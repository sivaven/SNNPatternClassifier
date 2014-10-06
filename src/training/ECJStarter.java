package training;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import classifier.Classifier;
import outputwriter.FileUtils;
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
	//public static int[] nNeurons = new int[] {32, 15, 3};
	
	public static void main(String[] args) {
		String parmsFile = "input/ecj2.params";
		float tSetFrac = 0.5f;  //(.1, .4) => n=15, 6
		float fitSetFrac = 0.6f; 
				
		DataSet dataSet = new IrisDataset();
		dataSetManager = new DataSetManager(dataSet);		
		dataSetManager.setDataSetPartitions(tSetFrac, fitSetFrac);
		encoder = new Encoder(dataSet, 8);	
						
		FileUtils.writeSummaryln("tSetKeys:"+dataSetManager.getTrainingSet().keySet().toString());
		FileUtils.writeSummaryln("eSetKeys:"+dataSetManager.getEvaluationSet().keySet().toString());
		
		try {	
			ParameterDatabase parameterDB = new ParameterDatabase(new File(parmsFile));			
			int nJobs = parameterDB.getInt(new Parameter("jobs"), new Parameter("jobs"));	
			//parameterDB.set(new Parameter("pop.subpop.0.species.genome-size"), 
			//		""+(new SNN(nNeurons).getNWeights()));
			
			for(int i=0; i<nJobs; i++)				{
					Output output = Evolve.buildOutput();
					String filePrefix = "output/job."; 
					output.setFilePrefix(filePrefix+i+".");
					final EvolutionState state = Evolve.initialize(parameterDB, i+1, output );	
					state.run(EvolutionState.C_STARTED_FRESH);
					updateSummaryFile(	i, 
										filePrefix,
										parameterDB.getInt(new Parameter("pop.subpop.0.species.genome-size"), 
															new Parameter("pop.subpop.0.species.genome-size"))
									);
				}	
			FileUtils.closeSummaryFile();
			FileUtils.closeStatFile();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
	}
	
	private static void updateSummaryFile(int trial, String ecOpFilePrefix,  int nParms) {
		float[] bestSoln = FileUtils.readBestSolution(ecOpFilePrefix+trial+".full", 6, nParms);		
		Classifier cl = new Classifier(ECJStarter.encoder);	
		EAGenes genes = new EAGenes(bestSoln);
		
		int hiddenN = (int) genes.getGene(0);
        int[] arch = new int[]{32,hiddenN,hiddenN/4,3};		        
		float[] cProb = genes.getGenes(1, 7);
		float[] cW = genes.getGenes(8, 7);
		SNN snn = new SNN(arch, cProb, cW);
		cl.setSNN(snn);
		
	    float tSetAcc = cl.evaluate(dataSetManager.getTrainingSet());
	    float eSetAcc = cl.evaluate(dataSetManager.getEvaluationSet());
	   
	    FileUtils.writeSummaryln(trial+" "+tSetAcc+" "+eSetAcc);
	}
}


