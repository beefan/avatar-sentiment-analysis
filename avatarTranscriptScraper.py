# import url request library
import urllib.request
# import regular expression library
import re
# import web scraping library
from bs4 import BeautifulSoup
# import json handling library
import json

def html_from_url(url):
  """
  get the html content of a url.
  """
  fp = urllib.request.urlopen(url)
  mybytes = fp.read()
  fp.close()
  return mybytes.decode("utf8")

def make_link(aTag):
  """
  make a full url to the transcript from a links href tag
  """
  return "https://avatar.fandom.com" + aTag['href']

def get_avatar_fan_wiki_soup():
  """
  get beautiful soup from the avatar fan wiki
  """
  wikiURL = "https://avatar.fandom.com/wiki/Avatar_Wiki:Transcripts"
  transcriptSoup = BeautifulSoup(html_from_url(wikiURL), "html.parser")
  return transcriptSoup

def is_transcript_link(tag):
  """
  check if a link is a transcript link
  and if it comes from Avatar Book One-Three
  """
  isLink = tag.has_attr('href') and tag.has_attr('title')
  if not isLink:
    return False
  
  isTranscript = ('Transcript' in tag['title'])
  if not isTranscript:
    return False

  headerId = ''
  for parent in tag.parents:
    prSib = parent.previous_sibling
    prPrSib = parent.previous_sibling.previous_sibling if prSib else None
    if prPrSib and prPrSib.name == 'h3':
        headerId = prPrSib.contents[0]['id']
        break

  result = re.compile('Book_One:_Water|Book_Two:_Earth|Book_Three:_Fire').search(headerId)
  return result

def get_transcript_links(transcriptSoup):
  """
  get transcript links from a beautiful soup object
  """
  transcriptLinkElements = transcriptSoup.find_all(is_transcript_link)
  transcriptLinks = []

  for elem in transcriptLinkElements:
    transcriptLinks.append(make_link(elem))
  return transcriptLinks

class Episode:
  """
  define an episode class
  """
  def __init__(self, title, lines):
    self.title = title
    self.lines = lines

def link_to_episode(link):
  """
  convert an episode's link to a python object
  with title and lines of the episode
  """
  soup = BeautifulSoup(html_from_url(link), "html.parser")
  title = soup.select('.page-header__title')[0].text[11:]
  lines = []
  for tr in soup.select('.wikitable > tr'):
      if (tr.th):
          lines.append([tr.th.text.strip(), tr.td.text.strip()])
  return Episode(title, lines)

def save_avatar_episodes_as_json(episodes):
  """
  open a json file and write the avatar episodes
  """
  eps = {
    'episodes': [{"title": e.title, "lines": e.lines} for e in episodes]
  }

  with open('avatar-episodes.json', 'w') as f:
    json.dump(eps, f)

def main():
  """
  scrape the avatar fan wiki for episode links
  save avatar episodes as json file
  """
  # get the html doc to main wiki
  avatarTranscriptSoup = get_avatar_fan_wiki_soup()
  # get all the avatar transcript links
  transcriptLinks = get_transcript_links(avatarTranscriptSoup)
  # convert all the links to episode objects
  avatarEpisodes = [link_to_episode(link) for link in transcriptLinks]
  # save episodes as a json file
  save_avatar_episodes_as_json(avatarEpisodes)

main()