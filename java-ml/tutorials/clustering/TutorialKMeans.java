package tutorials.clustering;

import java.io.File;

import net.sf.javaml.clustering.Clusterer;
import net.sf.javaml.clustering.KMeans;
import net.sf.javaml.core.Dataset;
import net.sf.javaml.tools.data.FileHandler;

public class TutorialKMeans {

	 /**
     * Tests the k-means algorithm with default parameter settings.
     */
    public static void main(String[] args) throws Exception {

        /* Load a dataset */
        Dataset data = FileHandler.loadDataset(new File("data/iris.data"), 4, ",");
        /*
         * Create a new instance of the KMeans algorithm, with no options
         * specified. By default this will generate 4 clusters.
         */
        Clusterer km = new KMeans();
        /*
         * Cluster the data, it will be returned as an array of data sets, with
         * each dataset representing a cluster
         */
        Dataset[] clusters = km.cluster(data);
        System.out.println("Cluster count: " + clusters.length);
        for (Dataset clu : clusters) {
        	System.out.println(clu);
        }

    }
    
}
