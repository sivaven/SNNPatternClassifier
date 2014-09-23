package training;

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
	        
	        Classifier cl = new Classifier(ECJStarter.nNeurons, 
	    			ECJStarter.encoder);				
	        
	        //System.out.println(ind2.genomeLength());
	        cl.setWeights(ind2.genome);	
	       
	        
	        
	        cl.evalStatDetailDisplay =true;
	        
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
