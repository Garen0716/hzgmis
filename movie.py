import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


url = "http://www.atmovies.com.tw/movie/next/"
Data = requests.get(url)
Data.encoding="utf-8"
#print(Data.text)

sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".filmListAllX li")
lastUpdate = sp.find("div", class_="smaller09").text[5:]



db = firestore.client()
doc_ref = db.collection("電影").document(movie_id)
doc_ref.set(doc)



for item in result:
  picture = item.find("img").get("src").replace(" ", "")
  title = item.find("div", class_="filmtitle").text
  movie_id = item.find("div", class_="filmtitle").find("a").get("href").replace("/", "").replace("movie", "")
  hyperlink = "http://www.atmovies.com.tw" + item.find("div", class_="filmtitle").find("a").get("href")
  show = item.find("div", class_="runtime").text.replace("上映日期：", "")
  show = show.replace("片長：", "")
  show = show.replace("分", "")
  showDate = show[0:10]
  showLength = show[13:]









# for x in result:
#     print("http://www.atmovies.com.tw" + x.find("a").get("href"))
#     print("電影海報:" + x.find("img").get("src").replace(" ",""))
#     print("片名:" + x.find("div",class_="filmtitle").text)
#     print("片名2:" + x.find("img").get("alt"))
#     print("修改日期:" + x.find(class_="runtime").text[5:15])
#     print()