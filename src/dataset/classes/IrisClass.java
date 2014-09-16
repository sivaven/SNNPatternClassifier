package dataset.classes;

public enum IrisClass {
	Iris_setosa(1),	Iris_versicolor(2), Iris_virginica(3);	
	
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
