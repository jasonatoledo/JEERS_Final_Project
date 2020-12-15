# JEERS_Final_Project



## Presentation

[Link](https://docs.google.com/presentation/d/1Snf4cU-scyTUzBSdKRYNp5xEPtBvUgXduF_YP0-fb5A/edit?usp=sharing) to Google Slides Presentation


### Select Topic

The JEERS group selected to work with the UFC Fighter Data. The Dataset encompasses numerous fighter statistics per match, per player.

### Reason

The reason the group chose this dataset is not only because group are UFC enthusiast, they also found the dataset appealing as it contains majorily numerical values. The JEERS group believes there lies plenty of functionality within the dataset and is eager to drive some of these values through machine learning methods to obtain solutions that can answer business questions.
 
### Description

The group will use an all time UFC fight history dataset and machine learning to help determine or predict a future winner in UFC match ups. The dataset was obtained from Kaggle.com.

### Questions Data Set Will Answer

Using machine learning algorithms, specifically using Random Forest, can a fight winner be determined based on fighter demographics: weight, weightclass, height, age, reach, stance, previous fight record, fight style and fight statistics.

### Description of the data exploration phase of the project

In order to understand what statistics were available within the dataset, as well as identifying which values would be ideal for the Machine Learning model, the team used Excel initially, to skim through the dataset and identify which characteristics of the dataset were preferred as well as locating null values. The dataset encompassed 5144 rows of detailed results between two fighters including, but not limited to, winner, number of rounds, win streaks, average body hits and several more. Some data transformation did occur within Excel, however most of the data clean up was done through Jupyter Notebook.

Jupyter Notebook was used to create two fighter dataframes; a red and blue fighter dataframe. This was done by dropping the columns that pertained to the opposing fighter. The columns were renamed accordingly, and an additional binary "outcome" column was added to both dataframes which kept track if the specified fighter won the match. Futhermore, both fighters dataframe was merged to form the fighter_dataset.csv file which encompasses each fighters individual stats per match.

### Description of the analysis phase of the project

- In progress...
  
## Technology Used in Project

- Github
- PostgreSQL
- Python / Machine Learning
- Google Docs
- Tableau
- AWS
- Excel

## Communication

In order to avoid any ambiguity during the process of the project, the JEERS group will meet a minimum of two days a week on Zoom while maintaing a clear line of communication via Slack, text and Google Drive. 
The team will assign roles to each member to maximize productivity and mitigate mistakes. Each team member will create their own branch to work independently from the main branch and will only merge their branches once they have tested that their segment of the project is functional and integrates seamlessly with the main branch.

## Machine Learning Model

- Description of preliminary data preprocessing

- Description of preliminary feature engineering and preliminary feature selection, including their decision-making process (JASON)

- Description of how data was split into training and testing sets

- Explanation of model choice, including limitations and benefits (SERGE)

## Dashboard

1. Storyboard for Dashboard
- The dashboard will consist of three different areas:
  1. Overview of the UFC (Includes figthers with most wins/fights, fights per weight class, wins by age, etc)
  2. Showing the rise of the UFC (Includes number of fight per year, location of fights, etc)
  3. Showing the findings of the machine learning algorithm (Includes accuracy, confusion maxtric, importance ranking, etc)
- Each of these three parts will guide the viewer along to show why we picked this dataset, what it consists of, and how effectively we were able to build a predictive model with it. 

2. Description of the tool(s) that will be used to create final dashboard

3. Description of interactive element(s)

### Questions

Input any questions we have or have had throughout the project timeline.

### Encountered Issues/Solutions

1. First version of model only had 34% accuracy.
 - Seperated Men and Women fighters stats.
 
2. Did not include age in dataset.
 - Added age to fighters table.
 - Updated ML model to include missing feature.


## Team Roles

### Deliverable One

- Jason: Database: PostgreSQL setup at least 2 tables
- Eric: Presentation/README.md Update  
- Enrique: Github/Readme
- Riley: AWS setup and provisioning
- Serge: Machine Learning pseudo code

### Deliverable Two

- Jason: Database Join/Adding data to SQL tables, assist with ML
- Eric:  Database Connector/Linking to AWS/SQLAlchemy/Django, AWS, or Flask research
- Enrique:  Presentation/ML help/Github
- Riley:  Tableau Dashboard & statistics on data
- Serge:  Create functional Machine Learning model

- Remove the unnecessary features and encode/scale the features we want to keep
- Get the machine learning model up & running
- Separate men & women fighters

### Deliverable Three

- Jason:  
- Eric:  
- Enrique:  
- Riley:  
- Serge:  

- Separate MLM by weight class and rerun by weight class & women fighters
- Merge records data table to best model to improve performance (hopefully)


### Deliverable Four

- Jason:  
- Eric:  
- Enrique:  
- Riley:  
- Serge:  

- Possible: run neural network to see if performance improves

Presentation: 15 min total: 10-13 min presentation and 2-3 min for Q&I
