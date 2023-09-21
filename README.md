# amadeusChallenge
This repository contains the code for the Amadeus challenge about users and airports
The objective of the challenge is to read two datasets, with the users and their geographical positions, while the other contains the code of an airport along with its geographical positions. The objective of the challenge is to generate an output where for each user the airport that is closest in geographical position and in this way deliver the appropriate advertising to each user.
Initially we will use the gzip library to read the files and in this way create the analysis dataframe, later a label will be added to each airport for subsequent analysis.
To determine the distance of each user from the airports, a function will be created that calculates the Euclidean distance between two points. This function will be used to evaluate each user with all airports and in this way mark the value with the shortest distance.
The labels are assigned to each user and as a subsequent step this information is crossed with that of the airport to generate an output of the user ID (uuid) and the code of each airport (iata_code).
Note: a variable called "long" has been generated that for testing purposes reduces the number of records in the files. If you want to run the test in its entirety, you can assign the value of 1 to this variable.
