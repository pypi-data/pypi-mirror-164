# xscreensaver_config
Python parser for .xscreensaver config file


## Installation

```
pip install xscreensaver-config
```

```
from xscreensaver_config.ConfigParser import ConfigParser
config = ConfigParser('/home/user/.xscreensaver')
# Read config as dict
print(config.read())
...

# Update config
config.update({'mode': 'one'})

# Save config
config.save()
```
