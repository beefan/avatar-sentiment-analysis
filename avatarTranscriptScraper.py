# import url request library
import urllib.request
# import regular expression library
import re
# import web scraping library
from bs4 import BeautifulSoup

# get the html content of a url.
def html_from_url(url):
  fp = urllib.request.urlopen(url)
  mybytes = fp.read()
  fp.close()
  return mybytes.decode("utf8")

# make a full url to the transcript from a links href tag
def make_link(aTag):
  return "https://avatar.fandom.com" + aTag['href']

# get beautiful soup from the avatar fan wiki
def get_avatar_fan_wiki_soup():
    wikiURL = "https://avatar.fandom.com/wiki/Avatar_Wiki:Transcripts"
    transcriptSoup = BeautifulSoup(html_from_url(wikiURL), "html.parser")
    return transcriptSoup

# check if a link is a transcript link
# an if it comes from Avatar Book One-Three
def is_transcript_link(tag):
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

# get transcript links from a beautiful soup object
def get_transcript_links(transcriptSoup):
  transcriptLinkElements = transcriptSoup.find_all(is_transcript_link)
  transcriptLinks = []

  for elem in transcriptLinkElements:
    transcriptLinks.append(make_link(elem))
  return transcriptLinks

# define an episode class
class Episode:
  def __init__(self, title, lines):
    self.title = title
    self.lines = lines

# convert an episode's link to a python object
# with title and lines of the episode
def link_to_episode(link):
    soup = BeautifulSoup(html_from_url(link), "html.parser")
    title = soup.select('.page-header__title')[0].text[11:]
    lines = []
    for tr in soup.select('.wikitable > tr'):
        if (tr.th):
            lines.append([tr.th.text.strip(), tr.td.text.strip()])
    return Episode(title, lines)

# main

# get the html doc to main wiki
avatarTranscriptSoup = get_avatar_fan_wiki_soup()
# get all the avatar transcript links
transcriptLinks = get_transcript_links(avatarTranscriptSoup)
# convert all the links to episode objects
avatarEpisodes = [link_to_episode(link) for link in transcriptLinks]