# PianoBotV1
A bot that will automatically play piano tiles
This program is designed to be used with the web version of piano tiles: https://www.silvergames.com/en/piano-tiles. As it is a demonstration software, there will be no further improvements.

Steps:

1. Fix Pillow ImageGrab Package. (Instructions listed under debugging)

2. Go to Link.(https://www.silvergames.com/en/piano-tiles)

3. Start clicking on the tiles.

4. IMPORTANT: Make sure there is only one block on the screen.

5. hold enter until failure.

Note: the program Does not require restarting upon losing just repeat the above steps.


Debuging:

All packages are installed automatically.


when running there might be an error where it says: "Traceback (most recent call last):
  File "c:\Users\<Your Username Here>\Desktop\PianoBot\Fiverr piano tile clicker.py", line 65, in <module>
    screen = np.array(ImageGrab.grab(bbox=dis)) #captures screen
  File "C:\Users\<Your Username Here>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\PIL\ImageGrab.py", line 59, in grab
    if bbox:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()"

To fix this type "C:\Users\<Your Username Here>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\PIL\ImageGrab.py" into your Explorer tab and press enter. scroll down to line 59 or type ctrl+f and type: "if bbox:"

it should say: 
if bbox:
there are three lines below that:
	x0, y0 = offset
	left, top, right, bottom = bbox
	im = im.crop((left - x0, top - y0, right - x0, bottom - y0))

change that to: (Copy/Paste Will Work)




try: #<--- there is Important text there Don't mess this up!
				if bbox:
					x0, y0 = offset
					left, top, right, bottom = bbox
					im = im.crop((left - x0, top - y0, right - x0, bottom - y0))
			except:
					if bbox.any():
						x0, y0 = offset
						left, top, right, bottom = bbox
						im = im.crop((left - x0, top - y0, right - x0, bottom - y0))




if you do the afformentioned and get this:
"TabError: inconsistent use of tabs and spaces in indentation
PS C:\Users\<Your Username Here>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\PIL>"

remove all of the spaces in between the left side of the window and the text, then repeatedly hit tab until in same position. you kight have to do this a few times but it should work.

MAKE SURE TO SAVE THE FILE!!!


Contact If you run into any more problems. (709-691-6910) MESSAGING ONLY PLEASE!!!

This is a bug in Pillow's code and not mine.
