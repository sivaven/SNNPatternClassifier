package ecj;

import ec.Evolve;
import ec.eval.Slave;

public class ECJStarter2s {
	public static void main(final String[] args) {
        assert (args != null);
        
        ECJStarter.init();
        
        if (args.length > 0 && args[0].equals("--slave"))
            Slave.main(tail(args));
        else
            Evolve.main(args);
    }
    
    private static String[] tail(final String[] array) {
        assert(array != null);
        final String[] result = new String[array.length - 1];
        for (int i = 0; i < result.length; i++)
            result[i] = array[i+1];
        return result;
    }
}
