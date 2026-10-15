import os
import pandas as pd
import kagglehub

pd.set_option("display.max_rows", None)

DATASET = "rovnez/fc-26-fifa-26-player-data"

def fetch_dataset() -> pd.DataFrame:
    dataset_dir = kagglehub.dataset_download(DATASET)
    file_path = os.path.join(dataset_dir, f"FC26_20250921.csv")

    return pd.read_csv(file_path, low_memory=False, dtype={"player_tags": str})