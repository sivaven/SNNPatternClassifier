package training;

public class EAGenes {

	float[] genes;
	public EAGenes(float[] genes){
		this.genes = genes;
	}
	public float getGene(int idx) {
		return genes[idx];
	}
	public float[] getGenes(int startIdx, int length){
		float[] rangedGene = new float[length];
		int idx=0;
		for(int i=startIdx;i<startIdx+length;i++){
			rangedGene[idx++] = this.genes[i];
		}
		return rangedGene;
	}
}
