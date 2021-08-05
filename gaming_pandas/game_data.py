#!/usr/bin/python3

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

graph_dir="/home/student/static/"

def top_ten_sorted_by_ratings(games):
    title = "Most Recommended Games at Steam"
    create_graph_title(title)
    sorted_by_ratings = games.sort_values(['RecommendationCount','ReleaseDate'], ascending=False)
    ratings_games = sorted_by_ratings[['ResponseName', 'ReleaseDate', 'RecommendationCount', 'PriceFinal']]
    print(ratings_games.head(10))
    graphit = input("\n\nWould you like to create a graph of this data? (y or n) ")
    if graphit.lower() == "y" or graphit.lower() == "yes":
        ratings_games = sorted_by_ratings[['ResponseName','RecommendationCount']]
        ratings_games.set_index('ResponseName', inplace=True)
        make_a_graph(ratings_games.head(10), title, 'RecommendationCount')
   

def bottom_ten_sorted_by_ratings(games):
    title = "Least Recommended Games at Steam"
    create_graph_title(title)
    sorted_by_ratings = games.sort_values(['RecommendationCount', 'ReleaseDate'], ascending=False)
    ratings_games = sorted_by_ratings[['ResponseName', 'ReleaseDate', 'RecommendationCount', 'PriceFinal']]
    print(ratings_games.tail(10))
    graphit = input("\n\nWould you like to create a graph of this data? (y or n) ")
    if graphit.lower() == "y" or graphit.lower() == "yes":
        ratings_games = sorted_by_ratings[['ResponseName','RecommendationCount']]
        ratings_games.set_index('ResponseName', inplace=True)
        make_a_graph(ratings_games.tail(10), title, 'RecommendationCount')
  
def most_recent_games(games):
    title = "Most Recent Games at Steam"
    create_graph_title(title)
    sorted_by_date = games.sort_values(['ReleaseDate'], ascending=False)
    recent_games = sorted_by_date[['ResponseName', 'ReleaseDate', 'RecommendationCount', 'PriceFinal']]
    print(recent_games.head(10))
    graphit = input("\n\nWould you like to create a graph of this data? (y or n) ")
    if graphit.lower() == "y" or graphit.lower() == "yes":
        ratings_games = sorted_by_date[['ResponseName','ReleaseDate']]
        ratings_games.set_index('ResponseName', inplace=True)
        make_a_graph(recent_games.head(10), title, 'ReleaseDate')


def highest_dlc_games(games):
    title = "Highest DLC Games at Steam"
    create_graph_title(title)
    sorted_by_dlc = games.sort_values(['DLCCount','RecommendationCount'], ascending=False)
    dlc_games = sorted_by_dlc[['ResponseName', 'ReleaseDate', 'RecommendationCount', 'DLCCount', 'PriceFinal']]
    print(dlc_games.head(10))
    graphit = input("\n\nWould you like to create a graph of this data? (y or n) ")
    if graphit.lower() == "y" or graphit.lower() == "yes":
        dlc_games = sorted_by_dlc[['ResponseName','DLCCount']]
        dlc_games.set_index('ResponseName', inplace=True)
        make_a_graph(dlc_games.head(10), title, 'DLCCount')

def top_ten_free(games):
    title = "Top Ten Free Games at Steam"
    create_graph_title(title)
    sorted_by_free = games.sort_values(['IsFree','RecommendationCount'], ascending=False)
    free_games = sorted_by_free[['ResponseName', 'ReleaseDate', 'RecommendationCount']]
    print(free_games.head(10))
    graphit = input("\n\nWould you like to create a graph of this data? (y or n) ")
    if graphit.lower() == "y" or graphit.lower() == "yes":
        free_games = sorted_by_free[['ResponseName','RecommendationCount']]
        free_games.set_index('ResponseName', inplace=True)
        make_a_graph(free_games.head(10), title, 'RecommendationCount')

def top_ten_indie(games):
    title = "Top Ten Indie Games at Steam"
    create_graph_title(title)
    sorted_by_indie = games.sort_values(['GenreIsIndie','RecommendationCount'], ascending=False)
    indie_games = sorted_by_indie[['ResponseName', 'ReleaseDate', 'RecommendationCount']]
    print(indie_games.head(10))
    graphit = input("\n\nWould you like to create a graph of this data? (y or n) ")
    if graphit.lower() == "y" or graphit.lower() == "yes":
        indie_games = sorted_by_indie[['ResponseName','RecommendationCount']]
        indie_games.set_index('ResponseName', inplace=True)
        make_a_graph(indie_games.head(10), title, 'RecommendationCount')

def top_ten_strategy(games):
    title = "Top Ten Strategy Games at Steam"
    create_graph_title(title)
    sorted_by_strategy = games.sort_values(['GenreIsStrategy','RecommendationCount'], ascending=False)
    strategy_games = sorted_by_strategy[['ResponseName', 'ReleaseDate', 'RecommendationCount']]
    print(strategy_games.head(10))
    graphit = input("\n\nWould you like to create a graph of this data? (y or n) ")
    if graphit.lower() == "y" or graphit.lower() == "yes":
        strategy_games = sorted_by_strategy[['ResponseName','RecommendationCount']]
        strategy_games.set_index('ResponseName', inplace=True)
        make_a_graph(strategy_games.head(10), title, 'RecommendationCount')


def top_ten_rpg(games):
    title = "Top Ten RPGs at Steam"
    create_graph_title(title)
    sorted_by_rpg = games.sort_values(['GenreIsRPG','RecommendationCount'], ascending=False)
    rpg_games = sorted_by_rpg[['ResponseName', 'ReleaseDate', 'RecommendationCount']]
    print(rpg_games.head(10))
    graphit = input("\n\nWould you like to create a graph of this data? (y or n) ")
    if graphit.lower() == "y" or graphit.lower() == "yes":
        rpg_games = sorted_by_rpg[['ResponseName','RecommendationCount']]
        rpg_games.set_index('ResponseName', inplace=True)
        make_a_graph(rpg_games.head(10), title, 'RecommendationCount')


def top_ten_casual(games):
    title = "Top Ten Casual Games at Steam"
    create_graph_title(title)
    sorted_by_casual = games.sort_values(['GenreIsCasual','RecommendationCount'], ascending=False)
    casual_games = sorted_by_casual[['ResponseName', 'ReleaseDate', 'RecommendationCount']]
    print(casual_games.head(10))
    graphit = input("\n\nWould you like to create a graph of this data? (y or n) ")
    if graphit.lower() == "y" or graphit.lower() == "yes":
        casual_games = sorted_by_casual[['ResponseName','RecommendationCount']]
        casual_games.set_index('ResponseName', inplace=True)
        make_a_graph(casual_games.head(10), title, 'RecommendationCount')



def make_a_graph(data, gtitle, col):
    num = input("How many items? (2 - 10) ")
    if num.isdigit() == False:
        num = 10
    elif int(num) < 2:
        num = 2
    elif int(num) > 10:
        num = 10
    else:
        num = int(num)
        
    graph_type = input("Which graph type? (barh, bar, line, hist, box, pie) " )
       
    if graph_type in ["barh", "bar", "line", "hist", "pie"]:
        try:
            if graph_type == "bar":
                ax = data[col].head(int(num)).plot(x='ResponseName', y=col, kind='bar', title=gtitle)
                x = "Game Title"
                y = col

            elif graph_type == "line":
                ax = data[col].head(int(num)).plot(x=data['ResponseName'], y=[col], xlabel='ResponseName', ylabel=col, kind='line', title=gtitle)
                x = "Game Title"
                y = col

            elif graph_type == "hist":
                ax = data[[col]].head(int(num)).plot(kind='hist', title=gtitle)
                x = "Game Title"
                y = col

            elif graph_type == "pie":
                ax = data[col].head(int(num)).plot(x='ResponseName', y=col, kind='pie', title=gtitle)
                x = ""
                y = ""

            else:  ## barh default
                ax = data[col].head(int(num)).plot(x='ResponseName', y=col, kind='barh', title=gtitle)
                x = col
                y = "Game Title"

            filename = graph_dir + gtitle.replace(" ", "") + graph_type + str(num) + ".png"
            ax.set_xlabel(x)
            ax.set_ylabel(y)
            plt.savefig(filename, bbox_inches='tight')
            print("PNG created:", filename)

        except TypeError:
            print("Sorry, couldn't make that graph. There's no numerical data to plot.")
        
        except:
            print("I dunno, man. No graph, no joy.")


def create_graph_title(title):
    width, height = os.get_terminal_size()
    print("\n\n\n")
    print(title.center(width))
    print("\n")



def create_menu():
    line1 = "Steam Spot"
    line2 = "c/o Steam and SteamSpy"
    width, height = os.get_terminal_size()
    print("\n\n\n")
    print(line1.center(width))
    print(line2.center(width))
    print("\n\n              MENU")
    print( """
        (1)  Most recommended games
        (2)  Least recommended games
        (3)  Most recent games
        (4)  Highest DLC count
        (5)  Top 10 free games
        (6)  Top 10 indie games
        (7)  Top 10 strategy games
        (8)  Top 10 RPG
        (9)  Top 10 casual games
        (x) Exit
    """)



def main():
    csv_file = "gaming.csv"
    games = pd.read_csv(csv_file)
    games.drop_duplicates(inplace=True)
    games = games[games['ReleaseDate'].notna()]
#    games.drop(['QueryID','ResponseID'], axis='columns', inplace=True)

    ## Create menu
    choice = "1"

    while choice.isdigit() and choice != "0":
        create_menu()
        choice = input(">> ")

        if choice == "1":
            top_ten_sorted_by_ratings(games)
        elif choice == "2":
            bottom_ten_sorted_by_ratings(games)
        elif choice == "3":
            most_recent_games(games)
        elif choice == "4":
            highest_dlc_games(games)
        elif choice == "5":
            top_ten_free(games)
        elif choice == "6":
            top_ten_indie(games)
        elif choice == "7":
            top_ten_strategy(games)
        elif choice == "8":
            top_ten_rpg(games)
        elif choice == "9":
            top_ten_casual(games)
        else:
            print("Thank you for using Steam Spot. View any generated graphs at", graph_dir)
            break



if __name__ == "__main__":
    main()
