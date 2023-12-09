https://static.vecteezy.com/ti/vecteur-libre/p3/2453856-chimie-flacon-dessin-anime-gratuit-vectoriel.jpg

# Python_DataAnalysis_Final_Project
QSAR Biodegradation :

- RB = ready biodegradable
- NRB = not ready biodegradable 


# If you want to run the django file : 
1) go to .../django in the terminal
2) write "py manage.py runserver" in the terminal
3) write this url : http://127.0.0.1:8000/polls/ in a web page


# What we've done : 
- Import the dataset (with pandas)
- Clean the dataset (null values, outliers values)
- Normalize the data (we used a sklearn library)
- We did the correlation matrix (to delete correlated columns)
- Some visualization (% and distribution of RB and NRB)
- We used some models to find the experimental class with the other columns (RandomForest, SVC, KNN, Logistic regression)
- Use django to put our visualization
