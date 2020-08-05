'''
Monte Carlo to calculate the value of Pi
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PlotWidth = 8

def MonteCarloPi(numDataPoints, numDecimalPoints=4 ,numCirclePoints = 360):
    #Draw a square and circle
    squareX = [1,-1,-1,1,1]
    squareY = [1,1,-1,-1,1]

    circleX = (np.cos(np.pi * np.arange(numCirclePoints +1) / 180))
    circleY = (np.sin(np.pi * np.arange(numCirclePoints +1) / 180))

    dfMonteCarloPi = pd.DataFrame(columns=['x','y','r','Location','CurrentPi'])
    #np.random.rand makes a number in the range [0,1], so this function makes ranges of [-1,1]
    dfMonteCarloPi['x'] = 2*(np.random.rand(numDataPoints)-0.5)
    dfMonteCarloPi['y'] = 2*(np.random.rand(numDataPoints)-0.5)
    #Radius, Tells us where the point is, whether inside or outside of the circle
    dfMonteCarloPi['r'] = np.sqrt(dfMonteCarloPi['x']**2 + dfMonteCarloPi['y']**2)
    dfMonteCarloPi.loc[dfMonteCarloPi['r'] <=1, 'Location'] = 'Inside'
    dfMonteCarloPi.loc[dfMonteCarloPi['r'] > 1, 'Location'] = 'Outside'
    dfMonteCarloPi['CurrentPi'] = 4*(dfMonteCarloPi['Location'] == 'Inside').cumsum()/(dfMonteCarloPi.index-1)

    piValue = np.round(np.array(dfMonteCarloPi['CurrentPi'])[-1],numDecimalPoints)
    #Rounds the percentage that pi is off of actual pi to 4 decimal places, then again to the number of decimal points given from function
    piError = np.round(round(100*((piValue-np.pi)/np.pi),4), numDecimalPoints)

    #Draw a 2D plot
    plt.figure(figsize=(PlotWidth,PlotWidth))
    plt.plot(squareX,squareY, color = '#000000')
    plt.plot(circleX,circleY, color = '#0000CC')
    sns.scatterplot(x='x', y='y', data= dfMonteCarloPi, hue='Location', palette= 'colorblind')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(bbox_to_anchor=(0,-.08), loc='upper left')
    plt.title('Locations of randomly drawn points')
    plt.show()

    #Draw a psuedo-time series plot of current estiamte of pi vs iteration number
    plt.figure(figsize=(PlotWidth,PlotWidth))
    plt.plot(dfMonteCarloPi.index+1, dfMonteCarloPi['CurrentPi'], color ='#009900')
    plt.axhline(y=np.pi,color = '#0F0F0F', ls ='--')
    plt.xlim(0, numDataPoints+1)
    plt.ylim(0,4)
    plt.xlabel('Iteration Number')
    plt.ylabel('Estimate for pi')
    plt.title('Current estimate for pi by iteration number')
    plt.show()

    print('\n' + f'Pi is approximately {piValue}') 
    print(f'This is {piError}% off the true value. \n')

MonteCarloPi(5000)