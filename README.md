# wallpaper downloader

It basically uses __requests__ python module to sent a request to <https://wallpaperscraft/com>
using  __Beautifulsoup__ class to scrap for the HTML anchor tags with *class="wallpapers__link"* then
extract the value of __href__

With the value of __href__. I used it to create download url that points exactly where the image is.
and __wget__ module to download the images.

![How the anchor is describe on the website](/img/anchor_tag.png)

if you're on linux: start by activating the virtual environment *source linux_env/bin/activate*, then *python main.py*
On windows: start by *env\scripts\activate*, then *python main.py*

![code in](/img/screenshot.png)
