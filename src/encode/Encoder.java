package encode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.TreeMap;

import snn.SpikeTimes;
import training.plasticity.STDP;
import utils.Utils;
import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import ecj.DataSetManager;
import ecj.ECJStarter;

public class Encoder {

	DataSet dataSet;
	GaussianRF[][] rf;
	int nRFs;
	
	public Encoder(DataSet dataset, int nRFs, float beta){
		dataSet = dataset;
		this.nRFs = nRFs;
		rf = new GaussianRF[dataSet.getnAttr()][nRFs];
		float[] attrMin = dataSet.getPatternAttrMin();
		float[] attrMax = dataSet.getPatternAttrMax();
		
		for(int i=0;i<rf.length;i++)
			for(int m=0;m<nRFs;m++){
				float mu = attrMin[i] + (((2*m - 3)/2) * ((nRFs-2)/(attrMax[i] - attrMin[i])));						
				float sigma = (nRFs-2)/(beta * (attrMax[i] - attrMin[i]));
				rf[i][m] = new GaussianRF(mu, sigma);
			}
	}
	
	public Encoder(DataSet dataset, int nRFs){
		this(dataset, nRFs, 1.5f);
	}
	
	public SpikeTimes[] encode(ArrayList<Float> attributes){
		SpikeTimes[] ipLayerSpikeTimes = new SpikeTimes[attributes.size()*this.nRFs];		
		for(int i=0;i<attributes.size();i++){
			for(int j=0;j<this.nRFs;j++){
				SpikeTimes spikeTimes = new SpikeTimes();
				float spikeTime = getSpikeTimeFromRFCode( this.rf[i][j].phi(attributes.get(i)) );
				spikeTimes.addSpikeTime(spikeTime);
				ipLayerSpikeTimes[(i*this.nRFs)+j] = spikeTimes;
			}		
		}
		return ipLayerSpikeTimes;
	}
	 
	 
	 public SpikeTimes[] encode(Map<Integer, Pattern> patternSet, float timeInterval){	
		 SpikeTimes[] ipLayerSpikeTimes = new SpikeTimes[dataSet.getnAttr()*this.nRFs];		 
		 float timeOffset = 0;
		 Iterator it = patternSet.entrySet().iterator();
		 int patternCnt = 0;
		 while (it.hasNext()) {
	        Map.Entry pairs = (Map.Entry)it.next();
	        Pattern pattern = (Pattern) pairs.getValue();
	        for(int i=0;i<pattern.getAttributes().size();i++){
				for(int j=0;j<this.nRFs;j++){
					if(patternCnt==0) {
						ipLayerSpikeTimes[(i*this.nRFs)+j] = new SpikeTimes();
					}
					float spikeTime = getSpikeTimeFromRFCode( this.rf[i][j].phi(pattern.getAttributes().get(i)) );
					ipLayerSpikeTimes[(i*this.nRFs)+j].addSpikeTime(spikeTime+timeOffset);					
				}		
			} 
	        timeOffset += timeInterval;
	        patternCnt+=1;
	   //     System.out.println(patternCnt+"\t"+timeOffset);
		 }			
			
		return ipLayerSpikeTimes;
		}
	/*
	 * rfCode = 1 => spikeTime = 0 (no delay)
	 * rfCode = 0 => spikeTime = 10
	 */
	public float getSpikeTimeFromRFCode(float rfCode){
		float spikeTime = Math.round((1-rfCode)*ECJStarter.PATTERN_WINDOW);
		if(spikeTime > 18) 
			spikeTime = 10000;
		return spikeTime;
	}
	public void displayRFmus(){
		for(int i=0;i<this.rf.length;i++)
			{
			for(int j=0;j<this.rf[i].length;j++)			
				System.out.print(rf[i][j].mu+",\t");			
			System.out.println();
			}		
	}
	public void displayRFsigmas(){
		for(int i=0;i<this.rf.length;i++)
			{
			for(int j=0;j<this.rf[i].length;j++)			
				System.out.print(rf[i][j].sigma+",\t");			
			System.out.println();
			}		
	}
	/*
	 * return the neuron idx that fires first
	 */
	public int decode(ArrayList<SpikeTimes> OpLayerspikeTimes) {
		int neuronIdx = -1;
		float earliestFiringTime = Float.MAX_VALUE;
		int i=0;
		for(SpikeTimes spikeTimes:OpLayerspikeTimes){
			if(spikeTimes!=null && spikeTimes.getSpikeTimes().size()>0){
				float currentNeuronFirTime = spikeTimes.getSpikeTimes().get(0);				
				if(Utils.isCloseEnough(currentNeuronFirTime, earliestFiringTime, 0.5f)){
					neuronIdx = -1;
					earliestFiringTime = currentNeuronFirTime;
				}else if(currentNeuronFirTime < earliestFiringTime){
					neuronIdx = i;
					earliestFiringTime = currentNeuronFirTime;
				}
			}
			i++;
		}
		return neuronIdx;
	}
	public DataSet getDataSet(){
		return this.dataSet;
	}
	public static void main(String[] args) {
		DataSet dataSet = new IrisDataset();		
		Encoder encoder = new Encoder(dataSet, 8);	
		
		Map<Integer, Pattern> testpattern = new TreeMap<Integer, Pattern>();
	
		
		testpattern.put(3, dataSet.getPatternSet().get(0));
		testpattern.put(1, dataSet.getPatternSet().get(50));
		testpattern.put(2, dataSet.getPatternSet().get(20));
		
		
		
		
	//	SpikeTimes[] times = encoder.encode(dataSet.getPatternSet().get(20).getAttributes());
		
		SpikeTimes[] times = encoder.encode(testpattern, 0);
		//for(SpikeTimes st: times)
		//st.display();
			for(int i=0;i<8;i++)
				times[i].display();
			
	}

}

class GaussianRF {
	float mu;
	float sigma;
	
	GaussianRF(float mu, float sigma) {
		this.mu = mu;
		this.sigma = sigma;
	}
    // return phi(x) = standard Gaussian pdf
    private float phi2(float x) {
        return (float)(Math.exp(-x*x / 2) / Math.sqrt(2 * Math.PI));
    }

    // return phi(x, mu, signma) = Gaussian pdf with mean mu and stddev sigma
    public float phi(float x) {
        return phi2((x - mu) / sigma) / sigma;
    }
    
}