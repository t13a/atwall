
# Attention Wallpaper Generator

![](img/atwall.png)

## Features

- Generate impressive wallpaper from CLI
- Implemented with OSS only

## Prerequisites

- [Python](https://www.python.org/)
- [ImageMagick](https://imagemagick.org/)
- [Wand](https://github.com/emcconville/wand)
- [Noto Serif Japanese](https://fonts.google.com/noto/specimen/Noto+Serif+JP)

## Getting started

Let's say "Hello world".

```
$ echo -n "こんにちは。\n世界。" | ./atwall.py img/hello-world.png
```

![](img/hello-world.png)

Customize the size, color, text and stripes of the images.

```
$ echo -n "見本 #00" | ./atwall.py -W 320 -H 180 -B '#af8346' -F '#29241d' --text-size 72 --stripe-band-width 0.4 img/example-00.png
$ echo -n "見本 #01" | ./atwall.py -W 320 -H 180 -B '#35214c' -F '#86a165' --text-size 72 --stripe-band-width 0.4 img/example-01.png
$ echo -n "見本 #02" | ./atwall.py -W 320 -H 180 -B '#803621' -F '#bbbbbb' --text-size 72 --stripe-band-width 0.4 img/example-02.png
```

![EXAMPLE-01](img/example-00b.png)
![EXAMPLE-01](img/example-01b.png)
![EXAMPLE-02](img/example-02b.png)

See help for more details.

```
$ ./atwall.py -h
```