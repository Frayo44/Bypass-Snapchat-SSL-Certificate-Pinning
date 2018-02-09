# Bypass-Snapchat-SSL-Certificate-Pinning
Bypass [Snapchat](https://play.google.com/store/apps/details?id=com.snapchat.android) android application certificate Pinning using [Frida](https://www.frida.re/docs/home/). Should work on any version of Snapchat.

###### Tested on version: 10.24.5.0

#### Usage:
```
./frida_spawn.py [path to certificate in PEM format]
```

#### Running example:
```
./frida_spawn.py ./ca.crt
```
