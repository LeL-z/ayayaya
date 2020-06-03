import json
import time
import mechanize
import wget
br = mechanize.Browser()
br.set_handle_robots(False)


br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')]

# with open('C:/Users/Jairus/PycharmProjects/CWheel/ripper/rip.json') as f:
#    pages = json.load(f)

# for pageImg in pages:
#    pageList = pageImg['image']
#    wget.download(pageList[1])



#br.retrieve('https://bu2.mkklcdnbuv1.com/mangakakalot/t2/tomochan_wa_onnanoko/chapter_1_ch01ch10/1.jpg', 'yum.jpg')
