package tutorials.classification;

import java.io.File;
import java.util.Map;

import net.sf.javaml.classification.Classifier;
import net.sf.javaml.classification.KNearestNeighbors;
import net.sf.javaml.classification.evaluation.CrossValidation;
import net.sf.javaml.classification.evaluation.PerformanceMeasure;
import net.sf.javaml.core.Dataset;
import net.sf.javaml.tools.data.FileHandler;

public class TutorialCrossValidation {

	public static void main(String[] args) throws Exception {
        /* Load data */
        Dataset data = FileHandler.loadDataset(new File("data/iris.data"), 4, ",");
        /* Construct KNN classifier */
        Classifier knn = new KNearestNeighbors(5);
        /* Construct new cross validation instance with the KNN classifier */
        CrossValidation cv = new CrossValidation(knn);
        /* Perform 5-fold cross-validation on the data set */
        Map<Object, PerformanceMeasure> p = cv.crossValidation(data);

        System.out.println("Accuracy=" + p.get("Iris-setosa").getAccuracy());
        System.out.println(p);

    }
	
}
