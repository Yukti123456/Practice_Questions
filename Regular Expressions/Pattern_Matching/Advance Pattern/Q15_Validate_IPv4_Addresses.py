#Q15_Validate IPv4 addresses(0-255 for each octect.).

import re

Text ="""Yesterday, the server was configured with IP 19.16.1.10 and backup server had 10.0.0.255.
      However, some incorrect entries were found in logs:
      256.100.50.25
      192.168.1
      172.16.300.1
      The firewall also recorded connections from 8.8.8.8 and 172.16.254.3.
      But these were invalid attempts:
      999.10.10.10  abc.1.1.1"""
      
Pattern = r'\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}\b'

Matches= re.findall(Pattern,Text)
for address in Matches:
    if(Matches):
         print(address," is valid IPV4 Address")

