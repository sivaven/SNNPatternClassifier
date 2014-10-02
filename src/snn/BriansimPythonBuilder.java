package snn;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class BriansimPythonBuilder {

	String fileName;
	String module;
	
	BriansimPythonBuilder(String fileName) {
		this.fileName = fileName;
	}
	void build(String dt,
			int[] nwArch, float[][] ipLW, float[][] hLW,
			SpikeTimes[] spikeTimes,
			boolean doPlot){
		init();
		setDT(dt);
		setNwParms(nwArch, ipLW, hLW );
		setIpLayerSpikeTimes(spikeTimes);
		setDefaultNeuronParms();
		writeCoreStatements();
		if(doPlot)
			writePlotStatements();
		write();
	}
	
	void build(String dt,
			int[] nwArch, float[][] ipLW, float[][] hLW,
			SpikeTimes[] spikeTimes,
			float[] neuronParms,
			boolean doPlot){
		init();
		setDT(dt);
		setNwParms(nwArch, ipLW, hLW );
		setIpLayerSpikeTimes(spikeTimes);
		setNeuronParms(neuronParms);
		writeCoreStatements();
		if(doPlot)
			writePlotStatements();
		write();
	}
	
	void init(){
		module = "from brian import *\nfrom time import time";		
	}
	void setDT(String dt){
		module += "\ndt_ =" + dt;
		module += "\nsimclock = Clock(dt=dt_*ms)";
		module += "\nmonclock = Clock(dt=dt_* ms)";
	}
	void setNwParms(int[] nwArch, float[][] ipLW, float[][] hLW) {
		writeLnToModule("n="+convertToString(nwArch));
		writeLnToModule("maxN=max(n)");
		
		writeLnToModule("ipLayerConnWeights="+convertToString(ipLW));
		writeLnToModule("hdLayerConnWeights="+convertToString(hLW));
	}
	
	void setIpLayerSpikeTimes(SpikeTimes[] spikeTimes) {				
		writeLnToModule("spikeTimesIter = "+convertToString(spikeTimes));		
		writeLnToModule("spikeTimes = [(i, t*ms) for i in xrange(len(spikeTimesIter)) for t in spikeTimesIter[i]]");
	}
	
	void setDefaultNeuronParms() {
		//DG Hicap parms
		setNeuronParms(0.571f, 0.130f, -2.714f, 111.506f, 81.2f, -60.5f, -34.8f, 42.4f, -60f, 0, 40);
	}
	void setNeuronParms(float[] parms) {
		setNeuronParms(parms[0], parms[1], parms[2], parms[3],
				parms[4], parms[5], parms[6], parms[7], parms[8],
				(int)parms[9], (int)parms[10]);
	}
	void setNeuronParms(float k, float a, float b, float d, 
						float C, float vR, float vT, float vP, float c, 
						int Is, int dur) {
		writeLnToModule("");
		writeLnToModule("k="+k+"/ms/mV");
		writeLnToModule("a="+a);
		writeLnToModule("b="+b);
		writeLnToModule("d="+d);
		writeLnToModule("C="+C);
		writeLnToModule("vR="+vR+"*mV");
		writeLnToModule("vT="+vT+"*mV");
		writeLnToModule("vPeak="+vP+"*mV");
		writeLnToModule("c="+c+"*mV");
		writeLnToModule("Is="+Is);
		writeLnToModule("dur="+dur);
		writeLnToModule("simDur="+dur);
		
		writeLnToModule("");		
		writeLnToModule("model9pEqs= Equations('''");
		writeLnToModule("\t\tdV/dt=(k*((V-vR)*(V-vT))-U+I)/(C) : volt");
		writeLnToModule("\t\tdU/dt=a*((b*(V-vR)/ms/ms)-(U/ms)) : volt/second");                                      
		writeLnToModule("\t\tI : mV/ms");                                                                              
		writeLnToModule("\t\t''')");
		
		writeLnToModule("");
		writeLnToModule("inputLayer = SpikeGeneratorGroup(n[0], spikeTimes, clock=simclock)");
		writeLnToModule("hiddenLayer = NeuronGroup(n[1], model=model9pEqs, threshold=\"V>vPeak\", reset=\"V=c;U+=d\", method= \"RK\", clock=simclock)");
		writeLnToModule("outputLayer = NeuronGroup(n[2], model=model9pEqs, threshold=\"V>vPeak\", reset=\"V=c;U+=d\", method= \"RK\", clock=simclock)");
		writeLnToModule("");			
	}
	
	void writeCoreStatements(){
		writeLnToModule("conn1 = Connection(inputLayer, hiddenLayer, 'V')");
		writeLnToModule("conn2 = Connection(hiddenLayer, outputLayer, 'V')");
		writeLnToModule("for i in xrange(0, n[0]):");
		writeLnToModule("\tfor j in xrange(0, n[1]):");
		writeLnToModule("\t\tconn1[i, j] =  ipLayerConnWeights[i][j]*mV");
		
		writeLnToModule("for i in xrange(0, n[1]):");
		writeLnToModule("\tfor j in xrange(0, n[2]):");
		writeLnToModule("\t\tconn2[i, j] =  hdLayerConnWeights[i][j]*mV");
		
		writeLnToModule("SM = [SpikeMonitor(inputLayer),SpikeMonitor(hiddenLayer),SpikeMonitor(outputLayer)]");
		writeLnToModule("VM = [StateMonitor(hiddenLayer, 'V', record=True, clock=monclock),StateMonitor(outputLayer, 'V', record=True, clock=monclock)  ]");
		writeLnToModule("");
		
		writeLnToModule("hiddenLayer.V = vR ");
		writeLnToModule("hiddenLayer.U =0");
		writeLnToModule("outputLayer.V = vR ");
		writeLnToModule("outputLayer.U =0");
		writeLnToModule("");
		
		writeLnToModule("t1 = time()");
		writeLnToModule("run(simDur*ms)");
		writeLnToModule("t2 = time()");
		writeLnToModule("print \"Simulation time:\", t2 - t1, \"s\"");
		
		writeLnToModule("print \"Output Layer Spike times:\"");
		writeLnToModule("for i in xrange(0, n[len(n)-1]):");
		writeLnToModule("\tprint str(SM[len(n)-1][i])");
		writeLnToModule("");
		
	}
	
	void writePlotStatements(){
		writeLnToModule("ipLayerV = [[vR for i in arange(0,simDur,dt_)] for i in xrange(n[0])]  ");
		writeLnToModule("ipLayerT = [i for i in arange(0,simDur,dt_)]");
		writeLnToModule("for i in xrange(0, len(spikeTimesIter)):");
		writeLnToModule("\tfor j in xrange(0, len(spikeTimesIter[i])):");
		writeLnToModule("\t\tipLayerV[i][int(spikeTimesIter[i][j]/dt_)] = vPeak");		
		
		writeLnToModule("");
		writeLnToModule("colors=[0,0,0]");
		writeLnToModule("cnt = -maxN");
		writeLnToModule("for i in xrange(0, len(n)):");
		writeLnToModule("\tcnt+=maxN");
		writeLnToModule("\tfor j in xrange(0, n[i]):");
		writeLnToModule("\t\tsubplot(len(n),n[i], (n[i]*i)+j+1)");
		writeLnToModule("\t\tif i > 0:");
		writeLnToModule("\t\t\tplot(VM[i-1].times / ms, VM[i-1][j] / mV, lw=1.0, color=colors)");
		writeLnToModule("\t\telse:");
		writeLnToModule("\t\t\tplot(ipLayerT, ipLayerV[j], lw=1.0, color=colors)");
		
		writeLnToModule("xlabel('Time (ms)')");
		writeLnToModule("ylabel('V (mV)')");
		writeLnToModule("show()");
			        	    
	}
	void writeLnToModule(String line){
		module += "\n"+line;
	}
	void write(){
		try {			
			BufferedWriter out = new BufferedWriter(new FileWriter(fileName));
			out.write(module);		
			out.close();			
		} catch (IOException e) {
			e.printStackTrace();
		}		
	}
	String convertToString(int[] array) {
		String str = "[";
		for(int i=0; i<array.length; i++) {
			if(i>0) str+=",";
			str+=array[i];
		}
		str+="]";
		return str;
	}
	String convertToString(float[] array) {
		String str = "[";
		for(int i=0; i<array.length; i++) {
			if(i>0) str+=",";
			str+=array[i];
		}
		str+="]";
		return str;
	}
	String convertToString(ArrayList<Float> array) {
		String str = "[";
		for(int i=0; i<array.size(); i++) {
			if(i>0) str+=",";
			str+=array.get(i);
		}
		str+="]";
		return str;
	}
	String convertToString(float[][] array) {
		String str = "[";
		for(int i=0; i<array.length; i++) {
			if(i>0) str+=",";
			str+=convertToString(array[i]);
		}
		str+="]";
		return str;
	}
	String convertToString(SpikeTimes[] array) {
		String str = "[";		
		for(int i=0; i<array.length; i++) {
			if(i>0) str+=",";
			str+=convertToString(array[i].spikeTimes);
		}
		str+="]";
		return str;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
