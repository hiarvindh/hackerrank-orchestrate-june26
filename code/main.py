from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent.parent
DATASET_DIR = ROOT / "dataset"

claims = pd.read_csv(DATASET_DIR / "claims.csv")
requirements = pd.read_csv(DATASET_DIR / "evidence_requirements.csv")
history = pd.read_csv(DATASET_DIR / "user_history.csv")
samples = pd.read_csv(DATASET_DIR / "sample_claims.csv")


from PIL import Image
for i in range(3):
    relative_path = samples.iloc[0]["image_paths"].split(";")[0]

    image_paths = samples.iloc[i]["image_paths"].split(";")

    for p in image_paths:
        image_path = DATASET_DIR / p
        print(image_path)
        
        img = Image.open(image_path)
        
        print("size =", img.size)
        
        img.show()
    print(image_path)
    print(image_path.exists())

    img = Image.open(image_path)

    print("Image size:", img.size)

    img.show()