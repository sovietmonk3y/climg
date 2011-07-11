import BeautifulSoup
import urllib2

def submit_meme(data):
    url = 'http://memegenerator.net/Instance/Create_POST'
    req = urllib2.Request(url, data)
    res = urllib2.urlopen(req).read()
    res_soup = BeautifulSoup.BeautifulSoup(res)
    instance_id = res_soup.findAll(attrs = {'class' : 'instance left'})[0]['data-instanceid']
    return instance_id

def get_instance_img(instance_id):
    url = 'http://memegenerator.net/instance/%s' % instance_id
    req = urllib2.Request(url)
    res = urllib2.urlopen(req).read()
    
