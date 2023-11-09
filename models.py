from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from data import dataset
X,y=dataset


x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

