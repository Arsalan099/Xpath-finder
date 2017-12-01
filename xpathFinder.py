import urllib.request
from bs4 import BeautifulSoup
import itertools
def xpath_find(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        previous = itertools.islice(parent.children, 0, parent.contents.index(child))
        xpath_tag = child.name
        xpath_index = sum(1 for i in previous if i.name == xpath_tag) + 1
        components.append(xpath_tag if xpath_index == 1 else '%s[%d]' % (xpath_tag, xpath_index))
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)
r=urllib.request.urlopen("https://www.homecanvas.com/product/Wooden-Street-Adler-L-Shape-Sofa--(White)/272937/")
soup = BeautifulSoup(r, 'lxml')
soup1=soup.find_all('div',{'class':'contents col-lg-6 col-md-6 col-sm-6 col-xs-6'})
soup2=soup.find_all('div',{'class':'price'})
soup3=soup.find_all('div',{'class':'vendor'})
soup4=soup.find_all('div',{'class':'no-padding-top prod-desc-details-div'})
soup5=soup.find_all('img',{'class':'producttt-img img-responsive'})
for i in range(0,len(soup1)):
    soup1[i]=soup1[i].find('h1').string
    print('Xpath for title is :' + xpath_find(soup1[i]))
    print('Xpath for price is :' + xpath_find(soup2[i]))
    soup3[i]=soup3[i].find('a').string
    print('Xpath for Seller is :' + xpath_find(soup3[i]))
    print('Xpath for Product Description is :' + xpath_find(soup4[i]))
    print('Xpath for image is :' + xpath_find(soup5[i]))