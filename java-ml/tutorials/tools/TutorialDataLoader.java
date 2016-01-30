package tutorials.tools;

import java.io.File;
import java.io.IOException;

import net.sf.javaml.core.Dataset;
import net.sf.javaml.tools.data.FileHandler;

public class TutorialDataLoader {

	public static void main(String[] args) throws IOException  {
        Dataset data = FileHandler.loadDataset(new File("data/iris.data"), 4, ",");
        System.out.println(data);
        data = FileHandler.loadSparseDataset(new File("data/smallsparse.tsv"), 0, " ", ":");
        System.out.println(data);

    }
	
}
