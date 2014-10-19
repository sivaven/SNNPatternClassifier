package briansim;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import snn.SpikeTimes;
import training.plasticity.STDP;

public class BriansimPythonBuilder {

	String fileName;
	String module;
	Map<BrianSimParameterLabel, Object> brianSimParms;
	boolean plot;
	
	public BriansimPythonBuilder(String fileName, Map<BrianSimParameterLabel, Object> brianSimParms, boolean plot) {
		this.fileName = fileName;
		this.module = "from brian import *\nfrom time import time";	
		this.brianSimParms = brianSimParms;
		this.plot = plot;
	}
	public void build() {
		writeParameters();
		writeOthers();
		write();
	}
	void writeParameters(){
		for(BrianSimParameterLabel parm: brianSimParms.keySet()) {
			writeLnToModule(parm.name()+"="+getStringed(parm));
		}
	}
	
	void writeOthers(){
		writeLnToModule("#\n#");
		writeDefaultNeuronParmsAndEqn();
		writeSTDPEqn();
		writeLnToModule("");
		writeLnToModule("simclock = Clock(dt=dt_*ms)");
		writeLnToModule("spikeTimes = [(i, t*ms) for i in xrange(len("+BrianSimParameterLabel.spike_times_iter_stdp.toString()+")) for t in "+BrianSimParameterLabel.spike_times_iter_stdp.toString()+"[i]]");
		writeLayerAndConnections();
		writeSTDP();
		writeMonitors();
		writeRunAndOutputs();
		writeFeedForwardModule();
	}
	
	void writeDefaultNeuronParmsAndEqn() {
		//DG Hicap parms
		setNeuronParms(0.571f, 0.130f, -2.714f, 111.506f, 81.2f, -60.5f, -34.8f, 42.4f, -60f, 0);
	}
	
	void setNeuronParms(float k, float a, float b, float d, 
						float C, float vR, float vT, float vP, float c, 
						int Is) {
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
		
		writeLnToModule("");		
		writeLnToModule("model9pEqs= Equations('''");
		writeLnToModule("\t\tdV/dt=(k*((V-vR)*(V-vT))-U+I)/(C) : volt");
		writeLnToModule("\t\tdU/dt=a*((b*(V-vR)/ms/ms)-(U/ms)) : volt/second");                                      
		writeLnToModule("\t\tI : mV/ms");                                                                              
		writeLnToModule("\t\t''')");
		
				
	}
	
	void writeSTDPEqn(){
		writeLnToModule("");
		writeLnToModule("eqs_stdp='''");
		writeLnToModule("dA_pre/dt=-A_pre/tau : 1");
		writeLnToModule("dA_post/dt=-A_post/tau : 1");
		writeLnToModule("'''");
		
	}
	
	void writeLayerAndConnections(){
		writeLnToModule("");
		writeLnToModule("inputLayer = SpikeGeneratorGroup("+BrianSimParameterLabel.nw_arch+"[0], spikeTimes, clock=simclock)");
		writeLnToModule("hiddenLayer = NeuronGroup("+BrianSimParameterLabel.nw_arch+"[1], model=model9pEqs, threshold=\"V>vPeak\", reset=\"V=c;U+=d\", method= \"RK\", clock=simclock)");
		writeLnToModule("outputLayer = NeuronGroup("+BrianSimParameterLabel.nw_arch+"[2], model=model9pEqs, threshold=\"V>vPeak\", reset=\"V=c;U+=d\", method= \"RK\", clock=simclock)");
		writeLnToModule("hiddenLayer.V = vR ");
		writeLnToModule("hiddenLayer.U =0");
		writeLnToModule("outputLayer.V = vR ");
		writeLnToModule("outputLayer.U =0");
		writeLnToModule("");
			
		writeLnToModule("conn1 = Connection(inputLayer, hiddenLayer, 'V', "
						+ "weight="+BrianSimParameterLabel.conn1_init_weight+"*mV, "
						+ "sparseness="+BrianSimParameterLabel.conn1_prob+")");
		writeLnToModule("conn2 = Connection(hiddenLayer, outputLayer, 'V', "
						+ "weight="+BrianSimParameterLabel.conn2_init_weight+"*mV, "
						+ "sparseness="+BrianSimParameterLabel.conn2_prob+")");		
	}
	void writeSTDP(){
		writeLnToModule("tau = "+BrianSimParameterLabel.stdp_tau+"*ms");
		writeLnToModule("stdp1=STDP(conn1,eqs=eqs_stdp,"
				+ "pre='A_pre+="+BrianSimParameterLabel.stdp1_a_step+"*mV;w+=A_post',"
				+ "post='A_post+="+BrianSimParameterLabel.stdp1_a_step+"*mV;w+=A_pre',wmax="+BrianSimParameterLabel.stdp_gmax+"*mV, clock=simclock)");
		writeLnToModule("stdp2=STDP(conn2,eqs=eqs_stdp,"
				+ "pre='A_pre+="+BrianSimParameterLabel.stdp2_a_step+"*mV;w+=A_post',"
				+ "post='A_post+="+BrianSimParameterLabel.stdp2_a_step+"*mV;w+=A_pre',wmax="+BrianSimParameterLabel.stdp_gmax+"*mV, clock=simclock)");
	}
	void writeMonitors(){
		writeLnToModule("SMO = SpikeMonitor(outputLayer)");
		writeLnToModule("");
		if(plot){
			writeLnToModule("SMI = SpikeMonitor(inputLayer)");
			writeLnToModule("SM = SpikeMonitor(hiddenLayer)");
			writeLnToModule("VM = StateMonitor(outputLayer, 'V', record=True, clock=simclock) ");
			writeLnToModule("");
		}
		
	}
	void writeRunAndOutputs() {	
//		writeLnToModule("t1 = time()");
		writeLnToModule("run("+BrianSimParameterLabel.sim_dur_stdp+"*ms)");
//		writeLnToModule("t2 = time()");
/*		writeLnToModule("print \"$"+BrianOutputLabel.sim_time+":\", t2 - t1, \"s\"");		
		writeLnToModule("print \"$"+BrianOutputLabel.op_layer_spike_times+":\"");
		writeLnToModule("for i in xrange(0, "+BrianSimParameter.nw_arch+"[len("+BrianSimParameter.nw_arch+")-1]):");
		writeLnToModule("\tprint \" \".join(str(p) for p in SMO[i])+\",\"");
		*/
		writeLnToModule("");
	}
	void writeFeedForwardModule() {
		writeLnToModule("#\n#");
		writeLnToModule("def feed_forward(spikeTimesIterList, ipPatternIdx):");
		writeLnToModule("\treinit(states=False)");
		writeLnToModule("\tspikeTimes = [(i, t*ms) for i in xrange(len(spikeTimesIterList)) for t in spikeTimesIterList[i]]");
		writeLnToModule("\tinputLayer.spiketimes=spikeTimes");
		writeLnToModule("\tt1 = time()");
		writeLnToModule("\trun("+BrianSimParameterLabel.sim_dur_ff+"*ms)");
		writeLnToModule("\tt2 = time()");
		writeLnToModule("\tprint \"#$"+BrianOutputLabel.ip_pattern_idx+":\", ipPatternIdx");
		writeLnToModule("\tprint \"$"+BrianOutputLabel.sim_time+":\", t2 - t1, \"s\"");	
		writeLnToModule("\tprint \"$"+BrianOutputLabel.op_layer_spike_times+":\"");
		writeLnToModule("\tfor i in xrange(0, "+BrianSimParameterLabel.nw_arch+"[len("+BrianSimParameterLabel.nw_arch+")-1]):");
		writeLnToModule("\t\tprint \" \".join(str(p) for p in SMO[i])+\",\"");
		writeLnToModule("");
		if(this.plot) {
			writeLnToModule("\tcolors=[0,0,0]");
			writeLnToModule("\tsubplot(311)");
			writeLnToModule("\traster_plot(SMI, title='Input Layer')");
			writeLnToModule("\taxis([0, "+BrianSimParameterLabel.sim_dur_ff+", 0, "+BrianSimParameterLabel.nw_arch+"[0]])");
			
			writeLnToModule("\tsubplot(312)");
			writeLnToModule("\traster_plot(SM, title='Hidden Layer')");
			writeLnToModule("\taxis([0, "+BrianSimParameterLabel.sim_dur_ff+", 0, "+BrianSimParameterLabel.nw_arch+"[1]])");
			
			writeLnToModule("\tsubplot(313)");
			writeLnToModule("\traster_plot(SMO, title='Output Layer')");
			writeLnToModule("\taxis([0, "+BrianSimParameterLabel.sim_dur_ff+", 0, "+BrianSimParameterLabel.nw_arch+"[2]])");
			writeLnToModule("\tshow()");
		}
		writeLnToModule("");
		writeLnToModule("stdp1 = None\nstdp2=None");
		writeLnToModule("hiddenLayer.V = vR ");
		writeLnToModule("hiddenLayer.U =0");
		writeLnToModule("outputLayer.V = vR ");
		writeLnToModule("outputLayer.U =0");
		writeLnToModule("for i in xrange(0, len("+BrianSimParameterLabel.spike_times_iter_ff3d+")):");
		writeLnToModule("\tfeed_forward(spikeTimesIterList = "+BrianSimParameterLabel.spike_times_iter_ff3d+"[i]"
				+ ", ipPatternIdx = "+BrianSimParameterLabel.ip_pattern_idx+"[i])");
		writeLnToModule("");		
	}
	void writePlotStatementsNodeByNode(){
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
	void writePlotStatementsHiddenScatterOpState(){
		
		writeLnToModule("doPlotOpLayer = True\ndoPlotRaster = True");
		writeLnToModule("");
		
		writeLnToModule("if doPlotRaster:");
		writeLnToModule("\tcolors=[0,0,0]");
		writeLnToModule("\tsubplot(311)");
		writeLnToModule("\traster_plot(SMI, title='Input Layer')");
		writeLnToModule("\taxis([0, simDur, 0, n[0]])");
		
		writeLnToModule("\tsubplot(312)");
		writeLnToModule("\traster_plot(SM, title='Hidden Layer')");
		writeLnToModule("\taxis([0, simDur, 0, n[1]])");
		
		writeLnToModule("\tsubplot(313)");
		writeLnToModule("\traster_plot(SMO, title='Output Layer')");
		writeLnToModule("\taxis([0, simDur, 0, n[2]])");
		
	/*	writeLnToModule("\tsubplot(513)");
		writeLnToModule("\tplot(VM.times / ms, VM[0] / mV, lw=1.0, color=colors)");
		
		writeLnToModule("\tsubplot(514)");
		writeLnToModule("\tplot(VM.times / ms, VM[1] / mV, lw=1.0, color=colors)");
		writeLnToModule("\tsubplot(515)");
		writeLnToModule("\tplot(VM.times / ms, VM[2] / mV, lw=1.0, color=colors)");*/
		
		writeLnToModule("\txlabel('Time (ms)')");
		writeLnToModule("\tylabel('V (mV)')");
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
			str+=convertToString(array[i].getSpikeTimes());
		}
		str+="]";
		return str;
	}
	String convertToString(SpikeTimes[][] array) {
		String str = "[";		
		for(int i=0; i<array.length; i++) {
			if(i>0) str+=",";
			str+=convertToString(array[i]);
		}
		str+="]";
		return str;
	}
	String getStringed(BrianSimParameterLabel parm) {
		Object obj = brianSimParms.get(parm);
		if(obj instanceof Float){
			return ((Float)obj).toString();
		}
		if(obj instanceof int[]){
			return convertToString((int[])obj);
		}
		if(obj instanceof float[]){
			return convertToString((float[])obj);
		}
		if(obj instanceof ArrayList){
			return convertToString((ArrayList<Float>)obj);
		}
		if(obj instanceof float[][]){
			return convertToString((float[][])obj);
		}
		if(obj instanceof SpikeTimes[]){
			return convertToString((SpikeTimes[])obj);
		}
		if(obj instanceof SpikeTimes[][]){
			return convertToString((SpikeTimes[][])obj);
		}
		System.out.println("No object instances matched!! BrianSimPythonBuilder.java");
		return null;
	}
	public static void main(String[] args) {
		Map<BrianSimParameterLabel, Object> parms = new HashMap<BrianSimParameterLabel, Object>();
		parms.put(BrianSimParameterLabel.dt_, 1.0f);
		parms.put(BrianSimParameterLabel.nw_arch, new int[]{32, 20, 3});
		parms.put(BrianSimParameterLabel.sim_dur_stdp, 500f);
		parms.put(BrianSimParameterLabel.sim_dur_ff, 500f);
		parms.put(BrianSimParameterLabel.conn1_init_weight, 3.0f);
		parms.put(BrianSimParameterLabel.conn2_init_weight, 5.0f);
		parms.put(BrianSimParameterLabel.stdp1_a_step, 1.0f);
		parms.put(BrianSimParameterLabel.stdp2_a_step, 1.0f);
		parms.put(BrianSimParameterLabel.stdp_tau, 10f);
		parms.put(BrianSimParameterLabel.stdp_gmax, 10000.0f);
		parms.put(BrianSimParameterLabel.spike_times_iter_stdp, new SpikeTimes[]{});
		parms.put(BrianSimParameterLabel.spike_times_iter_ff3d, new SpikeTimes[][]{});
		
		BriansimPythonBuilder builder = new BriansimPythonBuilder("testing.py", parms, false);
		builder.build();
		builder.write();
	}

}
