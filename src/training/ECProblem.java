package training;

import snn.SNN;
import classifier.Classifier;
import ec.EvolutionState;
import ec.Individual;
import ec.Problem;
import ec.simple.SimpleFitness;
import ec.simple.SimpleProblemForm;
import ec.vector.FloatVectorIndividual;

public class ECProblem extends Problem implements SimpleProblemForm{
	
	@Override
	public void evaluate(final EvolutionState state,
	        final Individual ind,
	        final int subpopulation,
	        final int threadnum)
	        {
		
	        if (ind.evaluated) return;	       
	        if (!(ind instanceof FloatVectorIndividual))
	            state.output.fatal("Whoa!  It's not a FloatVectorIndividual!!!",null);	         
	       
	        float fitness = 0;
	        FloatVectorIndividual ind2 = (FloatVectorIndividual)ind; 
	        EAGenes genes = new EAGenes(ind2.genome);
	        
	        Classifier cl = new Classifier(ECJStarter.encoder);		        
	        cl.evalStatDetailDisplay =false;
	       // cl.setDebug(true);
	        /*
	         * 
	         */
	        int hiddenN = (int) genes.getGene(0);
	        int[] arch = new int[]{32,hiddenN,hiddenN/4,3};		        
			float[] cProb = genes.getGenes(1, 7);
			float[] cW = genes.getGenes(8, 7);
			SNN snn = new SNN(arch, cProb, cW);
			cl.setSNN(snn);
	        /*
	         * 
	         */
	        fitness = cl.evaluate(ECJStarter.dataSetManager.sampleFitEvalSet());
	       
	       // System.out.println("evaluate");
	        
	        if (!(ind2.fitness instanceof SimpleFitness))
	            state.output.fatal("Whoa!  It's not a SimpleFitness!!!",null);
	        ((SimpleFitness)ind2.fitness).setFitness(state,
	            /// ...the fitness...
	            fitness,
	            ///... is the individual ideal?  Indicate here...
	            fitness == 1);
	        ind2.evaluated = true;	        
	}

}
