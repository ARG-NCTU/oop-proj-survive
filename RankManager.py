import pandas as pd
import time

import matplotlib.pyplot as plt

class RankManager:
    def __init__(self):
        self.max_show = 6
        # Read the data from the csv file
        try:
            self.data = pd.read_csv('rank_data.csv')
        except FileNotFoundError:
            # Create a new csv file if it doesn't exist
            self.data = pd.DataFrame(columns=['player_name', 'kills', 'time', 'score'])
            self.data.to_csv('rank_data.csv', index=False)

    def show_rank(self):
        # read the data from the csv file
        self.data = pd.read_csv('rank_data.csv')
        if not self.data.empty:
            # sort the data by score
            self.data = self.data.sort_values(by='score', ascending=False)
            # show the data with a bar chart
            if len(self.data) > self.max_show:
                top_data = self.data.head(self.max_show)
                top_data.plot(kind='bar', x='player_name', y='score')
            else:
                self.data.plot(kind='bar', x='player_name', y='score')
            
            plt.title('Ranking')
            plt.xlabel('Time')
            plt.ylabel('Score')
            # make the plot look better
            plt.tight_layout()
            # make the x-axis items horizontal
            plt.xticks(rotation=0)
            # show the plot
            plt.show()
        else:
            print("No data available to display.")

    def add_data(self, player_name, kills, time, score):
        # store the data
        new_data = pd.DataFrame({'player_name': [player_name], 'kills': [kills], 'time': [time], 'score': [score]})
        # append the data to the DataFrame
        self.data = pd.concat([self.data, new_data], ignore_index=True)
        # save the data to the csv file
        self.data.to_csv('rank_data.csv', index=False)

# Show the rank
# rank_manager = RankManager()

# # Add data
# rank_manager.add_data('player1', 10, 100, 200)
# rank_manager.add_data('player2', 20, 200, 400)
# rank_manager.add_data('player3', 30, 300, 600)
# current_date = time.strftime("%Y/%m/%d\n%H:%M:%S", time.localtime())
# rank_manager.add_data(current_date, 10, 150, 282)

# rank_manager.show_rank()
