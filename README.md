
# Attention Wallpaper Generator

![](img/atwall.png)

## Features

- Generate impressive wallpaper from CLI
- Implemented with OSS only
- Various parameters to tweak

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

Tweak the size, color, font, and stripes.

```bash
$ echo -n "EXAMPLE\n#00" | ./atwall.py -W 240 -H 240 -B '#af8346' -F '#29241d' --text-font 'Noto-Sans-Thin' --text-size 96 --text-scale-x 0.5 --stripe-height 0 img/example-00.png
$ echo -n "見本  #01" | ./atwall.py -W 240 -H 240 -B '#35214c' -F '#86a165' --text-size 96 --text-scale-x 0.5 img/example-01.png
$ echo -n "Beispiel\n#02" | ./atwall.py -W 240 -H 240 -B '#803621' -F '#bbbbbb' --text-font 'Noto-Serif-Black' --text-size 96 --text-scale-x 0.5 --text-scale-y 0.35 --stripe-band-width 0.4 img/example-02.png
```

![EXAMPLE-01](img/example-00.png)
![EXAMPLE-01](img/example-01.png)
![EXAMPLE-02](img/example-02.png)

Output environment information (following commands are for Linux).

```bash
$ OS_INFO="Linux $(uname -r)"
$ PY_INFO="$(python --version)"
$ IM_INFO="$(convert -version | grep -Po 'ImageMagick [0-9.-]+')"
$ WAND_INFO="Wand $(python -c "import pkg_resources; print(pkg_resources.get_distribution('Wand').version)")"
$ echo -n "開発環境\n${OS_INFO} / ${PY_INFO}\n${IM_INFO} / ${WAND_INFO}" | ./atwall.py -B '#3ba7bf' -F black --text-scale-x 0.6 img/development-envrionment.png
```

![Development Environment](img/development-envrionment.png)

See help for more details.

```
$ ./atwall.py -h
```