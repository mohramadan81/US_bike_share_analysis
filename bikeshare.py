import time
import pandas as pd
#import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
week_days_list = ['sunday', 'monday', 'tuesday', 'wensday', 'thrusday', 'friday', 'all']
 
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city =''
    print('Hello! Let\'s explore some US bikeshare data!')
    while city not in CITY_DATA:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = str(input('specify a city to analyze: ').lower())
        print("you choose city: {}".format(city))
    
    month = ''
    while  month not in months_list:     
        # get user input for month (all, january, february, ... , june)
        month= str(input('enter month or all: ').lower())
        print("you choose month: {}".format(month))
    
    day = ''
    while  day not in week_days_list:
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = str(input("input for day of week (all, monday, tuesday, ... sunday): ").lower())
        print("you choose day: {}".format(day))

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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    
    if month != 'all':
        month = months_list.index(month)+1
        df = df[df['month'] == month] 
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title() ]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("display the most common month: ",df['month'].mode()[0])

    # display the most common day of week
    print("display the most common day of week: ", df['day_of_week'].mode()[0])


    # display the most common start hour
    print("display the most common start hour: ", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("display most commonly used start station: ", df['Start Station'].mode()[0])


    # display most commonly used end station
    print("display most commonly used end station: ", df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['comb_stations'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    print("display most frequent combination of start station and end station trip : ", df['comb_stations'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("display total travel time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("display mean travel time: ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Display counts of user types: ", df['User Type'].value_counts())
    


    # Display counts of gender
    if city != 'washington':
        print(df["Gender"].value_counts())
     
    
    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print("Display earliest, most recent, and most common year of birth: ", int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city, df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
