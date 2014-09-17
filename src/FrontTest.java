import java.util.Map;

import dataset.DataSet;
import dataset.IrisDataset;
import dataset.Pattern;
import dataset.classes.IrisClass;


public class FrontTest {

	public static void main(String[] args) {
		DataSet dataSet = new IrisDataset();		
		IrisClass _class = IrisClass.Iris_setosa;
		float fraction = 0.1f;
		Map<Integer, Pattern> patternSet = ((IrisDataset)dataSet).samplePatternSetByClass(_class, fraction);
		System.out.println(patternSet.size());
		dataSet.displayDataSet(patternSet);
	}

}
