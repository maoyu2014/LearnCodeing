package tutorials.classification;

import java.io.File;
import java.io.IOException;

import net.sf.javaml.core.Dataset;
import net.sf.javaml.tools.data.FileHandler;

public enum TutorialData {

	IRIS("data/iris.data", 4, ",",null), SPARSE("data/sparse.tsv", 0, " ",":");

	private String file;
	private int classIndex;
	private String sep;
	private String sep2;

	private TutorialData(String file, int classindex, String sep, String sep2) {
		this.file = file;
		this.classIndex = classindex;
		this.sep = sep;
		this.sep2 = sep2;
	}

	public Dataset load() throws IOException {
		if (sep2 == null)
			return FileHandler.loadDataset(new File(file), classIndex, sep);
		else
			return FileHandler.loadSparseDataset(new File(file), classIndex, sep, sep2);
	}
	
}
