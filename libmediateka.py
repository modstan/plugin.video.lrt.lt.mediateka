import urllib
import re
MEDIATEKA_URL = 'http://www.lrt.lt/mediateka/'
regexp = {
	"pagrindinis": '<li ><a href="mediateka/(.*)">(.*)</a></li>',
	"tiesiogiai": 'xxxx', 
	"pasivyk": 'Pasivyk', 
	"temos": '<li><a href="http://www.lrt.lt/mediateka/temos/(.*)>(.*)</a></li>',
	"laidos": '<a href="mediateka/(.*)" style="float:left;">(.*)</a>',
	"grojarasciai": 'Grojara\xc5\xa1\xc4\x8diai',
	"prenumerata": 'Prenumerata',
	"laidu-list": '<a class="name popup" title=\".*"\shref="mediateka/(.*)\?popup">(.*)</a>\s*<p\sclass="date">(.*)</p>',
	"videolink": "type:\s*'html5'\,\s*config:\s*{\s*'file':\s*'(.*)',"
	}



def get_page_html(link):
	full_link = MEDIATEKA_URL+link
	print(full_link)
	res = urllib.urlopen(full_link)
	html = res.read()
	res.close()
	return html

def get_data(link, regexp):
	rexp = re.compile(regexp)
	html = get_page_html(link)
	return rexp.findall(html)

