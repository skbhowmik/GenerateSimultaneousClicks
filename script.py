import webbrowser
import sys

loopCount = int(sys.argv[1])
test_browser = sys.argv[2]

url = sys.argv[3]
gc = "C://Program Files//Google//Chrome//Application//chrome.exe"
ff = "C://Program Files//Mozilla Firefox//firefox.exe"
ie = "C://Program Files//Internet Explorer//iexplore.exe"
me = "C://Program Files (x86)//Microsoft\Edge//Application//msedge.exe"

if test_browser == 'gc':
    browser_name = gc

elif test_browser == 'ff':
    browser_name = ff

elif test_browser == 'me':
    browser_name = me

elif test_browser == 'ie':
    browser_name = ie

else:
    print("Enter correct browser shortcode")

i = 0
while i < loopCount:
    webbrowser.register('browser',None,webbrowser.BackgroundBrowser(browser_name))
    webbrowser.get('browser').open_new(url)
    i += 1