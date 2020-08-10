import requests,json
from bs4 import BeautifulSoup

#website used for webscrape
result = requests.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html')
source = result.content

soup = BeautifulSoup(source,'html.parser')

#webscraping from CDC website
total_cases = soup.find_all('span','count')[0]
total_deaths = soup.find_all('span','count')[1]
daily_info = soup.find_all('span','new-cases')
data = [words.text for words in soup.find_all('span','new-cases')]
#---------------------------------------------------------------------------------
def Total_US_Covid_Data():
    for cases in total_cases:
        for deaths in total_deaths:
            print("TOTAL of US COVID Cases: " + cases + "\nTOTAL of US COVID Deaths: " + deaths)
            print('-----------------------------------')
            print("Daily Cases and Deaths: ")
            for daily_cases_and_deaths in data:

                print(daily_cases_and_deaths)
    print('-----------------------------------\n')


user = input("Would You like to be briefed on the COVID-19 data in the United States? (y/n)")
if user == 'y' or user == 'Y':
    Total_US_Covid_Data()

#---------------------------------------------------------------------------------
def Covid_By_State():
    #webscraping from CDC website, getting json part
    result = requests.get('https://www.cdc.gov/covid-data-tracker/Content/CoronaViewJson_01/US_MAP_DATA.json')
    j = result.json()
    print('------------------------------------------------------')

    #input for user to enter state
    user_input = input('enter a state that you want to see COVID data for \n' +
    'otherwise enter (2) and I will show COVID data for All states: ').title().strip()
    for state in j['US_MAP_DATA']:
        number_of_cases =int(state['tot_cases'])
        name = str(state['name'])

        if user_input in name:
            if number_of_cases >=100000:
                print('WARNING HOTSPOT! WEAR a MASK to PREVENT EXPOSURE' )
                print('----------------------------------------------')
                print(f"State: {state['name']}, Total cases: {state['tot_cases']}, Total deaths: {state['tot_death']}")

            else:
                print('please remember to WEAR a MASK to prevent exposure!')
                print('----------------------------------------------')
        elif user_input == '2':
            print(f"State: {state['name']}, Total cases: {state['tot_cases']}, Total deaths: {state['tot_death']}")

#-------------------------------------------------------------------------------

input2 = input("Would You like to see COVID-19 data by state? in the United States? (y/n)")
if input2 == 'y' or input2 == 'Y':
    Covid_By_State()
else:
    print('goodbye')
