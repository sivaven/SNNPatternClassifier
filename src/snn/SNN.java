package snn;

import java.util.ArrayList;
import java.util.Random;
import java.util.StringTokenizer;

import snn.constants.LayerLabel;

public class SNN {
	Layer[] layers;
	int[] nNeurons;
		
	public SNN(int[] nNeurons) {
		this.nNeurons = nNeurons;
		layers = new Layer[nNeurons.length];
		for(int i=0;i<layers.length;i++) {
			LayerLabel label;
			if(i==0) {
				label = LayerLabel.INPUT;
			}else if(i==layers.length-1) {
				label = LayerLabel.OUTPUT;
			}else {
				label = LayerLabel.HIDDEN;
			}
			
			if(label.equals(LayerLabel.INPUT) || label.equals(LayerLabel.HIDDEN)) {
				layers[i] = new Layer(label, nNeurons[i], nNeurons[i+1]);
			}
			
			if(label.equals(LayerLabel.OUTPUT)) {
				layers[i] = new Layer(label, nNeurons[i]);
			}						
		}
	}
	
	public void randomizeWeights() {
		for(Layer layer: this.layers){
			if(!layer.getLabel().equals(LayerLabel.OUTPUT)) {
				layer.setRandomWeights();
			}
		}
	}
	/*
	 * argument - flat weight list for each layer
	 */
	public void setWeights(float[][] weights) {
		for(int i=0;i<weights.length;i++){
			this.layers[i].setWeightsToNextLayer(weights[i]);
		}			
	}
	/*
	 * arg - full flat list of weights for all layer
	 */
	public void setWeights(float[] weights) {
		int idx = 0;
		for(int i=0;i<layers.length-1;i++) {
			int lwn = getNWeights(i);
			float[] layerWeights = new float[lwn];			
			for(int j=0; j< lwn; j++){
				layerWeights[j] = weights[idx++];
			}
			
			this.layers[i].setWeightsToNextLayer(layerWeights);
		}
	}
	
	public int getNWeights() {
		int n=0;
		for(int i=0;i<layers.length-1;i++) {
			n += this.nNeurons[i]*this.nNeurons[i+1];
		}
		return n;
	}
	
	public int getNWeights(int layer) {
		return this.layers[layer].getnWeights();
	}
	public String getStructSimple(){
		String str = "";
		for(int n: nNeurons){
			//str +=
		}
		return str;
	}
	
	Layer getLayer(LayerLabel label){
		if(label.equals(LayerLabel.INPUT)) {
			return this.layers[0];
		}
		if(label.equals(LayerLabel.HIDDEN)) {
			return this.layers[1];
		}
		if(label.equals(LayerLabel.OUTPUT)) {
			return this.layers[this.layers.length-1];
		}
		return null;
	}
	
	public void setInputLayerSpikeTimes(float[][] spikeTimes) {
		this.layers[0].setNeuronSpikeTimes(spikeTimes);
	}
	
	public SpikeTimes[] getOutputLayerSpikeTimes(){
		return this.layers[this.layers.length-1].getNeuronSpikeTimes();
	}
}
/*
 * layer level info:
 */
class Layer {
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
	
	void setRandomWeights() {
		Random rnd = new Random();
		for(int i=0;i<weightsToNextLayer.length;i++)
			for(int j=0;j<weightsToNextLayer[i].length;j++) {
				weightsToNextLayer[i][j] = rnd.nextFloat();
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
