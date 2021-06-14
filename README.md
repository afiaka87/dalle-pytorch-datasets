# (Archived) 

## @robvanvolt has created a much more fleshed out version here: https://github.com/robvanvolt/DALLE-datasets

None of this code works yet. If you'd like to contribute, create a pull request! We need all the datasets we can get. Otherwise come back in a few weeks to check on progress.

This repository includes metadata and instructions for downloading many captioned datasets + generated captions from labels.

Thanks to @yashbonde, we eventually intend to include generated captions for a variety of datasets that don't include captions.

## Data Format

Since this is a highly versatile dataset we have a common format for each sample:
```
{
  "image_id": {
    "labels": ["car", "chair", "something else"],
    "score": [0, 1, 1],
    "caption": "caption goes here",
    "dataset": "open_images_v4"
    "source_split": "train",
    "original_language": "eng",
  }
}
```

* `image_id`: this will be expanded to the complete filepath when training
* `labels`: in case the given images has labels add those here, **default is `None`**
* `score`: in case there is a score against that labels eg. OpenImages, **default is `None`**
* `caption`: generated caption goes here
* `source_split`: what split was this a part of in the datasset it is of
* `dataset`: key of the dataset name
* `original_language`: in case this has multilingual dataset use [ISO-639-2 code](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes)


## Datasets

|name|size|image count|link|used for VAE|captions given|captions generated|
|-|-|-|-|-|-|-|
|Downscale OpenImagesv4|16GB|1.9M|[torrent](https://academictorrents.com/details/9208d33aceb2ca3eb2beb70a192600c9c41efba1)|✅| | |
|Stanford STL-10|2.64GB|113K|[torrent](https://academictorrents.com/details/a799a2845ac29a66c07cf74e2a2838b6c5698a6a)|✅| | |
|CVPR Indoor Scene Recognition|2.59GB|15620|[torrent](https://academictorrents.com/details/59aa0ad684e5d849f68bad9a6d43a9000a927164)|✅| | |
|The Visual Genome Dataset v1.0 + v1.2 Images|15.20GB|108K|[torrent](https://academictorrents.com/details/1bfe6871046860a2ff8c0cc1414318beb35dc916)|✅|✅| |
|Food-101|5.69GB|101K|[torrent](https://academictorrents.com/details/470791483f8441764d3b01dbc4d22b3aa58ef46f)|✅| | |
|The Street View House Numbers (SVHN) Dataset|2.64GB|600K|[torrent](https://academictorrents.com/details/6f4caf3c24803d114c3cae3ab9cb946cd23c7213)|✅| | |
|Downsampled ImageNet 64x64|12.59GB|1.28M|[torrent](https://academictorrents.com/details/96816a530ee002254d29bf7a61c0c158d3dedc3b)|✅| |
|COCO 2017|52.44GB|287K|[torrent](https://academictorrents.com/details/74dec1dd21ae4994dfd9069f9cb0443eb960c962) [website](https://cocodataset.org/#download)| | |
|Flickr 30k Captions (bad data, downloads duplicates)|8GB|31K|[kaggle](https://www.kaggle.com/hsankesara/flickr-image-dataset)| |✅| | 

## Other Projects

This a big community led effort, find more projects:
* [`DALLE-pytorch`](https://github.com/lucidrains/DALLE-pytorch/)
* [`dall-e-baby`](https://github.com/yashbonde/dall-e-baby)

## Connect with us

You can join the [discord](https://discord.gg/hBtKR6JF) for direct communication.
