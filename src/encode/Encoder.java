package encode;

import java.util.ArrayList;

import snn.SpikeTimes;
import dataset.DataSet;

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
	
	public SpikeTimes[] encode(ArrayList<Float> attributes, float factor){
		SpikeTimes[] ipLayerSpikeTimes = new SpikeTimes[attributes.size()*this.nRFs];		
		for(int i=0;i<attributes.size();i++){
			for(int j=0;j<this.nRFs;j++){
				SpikeTimes spikeTimes = new SpikeTimes();
				spikeTimes.addSpikeTime((float)this.rf[i][j].phi(attributes.get(i)) * factor);
				ipLayerSpikeTimes[(i*this.nRFs)+j] = spikeTimes;
			}		
		}
		return ipLayerSpikeTimes;
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
	public int decode(SpikeTimes[] spikeTimes) {
		int neuronIdx = -1;
		float earliestFiringTime = Float.MAX_VALUE;
		for(int i=0;i<spikeTimes.length;i++){
			if(spikeTimes[i]!=null && spikeTimes[i].getSpikeTimes().size()>0){
				float currentNeuronFirTime = spikeTimes[i].getSpikeTimes().get(0);
				if(currentNeuronFirTime < earliestFiringTime){
					neuronIdx = i;
					earliestFiringTime = currentNeuronFirTime;
				}
			}
		}
		return neuronIdx;
	}
	public DataSet getDataSet(){
		return this.dataSet;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

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