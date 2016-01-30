package tutorials.tools;

import net.sf.javaml.core.Dataset;
import net.sf.javaml.core.DefaultDataset;
import net.sf.javaml.core.Instance;
import net.sf.javaml.filter.normalize.NormalizeMidrange;
import net.sf.javaml.tools.InstanceTools;

public class Normalization {
	public static void main(String[] args) {
		/* Create data set with random instances */
		Dataset data=new DefaultDataset();
		for(int i=0;i<100;i++){
		  Instance rgA=InstanceTools.randomInstance(5);
		  data.add(rgA);
		}
		NormalizeMidrange nmr=new NormalizeMidrange(0.5,1);
		/* Instanciate new filter */
		nmr.build(data);
		 
		Instance rgB=InstanceTools.randomInstance(5);
		/* Filter another instances */
		nmr.filter(rgB);
		
		//归一化结束后，原始数据就被改变了，可以打印出来看看
		System.out.println(data);
		System.out.println(rgB);
	}
}
