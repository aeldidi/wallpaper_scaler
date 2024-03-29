# Wallpaper Scaler

Scales an image up to your monitor's resolution, blurring the background if it
doesn't fully cover your monitor. I use it to make wallpapers out of album
covers, but it should work with any picture really.

Depends on Pillow, which can be installed by:

```
python3 -m pip install Pillow
```

## How to Use

Modify the `width` and `height` variables in the `wallpaper_scaler.py` to your
monitor's resolution.

`usage: wallpaper_scaler.py file --width WIDTH --height HEIGHT [--output OUTPUT]`

## Example Input Image

![Input Picture](./luvisrage2.jpg)

## Generated Output Image

![Output Picture](./luvisrage2_output.png)

## Example #2

![Another Input Picture](./mohammedali.jpg)

## Output #2

![Output#2](./mohammedali_output.png)
