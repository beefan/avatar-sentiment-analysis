import json

def open_json_as_dict(path):
  """
  opens json file as python dictionary
  """
  with open(path) as f:
    data = json.load(f)
  return data

def save_json(pyDict, path):
  """
  dump a python dictionary object to a json file
  """
  with open(path, 'w') as f:
    json.dump(pyDict, f)

def get_emotion_totals(emotions):
  """
  from a list of emotions, get the totals of each NRC emotion
  """
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
  for emotion in emotions:
      if emotion != 'none':
          emotionMap[emotion] += 1
    
  emotions = list(emotionMap.keys())
  emotionTotals = list(emotionMap.values())
    
  return {"emotions": emotions, "totals": emotionTotals}
  
def generate_plots(nrcEp, vaderEp):
  """
  generate three sets of chart data for an avatar episode
  1. lines X nrcEmotions
  2. lines X vader compound scores
  3. emotions X number of appearances
  """
  plots = []
  title = nrcEp['title']
  numEps = len(nrcEp['lines'])
  lines = [ ln for ln in range(0, numEps) ]
  vader = [ vaderEp['vaderLines'][i][1]['compound'] for i in range(0, numEps) ] 
  nrc = [ nrcEp['lines'][i][1] for i in range(0, numEps) ]
  e = get_emotion_totals(nrc)
    
  plots.append({"name": title + ' Vader Compound Scores By Line', "x": lines, "y": vader})
  plots.append({"name": title + ' NRC Emotions By Line', "x": lines, "y": nrc})
  plots.append({"name": title + ' NRC Emotion Totals', "x": e['emotions'], "y": e['totals']})
        
  return plots

def generate_character_plots(nrcEp, vaderEp):
  """
  builds same chart data as generate_plots() but for each
  character with more than 5 lines
  """
  plots = []
  characters = { }
    
  lines = nrcEp['lines']
  vaderLines = vaderEp['vaderLines']
  for i in range(0, len(lines)):
      char = lines[i][0]
      if characters.get(char) == None:
          characters[char] = {"lines": [i], "nrc": [lines[i][1]], "vader": [vaderLines[i][1]['compound']]}
      else:
          characters[char]['lines'].append(i)
          characters[char]['nrc'].append(lines[i][1])
          characters[char]['vader'].append(vaderLines[i][1]['compound'])
    
  for entry in characters.items():
      char = entry[0]
      data = entry[1]
      # if less than 5 lines, don't include character
      if len(data['lines']) < 5:
          break
      e = get_emotion_totals(data['nrc'])
        
      plots.append({"name": char + ' Vader Compound Scores By Line', "x": data['lines'], "y": data['vader']})
      plots.append({"name": char + ' NRC Emotions By Line', "x": data['lines'], "y": data['nrc']})
      plots.append({"name": char + ' NRC Emotion Totals', "x": e['emotions'], "y": e['totals']})
    
  return plots

def get_plots_from_sentiment_data(nrcEp, vaderEp):
  """
  wrapper function which called two chart generation functions
  combines the data, and returns it
  """
  plots = generate_plots(nrcEp, vaderEp)
  plots.extend(generate_character_plots(nrcEp, vaderEp))
  return plots

def get_end_of_book_page(index, title, nrc, vader):
  """
  combines lines from an entire book and generates
  a cohesive sentiment analysis for that book
  """
  nrcL = []
  vaderL = []
    
  # if book 1
  if index == 22:
      for i in range(0,22):
          nrcL.extend(nrc[i]['lines'])
          vaderL.extend(vader[i]['vaderLines'])
  # book 2
  elif index == 42:
      for i in range(22,42):
          nrcL.extend(nrc[i]['lines'])
          vaderL.extend(vader[i]['vaderLines'])
  # book 3
  else:
      for i in range(42,len(nrc)):
          nrcL.extend(nrc[i]['lines'])
          vaderL.extend(vader[i]['vaderLines'])
    
  # combine all the lines for the book
  plots = get_plots_from_sentiment_data({ "title": title, "lines": nrcL }, { "title": title, "vaderLines": vaderL })

  return {"title": 'end-book', "bookTitle": title, "plots": plots}

def get_end_of_series_page(nrc, vader):
  """
  combines all lines from the entire series
  and generates a cohesive sentiment analysis
  """
  nrcL = []
  vaderL = []
  title = 'end-series'
    
  for i in range(0, len(nrc)):
      nrcL.extend(nrc[i]['lines'])
      vaderL.extend(vader[i]['vaderLines'])
        
  plots = get_plots_from_sentiment_data({ "title": title, "lines": nrcL }, { "title": title, "vaderLines": vaderL })
    
  return {"title": title, "bookTitle": '', "plots": plots}

def generate_chart_data(nrcData, vaderData):
  """
  main function that calls other functions to generate chart data
  loops through each episode and gets all the charts for that episode
  """
  bookTitles = ['Book One: Water', 'Book Two: Earth', 'Book Three: Fire']
  bookStarts = ['The Avatar State', 'Escape from the Spirit World']
  book = 0
  pages = []
  totalEps = len(nrcData)
  for i in range(0, totalEps):
      title = nrcData[i]['title']
      # if we are starting a new Book
      if title in bookStarts and title != bookStarts[book - 1]:
          book += 1
          pages.append(get_end_of_book_page(i, bookTitles[book], nrcData, vaderData))
      bookTitle = bookTitles[book]
      plots = get_plots_from_sentiment_data(nrcData[i], vaderData[i])
      page = { "title": title, "bookTitle": bookTitle, "plots": plots }
      pages.append(page)
    
  # if this is the last episode
  if i == (totalEps - 1):
      pages.append(get_end_of_book_page(i, bookTitle, nrcData[i], vaderData[i]))
      pages.append(get_end_of_series_page(nrcData, vaderData))
    
  return pages

def main():
  # get NRC and Vader data by episode
  nrcEmotionData = open_json_as_dict('data/avatar-episodes-nrc-emotion.json')['episodes']
  vaderScoreData = open_json_as_dict('data/avatar-episodes-vader-scores.json')['episodes']

  # generate page data
  pages = { "pages": generate_chart_data(nrcEmotionData, vaderScoreData) }

  # save the data as json file
  save_json(pages, 'data/avatar-chart-data.json')

main()