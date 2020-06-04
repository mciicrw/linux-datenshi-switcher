# Linux Datenshi Switcher

As the name said, this app is used to switch between [Official Bancho Server](https://osu.ppy.sh) and [Datenshi Private Server](https://datenshi.xyz), this one is forked from my other project but yet to be released, so stay tune.

Why there's none server switcher in linux? well, this happened because of wine's behavior, we can't directy install certificate into wine's trusted root certificate list via commandline, this app also can't do that, only make editing `/etc/hosts` easier, but there's prompt of "How to install certificate manually" evertime "Switch to Datenshi" button pressed, so don't worry if you forgot to install certificate in first place

## How to use

Simply run app as root via right-click menu or via terminal using `sudo ./switcher`

## Building from scratch

TODO: complete this section

### Prerequisites

- Linux Machine (yes)
- Python3 (Python 3.8.x recommended as i'm using this version)
- PyQt5 (5.12.8+)
- Pyinstaller (latest recommended)
- QDarkStyle (For dark theme)

#### Building

- install the dependency first `pip install PyQt5 pyinstaller qdarkstyle`
- move to linux server switcher folder
- run `pyinstaller --add-data 'dep:dep' switcher.py`
- compiled app can be found inside "dist" folder

If you don't want to use dark theme, then skip qdarkstyle installation and delete (or comment out) these lines:
- `import qdarkstyle`
- `dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()`
- `app.setStyleSheet(dark_stylesheet)`

#### Running app

- This app can be run from without compiling first, just make sure all dependecies are installed, then run `sudo python3 switcher.py`
- For compiled binaries you can run as root via right-click menu or via terminal using `sudo ./switcher`

## Support

This app is still in heavy development, not yet to be released, but if you want to help me developing this i highly appreciate that, you can contact me in discord here `TypicalNoob-#3733`