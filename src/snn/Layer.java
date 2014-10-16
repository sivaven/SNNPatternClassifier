package snn;

import java.util.Random;

import snn.constants.LayerLabel;

/*
 * layer level info:
 */
public class Layer {
	private int nNeurons;
	private LayerLabel label;
	private float[][] weightsToNextLayer = null;
	private SpikeTimes[] neuronSpikeTimes = null;
	private int nWeights;
	/*
	 * Input and Hidden layer initialization 
	 * requires nNeurons as well as next layer neuron count
	 */
	public Layer(LayerLabel label, int nNeurons, int nNeuronsNxtLyr){
		this.setnNeurons(nNeurons);
		this.setLabel(label);
		this.setWeightsToNextLayer(new float[nNeurons][nNeuronsNxtLyr]);	
		if(!label.equals(LayerLabel.HIDDEN)) {
			this.setNeuronSpikeTimes(new SpikeTimes[nNeurons]);
		}
		this.setnWeights(nNeurons*nNeuronsNxtLyr);
	}
	
	/*
	 * Output layer inits. no weights. no next layer neuron count
	 */
	public Layer(LayerLabel label, int nNeurons){
		this.setnNeurons(nNeurons);
		this.setLabel(label);			
		if(!label.equals(LayerLabel.HIDDEN)) {
			this.setNeuronSpikeTimes(new SpikeTimes[nNeurons]);
		}
		this.setnWeights(0);
	}

	public int getnNeurons() {
		return nNeurons;
	}

	public void setnNeurons(int nNeurons) {
		this.nNeurons = nNeurons;
	}

	public float[][] getWeightsToNextLayer() {
		return weightsToNextLayer;
	}

	public void setWeightsToNextLayer(float[][] weightsToNextLayer) {
		this.weightsToNextLayer = weightsToNextLayer;
	}

	public void setWeightsToNextLayer(float[] weights) {
		int idx =0;
		for(int i=0;i<weightsToNextLayer.length;i++) 
			for(int j=0;j<weightsToNextLayer[i].length;j++){
				weightsToNextLayer[i][j] = weights[idx++];
			}
	}
	
	public LayerLabel getLabel() {
		return label;
	}

	public void setLabel(LayerLabel label) {
		this.label = label;
	}

	
	public SpikeTimes[] getNeuronSpikeTimes() {
		return neuronSpikeTimes;
	}

	public void setNeuronSpikeTimes(SpikeTimes[] neuronSpikeTimes) {
		this.neuronSpikeTimes = neuronSpikeTimes;
	}
	
	public void setNeuronSpikeTimes(float[][] spikeTimes) {
		for(int i=0;i<this.neuronSpikeTimes.length;i++) {
			this.neuronSpikeTimes[i] = new SpikeTimes(spikeTimes[i]);
		}
	}
	
	void setRandomWeights(int magFactor) {
		Random rnd = new Random();
		for(int i=0;i<weightsToNextLayer.length;i++)
			for(int j=0;j<weightsToNextLayer[i].length;j++) {
				weightsToNextLayer[i][j] = rnd.nextFloat()*magFactor;
			}
	}
	public void displaySpikeTimes() {
		System.out.println(this.label.name()+" layer SpikeTimes:");
		for(SpikeTimes spikeTime: this.neuronSpikeTimes){
			spikeTime.display();
		}
	}

	public int getnWeights() {
		return nWeights;
	}

	public void setnWeights(int nWeights) {
		this.nWeights = nWeights;
	}
}