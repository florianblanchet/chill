from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import urllib.request
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
import time
from sqlalchemy import *
from datetime import datetime 

#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#token = os.environ.get('FB_ACCESS_TOKEN')
token = 'blabla'
POSTGRES = {
    'user': 'postgres',
    'pw': 'salade23',
    'db': 'haldb',
    'host': 'localhost',
    'port': '5432',
 }
engine = create_engine('postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'%POSTGRES)
#engine = create_engine(SQLALCHEMY_DATABASE_URI)
engine.echo = False
metadata = MetaData(engine)
users = Table('user', metadata, autoload=True)
news = Table('news', metadata, autoload=True)
Session = sessionmaker(bind=engine)
session = Session()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def mainscript():
    save_news()
    return 'Réponse Serveur : News actualisé'

# Marche pas fait planter le serveur
@app.route('/welcome')
def welcome():
    #send_welcome()
    print('welcome')
    return 'welcome'

@app.route('/snake')
def snake():
    print('Lance le snake')
    return render_template('index.html')


############ Send welcome   ##########
def send_link6 (sender,title1,subtitle1,image_url1,link1,title2,subtitle2,image_url2,link2,title3,subtitle3,image_url3,link3,title4,subtitle4,image_url4,link4,title5,subtitle5,image_url5,link5,title6,subtitle6,image_url6,link6):
    return {
    "recipient": {
      "id": sender
    },
    "message": {
      "attachment": {
        "type": "template",
        "payload": {
          "template_type": "generic",
          "image_aspect_ratio":'square',
          "elements": [{
            "title": title1,
            "subtitle": subtitle1,              
            "image_url": image_url1,
            "default_action":{"type":"web_url","url":link1},
            "buttons": [{
              "type": "web_url",
              "url": link1,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title1,
                            "subtitle": subtitle1,
                            "item_url": link1,               
                            "image_url": image_url1,
                            "buttons": [{
                              "type": "web_url",
                              "url": link1,
                              "title": "Accéder à l'article",
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title2,
            "subtitle": subtitle2,              
            "image_url": image_url2,
            "default_action":{"type":"web_url","url":link2},
            "buttons": [{
              "type": "web_url",
              "url": link2,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title2,
                            "subtitle": subtitle2,
                            "item_url": link2,               
                            "image_url": image_url2,
                            "buttons": [{
                              "type": "web_url",
                              "url": link2,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title3,
            "subtitle": subtitle3,         
            "image_url": image_url3,
            "default_action":{"type":"web_url","url":link3},
            "buttons": [{
              "type": "web_url",
              "url": link3,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title3,
                            "subtitle": subtitle3,
                            "item_url": link3,               
                            "image_url": image_url3,
                            "buttons": [{
                              "type": "web_url",
                              "url": link3,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title4,
            "subtitle": subtitle4,         
            "image_url": image_url4,
            "default_action":{"type":"web_url","url":link4},
            "buttons": [{
              "type": "web_url",
              "url": link4,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title4,
                            "subtitle": subtitle4,
                            "item_url": link4,               
                            "image_url": image_url4,
                            "buttons": [{
                              "type": "web_url",
                              "url": link4,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title5,
            "subtitle": subtitle5,          
            "image_url": image_url5,
            "default_action":{"type":"web_url","url":link5},
            "buttons": [{
              "type": "web_url",
              "url": link5,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title5,
                            "subtitle": subtitle5,
                            "item_url": link5,               
                            "image_url": image_url5,
                            "buttons": [{
                              "type": "web_url",
                              "url": link5,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }, {
            "title": title6,
            "subtitle": subtitle6,        
            "image_url": image_url6,
            "default_action":{"type":"web_url","url":link6},
            "buttons": [{
              "type": "web_url",
              "url": link6,
              "title": "Accéder à l'article"
            }, {
            "type": "element_share",
            "share_contents": { 
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": title6,
                            "subtitle": subtitle6,
                            "item_url": link6,               
                            "image_url": image_url6,
                            "buttons": [{
                              "type": "web_url",
                              "url": link6,
                              "title": "Accéder à l'article"
                                }]
                            }]
                        }
                    }
                }
            }]
          }]
        }
      }
    }
    } 
def send_text (sender,texte):

    return {'recipient': {'id': sender}, 'message': {'text': texte}}
def send_paquet(sender,payload):
    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
    print(r.text) # affiche la reponse à l'envoit; pratique si veut l'ID ou voir si bien envoyé
    pass
def extract_news(categorie):
    articles = []
    for newss in session.query(news).filter_by(categorie=categorie):
        article = {}
        article['titre'] = newss.titre
        article['journal'] = newss.journal
        article['lien'] = newss.lien
        article['image'] = newss.image
        articles.append(article)
    return articles
def liste_user():
    liste_id=[]
    for userss in session.query(users):
        liste_id.append([str(userss.user_id),str(userss.first_name)])
    return liste_id 
#def send_welcome():
    #liste_users = liste_user()
    #une = extract_news('une')
    #print("téléchargé")
    #for user in liste_users:
    #    print(user)
    #    texte = "Salut "+user[1]+"!\n"+"Commençons la journée avec un petit résumé de l'actu 😁 :"
    #    payload = send_text(user[0],texte)
    #    send_paquet(token,payload)
    #    payload = send_link6(user[0],une[0]['titre'],une[0]['journal'],une[0]['image'],une[0]['lien'],une[1]['titre'],une[1]['journal'],une[1]['image'],une[1]['lien'],une[2]['titre'],une[2]['journal'],une[2]['image'],une[2]['lien'],une[3]['titre'],une[3]['journal'],une[3]['image'],une[3]['lien'],une[4]['titre'],une[4]['journal'],une[4]['image'],une[4]['lien'],une[5]['titre'],une[5]['journal'],une[5]['image'],une[5]['lien'])
    #    send_paquet(token,payload)
    #print('welcome envoyé')

###########   Exctract  NEWS    ##########
def download_news2():
    req = urllib.request.Request('https://news.google.com/?edchanged=1&ned=fr&authuser=0')
    the_page = urllib.request.urlopen(req)
    page = the_page.read()
    soup = BeautifulSoup(page, 'html.parser')
    news ={}
    hello=[]
    articles = soup.find_all("div",attrs={"class":"esc-wrapper"})
    for i in range(len(articles)):
        articles[i] = BeautifulSoup(str(articles[i]),'html.parser')
        article={}
        photo = articles[i].find("img")
        if photo!=None:
            photo_url = photo.get('imgsrc')
            if photo_url!=None:
                article['image']='http:'+str(photo_url)
            else:
                article['image']='http:'+str(photo.get('src'))
        else:
            article['image']=''
        article['titre'] = str(articles[i].find("span",attrs={"class":"titletext"}).getText())
        article['lien'] = str(articles[i].find("a",attrs={"class":"article"}).get('url'))
        #contenu = articles[i].find_all("div",attrs={"class":"esc-lead-snippet-wrapper"})
        article['journal'] = str(articles[i].find("span",attrs={"class":"al-attribution-source"}).getText())
        hello.append(article)
    news['une'] = hello[0:6]
    news['world'] = hello[6:10]
    news['france'] = hello[10 : 14]
    news['economie'] = hello[14 : 18]
    news['science'] = hello[18 : 22]
    news['culture'] = hello[22 : 26]
    news['sport'] = hello[26 : 30]
    news['sante'] = hello[30 : 34]
    return news
def save_news():
    news_liste = download_news2()
    une = news_liste['une']
    world = news_liste['world']
    france = news_liste['france']
    economie = news_liste['economie']
    science = news_liste['science']
    culture = news_liste['culture']
    sport = news_liste['sport']
    sante = news_liste['sante']
    liste = [[une,'une'],[world,'world'],[france,'france'],[economie,'economie'],[science,'science'],[culture,'culture'],[sport,'sport'],[sante,'sante']]
    a=0
    for categorie,nom_categorie in liste :
        d = news.delete(news.c.categorie == nom_categorie)
        d.execute()
        for article in categorie:
            a+=1
            i = news.insert()
            i.execute(id=a,categorie=nom_categorie,titre=article['titre'],journal=article['journal'],lien=article['lien'],image=article['image'])
    print('news actualisée') 

if __name__ == '__main__':
    app.run()