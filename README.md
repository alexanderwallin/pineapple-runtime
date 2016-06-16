![pineapple-runtime](pineapple-runtime.png)

# pineapple-runtime

Run-time environment for controlling Ableton Live sets via pineapple.

## Prerequisites

* Ableton Live 9 Suite - Tested successfully on 9.2.3, not working on 9.6.1
* [LiveOSC](https://github.com/dinchak/LiveOSC) added [as a MIDI Control Surface](http://livecontrol.q3f.org/ableton-liveapi/liveosc/)
* [`liblo`](http://liblo.sourceforge.net/)

## Installation

Clone `pineapple-runtime` and install necessary dependencies:

```sh
git clone https://github.com/alexanderwallin/pineapple-runtime
cd pineapple-runtime
python setup.py install
```

Note that [`pylive`](https://github.com/ideoforms/pylive) uses [`pyliblo`](https://github.com/dsacre/pyliblo/issues/3), which in turn uses the [`liblo`](http://liblo.sourceforge.net/) C library, so you might have to install that first.

## Usage

1. Open up the Ableton Live set
2. Run `python src/run.py`
3. Hear the set being modified on every beat
4. Edit and save a reducer file in any text editor, and it will be hot-reloaded, making it's modification to the set to apply immediately
