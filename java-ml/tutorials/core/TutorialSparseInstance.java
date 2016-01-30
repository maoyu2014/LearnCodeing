package tutorials.core;

import net.sf.javaml.core.Instance;
import net.sf.javaml.core.SparseInstance;

public class TutorialSparseInstance {

    public static void main(String[]args){
        /*
         * Here we will create an instance with 10 attributes, but will only set
         * the attributes with index 1,3 and 7 with a value.
         */
        /* Create instance with 10 attributes */
        Instance instance = new SparseInstance(10);
        /* Set the values for particular attributes */
        instance.put(1, 1.0);
        instance.put(3, 2.0);
        instance.put(7, 4.0);
        
        System.out.println(instance);
        System.out.println();
    }
}
