package training.plasticity;

import snn.SNN;
import training.DataSetManager;
import classifier.Classifier;
import dataset.DataSet;
import dataset.IrisDataset;
import encode.Encoder;

public class STDP {

	public static void main(String[] args) {
		float tSetFrac = 0.1f;  //(.1, .4) => n=15, 6
		float fitSetFrac = 0.6f; 
				
		DataSet dataSet = new IrisDataset();
		DataSetManager dataSetManager = new DataSetManager(dataSet);		
		dataSetManager.setDataSetPartitions(tSetFrac, fitSetFrac);
		Encoder encoder = new Encoder(dataSet, 8);	

		SNN snn = new SNN(new int[] {32, 15, 3});
		snn.randomizeWeights(10);
		Classifier cl = new Classifier(snn, encoder);
		System.out.println(cl.evaluate(dataSetManager.getTrainingSet()));
	}

}
