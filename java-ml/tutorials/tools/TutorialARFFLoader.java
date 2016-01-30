package tutorials.tools;

import java.io.File;

import net.sf.javaml.core.Dataset;
import net.sf.javaml.tools.data.ARFFHandler;

public class TutorialARFFLoader {

	 public static void main(String[] args) throws Exception {
	        Dataset data = ARFFHandler.loadARFF(new File("data/iris.arff"), 4);
	        System.out.println(data);

	    }
	 
}
