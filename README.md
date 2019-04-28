# Case Study: Exploring Pandas, Matplotlib, and Regression for Custom Targeting

## Background:

For my final project, I opted to solve a work-related problem by automating a complicated process using Python.  I currently work in the pharmaceutical industry in a commercial operations function. One of the key responsibilities of the commercial organization is to determine which doctors should be targeted by sales representatives. That is, sales representatives from each territory across the country must find out which doctors they should speak to so they can educate them about our company’s products. The role of the commercial group is to help sales representatives pick which doctors they should focus on since there are hundreds of thousands to choose from in the database. My company is implementing a contest in which sales representatives must target doctors in which we are losing market share. My job is to select the best targets which will represent the greatest opportunity for my company. 


## Previous Process:

The first time these targets were selected, a manual process was used to run SQL queries, paste the results into Excel, and manipulate Excel with complicated formulas, sorting, and filtering. We scored each doctor based on a number of variables and calculated the total score for each one. This was used to select the top 20 doctors for each territory based on the total score. However, if requirements changed, it was very cumbersome and processes needed to be rerun from the beginning. In the end, multiple Excel spreadsheets cluttered my workspace, causing confusion which led to little confidence in the results. 


## Goal:

The goal of this project is to move away from a manual, Excel based approach, and codify the process using Python. When this process needs to be re-ran, the Python script can be executed and all necessary outputs will be saved without any manual intervention. There were 4 main milestones for this project. 

1. Connect to Oracle DB so SQL queries can be run and interpreted by Python. The result sets of these queries are added to Pandas dataframes, manipulated with Python code, and the outputs are saved back to a spreadsheet. The spreadsheet contains two tabs: one for the raw data with the added calculated fields and total score, and one with the final target list. 

2. Create a linear regression model to aid in determining ROI. Since the contest is aimed at those who are declining in market share, naturally the volume of this group is decreasing. If we had done nothing about this group, we would expect them to continue decreasing. Therefore a regression model was created to observe where the volume of these doctors would be in the future had no preventative actions taken place. Once the contest is over, we will compare to this regression trend line and see where the volume ended up, compared to where we predicted it would end up. The difference between the two represents and estimate of the ROI of the contest. 

3. Visualize trends using Matplotlib to display the actual trend, and the regression trendline with upper and lower bounds. Visualizing the trends was important in presenting to senior management to gain their support that a break even could be achieved. Previously, the regression and the plotting were performed in Excel, which was again a cumbersome process and not repeatable. 

4. Focus on reproducibility and security.  A focus of this project was to ensure that the entire process can be run from end to end without any manual intervention. To do this, pipenv was utilized to ensure the proper dependencies were captured and locked. Additionally, security was a top concern so secret database credentials were stored in a .env file and not added to version control systems. Finally, any corporate IDs were hashed using sha256 and salted to ensure randomness. 


## Design:

Within the src directory, there is a subdirectory called data. This is where any outputs will be saved and also where data.py lives. Data.py defines various functions to load data from a SQL database to a pandas dataframe and provides functionality to hash the IDs if needed. 

Under the src directory, there are 4 core python files: points.py, model.py, viz.py, and main.py. Points.py defines several functions that use the pandas dataframe to run calculations. These calculations are used to score each record. The functions are applied to the dataframe and a total points column is created. To generate the final target list, the dataframe is sorted and ranked by those with the highest points. The dataframe with the full column list and calculations as well as the final target list are sent to Excel in main.py.

Model.py is where the linear regression is implemented. I utilized statsmodels and scipy to run the regression and calculate the upper and lower bounds using a 95% confidence interval. A dataframe is returned by the regression() function which is used for visualization purposes. 

Viz.py contains a function which plots the trend of the actual data, as well as the regression trendline in a single plot. Matplotlib and seaborn are utilized for this. Additionally, the actual data is smoothed so it is visually more appealing in the final chart. The plot is saved as a .png in the data subdirectory. 

Finally, main.py is used as an interface between all of the previously mentioned python files. This file imports the needed functions from the others and uses them to generate the outputs. 


## Usage:

To run the script, simply execute “pipenv run python main.py” and this will run all of the required functions. There will be two main outputs. First is an Excel spreadsheet that contains two tabs: one for the raw data with calculations for the points, and one for the final target list. Second is a .png of the plot of the actual data and regression trendline. 
