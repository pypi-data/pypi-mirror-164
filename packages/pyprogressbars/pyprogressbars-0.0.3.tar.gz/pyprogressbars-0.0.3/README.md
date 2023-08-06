# PyProgressBars

[![N|Solid](https://media.giphy.com/media/H7qd9GtAdKvYuqGAWU/giphy.gif)](https://media.giphy.com/media/H7qd9GtAdKvYuqGAWU/giphy.gif)
#### _A minimalistic progress indicators for usage in CLI based python projects_

If you have CLI scripts which shows some kind of progress and if you want to show them in a animated way, then you are at the right place

What makes this library unique from others is the ability to control the color to use while displaying the progress indicators.

#### Currently Supports
 - Counter
 - Countdown
 - Loading Spinner
 - Filling progress bar
 - Filling progress bar with percentage
 - Growing progress bar
 - Process Indicator
 - Process Indicator with percentage

#### Installation
```commandline
pip3 install pyprogressbars
```


#### Usage
```python
import sys,time
from pyprogressbars import counter, loading_spinner, filling_progress_bar, growing_progress_bar, x_slash_y


counter(limit=50, prefix="Counter: ", delay=0.1)
sys.stdout.write("\n")

counter(limit=50, prefix="Countdown: ", delay=0.1, reverse=True)
sys.stdout.write("\n")

loading_spinner("Loading Spinner: ", color="red")
sys.stdout.write("\n")

for i in range(1,26):
    filling_progress_bar(25,i,0.3,"Filling Progress Bar: ", color="yellow")
sys.stdout.write("\n")

for i in range(1,26):
    filling_progress_bar(25, i, 0.3, "Filling Progress Bar (With percentage): ", color="yellow",show_percentage=True)
sys.stdout.write("\n")

growing_progress_bar(50, 0.2, "Growing Progress Bar: ", "green")
sys.stdout.write("\n")

for i in range(1,51):
    x_slash_y("Process Indicator: ",i,50, color="yellow")
    time.sleep(0.2)
    
sys.stdout.write("\n")
for i in range(1,51):
    x_slash_y("Process Indicator (With percentage): ", i,50, show_percentage=True)
    time.sleep(0.2)
    
sys.stdout.write("\n")
```