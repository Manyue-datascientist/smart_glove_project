import os
from dotenv import load_dotenv

# Install Roboflow package if not already installed
try:
    from roboflow import Roboflow
except ImportError:
    os.system("pip install roboflow")
    from roboflow import Roboflow

# Initialize Roboflow API
# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("ROBOFLOW_API_KEY")

if not API_KEY:
    raise ValueError(" Roboflow API key not found in .env file!")

rf = Roboflow(api_key=API_KEY)

# Define the destination folder
DATASET_DIR = "data/final_data/"
os.makedirs(DATASET_DIR, exist_ok=True)

def download_dataset(workspace, project_id, version_number, save_folder):
    """
    Downloads a dataset from Roboflow and saves it in the specified folder.
    """
    print(f"⬇ Downloading dataset: {project_id} (Version {version_number})")
    project = rf.workspace(workspace).project(project_id)
    version = project.version(version_number)
    dataset = version.download("yolov11")

    # Move downloaded files to the final data folder
    downloaded_folder = dataset.location
    #os.system(f"mv {downloaded_folder} {save_folder}")
    print(f"✅ {project_id} downloaded and saved to {save_folder}")

# Grocery Dataset (Individual images)
download_dataset(
    workspace="new-workspace-wfzw3",
    project_id="grocery-dataset-q9fj2",  
    version_number=5,
    save_folder=os.path.join(DATASET_DIR, "grocery_dataset")
)

# Groceries (Low-quality images)
download_dataset(
    workspace="identvintern",
    project_id="groceries-9vwuo", 
    version_number=3,
    save_folder=os.path.join(DATASET_DIR, "groceries")
)

# Shop (Good real shelf dataset)
download_dataset(
    workspace="yolo-test-whuo6",
    project_id="shop-mlcrc",  
    version_number=1,
    save_folder=os.path.join(DATASET_DIR, "shop")
)

# GroceryItems (Good real shelf dataset)
download_dataset(
    workspace="testworkspace-lkgpm",
    project_id="groceryitems-mhbyk",  # This one is provided
    version_number=1,
    save_folder=os.path.join(DATASET_DIR, "grocery_items")
)

print("All datasets downloaded successfully!")
