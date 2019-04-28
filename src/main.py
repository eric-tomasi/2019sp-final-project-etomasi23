from data.data import generate_df
from points import total_points, final_target_list
from model import filter_df, regression
from viz import plot_trend
import pandas as pd

def main():

    #generate initial dataframe
    df = generate_df('data/query.sql')

    #create two new dataframes- one that contains all data and one that contains a final target list
    points = total_points(df)

    final_targets = final_target_list(points)

    #create ExcelWriter that sends both dataframes to an excel spreadsheet.
    writer = pd.ExcelWriter('data/contest_targets.xlsx', engine='xlsxwriter')

    points.to_excel(writer, sheet_name='data')
    final_targets.to_excel(writer,sheet_name='final_targets')

    writer.save()


    #create roi dataframe to run regression which prints to console and plot trends (actuals and predictions)
    roi = generate_df('data/roi.sql')

    roi = filter_df(roi)
    
    plot_trend(roi)


main()
