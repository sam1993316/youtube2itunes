import youtube_dl
import os
import shutil

user = 'Jason'

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'outtmpl' : 'C:/Users/'+ user +'/Music/%(title)s.%(ext)s'
}

def download_mp3(url):
    # filtering url
    if '&list' in url:
        index = url.index('&list')
        url = remove_at(index, url)
        while(url[index]) != '&':
            url = remove_at(index, url)
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    # downloads the song and gets title
    title = (ydl.extract_info(url, download=True)['title'])
    title.strip()
    title_as_list = list(title)
    for idx, char in enumerate(title_as_list):
        if char == '|' :
            title_as_list[idx] = '_'
    title = ''.join(title_as_list)
    return title

def move_to_itunes(title):
    source = 'C:/Users/'+ user +'/Music/' + title + '.mp3'
    dest = 'C:/Users/'+ user +'/Music/iTunes/iTunes Media/Automatically Add to iTunes/' + title + '.mp3'
    result = shutil.move(source, dest)
    print(source + '\n' + dest)

def remove_at(i, s):
    return s[:i] + s[i+1:]

if __name__ == '__main__':
    print('##########################################')
    print('This program takes in a Youtube link, \nconverts it to sound file, and move the\nsound file into iTunes library')
    print('##########################################')
    while True:
        url = input('Enter url: ' )
        title = download_mp3(url)
        move_to_itunes(title)
        print('Done! ' + title + ' moved to iTunes music library. Enter your next song.')
        
        



    

