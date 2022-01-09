from tkinter import simpledialog 
from tkinter import * 
import webbrowser 



root = Tk()
root.title("Open Web")
root.geometry("200x100")
root.minsize(200,100)
root.maxsize(200,100)


urls = {"github":"github.com","google":"google.com","youtube":"youtube.com"}

def open_web(url):
	if url in urls.keys():
		url = urls[url]
	else:
		url = url 

	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
	webbrowser.get('chrome').open_new_tab(url)


def get_url():
	url = urlvar.get()
	open_web(url)

	urlvar.set("")



label = Label(root,text="Enter Url To Open :").pack()

urlvar = StringVar()
url_entry = Entry(root,textvariable=urlvar)
url_entry.pack()


btn = Button(root,text="Open",command=get_url)
btn.pack()


root.mainloop()