import numpy as np
#lists
#create a list and print it
#a list can have multiple data types in it ex: ['Hello', 12, True]
# hall = input('what is the area of hall?')
# kitchen = input('what is the area of kitchen?')
# room = input('what is the area of room?')
# terrace = input('what is the area of terrace?')
# area_of_house = ['Hall:',hall, 'Kitchen:', kitchen, 'Room:', room, 'Terrace:', terrace]
# print(area_of_house)

# Create the areas list
# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# # Print out second element from areas
# print(areas[1])
# # Print out last element from areas
# print(areas[-1])
# # Print out the area of the living room
# print(areas[5])

# # Use slicing to create downstairs
# downstairs = areas[:6]
# # Use slicing to create upstairs
# upstairs = areas[6:]
# # Print out downstairs and upstairs
# print(upstairs)
# print(downstairs)

#access the only living room from the list
# house = [["hallway", 11.25],
#          ["kitchen", 18.0],
#          ["living room", 20.0],
#          ["bedroom", 10.75],
#          ["bathroom", 9.50]]

# print(house[2][0])

# Create the areas list
# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area to 10.50
# areas[-1] = 10.50
# Change "living room" to "chill zone"
# areas[4] = 'Chill Zone'

# print(areas)

# Create the areas list and make some changes
# areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
#          "bedroom", 10.75, "bathroom", 10.50]
# # Add poolhouse data to areas, new list is areas_1
# areas_1 = areas + ['poolhouse', 48.1]
# # Add garage data to areas_1, new list is areas_2
# areas_2 = areas_1 + ['garage', 20.2]
# print(areas_2)

# # Delete the string and float for the "poolhouse" from your areas list.
# # Print the updated areas list.

# del areas_2[10:12]

# print(areas_2)

# Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# # Create areas_copy
# c_areas = list(areas)
# # Change areas_copy
# c_areas[3] = 21.4
# # Print areas
# print(areas, c_areas)

#functions
# Create variables var1 and var2
# var1 = [1, 2, 3, 4]
# var2 = True
# var3 = False
# # Print out type of var1
# print(type(var1))
# # Print out length of var1
# print(len(var1))
# # Convert var2 to an integer: out2
# out2 = int(var2)
# out3 = int(var3)
# print(out2, out3)

# # Create lists first and second
# first = [11.25, 18.0, 20.0]
# second = [10.75, 9.50]
# # Paste together first and second: full
# full = first + second
# print(full)
# # Sort full in descending order: full_sorted
# full_sorted = sorted(full, reverse=True)
# # Print out full_sorted
# print(full_sorted)

#Methods --
# string to experiment with: place
# place = "poolhouse"

# # Use upper() on place: place_up
# place_upper = place.upper()
# # Print out place and place_up
# print(place, place_upper)
# # Print out the number of o's in place
# print(place.count('o'))

# # Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# # Print out the index of the element 20.0
# print(areas.index(20.0))
# # Print out how often 9.50 appears in areas
# print(areas.count(9.50))

# # Use append twice to add poolhouse and garage size
# areas.append(12.5)
# areas.append(27.4)
# # Print out areas
# # print(areas)
# # Reverse the orders of the elements in areas
# areas.reverse() 
# #this actually reverse the string if we assign this to areas = areas.reverse it will return None 
# print(areas)

#Packages
# Import the math package
# import math
# Definition of radius
# r = 0.43
# # Calculate Circumference C = 2pi*r
# C = 2 * math.pi * r
# # Calculate A Area = pi*r(raise to power 2 or r-square)
# A = math.pi * r**2
# # Build printout
# print("Circumference: ", round(C,2))
# print("Area: ", round(A, 2))

# # Import radians function of math package
# from math import radians
# # Definition of radius
# r = 192500
# # Travel distance of Moon over 12 degrees. Store in dist.
# angle = 12
# phi = radians(angle) # getting the radian of the angle
# distance = r*phi # formula to calculate the distance 
# print(distance)

# Import the numpy package as np

# Create list baseball
# baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# # Create a numpy array from baseball: np_baseball
# np_baseball = np.array(baseball)
# # Print out type of np_baseball
# print(type(np_baseball))

# heigth_in = [120, 151.4,95.7, 90.5,100.6]
# # Create a numpy array from height_in: np_height_in
# np_height_in = np.array(heigth_in)
# # Print out np_height_in
# print(np_height_in)
# # Convert np_height_in to m: np_height_m -> to convert it to meters we do height_in * 0.0254
# np_height_m = np_height_in * 0.0254
# # Print np_height_m
# print(np_height_m)

# # Create baseball, a list of lists
# #baseball = [[height, weight]] -> this is for all of them accordingly
# baseball = [[180, 78.4],
#             [215, 102.7],
#             [210, 98.5],
#             [188, 75.2]]
# # Create a 2D numpy array from baseball: np_baseball
# np_baseball = np.array(baseball)
# # Print out the type of np_baseball
# print(type(np_baseball))
# # Print out the shape of np_baseball
# print(np_baseball.shape)

# # Print out the 4th row of np_baseball
# # print(np_baseball[3,:])
# # Select the entire second column of np_baseball: np_weight_lb
# print(np_baseball[:, 1])
# # Print out height of 1st player
# print(np_baseball[0, 0])

#simulate random data for diff sort of calculations
#considering height and weight and then perform the calculation such as:
# mean, median or any other stats funtions

# height = np.round(np.random.normal(1.75, 0.20, 200), 2)
# weight = np.round(np.random.normal(60.32, 15, 200), 2)
# #now we will get these columns together respectively using a function called np.column_stack((column1, column2))
# np_city_data = np.column_stack((height,weight))
# # print(np_city_data)
# print((np_city_data[0,0]))

# #get the mean of all the heights 
# avg_height = np.mean(np_city_data[0:, 0])
# print('Avg height: ', str(avg_height)) 
# #get the median
# med_height = np.median(np_city_data[0:, 0])
# print('Median height: ', str(med_height))
# #get standard deviation and Corelation
# std_height = np.std(np_city_data[0:, 0])
# cor_height = np.corrcoef(np_city_data[0:, 0], np_city_data[0:, 1])
# print('Standard Deviation of Height: ', str(std_height))
# print('Correlation of height: ', str(cor_height))