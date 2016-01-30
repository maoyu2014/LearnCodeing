package tutorials.classification;

import java.io.File;
import java.util.Map;

import net.sf.javaml.classification.Classifier;
import net.sf.javaml.classification.KNearestNeighbors;
import net.sf.javaml.classification.evaluation.EvaluateDataset;
import net.sf.javaml.classification.evaluation.PerformanceMeasure;
import net.sf.javaml.core.Dataset;
import net.sf.javaml.tools.data.FileHandler;

public class TutorialEvaluateDataset {

	public static void main(String[] args) throws Exception { 
        Dataset data = FileHandler.loadDataset(new File("data/iris.data"), 4, ",");
        /*
         * Contruct a KNN classifier that uses 5 neighbors to make a decision.
         */
        Classifier knn = new KNearestNeighbors(5);
        knn.buildClassifier(data);

        /*
         * Load a data set for evaluation, this can be a different one, but for
         * this example we use the same one.
         */
        Dataset dataForClassification = FileHandler.loadDataset(new File("data/iris.data"), 4, ",");

        Map<Object, PerformanceMeasure> pm = EvaluateDataset.testDataset(knn, dataForClassification);
        for (Object o : pm.keySet())
            System.out.println(o + ": " + pm.get(o).getAccuracy());

    }
	
}
