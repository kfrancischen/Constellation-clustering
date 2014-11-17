### Constellation-clustering

CS 229 Project for constellation clustering. It contains a command version and a GUI version.

Author: Kaifeng Chen, <kfrancischen@gmail.com>.
#### List of files:     
1. **dataProcessing.py**: function for database processing
2. **algorithms.py**: script containing all the algorithm classes.
3. **basicFun.py**: script including all the basic and commonly used functions.
4. **visualization.py**: script of doing 3D visualization.
5. **clustering.py**: main script of runing the proper algorithm and generate figure.
6. **database.json**: database for stars.

#### Running Command Version:
Running **Kmeans**:
```shellscript
  python clustering.py -a Kmeans k [the k value]
```
Running **DBSCAN**:
```shellscript
  python clustering.py -a DBSCAN eps [the eps value] mindist [the mindist value]
```
#### Running GUI Version:
```shellscript
  python main.py
```
#### Requirements:
1. [scipy](http://www.scipy.org/), [numpy](http://www.numpy.org/).
2. [sklearn](http://scikit-learn.org/stable/): package for machine learning.
3. additional requirement for GUI version: [PyQt5](http://www.riverbankcomputing.com/software/pyqt/download5).
