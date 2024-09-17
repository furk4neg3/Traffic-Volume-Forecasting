# Explanation of Project:
Project that I created while my internship in Ministry of Transportation and Infrastructure, Turkiye. Things that I'm about to tell are done in Colab notebooks, and for legal requirements, I can't share these notebooks. 

In the beginning, data I received had so many issues. I cleaned the data, then done some feature engineering on it. After that, I added things to data (the most important things which are lat_bin, lon_bin and count are added by me, they were not in the data). 

Then I created AI models to predict traffic volume. Tried MLP, LSTM, GRU, bidirectional LSTM, LSTM - GRU mixed and transformer models. Best performing one was bidirectional LSTM so I chose it. I visualized the predictions and true data, and it was working nearly perfect.

Afterwards, I created frontend for the project using React. Used Flask for data exchange between Python backend and React frontend. Used OpenLayers to draw the map.

## Notes: 
1- There's only day and hour inputs in the project. That's because data that I received only contained 2 weeks. At first, I was going to draw real map on the website too, that's why I created model to take only this amount of day. In the scenario when receiving data for multiple years, month and year inputs can be added.

2- I excluded density_data.csv and bi_lstm_model because I don't want to share them. That's why project wont work in your computer, but I added example images of project to show what it looks like when working. 
