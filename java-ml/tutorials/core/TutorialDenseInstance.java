package tutorials.core;

import net.sf.javaml.core.DenseInstance;
import net.sf.javaml.core.Instance;

public class TutorialDenseInstance {

	public static void main(String[] args) {
		/* values of the attributes. */
		double[] values = new double[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        /*
         * The simplest incarnation of the DenseInstance constructor will only
         * take a double array as argument an will create an instance with given
         * values as attributes and no class value set. For unsupervised machine
         * learning techniques this is probably the most convenient constructor.
         */
        Instance instance = new DenseInstance(values);

        System.out.println("Instance with only values set: ");
        System.out.println(instance);
        System.out.println();
        
        /*
         * To create instances that have a class value set, you can use the two
         * argument constructor which takes the values and the class value as
         * parameters.
         */
        Instance instanceWithClassValue = new DenseInstance(values, 1);

        System.out.println("Instance with class value set to 1: ");
        System.out.println(instanceWithClassValue);
        System.out.println();
	}
}
