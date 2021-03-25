# python file to get the captions

import io
import os
import json
import random
import pandas as pd
from tqdm import trange
from ast import literal_eval
from argparse import ArgumentParser

# declare URLS
CLASSES = "https://storage.googleapis.com/openimages/2018_04/class-descriptions-boxable.csv"
RELATION_LABELS = "https://storage.googleapis.com/openimages/2019_01/challenge-2018-relationships-description.csv"
ATTRIBUTES = "https://storage.googleapis.com/openimages/2019_01/challenge-2018-attributes-description.csv"

IMAGE_LABELS = {
  "train": "https://storage.googleapis.com/openimages/2018_04/train/train-annotations-human-imagelabels-boxable.csv",
  "val": "https://storage.googleapis.com/openimages/2018_04/validation/validation-annotations-human-imagelabels-boxable.csv",
  "test": "https://storage.googleapis.com/openimages/2018_04/test/test-annotations-human-imagelabels-boxable.csv"
}
NARRATIVES = {
  "train": "https://storage.googleapis.com/localized-narratives/annotations/open_images_train_v6_captions.jsonl",
  "val": "https://storage.googleapis.com/localized-narratives/annotations/open_images_validation_captions.jsonl",
  "test": "https://storage.googleapis.com/localized-narratives/annotations/open_images_test_captions.jsonl"
}

# https://storage.googleapis.com/openimages/web/download_v4.html
# NOTE: we will provide visual relationships annotations on the test and validation sets soon - stay tuned!
RELATIONS_TRAIN = "https://storage.googleapis.com/openimages/2019_01/train/challenge-2018-train-vrd.csv"


# ---- functions
def fetch(url):
  # https://github.com/geohot/tinygrad/blob/master/extra/utils.py
  import requests, os, hashlib, tempfile
  fp = os.path.join(tempfile.gettempdir(), hashlib.md5(url.encode('utf-8')).hexdigest())
  if os.path.isfile(fp) and os.stat(fp).st_size > 0:
    with open(fp, "rb") as f:
      dat = f.read()
  else:
    print("fetching %s" % url)
    dat = requests.get(url).content
    with open(fp+".tmp", "wb") as f:
      f.write(dat)
    os.rename(fp+".tmp", fp)
  return dat


def get_data_narratives(merged_labels, split = "train"):
  # takes the merged_labels and split and returns a dictionary object
  if split not in ["test", "train", "val"]:
    raise ValueError("split should be one of `test`, `train`, `val`")

  print("-"*70)
  print("Starting Process for", split.upper())

  # this process creates temporary fetch files because we don't really need to store those
  # labels
  image_labels = pd.read_csv(io.BytesIO(fetch(IMAGE_LABELS[split])))
  image_labels.LabelName = [merged_labels[x] for x in image_labels.LabelName.values]
  
  # narratives
  narratives = [literal_eval(x) for x in  fetch(NARRATIVES[split]).decode("utf-8").split("\n")[:-1]]
  narratives_train_by_id = {}
  for x in narratives:
    narratives_train_by_id[x["image_id"]] = x["caption"]

  # now we need to match the image ids with the ones in our labels
  img_ids_train = set(image_labels.ImageID.unique().tolist())
  print(f"[{split.upper()}] Total images in labels:", len(img_ids_train))
  img_ids_train_narratives = set(narratives_train_by_id.keys())
  print(f"[{split.upper()}] Total images in narratives:", len(img_ids_train_narratives))
  common = img_ids_train_narratives.intersection(img_ids_train)
  print(f"[{split.upper()}] Total images in common:", len(common))

  # convert to target format
  all_data = []
  common = list(common)
  for _, _id in zip(trange(len(common)), common):
    df_sub = image_labels[image_labels.ImageID == _id]
    _d = {
      "labels": df_sub.LabelName.values.tolist(),
      "score": df_sub.Confidence.values.tolist(),
      "caption": narratives_train_by_id[_id],
      "source_split": split,
      "original_language": "en", # all narratives are in english so we can hardcode
      "dataset": "open_images_v4"
    }
    all_data.append(_d)

  # print two samples for user
  print("-"*70)
  print("Two Samples:\n")
  for _ in range(2):
    print(random.choice(all_data))
    print()

  return all_data


if __name__ == "__main__":
  args = ArgumentParser(description="""Get captions for OpenImagesv4.""")
  args.add_argument(
    "--only-narratives",
    action = "store_true",
    default = False,
    help = "If passed file only loads the captions from Google's Localized Narratives "
    "(google.github.io/localized-narratives/)"
  )
  args.add_argument(
    "--target-path",
    default = "./",
    help = "Pass the path where you want to store (def: `./`)"
  )
  args = args.parse_args()

  # while the captions are not ready we are only using narratives
  if not args.only_narratives:
    raise ValueError("Can only load narratives right now")

  # define things that will be used for each split
  classes = pd.read_csv(io.BytesIO(fetch(CLASSES)), names = ["id", "name"])
  class_labels = {}
  for x in json.loads(classes.to_json(orient = "records")):
    class_labels.update({x["id"]: x["name"]})
  
  attributes = pd.read_csv(io.BytesIO(fetch(ATTRIBUTES)), names = ["id", "name"])
  attributes_labels = {}
  for x in json.loads(attributes.to_json(orient = "records")):
    attributes_labels.update({x["id"]: x["name"]})

  # In the relations the LabeleName2 can have either classes or attributes
  # thus create a common merged dict
  merged_labels = {}
  merged_labels.update(class_labels)
  merged_labels.update(attributes_labels)

  # now go over different splits and get the output
  for split in IMAGE_LABELS:
    data = get_data_narratives(merged_labels, split)
    path = os.path.join(args.target_path, f"open_images_{split}.json")
    print("Writing file:", path)
    with open(path) as f:
      f.write(json.dumps(data))

  print("Completed Process")
  print("-" * 70)
