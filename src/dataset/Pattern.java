package dataset;

import java.util.ArrayList;

import dataset.classes.IrisClass;

public class Pattern {
	
	private ArrayList<Float> attributes;
	private IrisClass _class;	
	
	Pattern(){		
		this.attributes = new ArrayList<>();
	}
	Pattern(ArrayList<Float> attributes, IrisClass _class) {		
		this.attributes = attributes;
		this._class = _class;
	}
	public ArrayList<Float> getAttributes() {
		return attributes;
	}
	public void setAttributes(ArrayList<Float> attributes) {
		this.attributes = attributes;
	}
	public void addAttribute(Float attribute) {
		this.attributes.add(attribute);
	}
	public IrisClass get_class() {
		return _class;
	}
	public void set_class(IrisClass _class) {
		this._class = _class;
	}
	public void displayPattern() {		
		System.out.println(attributes +"\t"+_class.name());
	}
}
