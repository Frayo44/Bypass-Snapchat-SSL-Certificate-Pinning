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

The certificate that is passed to frida_spawn.py is the trusted certifcate. This certificate can be exported from Burp, note that it must be in PEM format.
