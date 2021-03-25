import os

# visual Genome captions
def get_genome_captions(root_folder="../output/VG_100K_2"):

  with open(os.path.join(root_folder, region_descriptions.json) as f:
    regdes = json.load(f)
    
  captions = {}
  dropped = []
  for item in regdes:
    id = item["id"]
    path = f"../VG_100K_2/VG_100K/{id}.jpg"
    if not os.path.exists(path):
      path = f"../VG_100K_2/VG_100K_2/{id}.jpg"
    if not os.path.exists(path):
      dropped.append(id)
      continue
    captions["genome_"+str(item["id"])] = {
      "caption":" ".join([x["phrase"] for x in item["regions"]]),
      "path": path
    }
    
  return captions, dropped
