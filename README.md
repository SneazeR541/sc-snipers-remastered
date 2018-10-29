# How to use

Download [TriGen](http://www.staredit.net/topic/17244/). ([Mirror](http://www.mediafire.com/file/ljglr6eshel5tmg/TriGen.0.0.5.zip/file)).

Make sure you have Python installed. (I've only tested with Python 2.7)

Place `map.py` into the same directory as your `TriGen` folder.

Open a PowerShell window into that same folder. (shift+right click in Windows Explorer).

Open the `.scx` map in SCMDraft 2.

After every change:
- Run `python ./map.py map.txt`
- Open `map.txt`
- Copy the contents of `map.txt` into the Trigger Editor in SCMDraft.
- Press Compile (the check mark). If it fails, it'll tell you a line number which you can use to debug.
- Save the map and run it in Starcraft.