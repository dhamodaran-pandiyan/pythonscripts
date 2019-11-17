import youtube_dl
ydl_opts = {}
def dwl():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([txt])
        ch = 1
        while (ch == int(1)):
            url = input("Copy paste video Url:")
            txt = url.strip()
            dwl()
            ch=int(input("To Download more Videos Enter 1 else press 0:"))
