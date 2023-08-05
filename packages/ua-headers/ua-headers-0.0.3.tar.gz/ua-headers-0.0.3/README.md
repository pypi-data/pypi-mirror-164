## Fake Headers

**An ideal tool for generating random user agents**

```
User Agents:

Elementaryos # elementary OS
Blackberry   # blackberry
Openbsd      # openbsd
Windows      # windows
Console      # nintendo/ps/xbox
Android      # android
Sumbian      # sumbian OS
Sunos        # Sun OS
Linux        # fedora/ubuntu/debian & other
Ios          # ios
```

```python
from headers import ua

ua.elementaryos() #Generate elementary OS user agent
ua.blackberry() #Generate Blackberry user agent
ua.windows() #Generate Windows user agent
ua.console() #Generate Nintendo/PS/Xbox user agent

ua.openbsd() #Generate OpenBSD user agent
ua.sumbian() #Generate Sumbian user agent
ua.android() #Generate Android user agent
ua.sunos() #Generate sun OS user agent
ua.linux() #Generate Linux user agent
ua.ios() #Generate IOS user agent
```
