package ecj;

import code.Decoder;
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
	        SnnParameters snnParms = new SnnParameters(ind2.genome);
	        
	        /*
	         * first setup decoder from genes
	         */	     
			float bin  = 1;
			Decoder decoder = new Decoder(snnParms.getPopRateThresh(), bin, snnParms.getClassTimesToThresh());	       
	        Classifier cl = new Classifier(ECJStarter.encoder, decoder);		        
	        cl.evalStatDetailDisplay =false;
	       // cl.setDebug(true);
	        /*
	         * then setup snn parmaeters
	         */
			cl.setSNN(snnParms.constructSnn());
	        
			
	        fitness = cl.doStdpThenevaluate(ECJStarter.dataSetManager.getSampleEvaluationSet(ECJStarter.sampleEvalSetFrac));
	       
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
