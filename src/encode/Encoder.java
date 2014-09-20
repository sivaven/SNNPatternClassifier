package encode;

import snn.SpikeTimes;
import dataset.DataSet;

public class Encoder {

	DataSet dataSet;
	GaussianRF[][] rf;
	int nRFs;
	
	public Encoder(DataSet dataset, int nRFs, double beta){
		dataSet = dataset;
		this.nRFs = nRFs;
		rf = new GaussianRF[dataSet.getnAttr()][nRFs];
		float[] attrMin = dataSet.getPatternAttrMin();
		float[] attrMax = dataSet.getPatternAttrMax();
		
		for(int i=0;i<rf.length;i++)
			for(int m=0;m<nRFs;m++){
				double mu = attrMin[i] + (((2*m - 3)/2) * ((nRFs-2)/(attrMax[i] - attrMin[i])));						
				double sigma = (nRFs-2)/(beta * (attrMax[i] - attrMin[i]));
				rf[i][m] = new GaussianRF(mu, sigma);
			}
	}
	
	public Encoder(DataSet dataset, int nRFs){
		this(dataset, nRFs, 1.5);
	}
	public  SpikeTimes encode(double realVal, int attrIdx){
		float[] spikeTimesArray = new float[nRFs];
		for(int i=0;i<nRFs;i++){
			spikeTimesArray[i] = (float) this.rf[attrIdx][i].phi(realVal);
		}
		return new SpikeTimes(spikeTimesArray);
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
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class GaussianRF {
	double mu;
	double sigma;
	
	GaussianRF(double mu, double sigma) {
		this.mu = mu;
		this.sigma = sigma;
	}
    // return phi(x) = standard Gaussian pdf
    private double phi2(double x) {
        return Math.exp(-x*x / 2) / Math.sqrt(2 * Math.PI);
    }

    // return phi(x, mu, signma) = Gaussian pdf with mean mu and stddev sigma
    public double phi(double x) {
        return phi2((x - mu) / sigma) / sigma;
    }
    
}