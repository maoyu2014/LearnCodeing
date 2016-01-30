package tutorials.featureselection;

import java.io.File;

import net.sf.javaml.core.Dataset;
import net.sf.javaml.featureselection.scoring.GainRatio;
import net.sf.javaml.tools.data.FileHandler;

public class TutorialFeatureScoring {

	/*
	 * 注意这里的feature就是指的attribute，也就是一共有多少列数据，
	 * 最终会给出每一列的分数，分数越高说明这一列越重要
	 */
	public static void main(String[] args) throws Exception {
        /* Load the iris data set */
        Dataset data = FileHandler.loadDataset(new File("data/iris.data"), 4, ",");

        GainRatio ga = new GainRatio();
        /* Apply the algorithm to the data set */
        ga.build(data);
        /* Print out the score of each attribute */
        System.out.println(ga.noAttributes());
        for (int i = 0; i < ga.noAttributes(); i++)
            System.out.println(ga.score(i));
    }
	
}
