import json
# python nlp toolkit
import nltk
# vader sentiment analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# opens json file saved in part 1 as a py dictionary
def open_json_as_dict():
  with open('data/avatar-episodes.json') as f:
    data = json.load(f)
  return data

# creates a line to line mapping of vader scores for one episode
def create_vader_mapping(episode):
  sid = SentimentIntensityAnalyzer()
  vaderLines = [ [l[0], sid.polarity_scores(l[1])] for l in episode['lines'] ]
  vaderMapping = {"title": episode['title'], "vaderLines": vaderLines}
  return vaderMapping

# dump a python dictionary object to a json file
def save_vader_mapping_as_json(vaderDict):
  with open('avatar-episodes-vader-scores.json', 'w') as f:
    json.dump(vaderDict, f)

def convert_episodes_to_vader_array(episodes):
  result = []
  for episode in episodes:
    vader = create_vader_mapping(episode)
    result.append(vader)
  return result

# get the data
data = open_json_as_dict()

# convert the episode lines to vader representation
vaderArray = convert_episodes_to_vader_array(data['episodes'])

# create the python dictionary
vaderMap = {
    'episodes': vaderArray
  }

# finally, save the mapping to json
save_vader_mapping_as_json(vaderMap)