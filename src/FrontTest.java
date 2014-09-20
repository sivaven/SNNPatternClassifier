import java.util.Iterator;
import java.util.Map;

import snn.SpikeTimes;
import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import encode.Encoder;


public class FrontTest {

	public static void main(String[] args) {
		DataSet dataSet = new IrisDataset();		
	//	IrisClass _class = IrisClass.Iris_setosa;
	//	float fraction = 0.1f;
	//	Map<Integer, Pattern> patternSet = ((IrisDataset)dataSet).samplePatternSetByClass(_class, fraction);		
	Encoder encoder = new Encoder(dataSet, 8);
/*	int attrIdx = 0;
	
	Iterator it = dataSet.getPatternSet().entrySet().iterator();
	while (it.hasNext()) {
        Map.Entry pairs = (Map.Entry)it.next();
        Pattern pattern = (Pattern) pairs.getValue();
        SpikeTimes times = encoder.encode(pattern.getAttributes().get(attrIdx), attrIdx);
        times.display();
	}	
	*/
	encoder.displayRFsigmas();
	//encoder.displayRFmus();
	}
}
