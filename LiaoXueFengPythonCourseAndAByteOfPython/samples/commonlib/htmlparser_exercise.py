from html.parser import HTMLParser
from html.entities import name2codepoint

class myHtmlParser(HTMLParser):

    def __init__(self):
        super(myHtmlParser, self).__init__()
        self._flag = ''
        self._first_time = 0

    def handle_starttag(self, tag, attrs):
        if ('class','event-title') in attrs:
            self._flag = 'Title:'
        elif ('class','event-location') in attrs:
            self._flag = 'Location:'
        elif tag=='time':
            self._flag = 'Time:'

    def handle_data(self, data):
        if self._flag in ('Title:','Location:','Time:'):
            if self._flag in ('Title:','Location:'):
                print(self._flag,data.strip())
                self._flag=''
                return
            else:
                if self._first_time==0:
                    print(self._flag,data.strip(), end='-')
                    self._first_time+=1
                else:
                    print(data.strip())
                    self._flag=''
                    self._first_time=0

            


parser = myHtmlParser()
with open('html.txt','r') as f:
    parser.feed(f.read())
    parser.feed(f.read())

