package dataset.classes;

public enum IrisClass {
	Iris_setosa(0),	Iris_versicolor(1), Iris_virginica(2);	
	
	private int numericClass;	
	IrisClass(int numericClass) {
		setNumericClass(numericClass);
	}
	public int getNumericClass() {
		return numericClass;
	}
	public void setNumericClass(int numericClass) {
		this.numericClass = numericClass;
	}
}
