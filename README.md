# tablo_npvr
TabloTV M3U generator for use with NextPVR
---
I wrote this for a few reasons...
1. To practice my Python coding.
2. I had just bought a Tablo device and wanted to explore it.
3. I couldn't use the new Tablo with Plex and so I decided to move on to another in-home streaming platform.

Much of the credit goes to [tmm1](https://github.com/tmm1) and his [tablo-for-channels](https://github.com/tmm1/tablo-for-channels) project.  But I wanted it in Python, not Go, and I didn't want to mess with Docker for such a lightweight use case.  So here we are.  I really made this for me, but if someone finds it helpful then rock on.  I've tested it on NextPVR v6.1.1.221106 and also with Jellyfin 10.8.9 but any platform that accepts M3U tuners should work with little or no modification.

## Setup
The only dependency you should need that's not already included in Python is the 'requests' module.
>pip install requests

You'll need the IP address of the TabloTV device to put into the tabloIP variable in each of the scripts.  Make sure your channel scan has been performed within the Tablo itself.

Also I run this on the same box as my NextPVR setup so the scripts use 127.0.0.1 to reflect that.  Your setup may be different and you'll need to account for that.

## Running
- First run channel_update.py to pull the list of available channels from the Tablo.  This creates your M3U file for NextPVR to use.
- Once the playlist.m3u is generated you can run tablo_npvr.py to start your server on port 8050 (or any other port you choose.)  You could also set it to run at bootup using whetever method your OS supports.
- Once the server is listening on 8050, import a new IPTV device in NextPVR and point it to http://127.0.0.1:8050/playlist.m3u, or whatever IP/Port combination you decide to go with.
