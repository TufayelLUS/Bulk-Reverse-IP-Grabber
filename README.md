# Bulk Reverse IP Tool
WARNING: this script will generate a huge list of domains and will take time to generate websites depending on your internet speed (up to millions!).<br>Keeping in mind Python's maximum ability to read and write files, kindly do not try to get millions of site at one shot, rather take time and do that in part by part! And if you see nothing is fetched after some moment, it's probably because the site is blocking massive requests from your IP address. Try using tor chain network to get rid of being blocked from sending requests to the source server. Although I added a sleep timer of 1-2 seconds, if that doesn't help, increase the sleep(value) in the code or delete it if you are sure you are not going to be blocked by the server.
<br>
This is not the usual Reverse IP address lookup tool you see around!<br>The special ability of this script is, it will generate a valid IP address range for each of the IP addresses you provide! So, that's going to become a massive thing for you! Try it, and let me know your feelings about it!<br><br>
# Install additional library using the command:
<pre>pip install requests</pre><br>
Usage:
-------
> $terminal: python grab.py<br>
--> IP list file name: list.txt<br>
--> [!] Enable IP range generator? (y/n): y
<br>
list.txt file should contain unique IP addresses separated by new lines so that your data does not become duplicate thus wasting unusual time!<br>
The rest of the work is automated!<br>You can toggle between range generator mode.<br>
Contact for support: no support!
<br>
Thanks to statsnode.com<br>All information collected are provided by statsnode and I will not be responsible for what you do with the information collected by this script.<br><b>Don't forget to follow and give stars if like!</b>
