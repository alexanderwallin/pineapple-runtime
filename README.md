![pineapple-runtime](pineapple-runtime.png)

# pineapple-runtime

Run-time environment for controlling Ableton Live sets via pineapple.

## Installation

Download `pineapple-runtime` and install necessary dependencies:

```sh
git clone https://github.com/alexanderwallin/pineapple-runtime
cd pineapple-runtime
python setup.py install
```

Note that [`pylive`](https://github.com/ideoforms/pylive) uses [`pyliblo`](https://github.com/dsacre/pyliblo/issues/3), which in turn uses the [`liblo`](http://liblo.sourceforge.net/) C library, so you might have to install that first.

## Usage

1. Open up the Ableton Live set
2. Run `python src/run.py`
3. Watch and listen for modifications on the live set
4. Edit and save the reducer files in any text editor, and they will be hot replaced
