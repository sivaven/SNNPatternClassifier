import dataset.DataSet;
import dataset.IrisDataset;


public class FrontTest {

	public static void main(String[] args) {
		DataSet dataSet = new IrisDataset();
		dataSet.displayDataSet();
	}

}
