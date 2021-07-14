# wallpaper downloader

It basically uses __requests__ python module to sent a request to <https://wallpaperscraft.com>
using  __Beautifulsoup__ class to scrap for the HTML anchor tags with *class="wallpapers__link"* then
extract the value of __href__

With the value of __href__. I used it to create download url that points exactly where the image is.
and __wget__ module to download the images.

# how to run it
create virtual environment: *virtualenv env*
activate the virtual envronment: *env\Scripts\activate* (In windows) or *source env/bin/activate* (in linux)
finally, run: *python main.py*

1. choose the category of photos you want
2. enter page number to start e.g. 1 
3. enter the page number to end e.g. 3 (limit=10)
that's it


pip install -r requirements.txt

![How the anchor is describe on the website](/img/anchor_tag.png)

![code in](/img/Screensho.png)


