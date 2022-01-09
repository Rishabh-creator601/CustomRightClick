from pytube import YouTube 
from tkinter import * 
from tkinter import simpledialog ,messagebox 


def download(url):
	yt = YouTube(url)

	title = yt.title

	video = yt.streams.get_highest_resolution()
	video.download()

	return title 





root = Tk()
root.title("YouTube ")
root.geometry("200x150")
root.maxsize(200,150)
root.minsize(200,150)




def get_url():
	url = urlvar.get()
	title = download(url)
	urlvar.set("")
	messagebox.showinfo("Info !",f"YouTube Video {title} Downloaded")




urlvar = StringVar()


label = Label(root,text='Enter YouTube Video Url :').pack()

entry = Entry(root,textvariable=urlvar)
entry.pack(fill=BOTH)


btn = Button(root,text='download',command=get_url)
btn.pack()


root.mainloop()