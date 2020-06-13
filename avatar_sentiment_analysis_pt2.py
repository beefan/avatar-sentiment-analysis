import json
# python nlp toolkit
import nltk
# vader sentiment analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk stop words to remove from our text
from nltk.corpus import stopwords
# nltk tokenizers
from nltk.tokenize import sent_tokenize, word_tokenize
# nltk lemmatizer
lemma = nltk.wordnet.WordNetLemmatizer()

def open_json_as_dict():
  """
  opens the avatar episodes json generated in pt1 
  as a python dictionary 
  """
  with open('data/avatar-episodes.json') as f:
    data = json.load(f)
  return data

def create_vader_mapping(episode):
  """
  creates a line to line mapping of vader scores for one episode
  """
  sid = SentimentIntensityAnalyzer()
  vaderLines = [ [l[0], sid.polarity_scores(l[1])] for l in episode['lines'] ]
  vaderMapping = {"title": episode['title'], "vaderLines": vaderLines}
  return vaderMapping

def save_dictionary_as_json(dictionary, path):
  """
  dump a python dictionary object to a json file
  """
  with open(path, 'w') as f:
    json.dump(dictionary, f)

def convert_episodes_to_vader_array(episodes):
  """
  convert the line array of every episode to contain 
  vader scores for that line
  """
  result = []
  for episode in episodes:
    vader = create_vader_mapping(episode)
    result.append(vader)
  return result

def open_lexicon_as_list():
  """
  opens and returns the NRC lexicon dictionary as a list
  """
  result = []
  with open('data/NRC-Emotion-Lexicon.txt', 'r') as f:
      for l in f:
        result.append(l)
  return result

def replace_contractions(line):
  """
  v simple contraction substitution
  """
  line = line.replace("'s", '')
  line = line.replace("'m", " am")
  line = line.replace("'d", " had")
  line = line.replace("'re", " are")
  line = line.replace("n't", " not")
  line = line.replace("'ve", " have")
  line = line.replace("'ll", " will")
  line = line.replace("'", '')
  return line

def lemmalize(word):
  """
  use nltk to get the lemma of the word
  for better matching with lexicon
  """
  return lemma.lemmatize(word)

def create_tokens_from_line(line):
  """
  returns nltk tokenized line after some formatting
  """
  line = replace_contractions(line.lower())
  tokens = word_tokenize(line)
  noWords = ['.',',','?',':',';','!','...','[',']','``']
  stopWords = set(stopwords.words('english'))
  noWords.extend(stopWords)
  filtered = [lemmalize(w) for w in tokens if not w in noWords]
  return filtered

def emotion_from_episode_line(line, lexicon):
  """
  from a line of text, format and then look up
  each word in a lexicon found at link below:
  http://sentiment.nrc.ca/lexicons-for-research/ 

  emotion with highest ranking per line is returned
  or "none" if all 0.
  """
  tokens = create_tokens_from_line(line)

  # possible emotions according to NRC lexicon used
  emotionMap = {
      "anger": 0,
      "anticipation": 0,
      "disgust": 0,
      "fear": 0,
      "joy": 0,
      "negative": 0,
      "positive": 0,
      "sadness": 0,
      "surprise": 0,
      "trust": 0
  }
  
  # increment emotions for each word that maps to that emotion
  wordLookUp = []
  for word in tokens:
    mission = 10
    for l in lexicon:
        if l[0:len(word) + 1].strip() == word:
            mission -= 1
            wordLookUp.append(l.split('\t')[2].strip())
        if mission <= 0:
            break

  if wordLookUp:
      emotionMap["anger"] += int(wordLookUp[0])
      emotionMap["anticipation"] += int(wordLookUp[1])
      emotionMap["disgust"] += int(wordLookUp[2])
      emotionMap["fear"] += int(wordLookUp[3])
      emotionMap["joy"] += int(wordLookUp[4])
      emotionMap["negative"] += int(wordLookUp[5])
      emotionMap["positive"] += int(wordLookUp[6])
      emotionMap["sadness"] += int(wordLookUp[7])
      emotionMap["surprise"] += int(wordLookUp[8])
      emotionMap["trust"] += int(wordLookUp[9])

  # return the emotion which maps most closely to the line
  maxEmotion = 0
  emotion = 'none'
  for entry in emotionMap.items():
    if entry[1] > maxEmotion:
        maxEmotion = entry[1]
        emotion = entry[0]
        
  return emotion

def convert_episodes_to_emotion_array(episodes, lexicon):
  """
  convert episode lines to arrays of nrc emotion data
  """
  for episode in episodes:
    lines = episode['lines']
    for line in lines:
      print('converting line {' + line[1][0:8] + '} from ' + episode['title'] + '...' )
      emotion = emotion_from_episode_line(line[1], lexicon)
      line[1] = emotion
        
  return episodes

def generate_vader_data():
  """
  generate vader sentiment data mapping for every line of every
  episode. save vader data to json
  """
  data = open_json_as_dict()
  vaderArray = convert_episodes_to_vader_array(data['episodes'])
  vaderMap = {
    'episodes': vaderArray
  }
  
  outpath = 'data/avatar-episodes-vader-scores.json'
  save_dictionary_as_json(vaderMap, outpath)

def generate_nrc_emotion_data():
  """
  generate emotion to line mapping for every line of every episode
  save emotional mapping to json
  """
  data = open_json_as_dict()
  lexicon = open_lexicon_as_list()
  emotionArray = convert_episodes_to_emotion_array(data['episodes'], lexicon)
  emoteArray = {
    'episodes': emotionArray
    }

  outpath = 'data/avatar-episodes-nrc-emotion.json'
  save_dictionary_as_json(emotionArray, outpath)

def main():
  """
  generate avatar airbender sentiment data and save as json
  """
  generate_vader_data()
  generate_nrc_emotion_data()

main()
