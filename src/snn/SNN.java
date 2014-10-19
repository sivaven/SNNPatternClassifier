package snn;

import java.util.HashMap;
import java.util.Map;

import snn.constants.LayerLabel;
import briansim.BrianSimParameterLabel;

public class SNN {
	Layer[] layers;
	Map<BrianSimParameterLabel, Object> parms;
	
	public SNN(int[] nNeurons) {
		parms = new HashMap<BrianSimParameterLabel, Object>();
		addParameter(BrianSimParameterLabel.nw_arch, nNeurons);
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
	
	public void addParameter(BrianSimParameterLabel parm, Object value){
		parms.put(parm, value);
	}
	
	public Map<BrianSimParameterLabel, Object> getParms(){
		return this.parms;
	}
	public void setParms(Map<BrianSimParameterLabel, Object> parms){
		this.parms = parms;
	}
	public void randomizeWeights(int magFactor) {
		for(Layer layer: this.layers){
			if(!layer.getLabel().equals(LayerLabel.OUTPUT)) {
				layer.setRandomWeights(magFactor);
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
			n += this.getArch()[i]*this.getArch()[i+1];
		}
		return n;
	}
	
	public int getNWeights(int layer) {
		return this.layers[layer].getnWeights();
	}
	public String getStructSimple(){
		String str = "";
		for(int n: getArch()){
			//str +=
		}
		return str;
	}
	
	public Layer getLayer(LayerLabel label){
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
	
	public void setInputLayerSpikeTimes(SpikeTimes[] spikeTimes) {
		this.layers[0].setNeuronSpikeTimes(spikeTimes);
	}
	
	public SpikeTimes[] getOutputLayerSpikeTimes(){
		return this.layers[this.layers.length-1].getNeuronSpikeTimes();
	}
	public void displayOutputLayerSpikeTimes(){
		SpikeTimes[] olST = getOutputLayerSpikeTimes();		
		for(SpikeTimes spikeTime: olST)
			spikeTime.display();
	}


	public int[] getArch() {
		return (int[]) this.parms.get(BrianSimParameterLabel.nw_arch);
	}
}

