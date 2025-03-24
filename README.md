# HEIC to PNG Converter

This Python script converts all HEIC files in a directory into several formats, including `PPM`, `PNG`, `JPEG`, `GIF`, `TIFF`, and `BMP`. It's a fork of the [`heic-to-png` repository](https://github.com/victorlvl47/heic-to-png) by [`victorlvl47`](https://github.com/victorlvl47), with modifications to dynamically specify the output directory and file extension, and it also adds support for macOS. The script uses the `pillow-heif` library to read the HEIC files and the `Pillow` library to save them in the specified formats. By default, the converted images are saved as `.png` files in a folder named `heic_img`, located within the same directory as the original HEIC files. 

![heic to png](heic-to-png.png)

## Requirements

This script requires the following libraries to be installed:

- `Pillow`
- `pillow-heif`

You can install them by running:

```
pip install pillow
```

```
 pip install pillow-heif
```

## Usage

0. Clone this repo to any directory of your choosing on your machine. I tested this on an Apple silicon MacBook, but it should work on other operating systems.

1. Place all the `HEIC` files you want to convert in the repo's root directory (`heic-to-png`), i.e., the one containing the `main.py` file.

2. Run the `main.py` script using the following command:

   ```
   python main.py
   ```

3. All HEIC files in the repo's directory will be converted to `PNG` format and saved in a directory named `heic_img` with the `.png` extension within the repo's root directory.

4. Optionally, you can specify a custom directory name **and** output image file extension by using the following command:
   
   ```
   python main.py <your_custom_dir_name> <your_custom_file_extension>
   ```
Example: `python main.py my_save_dir jpeg`. 

**Note**: You must specify BOTH a custom directory AND a custom file extension (see supported extensions below) for the conversion process to work. Not specifying one or the other will cause the conversion to fail.

### Supported File Extensions for `heic-to-png`

| Format Name | File Extension | Example Command                     |
|-------------|----------------|-------------------------------------|
| PPM         | `.ppm`         | `python main.py my_save_dir ppm`   |
| PNG         | `.png`         | `python main.py my_save_dir png`   |
| JPEG        | `.jpeg`        | `python main.py my_save_dir jpeg`  |
| GIF         | `.gif`         | `python main.py my_save_dir gif`   |
| TIFF        | `.tiff`        | `python main.py my_save_dir tiff`  |
| BMP         | `.bmp`         | `python main.py my_save_dir bmp`   |

## Notes

- This script was modified from the original and tested on macOS Sonoma 14.7.4.
