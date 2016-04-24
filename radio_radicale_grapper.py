from urllib.request import urlopen
import re


def get_page(url):
	response = urlopen(url)
	html = response.read().decode("utf-8")
	return html
#https://www.radioradicale.it/archivio?raggruppamenti_radio=6&field_data_1&field_data_2&page=0
#https://www.radioradicale.it/archivio?raggruppamenti_radio=6&field_data_1&field_data_2&page=1

#<li class="pager__item pager__item--last"><a title="Vai all'ultima pagina" href="/archivio?raggruppamenti_radio=6&amp;field_data_1=&amp;field_data_2=&amp;page=1083">ultima »</a></li>


#retrieve file from process session page 'https://www.radioradicale.it/scheda/473053/processo-madonia-salvatore-altri-strage-di-capaci-bis'

html = get_page('https://www.radioradicale.it/scheda/473053/processo-madonia-salvatore-altri-strage-di-capaci-bis')

#print(html)
#p=re.compile('http://audio\-aac\.radioradicale\.it:1935/aac\-1/_definst_/[0-9]{4}/[0-9]{2}/[0-9]{2}/(.+)\.m4a/playlist\.m3u8')


#get the url for retrieving chunk list
p=re.findall('(http://audio\-aac\.radioradicale\.it:1935/aac\-1/_definst_/[0-9]{4}/[0-9]{2}/[0-9]{2}/.+\.m4a/)playlist\.m3u8',html)
print (p)
tracker_base_url=p[0]

print (tracker_base_url)

tracker_file_txt = get_page(tracker_base_url + 'playlist.m3u8')

#print (tracker_file_txt)

#chunklist regexp to retrieve chunklist file
tracker=re.findall('chunklist.*\.m3u8',tracker_file_txt)


chuncks_url=tracker_base_url + tracker[0]

print (chuncks_url)

chuncks_file_txt=get_page(chuncks_url)

#print (chuncks_file_txt)

#media_w865073444_487.ts
chuncks=re.findall('media_.+\.ts',chuncks_file_txt)

#print (chuncks)

with open("test.ts", "a") as myfile:
    
	for chunck in chuncks:
		chunck_file=urlopen(tracker_base_url+chunck)
		chunck_file_txt=str(chunck_file.read())
		myfile.write(chunck_file_txt)



print ('finito')


