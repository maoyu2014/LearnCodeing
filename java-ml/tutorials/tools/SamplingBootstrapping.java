package tutorials.tools;

import java.io.File;
import java.io.IOException;
import java.util.Map;

import be.abeel.util.Pair;
import libsvm.LibSVM;
import net.sf.javaml.classification.Classifier;
import net.sf.javaml.classification.evaluation.EvaluateDataset;
import net.sf.javaml.core.Dataset;
import net.sf.javaml.sampling.Sampling;
import net.sf.javaml.tools.data.FileHandler;

public class SamplingBootstrapping {
	
	public static void main(String[] args) throws IOException {
		
		Dataset data=FileHandler.loadDataset(new File("data/iris.data"),4,",");
		Sampling s=Sampling.SubSampling;
		for(int i=0;i<5;i++){
			Pair<Dataset, Dataset> datas=s.sample(data, (int)(data.size()*0.8), i);
			Classifier c=new LibSVM();
			c.buildClassifier(datas.x());
			Map pms=EvaluateDataset.testDataset(c, datas.y());
			System.out.println(pms);
			
		}
	}
	
}
