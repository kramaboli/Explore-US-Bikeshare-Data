import pandas as pd
import time
import numpy as np

#dictionary to hold cities and the recorded information of users using bikeshare bikes
bikeshare_cities = { 'chicago': 'chicago.csv',
                     'new york city': 'new_york_city.csv',
                     'washington': 'washington.csv' }

#Two lists that contain months and days that the bikeshare service is used by the customers
bikeshare_months = ['january','february','march','april','may','june','all']
bikeshare_weekdays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']


def get_filters():
    """
    Prompt user to specify a city, month, and day to analyze Bike share data.The user input method ignores case sensitivity as long as the         spelling is correct!

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\n------------------WELCOME TO BIKESHARE SYSTEM---------------------\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("\n[Please Select the city you would like to view Bikeshare data within :[New York City, Chicago or Washington]?\n").lower()
      if city not in bikeshare_cities:
        print("Invalid city selection,Please try again!!!")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\n[Please select Particular month [January - June] or [all] to view Bikeshare data on monthly basis :]\n").lower()
      if month not in bikeshare_months :
        print("Invalid month selection,Please try again!!!")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\n[Please select a partucular day or select all days to view Bikeshare data on daily basis : [all, Monday - Tuesday]\n").lower()
      if day not in bikeshare_weekdays :
        print("Invalid day selection,Please try again!!!")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(bikeshare_cities[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month,day and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month = bikeshare_months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] ==month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
 

def Know_Your_Customer_Stats(df):
    """The function Display the detailed information of users using Bikeshare system from 3 different Cities"""
    print('**************YOU HAVE REACHED BIKESHARE KNOW_YOUR_CUSTOMER MENU***************\n')
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Categories Avalaible :\n',user_types)
    
    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Categories Available :\n',gender_types)
    except KeyError:
      print("\nGender Categories Available :\nThere is no Gender data available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Birth Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Birth Year:\nThere is no data available!.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Birth Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Birth Year:\nThere is no data available!.")

    try:
      Most_Common_Year = df['Birth Year'].mode()[0]
      print('\nMost Common Birth Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Birth Year:\nThere is no data available!.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
   
def station_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('**************YOU HAVE REACHED BIKESHARE STATION STATISTICS MENU***************\n')
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_Common_Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station :', Most_Common_Start_Station)


    # TO DO: display most commonly used end station
    Most_Common_End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station :',  Most_Common_End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    Most_Frequent_Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start and end stations:', Most_Common_Start_Station, " & ",                   Most_Common_End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""
    print('**************YOU HAVE REACHED BIKESHARE TIME STATISTICS MENU***************\n')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    if most_common_month == 1:
        print('Most Common Month: January')
    elif most_common_month == 2:
        print('Most Common Month: February')
    elif most_common_month == 3:
        print('Most Common Month: March')
    elif most_common_month == 4:
        print('Most Common Month: April')
    elif most_common_month == 5:
        print('Most Common Month: May')
    elif most_common_month == 6:
        print('Most Common Month: June')

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', most_common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('**************YOU HAVE REACHED BIKESHARE TRIP DURATION STATISTICS MENU***************\n')
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time)

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def Bikeshare_Raw_Data(df):
    """ Displays raw data of the selected city in rows of 5 till the end of rows """
    
    #Prompts user if they want to view raw data
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    
    #As long as the user wants to see raw data, keep showing data in rows of 5
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

    


      
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        Know_Your_Customer_Stats(df)
        time_stats(df)
        trip_duration_stats(df)
        station_stats(df)
        Bikeshare_Raw_Data(df)
       
        
        
        restart = input('\nWould you like to go back to the main Menu? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break   

if __name__ == "__main__":
	main()
