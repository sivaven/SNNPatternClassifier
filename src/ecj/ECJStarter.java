package ecj;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Map;

import code.Decoder;
import code.Encoder;
import classifier.Classifier;
import outputwriter.FileUtils;
import snn.SNN;
import snn.SpikeTimes;
import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import ec.EvolutionState;
import ec.Evolve;
import ec.util.Output;
import ec.util.Parameter;
import ec.util.ParameterDatabase;

public class ECJStarter {
	private static float tSetFrac = 0.5f;  //(.1, .4) => n=15, 6
	private static float fitSetFrac = 0.0f; // of tSet
	public static float sampleEvalSetFrac = 1.0f; // of evalSet
	
	public static  DataSetManager dataSetManager;
	public static Encoder encoder;
	public static Decoder decoder;
	public static SpikeTimes[] stdpSpikeTimes;
	
	public static final float PATTERN_WINDOW = 20;
	public static final float FF_SIM_DUR = 50;
	//public static int[] nNeurons = new int[] {32, 15, 3};
	
	public static void init() {
		DataSet dataSet = new IrisDataset();		
		encoder = new Encoder(dataSet, 8);	
		
	/*	float popRateThresh = 150;
		float bin  = 1;
		float[] classSpikeTimes = new float[] {18, 19, 20};
		decoder = new Decoder(popRateThresh, bin, classSpikeTimes);
		*/
			
		dataSetManager = new DataSetManager(dataSet);
	}
	public static void resampleDataSets() {		
		dataSetManager.setDataSetPartitions(tSetFrac, fitSetFrac);
		Map<Integer, Pattern> tSet = dataSetManager.getTrainingSet();
		DataSet.shuffleMap(tSet);
		stdpSpikeTimes = encoder.encode(tSet, PATTERN_WINDOW);
	}
	
	public static void main(String[] args) {
		String parmsFile = "input/ecj3.params";	
		init();		
						
	//	FileUtils.writeSummaryln("tSetKeys:"+dataSetManager.getTrainingSet().keySet().toString());
	//	FileUtils.writeSummaryln("eSetKeys:"+dataSetManager.getEvaluationSet().keySet().toString());
		
		try {	
			ParameterDatabase parameterDB = new ParameterDatabase(new File(parmsFile));			
			int nJobs = parameterDB.getInt(new Parameter("jobs"), new Parameter("jobs"));	
			//parameterDB.set(new Parameter("pop.subpop.0.species.genome-size"), 
			//		""+(new SNN(nNeurons).getNWeights()));
			
			for(int i=0; i<nJobs; i++){
				resampleDataSets();
				Output output = Evolve.buildOutput();
				String filePrefix = "output/job."; 
				output.setFilePrefix(filePrefix+i+".");
				final EvolutionState state = Evolve.initialize(parameterDB, i+1, output );	
				state.run(EvolutionState.C_STARTED_FRESH);
/*				updateSummaryFile(	i, 
									filePrefix,
									parameterDB.getInt(new Parameter("pop.subpop.0.species.genome-size"), 
														new Parameter("pop.subpop.0.species.genome-size"))
								);*/
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
		Classifier cl = new Classifier(ECJStarter.encoder, null);	
		EAGenes genes = new EAGenes(bestSoln);
		
		int hiddenN = (int) genes.getGene(0);
        int[] arch = new int[]{32,hiddenN,hiddenN/4,3};		        
		float[] cProb = genes.getGenes(1, 7);
		float[] cW = genes.getGenes(8, 7);
		SNN snn = null;//new SNN(arch, cProb, cW);
		cl.setSNN(snn);
		
	    float tSetAcc = cl.evaluate(dataSetManager.getTrainingSet());
	    float eSetAcc = cl.evaluate(dataSetManager.getEvaluationSet());
	   
	    FileUtils.writeSummaryln(trial+" "+tSetAcc+" "+eSetAcc);
	}
}


