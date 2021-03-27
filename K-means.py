#import Numpy for numpy arrays
import numpy as np


#import matplotlib for graphing
import matplotlib.pyplot as plt

#Initialise variable for the number of data points (can be any number you want)
number_of_points = 300

#Initiliase variable for the greatest random number that will be generated (can by any number you want)
max_number_generated = 100

#Declare and Initialise arrays for x and y data (using rand function)
x = np.random.rand(number_of_points)
y = np.random.rand(number_of_points)

#Multiply arrays to create larger numbers
x *= max_number_generated
y *= max_number_generated

#Initalise array of centroid coordinates
centroids = []

#Create random coordinated for centroids (we will use 4)
number_of_centroids = 4
for centroid_number in range(0, number_of_centroids):
    centroids.append([np.random.rand(1) * max_number_generated, 
                      np.random.rand(1) * max_number_generated])


#Boolean to check if centroids are moving or not
isDone = False

#Loop of steps 2 and 3 (see slideshow)
while True:
    #Initialise empty clusters (we will store the points belonging to each cluster here)
    clusters = []
    for centroid_number in range(0, number_of_centroids):
        clusters.append([])
    
    #Variable which will indicate which cluster to add each point to
    cluster = 0
    
    #Create a copy of the centroid coordinates so we can check later if they have moved or not
    centroidsCopy = centroids.copy()
    
    #Loop through every point
    for point in range(0, number_of_points):
        
        #Set distance as infinity or any high number so the if statement below always returns true 
            #the first time it is run
        lowest_distance = float('inf')
        
        #Loop through every centroid and calculate distance from the point
        for centroid_number in range (0, number_of_centroids):
            #Assigning a variable for each centroid (makes reading easier)
            centroid = centroids[centroid_number]
            
            #Calculate distance between centroid and point and check if it is lower
                #than the currently lowest distance
            if lowest_distance > ((x[point] - centroid[0])**2 + (y[point] - centroid[1])**2)**(1/2):
                
                #If the distance just calculated is lower, than make that the new lowest distance
                lowest_distance = ((x[point] - centroid[0])**2 + (y[point] - centroid[1])**2)**(1/2)
                
                #Assign the centroid with the currently lowest distance from the point to the
                    #cluster variable
                cluster = centroid_number
        
        #Add the point to the centroid it has the lowest distance to
        clusters[cluster].append([x[point], y[point]])
    
    #Loop through each centroid
    for centroid_number in range(0, number_of_centroids):
        
        #Make sure not to take take average if there are no points associated with the centroid
        if len(clusters[centroid_number]) != 0:
            
            #Take average of x and y coordinates
            sumx = 0
            sumy = 0
            avex = 0
            avey = 0
            #Loops through each point associated with a centroid to sum all coordinate values
            for coordinate in range(0, len(clusters[centroid_number])):
                sumx += clusters[centroid_number][coordinate][0]
                sumy += clusters[centroid_number][coordinate][1]
            avex = sumx/len(clusters[centroid_number])
            #Change the centroid position to the average coordinates
            avey = sumy/len(clusters[centroid_number])
            centroids[centroid_number] = [avex, avey]
    
    #Check if the newly calculated centroids have the same coordinates as the old centroids
    for centroid_number in range(0, number_of_centroids):
        if centroids[centroid_number][0] - centroidsCopy[centroid_number][0] == 0 or centroids[centroid_number][1] - centroidsCopy[centroid_number][1] == 5:
            isDone = True
        else:
            isDone = False
    if isDone:
        break

#Plot points (with different colour for different clusters)
for coord in clusters[0]:
    plt.plot(coord[0], coord[1], 'ro')
for coord in clusters[1]:
    plt.plot(coord[0], coord[1], 'bo')
for coord in clusters[2]:
    plt.plot(coord[0], coord[1], 'go')
for coord in clusters[3]:
    plt.plot(coord[0], coord[1], 'yo')

#Plot centroids
plt.plot(centroids[0][0], centroids[0][1], 'ks')
plt.plot(centroids[1][0], centroids[1][1], 'ks')
plt.plot(centroids[2][0], centroids[2][1], 'ks')
plt.plot(centroids[3][0], centroids[3][1], 'ks')
plt.show()