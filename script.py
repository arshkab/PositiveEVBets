import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
#import requests
#from bs4 import BeautifulSoup
import urllib.request
import re
from collections import defaultdict

# s = Service("./drivers/chromedriver")
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--start-maximized") #open Browser in maximized mode
# options.add_argument("--no-sandbox") #bypass OS security model

# options.add_argument("--remote-debugging-port=9230")
# options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# browser = webdriver.Chrome(service=s,options=options)
#Scraping test
# website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
# browser.get(website)
# #used to click the button
# all_matches_button = browser.find_element(by=By.XPATH,value='//label[@analytics-event="All matches"]')
# # click on a button
# all_matches_button.click()



def draft_kings_hockey():
# # DONE
    website1 = 'https://sportsbook.draftkings.com/leagues/hockey/88670853?category=player-props&subcategory=points'
    browser.get(website1)
    player_prop = browser.find_elements(by=By.CLASS_NAME,value = 'sportsbook-table__body')
    player_names = []
    goal_scorers = []
    dict = {}
    counter = 0
    for i in player_prop:
        print(i.text)
        data = i.text
        print("---")
    split_data = data.split("\n")
    for i in split_data:
        if counter == 0:
            player = i
            dict[player] = []
            counter = counter + 1
        elif counter == 6:
            dict[player].append(i)
            counter = 0
        else:
            dict[player].append(i)
            counter = counter + 1

    print(dict)
def draft_kings_baseball_odds(website_hr):
    s = Service("./drivers/geckodriver")
    options = FirefoxOptions()
    options.headless = True
    browser = webdriver.Firefox(service=s,options = options)
    browser.get(website_hr)
    print('Title: %s' % browser.title)
    dict = {}
    player_prop3 = browser.find_elements(by=By.CLASS_NAME,value = 'sportsbook-table__body')
    #print(player_prop3)
    games = []
    counter = 0
    for i in player_prop3:
        #print(i.text)
        data = i.text
        #data.split
        games.append(data.split("\n"))
        #print("---")


    #print("games",games)
    for i in games:
        for j in i:
            if counter == 0:
                player = j
                dict[player] = []
                counter = counter + 1
            elif counter == 6:
                dict[player].append(j)
                counter = 0
            else:
                dict[player].append(j)
                counter = counter + 1
    print(dict)
    return dict

    
    

#Old: bases_dk,home_runs_dk,earned_runs_dk,hits_allowed_dk,pitching_outs_dk,strikeouts_dk = draft_kings_baseball_odds('https://sportsbook.draftkings.ewffw/leagues/baseball/88670847?category=batter-props&subcategory=total-bases'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=batter-props&subcategory=home-runs'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=pitcher-props&subcategory=earned-runs'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=pitcher-props&subcategory=hits-allowed'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=pitcher-props&subcategory=outs-recorded'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=pitcher-props&subcategory=strikeouts')
bases_dk,home_runs_dk,earned_runs_dk,hits_allowed_dk,pitching_outs_dk,strikeouts_dk = draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/mlb?category=batter-props&subcategory=total-bases'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/mlb?category=batter-props&subcategory=home-runs'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/mlb?category=pitcher-props&subcategory=earned-runs'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/mlb?category=pitcher-props&subcategory=hits-allowed'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/mlb?category=pitcher-props&subcategory=outs-recorded'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/mlb?category=pitcher-props&subcategory=strikeouts')

#draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=batter-props&subcategory=total-bases')
print('********************')
#draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=batter-props&subcategory=hits')

#EDGE CASE THAT NEEDS TO BE FIXED LATER: IDENTIFY ODDS THAT ARE LOCKED 
def pinnacle_baseball_player_props(website):

    s = Service("./drivers/geckodriver")
    options = FirefoxOptions()
    options.headless = True
    browser = webdriver.Firefox(service=s,options = options)
    browser.get(website)
    #print('Title: %s' % browser.title)
    player_prop = browser.find_elements(by='id',value = 'root')
    #print(player_prop[0].text)
    bases,bases_arr,counter, detected = "Bases",{},0,False
    home_runs,home_runs_arr,counter_hr,detected_hr = "Home Runs",{},0,False
    earned_runs, earned_runs_arr, counter_runs, detected_runs = "Earned Runs",{},0,False
    hits_allowed, hits_allowed_arr, counter_hits, detected_hits = "Hits Allowed",{},0,False
    pitching_outs, pitching_outs_arr, counter_pitches, detected_pitch = "Pitching Outs",{},0,False
    strikeouts, strikeouts_arr,counter_st,detected_st  = "Strikeouts",{},0,False
    for i in player_prop:
        #print(i)
        data = i.text
        split_data = data.split("\n")
        for j in split_data:
            
            if bases in j:
                if counter == 0:
                    #print(j)
                    player_bases = j.replace(" (Total Bases)(must start)","")
                    
                    bases_arr[player_bases] = []
                    detected = True
                    counter = counter + 1
            if home_runs in j:
                 if counter_hr == 0:
                    #print(j)
                    player_hrs = j.replace(" (Home Runs)(must start)","")
                   
                    home_runs_arr[player_hrs] = []
                    detected_hr = True
                    counter_hr = counter_hr + 1
            if earned_runs in j:
                 if counter_runs == 0:
                    #print(j)
                    player_runs = j.replace(" (Earned Runs)(must start)","")
                    earned_runs_arr[player_runs] = []
                    detected_runs = True
                    counter_runs = counter_runs + 1
            
            if hits_allowed in j:
                 if counter_hits == 0:
                    #print(j)
                    player_hits = j.replace(" (Hits Allowed)(must start)","")
                    hits_allowed_arr[player_hits] = []
                    detected_hits = True
                    counter_hits = counter_hits + 1
            if pitching_outs in j:
                 if counter_pitches == 0:
                    #print(j)
                    player_pitches = j.replace(" (Pitching Outs)(must start)","")
                    pitching_outs_arr[player_pitches] = []
                    detected_pitch = True
                    counter_pitches = counter_pitches + 1
            
            if strikeouts in j:
                 if counter_st == 0:
                    #print(j)
                    player_st = j.replace(" (Total Strikeouts)(must start)","")
                    strikeouts_arr[player_st] = []
                    detected_st = True
                    counter_st = counter_st + 1
            
            if detected == True:
                if counter == 5:
                    bases_arr[player_bases].append(j)
                    detected = False
                    counter = 0
                elif(counter == 1):
                    counter = counter + 1
                else:
                    bases_arr[player_bases].append(j)
                    counter = counter + 1
            if detected_hr == True:
                if counter_hr == 5:
                    home_runs_arr[player_hrs].append(j)
                    detected_hr = False
                    counter_hr = 0
                elif(counter_hr == 1):
                    counter_hr = counter_hr + 1
                else:
                    home_runs_arr[player_hrs].append(j)
                    counter_hr = counter_hr + 1
            if detected_runs == True:
                if counter_runs == 5:
                    earned_runs_arr[player_runs].append(j)
                    detected_runs = False
                    counter_runs = 0
                elif(counter_runs== 1):
                    counter_runs = counter_runs + 1
                else:
                    earned_runs_arr[player_runs].append(j)
                    counter_runs = counter_runs + 1
            if detected_hits == True:
                if counter_hits == 5:
                    hits_allowed_arr[player_hits].append(j)
                    detected_hits = False
                    counter_hits = 0
                elif(counter_hits == 1):
                    counter_hits = counter_hits + 1
                else:
                    hits_allowed_arr[player_hits].append(j)
                    counter_hits = counter_hits + 1
                    
            if detected_pitch == True:
                if counter_pitches == 5:
                    pitching_outs_arr[player_pitches].append(j)
                    detected_pitch = False
                    counter_pitches = 0
                elif(counter_pitches == 1):
                    counter_pitches = counter_pitches + 1
                else:
                    pitching_outs_arr[player_pitches].append(j)
                    counter_pitches = counter_pitches + 1

            if detected_st == True:
                if counter_st == 5:
                    strikeouts_arr[player_st].append(j)
                    detected_st = False
                    counter_st = 0
                elif(counter_st == 1):
                    counter_st = counter_st + 1
                else:
                    strikeouts_arr[player_st].append(j)
                    counter_st = counter_st + 1             
    #print(bases_arr)
    # print(earned_runs_arr)
    # print(hits_allowed_arr)
    # print(pitching_outs_arr)
    # print(strikeouts_arr)
    return bases_arr,home_runs_arr,earned_runs_arr,hits_allowed_arr,pitching_outs_arr,strikeouts_arr
        

#draft_kings_hockey()
#bases_pinnacle,home_runs_pinnacle,earned_runs_pinnacle,hits_allowed_pinnacle,pitching_outs_pinnacle,strikeouts_pinnacle = pinnacle_baseball_player_props('https://www.pinnacle.com/en/baseball/mlb/arizona-diamondbacks-vs-colorado-rockies/1554940577#player-props')


#For some reason only works on the root id
#redo to automate it
#not done yet; dict placement isn't finished
def pinnacle_player_prop():
    website2 = 'https://www.pinnacle.com/en/hockey/nhl/colorado-avalanche-vs-tampa-bay-lightning/1554901383#player-props'
    browser.get(website2)
    print('Title: %s' % browser.title)
    player_prop4 = browser.find_elements(by='id',value = 'root')
    print(type(player_prop4))
    print(len(player_prop4))
    print("00000000000000000000000000000000000")
    points = "Points"
    detected = False
    dict = {}
    for i in player_prop4:
        data = i.text
        print("Dta",data)
        split_data = data.split("\n")
        for j in split_data:
            counter = 0
            if points in j:
                print(j)
                print("----")
                #counter = counter + 1
                #if counter == 1:
                player = j.replace(" (Points)(must play)","")
                print("Player",player)
                dict[player] = []
                detected = True
            if detected == True:

                if counter == 4:
                    dict[player].append(j)
                    detected = False
                else:
                    dict[player].append(j)
                    counter = counter + 1
    print(dict)

#pinnacle_baseball_player_props('https://www.pinnacle.com/en/baseball/mlb/colorado-rockies-vs-los-angeles-dodgers/1555018363#player-props')



def testing():
    #TEST 2
    # website = 'https://sports.tipico.de/en/all/football/spain'
    # browser.get(website)
    # #box = browser.find_element(by=By.XPATH,value='//div[contains(@testid, "Program_SELECTION")]')
    # sport_title = browser.find_elements(by=By.CLASS_NAME,value = 'styles-app-structure-program')
    # print(sport_title[0].text)
    # #print(sport_title[0].get_attribute('innerHTML'))
    # parent = sport_title[0].find_element(by=By.XPATH,value='./..')
    # #print(parent)
    # #print(parent.get_attribute('innerHTML'))
    # grandparent = sport_title[0].find_element(by=By.XPATH,value='./..')
    # print(grandparent[0].text)
    # soup = BeautifulSoup(browser.page_source, 'html.parser')
    # #print(soup)
    # links = soup.select("sportsbook-outcome-cell")
    # print(links)
    #elem.clear()
    #elem.send_keys("pycon")
    #elem.send_keys(Keys.RETURN)
    'dsdsd'
    # url = "https://www.tipico.de/de/live-wetten/"
    # try:
    #  page = urllib.request.urlopen(url)
    # except:
    #  print("An error occured.")

    # soup = BeautifulSoup(page, "html.parser")
    #print(soup)
    #EventOddGroup-styles-odd-groups
    # regex = re.compile('EventOddButton-styles-selected ')
    # content_lis = soup.find_all('button id', attrs={'span class': regex})
    # print("Content_lis",content_lis)
    # regex = re.compile('c_but_base c_but')
    # content_lis = soup.find_all('button', attrs={'class': regex})
    # print(content_lis)
    return 0

def decimal_to_american(decimal_odds):
    decimal_odds = float(decimal_odds)
    if decimal_odds >= 2:
        american_odds = (decimal_odds - 1) * 100
    elif decimal_odds >= 1.01 and decimal_odds <= 1.99:
        american_odds = -100 / (decimal_odds-1)
    return american_odds
# this function takes in pinnacle odds with any + or -

def non_vig_fair_odds(underdog,favorite):

    if underdog < 0 and favorite < 0:
        #underdog, favorite = float(underdog),float(favorite)
        
        favorite = favorite * -1
        underdog = underdog * -1
        calc1 = underdog/(underdog+100)
        calc2 = favorite/(favorite+100)
        sum = calc1 + calc2
        calc1 = calc1/sum
        calc2 = calc2/sum
    elif underdog > 0 and favorite > 0:
        underdog, favorite = float(underdog),float(favorite)
        calc1 = 100 /(underdog+100)
        calc2 = 100 /(favorite+100)
        sum = calc1 + calc2
        calc1 = calc1/sum
        calc2 = calc2/sum

    else:
        favorite = favorite * -1
        #underdog, favorite = float(underdog),float(favorite)
        calc1 = 100 /(underdog+100)
        calc2 = favorite/(favorite+100)
        sum = calc1 + calc2
        calc1 = calc1/sum
        calc2 = calc2/sum

    return calc1,calc2

def positive_ev_below(bet_odds,non_vig_odd,odd2,stake=100):
    profit = (100/bet_odds)*stake
    return profit * non_vig_odd - stake * odd2

def positive_ev_above(bet_odds,non_vig_odd,odd2,stake=100):
    profit = (bet_odds/100)*stake
    return profit * non_vig_odd - stake * odd2

def comparsion_iteration(test_dk,test2):
    similar_keys = test_dk.keys() & test2.keys()
    #print(similar_keys)

    for i in similar_keys:
        #print(test_dk[i],test2[i])
        # the higher the decimal value, the higher the odds - the more the underdog; +110,-120
        if(test_dk[i][1] in test2[i][0]):
            check = False
            if test2[i][1] > test2[i][3]:
                pinnacle_underdog = test2[i][1]
                pinnacle_favorite = test2[i][3]
                check = True
            else:
                pinnacle_underdog = test2[i][3]
                pinnacle_favorite = test2[i][1]

            pinnacle_underdog = decimal_to_american(pinnacle_underdog)
            pinnacle_favorite = decimal_to_american(pinnacle_favorite)
            print(i)
            print(test_dk[i],test2[i])
            
            
            no_vig_odds1,odds2 = non_vig_fair_odds(pinnacle_underdog,pinnacle_favorite)
            print("Non-vig odds:",no_vig_odds1,odds2)
            print("pinnacle",test2[i][1],test2[i][3])
            print("dk_odds",test_dk[i][2],test_dk[i][5])
            print("pinnacle_american",pinnacle_underdog,pinnacle_favorite)
            if check:
        
                dk_odd1 = test_dk[i][2]
                dk_odd2 = test_dk[i][5]
            else:

                dk_odd1 = test_dk[i][5]
                dk_odd2 = test_dk[i][2]
            
            negative_odd1 = False
            negative_odd2 = False
            if "-" in dk_odd1:
                dk_odd1 = dk_odd1.replace("-","")
                negative_odd1 = True
            if "+" in dk_odd1:
                dk_odd1 = dk_odd1.replace("+","")
            if "-" in dk_odd2:
                dk_odd2 = dk_odd2.replace("-","")
                negative_odd2 = True
            if "+" in dk_odd2:
                dk_odd2 = dk_odd2.replace("+","")
            
            print("dk_odds",dk_odd1,dk_odd2)
            dk_odd1 = float(dk_odd1)
            dk_odd2 = float(dk_odd2)

            
            if negative_odd1:
                positive_ev_bet1 = positive_ev_below(dk_odd1,no_vig_odds1,odds2)
            else:
                positive_ev_bet1 = positive_ev_above(dk_odd1,no_vig_odds1,odds2)
            
            if negative_odd2:
                positive_ev_bet2 = positive_ev_below(dk_odd2,odds2,no_vig_odds1)
            else:
                positive_ev_bet2 = positive_ev_above(dk_odd2,odds2,no_vig_odds1)
            
            #print("positive_1",positive_ev_bet1)
            #print("positive_2",positive_ev_bet2)
            if(positive_ev_bet1>0):

                print("WE GOT ONE!!!!!!!!!!!!!!")
                print(i)
                print(test_dk[i],test2[i])
                print("Non-vig odds:",no_vig_odds1,odds2)
                print("pinnacle",test2[i][1],test2[i][3])
                print("dk_odds",test_dk[i][2],test_dk[i][5])
                print("pinnacle_american",pinnacle_underdog,pinnacle_favorite)
                print("dk_odds",dk_odd1,dk_odd2)
                print("positive_1",positive_ev_bet1)
            if(positive_ev_bet2>0):
                print("WE GOT ONE!!!!!!!!!!!!!!")
                print(i)
                print(test_dk[i],test2[i])
                print("Non-vig odds:",no_vig_odds1,odds2)
                print("pinnacle",test2[i][1],test2[i][3])
                print("dk_odds",test_dk[i][2],test_dk[i][5])
                print("pinnacle_american",pinnacle_underdog,pinnacle_favorite)
                print("dk_odds",dk_odd1,dk_odd2)
                print("positive_2",positive_ev_bet2)

def compare_odds(pinnacle_website):
    print(pinnacle_website)
    bases_pinnacle,home_runs_pinnacle,earned_runs_pinnacle,hits_allowed_pinnacle,pitching_outs_pinnacle,strikeouts_pinnacle = pinnacle_baseball_player_props(pinnacle_website)
    # #bases_dk,home_runs_dk,earned_runs_dk,hits_allowed_dk,pitching_outs_dk,strikeouts_dk = draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=batter-props&subcategory=total-bases'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=batter-props&subcategory=home-runs'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=pitcher-props&subcategory=earned-runs'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=pitcher-props&subcategory=hits-allowed'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=pitcher-props&subcategory=outs-recorded'),draft_kings_baseball_odds('https://sportsbook.draftkings.com/leagues/baseball/88670847?category=pitcher-props&subcategory=strikeouts')
    # print(bases_pinnacle)
    # print(home_runs_pinnacle)
    # print(earned_runs_pinnacle)
    # print(hits_allowed_pinnacle)
    # print(pitching_outs_pinnacle)
    # print(strikeouts_pinnacle)
    # print("-----------")
   
    comparsion_iteration(bases_dk,bases_pinnacle)
    comparsion_iteration(home_runs_dk,home_runs_pinnacle)
    comparsion_iteration(earned_runs_dk,earned_runs_pinnacle)
    comparsion_iteration(hits_allowed_dk,hits_allowed_pinnacle)
    comparsion_iteration(pitching_outs_dk,pitching_outs_pinnacle)
    comparsion_iteration(strikeouts_dk,strikeouts_pinnacle)



    #####Bases Comparison#######
    bases_dk_test = {'Alec Bohm': ['O', ' 1.5', '+145', 'U', ' 1.5', '-190'], 'Andrew Knizner': ['O', ' 0.5', '-110', 'U', ' 0.5', '-120']}
    test_dk = {'AJ Pollock': ['O', ' 1.5', '+115', 'U', ' 1.5', '-150'], 'Alex Kirilloff': ['O', ' 1.5', '+120', 'U', ' 1.5', '-160'], 'Andrew Vaughn': ['O', ' 1.5', '-105', 'U', ' 1.5', '-130'], 'Byron Buxton': ['O', ' 1.5', '-105', 'U', ' 1.5', '-125'], 'Carlos Correa': ['O', ' 1.5', '+105', 'U', ' 1.5', '-140'], 'Gavin Sheets': ['O', ' 1.5', '+125', 'U', ' 1.5', '-170'], 'Gio Urshela': ['O', ' 0.5', '-210', 'U', ' 0.5', '+155'], 'Jorge Polanco': ['O', ' 1.5', '+115', 'U', ' 1.5', '-155'], 'Jose Abreu': ['O', ' 1.5', '-110', 'U', ' 1.5', '-120'], 'Jose Miranda': ['O', ' 0.5', '-190', 'U', ' 0.5', '+140'], 'Leury Garcia': ['O', ' 0.5', '-200', 'U', ' 0.5', '+145'], 'Luis Arraez': ['O', ' 1.5', '+105', 'U', ' 1.5', '-135'], 'Luis Robert': ['O', ' 1.5', '-125', 'U', ' 1.5', '-105'], 'Max Kepler': ['O', ' 1.5', '+115', 'U', ' 1.5', '-150'], 'Ryan Jeffers': ['O', ' 0.5', '-135', 'U', ' 0.5', '+105'], 'Seby Zavala': ['O', ' 0.5', '-130', 'U', ' 0.5', '+100'], 'Tim Anderson': ['O', ' 1.5', '-115', 'U', ' 1.5', '-115'], 'Yoan Moncada': ['O', ' 0.5', '-185', 'U', ' 0.5', '+140'], 'Alejandro Kirk': ['O', ' 1.5', '+115', 'U', ' 1.5', '-155'], 'Bo Bichette': ['O', ' 1.5', '-110', 'U', ' 1.5', '-125'], 'Cavan Biggio': ['O', ' 0.5', '-125', 'U', ' 0.5', '-105'], 'Elvis Andrus': ['O', ' 0.5', '-150', 'U', ' 0.5', '+110'], 'George Springer': ['O', ' 1.5', '+125', 'U', ' 1.5', '-165'], 'Lourdes Gurriel Jr.': ['O', ' 1.5', '+130', 'U', ' 1.5', '-170'], 'Matt Chapman': ['O', ' 0.5', '-165', 'U', ' 0.5', '+125'], 'Nick Allen': ['O', ' 0.5', '-110', 'U', ' 0.5', '-120'], 'Ramon Laureano': ['O', ' 0.5', '-140', 'U', ' 0.5', '+105'], 'Santiago Espinal': ['O', ' 0.5', '-180', 'U', ' 0.5', '+135'], 'Sean Murphy': ['O', ' 0.5', '-165', 'U', ' 0.5', '+125'], 'Seth Brown': ['O', ' 1.5', '+135', 'U', ' 1.5', '-180'], 'Skye Bolt': ['O', ' 0.5', '-120', 'U', ' 0.5', '-110'], 'Stephen Vogt': ['O', ' 0.5', '-135', 'U', ' 0.5', '+105'], 'Teoscar Hernandez': ['O', ' 1.5', '-105', 'U', ' 1.5', '-130'], 'Tony Kemp': ['O', ' 0.5', '-205', 'U', ' 0.5', '+150'], 'Vimael Machin': ['O', ' 0.5', '-140', 'U', ' 0.5', '+105'], 'Vladimir Guerrero Jr.': ['O', ' 1.5', '+105', 'U', ' 1.5', '-140'], 'Brendan Rodgers': ['O', ' 0.5', '-200', 'U', ' 0.5', '+150'], 'C.J. Cron': ['O', ' 0.5', '-150', 'U', ' 0.5', '+110'], 'Chris Taylor': ['O', ' 1.5', '+135', 'U', ' 1.5', '-180'], 'Cody Bellinger': ['O', ' 0.5', '-155', 'U', ' 0.5', '+115'], 'Connor Joe': ['O', ' 0.5', '-160', 'U', ' 0.5', '+120'], 'Elias Diaz': ['O', ' 0.5', '-145', 'U', ' 0.5', '+110'], 'Freddie Freeman': ['O', ' 1.5', '+120', 'U', ' 1.5', '-160'], 'Garrett Hampson': ['O', ' 0.5', '-105', 'U', ' 0.5', '-130'], 'Hanser Alberto': ['O', ' 0.5', '-185', 'U', ' 0.5', '+135'], 'Jose Iglesias': ['O', ' 0.5', '-175', 'U', ' 0.5', '+130'], 'Justin Turner': ['O', ' 1.5', '+115', 'U', ' 1.5', '-150'], 'Kris Bryant': ['O', ' 0.5', '-185', 'U', ' 0.5', '+135'], 'Mookie Betts': ['O', ' 1.5', '-110', 'U', ' 1.5', '-120'], 'Randal Grichuk': ['O', ' 0.5', '-160', 'U', ' 0.5', '+120'], 'Trayce Thompson': ['O', ' 0.5', '-170', 'U', ' 0.5', '+125'], 'Trea Turner': ['O', ' 1.5', '-125', 'U', ' 1.5', '-105'], 'Will Smith': ['O', ' 1.5', '+110', 'U', ' 1.5', '-145'], 'Yonathan Daza': ['O', ' 1.5', '+160', 'U', ' 1.5', '-220']}
    test2 = {'Abraham Toro': ['Over 0.5 TotalBases', '1.714', 'Under 0.5 TotalBases', '2.050'], 'Adam Frazier': ['Over 0.5 TotalBases', '1.555', 'Under 0.5 TotalBases', '2.320'], 'Alejandro Kirk': ['Over 0.5 TotalBases', '1.500', 'Under 0.5 TotalBases', '2.450'], 'Bo Bichette': ['Over 1.5 TotalBases', '2.160', 'Under 1.5 TotalBases', '1.641'], 'Cal Raleigh': ['Over 0.5 TotalBases', '1.591', 'Under 0.5 TotalBases', '2.250'], 'Carlos Santana': ['Over 0.5 TotalBases', '1.621', 'Under 0.5 TotalBases', '2.200'], 'Dylan Moore': ['Over 0.5 TotalBases', '2.050', 'Under 0.5 TotalBases', '1.714'], 'Eugenio Suarez': ['Over 0.5 TotalBases', '1.769', 'Under 0.5 TotalBases', '1.980'], 'George Springer': ['Over 0.5 TotalBases', '1.617', 'Under 0.5 TotalBases', '2.200'], 'J.P. Crawford': ['Over 0.5 TotalBases', '1.448', 'Under 0.5 TotalBases', '2.580'], 'Julio Rodriguez': ['Over 1.5 TotalBases', '2.710', 'Under 1.5 TotalBases', '1.418'], 'Lourdes Gurriel Jr.': ['Over 0.5 TotalBases', '1.492', 'Under 0.5 TotalBases', '2.470'], 'Matt Chapman': ['Over 0.5 TotalBases', '1.769', 'Under 0.5 TotalBases', '1.980'], 'Raimel Tapia': ['Over 0.5 TotalBases', '1.595', 'Under 0.5 TotalBases', '2.250'], 'Santiago Espinal': ['Over 0.5 TotalBases', '1.632', 'Under 0.5 TotalBases', '2.180'], 'Teoscar Hernandez': ['Over 1.5 TotalBases', '2.310', 'Under 1.5 TotalBases', '1.561'], 'Ty France': ['Over 0.5 TotalBases', '1.450', 'Under 0.5 TotalBases', '2.580'], 'Vladimir Guerrero Jr.': ['Over 1.5 TotalBases', '1.980', 'Under 1.5 TotalBases', '1.769']} 
    pinacle_dk_test = {'Brendan Rodgers': ['Over 0.5 TotalBases', '1.476', 'Under 0.5 TotalBases', '2.510']}
    #comparsion_iteration(test_dk,test2)

# def pinnacle_baseball_games():
#     s = Service("./drivers/geckodriver")
#     options = FirefoxOptions()
#     options.headless = True
#     browser = webdriver.Firefox(service=s,options = options)
#     browser.get("https://www.pinnacle.com/en/baseball/mlb/#period:0")
#     #all_matches_button = browser.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[2]/main/div/div[4]/div[2]/div/div[4]/div[1]/div/a').click()
#     player_prop = browser.find_elements(by='id',value = 'root')
#     all_matches_button2 = browser.find_element(by=By.XPATH,value='/html/body/div[2]/div/div[2]/main/div/div[4]/div[2]/div/div[3]/div[4]/a').click()
    
#     print(all_matches_button2)

#pinnacle_baseball_games()
#Atomate this manual labor
compare_odds('https://www.pinnacle.com/en/baseball/mlb/san-diego-padres-vs-new-york-mets/1555830842#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/minnesota-twins-vs-detroit-tigers/1555776062#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/st-louis-cardinals-vs-cincinnati-reds/1555776093#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/miami-marlins-vs-pittsburgh-pirates/1555776041#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/new-york-yankees-vs-baltimore-orioles/1555776042#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/san-diego-padres-vs-new-york-mets/1555776092#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/colorado-rockies-vs-milwaukee-brewers/1555776446#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/tampa-bay-rays-vs-kansas-city-royals/1555776099#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/san-francisco-giants-vs-los-angeles-dodgers/1555776051#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/los-angeles-angels-vs-atlanta-braves/1555776049#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/texas-rangers-vs-oakland-athletics/1555776477#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/san-francisco-giants-vs-los-angeles-dodgers/1555776460#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/washington-nationals-vs-arizona-diamondbacks/1555831040#player-props')
# compare_odds('https://www.pinnacle.com/en/baseball/mlb/texas-rangers-vs-oakland-athletics/1555831020#player-props')
