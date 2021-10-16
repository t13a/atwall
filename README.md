
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

```bash
$ echo -n "こんにちは。\n世界。" | ./atwall.py img/hello-world.png
```

![](img/hello-world.png)

Customize the size, color, text and stripes of the images.

```bash
$ echo -n "見本  #00" | ./atwall.py -W 240 -H 240 -B '#af8346' -F '#29241d' --text-size 96 --text-scale-x 0.5 img/example-00.png
$ echo -n "見本  #01" | ./atwall.py -W 240 -H 240 -B '#35214c' -F '#86a165' --text-size 96 --text-scale-x 0.5 img/example-01.png
$ echo -n "見本  #02" | ./atwall.py -W 240 -H 240 -B '#803621' -F '#bbbbbb' --text-size 96 --text-scale-x 0.5 img/example-02.png
```

![EXAMPLE-01](img/example-00.png)
![EXAMPLE-01](img/example-01.png)
![EXAMPLE-02](img/example-02.png)

Output environment information (following commands are for Linux).

```bash
$ OS_VER="Linux $(uname -r)"
$ PY_VER="$(python --version)"
$ IM_VER="ImageMagick $(convert -version | grep -Po '(?<=ImageMagick) ([0-9.-]+)')"
$ WAND_VER="Wand $(python -c "import pkg_resources; print(pkg_resources.get_distribution('Wand').version)")"
$ echo -n "開発環境\n${OS_VER} / ${PY_VER}\n${IM_VER} / ${WAND_VER}" | ./atwall.py -B black -F orange --text-scale-x 0.6 img/development-envrionment.png
```

![Development Environment](img/development-envrionment.png)

See help for more details.

```
$ ./atwall.py -h
```