# JEERS_Final_Project


---
## Presentation

[Link](https://docs.google.com/presentation/d/1Snf4cU-scyTUzBSdKRYNp5xEPtBvUgXduF_YP0-fb5A/edit?usp=sharing) to Google Slides Presentation

---
### Select Topic

The JEERS group selected to work with the UFC Fighter Data. The Dataset encompasses numerous fighter statistics per match, per player.

---
### Reason

The reason the group chose this dataset is not only because group are UFC enthusiast, they also found the dataset appealing as it contains majorily numerical values. The JEERS group believes there lies plenty of functionality within the dataset and is eager to drive some of these values through machine learning methods to obtain solutions that can answer business questions.

---
### Description

The group will use an all time UFC fight history dataset and machine learning to help determine or predict a future winner in UFC match ups. The dataset was obtained from Kaggle.com.

---
### Questions Data Set Will Answer

Using machine learning algorithms, specifically using Random Forest, can a fight winner be determined based on fighter demographics: weight, weightclass, height, age, reach, stance, previous fight record, fight style and fight statistics.

---
## Description of the data exploration phase of the project

In order to understand what statistics were available within the dataset, as well as identifying which values would be ideal for the Machine Learning model, the team used Excel initially, to skim through the dataset and identify which characteristics of the dataset were preferred as well as locating null values. The dataset encompassed 5144 rows of detailed results between two fighters including, but not limited to, winner, number of rounds, win streaks, average body hits and several more. Some data transformation did occur within Excel, however most of the data clean up was done through Jupyter Notebook.

Jupyter Notebook was used to create two fighter dataframes; a red and blue fighter dataframe. This was done by dropping the columns that pertained to the opposing fighter. The columns were renamed accordingly, and an additional binary "outcome" column was added to both dataframes which kept track if the specified fighter won the match. Futhermore, both fighters dataframe was merged to form the fighter_dataset.csv file which encompasses each fighters individual stats per match.

---
## Description of the analysis phase of the project

The analysis phase consisted of creating four SQL tables using PGadmin to prepare our data for the machine learning model. The tables created are the 'fights', 'fighters', 'records', and 'referees' table. Using the 'fighters' table and joining the 'records' and 'fights' table on fight_id and b_fighter_id, respectively. The combined SQL query was exported as the 'fights_fighters_records_v2.csv' file. This file was used to train and test our machine learning model. 

Using Jupyter Notebook, the CSV file was imported and the number of columns was reduced in an iterative process; columns with null values were filled or dropped according to importance. All objects were converted float64 or int64 variables and encoded. The encoded dataframe was split into training and testing sets. The values for 'X' were all values, with the exception of the 'winner' column which was used for the 'y' values.

The training set was ran through a BalancedRandomForestClassifier machine learning model. a balanced accuracy score test was run multiple times with different iteration of the initial CSV file to find the most accurate score. Our initial accuracy score was 33% but after seperating the womans fighter data, removed any fights with a 'Draw' value in the 'winner' column, and included the mens age record, our models' accuracy increased over 63%

Ultimately we found that keeping our data as binary as possible renders better accuracy for the machine learning model selected; furthermore, we found the top features with the greatest importance to be age, reach, height, and weight.

---

# Technologies Used

## Source Control
Github will be the primary code hosting platform.

## Data Cleaning and Analysis
Excel will be used as an overview to the data. Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python and Jupyter Notebook.

## Database Storage
PostgreSQL is the database we intend to use, and we will integrate AWS to display the data.

## Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. Our training and testing setup is using an 75/25 train-test split ratio. The training set was then fit into a Logistic Regression classifier.

## Dashboard
In addition to using a Flask template, and Googles Slides,  we will also integrate Tableau for a fully functioning and interactive dashboard. It will be hosted on Tableau public.

--- 
## Machine Learning Model

- Description of preliminary data preprocessing (Enrique)

For the preliminary data preprocessing, excel was used as an overview of the dataset downloaded from kaggle. Features with high null values were acknowledged and later dropped or modified. Most of the values were highly numerical with a few being object type variables; however, the initial dataset contained too many columns which were not considered as valuable, such as 'referee name', so the data was broken up into four SQL tables.

- Description of preliminary feature engineering and preliminary feature selection, including their decision-making process (JASON)

For our preliminary features, we decided to first use all of the physical attributes of a fighter, including weight, height, reach, fighter stance, and age. We added in additional features, including weight class, and number of rounds fought to see if the added features would improve the model. We'd like to add in fighter win history data to see if the model improves in our next iteration of the model.

- Description of how data was split into training and testing sets (Riley)

Training and testing sets were split up using an 80/20 approach. This was because the dataset contained over 5000 values allowing us to train our model with plenty of values while still maintaining enough to test with.


- Explanation of model choice, including limitations and benefits (SERGE)

We decided to use supervised machine learning model as we already know the target outcome that we are trying to predict (in other words the outcome is discrete) - whether or not a UFC fighter would win against another UFC fighter, based on demographic and fights data. 

One of the limitations of the Random Forests model is the binary nature of the model’s output. In other words, having “red fighter” win, “blue fighter” win, and “draw” as the three potential outcomes of a fight was not perfect for our research. In order to solve that, we removed all “draws” from the dataset (which didn’t affect the number of rows significantly) and return the model to the binary outcome, which improved the overall model’s accuracy. 

-- BalancedRandomForest
-- Binary dataset returned greater accuracy
-- Limitations: Not as robust as Neural Network. Can have a "black box" effect, making it harder to effectively optimize the machine learning model

-- Benefits: Due to feature size of dataset, it allowed multiple weak learners to create a more accurate and robust prediction engine model. Also, helps with dealing with overfitting, ranks feature importance.

-- Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables)

In an attempt to improve our accuracy score, we moved over to using a logistic regression model approach.

-- Description of how they have trained the model thus far, and any additional training that will take place

We have had eight machine learning iterations in which we have dropped certain features, made our training values all numerical values, replaced null values with the mean values for specific features, and encoded our features to be binary.

-- Description of current accuracy score

When using the BalancedRandomForest model, the best accuracy scores obtained was 64%; Using the logistic regression approach, our accuracy score improved to 69%.

---
## Dashboard

1. Storyboard for Dashboard
- The dashboard will consist of three different areas:
  1. Overview of the UFC (Includes figthers with most wins/fights, fights per weight class, wins by age, etc)
  2. Showing the rise of the UFC (Includes number of fight per year, location of fights, etc)
  3. Showing the findings of the machine learning algorithm (Includes accuracy, confusion maxtric, importance ranking, etc)
- Each of these three parts will guide the viewer along to show why we picked this dataset, what it consists of, and how effectively we were able to build a predictive model with it. 

2. Description of the tool(s) that will be used to create final dashboard
- The main tool used to create the dashboard will be Tableau. Within Tableau we will use interactive bar charts, line charts, pie charts, and treemaps to create the dashboard. 

3. Description of interactive element(s)
- By using Tableau and posting the dashboard on the Tableau public website, viewers can visit the url and interactive with every chart as each offers specific information about each data point so that viewers can learn more about our analysis. 

---
### Questions

Input any questions we have or have had throughout the project timeline.

---
### Encountered Issues/Solutions

1. First version of model only had 34% accuracy.
 - Seperated Men and Women fighters stats.
 
2. Did not include age in dataset.
 - Added age to fighters table.
 - Updated ML model to include missing feature.
 - accuracy improved to 39%
 
3. Accuracy was still low after adding age to dataset. Used reset_index() method and old index appeared as a column in the data, which should not have been a feature
 - Added drop=True to remove the old column with reset_index().
 - Separated women fighters from dataset and will run separately in next deliverable
 - Accuracy increased to 46%

---
## Team Roles

### Deliverable One

1 Jason: Database: PostgreSQL setup at least 2 tables
- Sample data that mimics the expected the expected final database structure or schema
- Draft machine learning module is connected to the provisional database

2 Eric: Presentation
- Selected topic
- Reason why they selected their topic
- Description of their source of data


3 Enrique: Github
- Includes a README.md
- At least one branch for each team member
- Each team member has at least four commits from the duration of the first segment

4 Riley: AWS setup and provisioning
- Question they hope to answer
- Description of the communication protocols

5 Serge: Machine Learning pseudo code
- Takes in data from the provisional database
- Outputs label(s) for input data


### Deliverable Two

1 Jason: Database Join/Adding data to SQL tables, assist with ML
- Sample data that mimics the expected the expected final database structure or schema
- Draft machine learning module is connected to the provisional database
- Database stores static data for use during the project
- Database interfaces with the project in some format (e.g., scraping updates the database, or database connects to the model)
- Includes at least two tables (or collections, if using MongoDB)
- Includes at least one join using the database language (not including any joins in Pandas)
- Includes at least one connection string (using SQLAlchemy or PyMongo)


2 Eric:  Database Connector/Linking to AWS/SQLAlchemy/Django, AWS, or Flask research
- Selected topic
- Reason why they selected their topic
- Description of their source of data
- All code necessary to perform exploratory analysis
- Some code necessary to complete the machine learning portion of the project
- Outline of the project (this may include images, but should be easy to follow and digest)

3 Enrique:  Presentation/ML help
- Includes a README.md
- At least one branch for each team member
- Each team member has at least four commits from the duration of the first segment
- Description of the data exploration phase of the project
- Description of the analysis phase of the project
- Presentations are drafted in Google Slides.

4 Riley: Tableau Dashboard & statistics on data
- Question they hope to answer
- Description of the communication protocols
- Storyboard on Google Slide(s)
- Description of the tool(s) that will be used to create final dashboard
- Description of interactive element(s)

5 Serge:  Create functional Machine Learning model
- Takes in data from the provisional database
- Outputs label(s) for input data
- Description of preliminary data preprocessing
- Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
- Description of how data was split into training and testing sets
- Explanation of model choice, including limitations and benefits


---
- Remove the unnecessary features and encode/scale the features we want to keep
- Get the machine learning model up & running
- Separate men & women fighters

### Deliverable Three

1 Jason: Database Management/Adding data to SQL tables, assist with ML
- Sample data that mimics the expected the expected final database structure or schema
- Draft machine learning module is connected to the provisional database
- Database stores static data for use during the project
- Database interfaces with the project in some format (e.g., scraping updates the database, or database connects to the model)
- Includes at least two tables (or collections, if using MongoDB)
- Includes at least one join using the database language (not including any joins in Pandas)
- Includes at least one connection string (using SQLAlchemy or PyMongo)
- Description of how they have trained the model thus far, and any additional training that will take place


2 Eric:  Presentation/Flask Front-End Developement
- Selected topic
- Reason why they selected their topic
- Description of their source of data
- All code necessary to perform exploratory analysis
- Some code necessary to complete the machine learning portion of the project
- Outline of the project (this may include images, but should be easy to follow and digest)
- Communication Protocols removed
- Created front end webpage for presentation

3 Enrique:  Presentation/ML help
- Includes a README.md
- At least one branch for each team member
- Each team member has at least four commits from the duration of the first segment
- Description of the data exploration phase of the project
- Description of the analysis phase of the project
- Presentations are drafted in Google Slides.
- Technologies, Languages, tools, and algorithms used throughout the project

4 Riley: Tableau Dashboard & statistics on data/Machine Learning Model 
- Question they hope to answer
- Description of the communication protocols
- Storyboard on Google Slide(s)
- Description of the tool(s) that will be used to create final dashboard
- Description of interactive element(s)

5 Serge:  Create functional Machine Learning model
- Takes in data from the provisional database
- Outputs label(s) for input data
- Description of preliminary data preprocessing
- Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
- Description of how data was split into training and testing sets
- Explanation of model choice, including limitations and benefits
- Explanation of changes in model in model choice
- Description of current accuracy score


### Deliverable Four

1 Jason: Database Management/Adding data to SQL tables, assist with ML
- Sample data that mimics the expected the expected final database structure or schema
- Draft machine learning module is connected to the provisional database
- Database stores static data for use during the project
- Database interfaces with the project in some format (e.g., scraping updates the database, or database connects to the model)
- Includes at least two tables (or collections, if using MongoDB)
- Includes at least one join using the database language (not including any joins in Pandas)
- Includes at least one connection string (using SQLAlchemy or PyMongo)
- Description of how they have trained the model thus far, and any additional training that will take place
- Team members present a final project with a fully integrated database.
- Recommendation for future analysis
- Anything the team would have done differently


2 Eric:  Presentation/Flask Front-End Developement
- Selected topic
- Reason why they selected their topic
- Description of their source of data
- All code necessary to perform exploratory analysis
- Some code necessary to complete the machine learning portion of the project
- Outline of the project (this may include images, but should be easy to follow and digest)
- Communication Protocols removed
- Created front end webpage for presentation
- Slides are primarily images or graphics (rather than primarily text)
- Images are clear, in high-definition, and directly illustrative of subject matter

3 Enrique:  Presentation/ML help/Github
- Includes a README.md
- At least one branch for each team member
- Each team member has at least four commits from the duration of the first segment
- Description of the data exploration phase of the project
- Description of the analysis phase of the project
- Presentations are drafted in Google Slides.
- Technologies, Languages, tools, and algorithms used throughout the project
- All code in the master branch is production-ready.
- All code is clean, commented, easy to read, and adheres to a coding standard
- All code necessary to perform exploratory analysis
- All code necessary to complete machine learning portion of project 
- Any images that have been created (at least three)

4 Riley: Tableau Dashboard & statistics on data/Machine Learning Model 
- Question they hope to answer
- Description of the communication protocols
- Storyboard on Google Slide(s)
- Description of the tool(s) that will be used to create final dashboard
- Description of interactive element(s)
- Images from the initial analysis
- Data (images or report) from the machine learning task
- At least one interactive element
- Description and explanation of model’s confusion matrix, including final accuracy score
- Result of analysis

5 Serge:  Create functional Machine Learning model
- Takes in data from the provisional database
- Outputs label(s) for input data
- Description of preliminary data preprocessing
- Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
- Description of how data was split into training and testing sets
- Explanation of model choice, including limitations and benefits
- Explanation of changes in model in model choice
- Description of current accuracy score 
- All code necessary to perform exploratory analysis
- All code necessary to complete machine learning portion of project


- Possible: run neural network to see if performance improves
- Separate MLM by weight class and rerun by weight class & women fighters

Live Presentation
---
- All team members present in equal proportions
- The team demonstrates interactivity of dashboard in real time
- The presentation falls within any time limits provided by instructor 
