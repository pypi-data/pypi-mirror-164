# style2pic

This repository contains implementations for a set of popular style transfer methods between images. The core process is described by the following:

<img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/content_style_synthesized.jpg" width="50%" align="right">

* two images of arbitrary shapes are used, where the style of the first one (style image) is applied to the content of the second one (content image)
* the process is configurable with various parameters that control trade-offs like speed vs quality, stylization strength vs content preservation, fine-grained details vs coarse-level details, etc.
* one has the option to provide a spatial mapping to match the areas that should transfer between the images by means of providing some masks of the same shape as the inputs
* the running time is relatively fast (<30 seconds) especially when using a GPU; for greater details or higher resolution images the process can be prolonged

Last but not least, the package **stram** (**s**tyle **tra**nsfer **m**achine) is also introduced and it's available to use in other applications as a standalone python library.

## Outline
1. [Methods](#1-methods)
    * [Gatys](#gatys)
    * [Yijun](#yijun)
    * [Reinhard](#reinhard)
2. [Installation](#2-installation)
    * [Option 1: By cloning the repo](#option-1-by-cloning-the-repo)
    * [Option 2: By installing the library](#option-2-by-installing-the-library)
3. [How to use](#3-how-to-use)
    * [Option 1: After cloning the repo](#option-1-after-cloning-the-repo)
    * [Option 2: Using the API](#option-2-using-the-api)

## 1. Methods

### Gatys

Based on *"A Neural Algorithm of Artistic Style"* by Leon A. Gatys, Alexander S. Ecker and Matthias Bethge (https://arxiv.org/abs/1508.06576). The implementation can be found [here](stram/domain/methods/gatys_method.py).

The algorithm works by using a well pretrained classification model (VGG19) as a feature extractor. Content is kept by directly minimizing the loss between the features from the content image and the features from the synthesized image from various levels of VGG19. Style is enforced by mathcing statistics between the features of the style image and the features of the synthesized image. These statistics are obtained by computing the gram matrix on the channel dimension.

It acts as a proper style transfer technique and it works best when the style image has a lot of coherent patterns as generally found in artistic paintings.

<p align="center">
  <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/example_gatys.jpg" width="75%"><br>
</p>

### Yijun

Based on *"A Closed-form Solution to Photorealistic Image Stylization"* by Yijun Li, Ming-Yu Liu, Xueting Li, Ming-Hsuan Yang, Jan Kautz (https://arxiv.org/abs/1802.06474). The implementation can be found [here](stram/domain/methods/yijun_method.py).

The algorithm works in 2 steps. The first, called photorealistic stylization, embbeds the content and style images using intermediary layers VGG19 encoders and attempts to make the content feature correlations match the style feature correlations by appying the whitening-colouring transform (WCT). The resulted feature map is then decoded back to RGB space using some pretrained VGG19 layer decoders. The second step, called photorealistic smoothing, takes the result from step 1 and the original content image and tries to ensure consistency between the stylizations of semantically similar regions (using the content image as reference). There are two options for this step, the precise optimization using the matting affinity laplacian and the faster guided image filtering.

The algorithm is focused more on transferring colour rather than structural patterns, so it acts more like a scene ambiance transfer than an actual style transfer.

<p align="center">
  <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/example_yijun.jpg" width="75%"><br>
</p>

### Reinhard

Based on *"Colour Transfer between Images"* by Erik Reinhard, Michael Ashikhmin, Bruce Gooch, Peter Shirley (https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf). The implementation can be found [here](stram/domain/methods/reinhard_method.py).

Performs the transfer of colour from one image to another by borrowing statistical charactersitics. Both images are converted into LAB space, a colour space where the values between different channels are almost completely decorrelated. Then, the first and second order stats (mean and std) are computed for both images and the stats of the style image are enforced onto the content image by means of applying a simple normalization.

This rather naive method is most commonly used for stain normalization and augmentation in the medical domain. Its artistic power is quite limited, but can be used when a very quick and plain colour distribution exchange is desired.

<p align="center">
  <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/example_reinhard.jpg" width="75%"><br>
</p>

## 2. Installation

This package requires `python==3.7` and `tensorflow>=2.7`.

### Option 1: By cloning the repo

The following instructions are meant for Linux platforms, but some variations are also supported by Windows and macOS.

1. Clone the repo.
2. Install conda (https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
3. Open a command prompt and run:
    ```
    make install
    ```
    This will create a virtual environment with all the requirements.
4. Activate the environment and you're good to go (on Windows you might have to use `source` instead of `conda`):
    ```
    conda activate s2p
    ```

### Option 2: By installing the library

1. (Optional) Create a virtual python environment (of any kind).
2. Run:
    ```
    pip install stram
    ```

## 3. How to use

### Option 1: After cloning the repo

By cloning the repo, one could take advantage of the scripts designed to make the style transfer process fast and easy. In order to check if your setup is in good shape (presumably after following the instructions from the installation section), you can run:
```
make test
```
If all tests passed, then the repo has been set up successfully.

Now back to running a simple style transfer process using two images. All one needs to do is to run `scripts/run_stram.py` which expects the following arguments:
* `-s` / `--style_image`: path to the image to copy style from
* `-c` / `--content_image`: path to the image on which to apply the style
* `-f` / `--config_file`: path to a json file that specifies some parameters for the process (including which method to use)
* `-o` / `--output_folder`: path to a directory where the results will be saved

We will use the two images from the `tests/data` directory to exemplify this. Try running:
```
python scripts/run_stram.py -s tests/data/style_image.jpg -c tests/data/content_image.jpg -f configs/gatys_config.json -o outputs/example_run
```
This call starts a style transfer process and you should expect to see a folder `outputs/example_run` in which the resulting image is saved. The final synthesized image probably looks something like this:

<p align="center">
  <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/run_example.jpg" width="35%"><br>
</p>

The image has a weird name which represents its hash value. Hash values are also computed for input images and even for input configurations (from the config file), and they ensure that a process is not performed twice with the same overall inputs. For example, if you run the above command again you'll notice the process will not do anything because it sees that for the given input images and configurations, a synthesized image has already been computed. You can see the configurations used along with the hashes for the style image, content image and input parameters in the `outputs/example_run/worklog.json` file.

---

The system was conceived to support a **grid search** over many parameters for the same input images. To search over the space of multiple values for a given parameter, simply turn the value to a list of values in the config file. For example, one could change the fields `content_layers` and `style_loss_weight` in `configs/gatys_config.json` to:
```
"content_layers": [
    {
        "block2_conv2": 1.0
    },
    {
        "block5_conv2": 1.0
    }
],
"style_loss_weight": [0.01, 0.1, 10.0],
```
and run the same command as before but with a different output folder:
```
python scripts/run_stram.py -s tests/data/style_image.jpg -c tests/data/content_image.jpg -f configs/gatys_config.json -o outputs/example_run_grid
```
The worklog file `outputs/example_run_grid/worklog.json` looks a bit more complicated now. It maps the name of the images (their hashes) to the configurations used for obtaining them. The resulting images would probably look something like this based on the configs provided:

Style Loss Weight \ Content Layers | block2_conv2 | block5_conv2
--- | --- | ---
**0.01** | <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/run_example_block2_1e-2.jpg"> | <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/run_example_block5_1e-2.jpg"> |
**0.1** | <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/run_example_block2_1e-1.jpg"> | <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/run_example_block5_1e-1.jpg"> |
**10.0** | <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/run_example_block2_1e1.jpg"> | <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/run_example_block5_1e1.jpg"> |

This grid search can be useful since it's hard to know from the beginning which configuration works best with your pair of input images. Be careful though as the number of instances to run can grow exponentially with the number of arguments (and the number of associated values) to iterate over. You can however avoid pairing every value with every value by constructing parallel grids. This is done by chaining multiple dicts in the high level `configs` list from the provided json. One such example is provided in `configs/all_config.json` which performs a set of runs for each separate method. Notice that when using this config, the values for `"style_loss_weight": [1e0, 1e-2, 1e-4]` are only iterated over in the local context of the `gatys` dict, and do not interfere with the other dicts provided for `yijun` method.

---

The last thing to be discussed is the usage of mapping **masks**. The script also takes some optional params:
* `-j` / `--style_mask`: path to the mask for the style image
* `-k` / `--content_mask`: path to the mask for the content image

The masks constrain the style transfer process to map spatial regions from one image to another. They contain per pixel labels and the set of labels for the two masks must be the same. The label `0` is special and represents an area that should not be modified in the content image, and an area which is ignored completely in the style image. The masks must have the same shape as their corresponding input image.

Let's come back to the first run, but provide masks this time:
```
python scripts/run_stram.py -s tests/data/style_image.jpg -c tests/data/content_image.jpg -j tests/data/style_mask.png -k tests/data/content_mask.png -f configs/gatys_config.json -o outputs/example_run_masked
```
The resulting image should look something like this:

<p align="center">
  <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/run_example_masked.jpg" width="35%"><br>
</p>

This makes sense since the superposition of the input images with their masks looks something like this:

<p align="center">
  <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/content_mask_superposition.jpg" width="35%">
  <img src="https://gitlab.com/forgeai/style2pic/-/raw/master/assets/style_mask_superposition.jpg" width="26.11%">
</p>

where the labels `(0, 1, 2)` run from top to bottom for the content image and as `(1, 0, 2)` from left to right on the style image.

### Option 2: Using the API

A quick demo is presented here:
https://colab.research.google.com/drive/1PlkUmpzSdcISntR8lDiGEkMQlaYGmeFh?usp=sharing
