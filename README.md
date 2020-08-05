# monteCarloPi
This project uses matplotlib,numpy,seaborn to approximate value of Pi.

Monte Carlo method/experiments- computational algorithms that rely on repeated random sampling to obtain numerical results. The underlying concept is to use randomness to solve problems that might be deterministic in principle.

##File Usage
EstimateOutput.PNG - Sample output shown after program run
EstimationGraph.png- Sample graph 
MonteCarloPi.py- Python 3 code to make graphs
PlotPoints.png - sample graph of the circle inscribed in square

##Project Description

In this project, we use this by making a length 1 square and inscribing a circle inside. We then make random points inside of the square, some inside and some not inside and track each of them. Because a circle's area is  π r^2,our circle inside of the square has radius 0.5, giving us an area of  π/4. We know the area of the square must be 1, so taking the ratio of circle over area of square should give  π/4.

 So  π = 4 * (# of points in circle/ # of points in square)
 
 
