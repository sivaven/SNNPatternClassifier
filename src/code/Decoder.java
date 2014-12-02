package code;

import java.util.ArrayList;

import utils.Utils;

public class Decoder {

	float popRateThresh;
	float bin;
	float[] classSpikeTimes;
	
	public Decoder(float popRateThresh, float bin, float[] classSpikeTimes) {
		this.popRateThresh = popRateThresh;
		this.bin = bin;
		this.classSpikeTimes = classSpikeTimes;		
	}
	public int decode(ArrayList<Float> popRates){
		int class_ = -1;
		float time = 0;
		for(int i=0;i<popRates.size();i++){
			if(popRates.get(i)>=popRateThresh){
				class_ = interpretClassByPreciseTime(time);
				break;
			}
			time += bin;
		}
		return class_;
	}
	
	private static final float ACCEPTANCE = 0.1f;
	private int interpretClassByPreciseTime(float time) {
		float time2 = (float)(int)time;
		for(int i=0;i<classSpikeTimes.length;i++) {
			if(Utils.isCloseEnough(time2, classSpikeTimes[i], ACCEPTANCE)){
				return i;
			}
		}
		return -1;
	}
	public static void main(String[] args) {
		float f = 17.9f;
		

	}

}
