# Energy Consumption Spotify on macOS device 
To rerun the experiment described in the blogpost (add a link!), follow these steps. 

## Necessary software 
We use a python package called spotify-cli to be able to play, pause, save (/download) music through the Spotify application installed on your device. 

### Installing Spotify-cli 
Follow the steps according to the spotify-cli [README](https://github.com/pwittchen/spotify-cli-linux). 
Important to note is that you need to have your Spotify client up and running to use the interface. 
Summarized:
1. In terminal, run: pip3 install spotify-cli --upgrade 
2. In terminal, run: spotify auth login 
3. This runs guides to an online login page, where you need to login to Spotify to be able to use the interface 
4. For instructions on the possibilities, run spotify --help, this contains all the instructions necessary to use the interface

### Installing Intel Power Gadget 

We use Intel Power Gadget to measure the energy usage on the device. Install this using the [instructions](https://www.intel.com/content/www/us/en/developer/articles/tool/power-gadget.html) on the website. 

## Script

The script file used for the first run (with inconclusive results) can be found [here](script_test.py)
