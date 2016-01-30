package tutorials.core;

import java.util.SortedSet;

import net.sf.javaml.core.Dataset;
import net.sf.javaml.core.DefaultDataset;
import net.sf.javaml.core.Instance;
import net.sf.javaml.tools.InstanceTools;

public class TutorialDataset {

	public static void main(String[]args){
        Dataset data = new DefaultDataset();
        for (int i = 0; i < 10; i++) {
            Instance tmpInstance = InstanceTools.randomInstance(25);
            data.add(tmpInstance);
        }
        /* Retrieve all class values that are ever used in the data set */
        SortedSet<Object> classValues = data.classes();
        

        System.out.println(data.noAttributes());
        System.out.println(data.size());
        System.out.println(classValues.size());

    }
	
}
