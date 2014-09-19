package snn;

import java.util.ArrayList;
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
	
	public String getStructSimple(){
		String str = "";
		for(int n: nNeurons){
			//str +=
		}
		return str;
	}
	
}
/*
 * layer level info:
 */
class Layer {
	private int nNeurons;
	private LayerLabel label;
	private float[][] weightsToNextLayer;
	private SpikeTimes[] neuronSpikeTimes;
	/*
	 * Input and Hidden layer initialization 
	 * requires nNeurons as well as next layer neuron count
	 */
	public Layer(LayerLabel label, int nNeurons, int nNeuronsNxtLyr){
		this.setnNeurons(nNeurons);
		this.setLabel(label);
		this.setWeightsToNextLayer(new float[nNeurons][nNeuronsNxtLyr]);	
		if(label.equals(LayerLabel.HIDDEN)) {
			this.setNeuronSpikeTimes(null);
		}else{
			this.setNeuronSpikeTimes(new SpikeTimes[nNeurons]);
		}
	}
	
	/*
	 * Output layer inits. no weights. no next layer neuron count
	 */
	public Layer(LayerLabel label, int nNeurons){
		this.setnNeurons(nNeurons);
		this.setLabel(label);
		this.setWeightsToNextLayer(null);	
		if(label.equals(LayerLabel.HIDDEN)) {
			this.setNeuronSpikeTimes(null);
		}else{
			this.setNeuronSpikeTimes(new SpikeTimes[nNeurons]);
		}
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
	
	public void displaySpikeTimes() {
		System.out.println(this.label.name()+" layer SpikeTimes:");
		for(SpikeTimes spikeTime: this.neuronSpikeTimes){
			spikeTime.display();
		}
	}
}
/*
 * Neuron level info: currently only spike times
 */
class SpikeTimes {
	private static final char[] STOP_CHARS = {'[',']'}; // if adding, update removeStopChars method!!
	
	ArrayList<Float> spikeTimes;
	SpikeTimes(ArrayList<Float> spikeTimes){
		this.spikeTimes = spikeTimes;
	}
	SpikeTimes(String spikeTimesStringList) {
		spikeTimes = new ArrayList<>();
		spikeTimesStringList = removeStopChars(spikeTimesStringList);
		
		StringTokenizer st = new StringTokenizer(spikeTimesStringList, " ");
		String token = null;		
		while(st.hasMoreTokens()) {
			token = st.nextToken();
			spikeTimes.add(Float.parseFloat(token));
		}
	}
	private String removeStopChars(String str){
		return str.replace(STOP_CHARS[0], ' ').replace(STOP_CHARS[1], ' ');		
	}
	
	public void display(){
		System.out.println(spikeTimes);
	}
}