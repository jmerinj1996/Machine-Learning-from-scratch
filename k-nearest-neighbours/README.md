# K nearest neigbours from scratch
K nearest neighbour is a Supervised Machine Learning algorithm in which the classification of datapoints is purely based on proximity. 
It checks how many points are close to the point we want to classify.
The value of k must be odd otherwise we will get an even split.
To measure the closeness of datapoints we use Euclidean distance

Disadvantage: 
* The algorithm runs pretty bad on large datasets.

Advantage :
* This algorithm provides both accuracy of the model and confidence in the datapoint
* KNN can work on both linear and non-linear data
* KNN can be threaded heavily

The only formula that's required is the Euclidean distance
###  euclidean distance = sqrt(sum(datapoints - predict_feature)^2))
### How can we fasten the process of k-nearest neigbours? 
We could take a radius and consider all points ourside the radius as outliers.

* Note that increasing the value of k does not necessarily increase Accuracy

Check out the scikit-learn equivalent of this algorithm in the Machine-Learning-using-scikitlearn repository.
