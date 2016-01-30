package tutorials.tools;

import java.io.File;

import net.sf.javaml.core.Dataset;
import net.sf.javaml.tools.data.FileHandler;

public class TutorialStoreData {

	public static void main(String[] args) throws Exception {
        /* Load the iris data set from file */
        Dataset data = FileHandler.loadDataset(new File("data/iris.data"), 4, ",");
        System.out.println(data);
        /* Store the data back to another file */
        FileHandler.exportDataset(data, new File("data/output.txt"));

        data = FileHandler.loadDataset(new File("data/output.txt"), 0,"\t");
        System.out.println(data);
    }
	
}
