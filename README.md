Some data from [Tip of the Hats 2015](http://tipofthehats.org). I intend to post some of my findings, so it's probably a good idea to upload the raw data and what I used to collect it. There's not much to the code, but I included it anyway.

The data includes [toth_chat](toth_chat.log) (the Twitch chat) and [toth_data](toth_data.txt) (some statistics). The chat was collected using [HexChat](https://hexchat.github.io) (I wrote [irc_logger](irc_logger3.py) to do something like this, but it was bugged for most of the stream). The statistics, including viewers, followers, and views, were collected using Twitch's API (the latter two are approximations, but they're the less interesting statistics anyway). 

As far as the scripts go, [collect_stats](collect_stats.py) was of course used to fetch stream data every minute (starting abaout 4 hours into the stream, when I had the idea to write it), and includes a little over 2000 entries. [Counter](counter.py) and [Counter2](counter2.py) were quick tools used to sift through the data (they were pretty much just caught up in the push).

I'll probably make and post some graphs of the data; feel free to do the same.
