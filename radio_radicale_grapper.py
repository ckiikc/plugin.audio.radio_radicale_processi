import urllib2
import re



#retrieve file from process session page
response = urllib2.urlopen('https://www.radioradicale.it/scheda/473053/processo-madonia-salvatore-altri-strage-di-capaci-bis')
html = response.read()


#p=re.compile('http://audio\-aac\.radioradicale\.it:1935/aac\-1/_definst_/[0-9]{4}/[0-9]{2}/[0-9]{2}/(.+)\.m4a/playlist\.m3u8')


#get the url for retrieving chunk list
p=re.findall('(http://audio\-aac\.radioradicale\.it:1935/aac\-1/_definst_/[0-9]{4}/[0-9]{2}/[0-9]{2}/.+\.m4a/)playlist\.m3u8',html)

print p

tracker_base_url=p[0]

print tracker_base_url

tracker_file=urllib2.urlopen(tracker_base_url + 'playlist.m3u8')
tracker_file_txt = tracker_file.read()

#print tracker_file_txt

#chunklist regexp to retrieve chunklist file
tracker=re.findall('chunklist.*\.m3u8',tracker_file_txt)


chuncks_url=tracker_base_url + tracker[0]

print chuncks_url


chuncks_file=urllib2.urlopen(chuncks_url)
chuncks_file_txt=chuncks_file.read()

print chuncks_file_txt

#media_w865073444_487.ts
chuncks=re.findall('media_.+\.ts',chuncks_file_txt)

print chuncks

with open("test.ts", "a") as myfile:
    
	for chunck in chuncks:
		print tracker_base_url+chunck
		chunck_file=urllib2.urlopen(tracker_base_url+chunck)
		chunck_file_txt=chunck_file.read()
		#print chunck_file_txt
		myfile.write(chunck_file_txt)



print 'finito2'

