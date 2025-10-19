import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from src.cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read YAML file and return a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If YAML file is empty.
        e: If there is any other exception while reading file.

    Returns:
        ConfigBox: Parsed YAML content as an object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"YAML file: {path_to_yaml} is empty")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is not properly formatted")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Create directories from a list of paths.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): Whether to log messages. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Save dictionary as JSON file.
    
    Args:
        path (Path): File path to save the JSON.
        data (dict): Data to write.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load JSON file and return as ConfigBox.
    
    Args:
        path (Path): File path to load the JSON from.

    Returns:
        ConfigBox: Loaded data.
    """
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save data as binary (using joblib).
    
    Args:
        data (Any): Python object to save.
        path (Path): File path.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary file (using joblib).
    
    Args:
        path (Path): File path to load.
    
    Returns:
        Any: Loaded Python object.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of a file in KB.
    
    Args:
        path (Path): File path.
    
    Returns:
        str: Size in KB (rounded).
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def decodeImage(imgstring: str, filename: str):
    """Decode a base64 image string and save to a file."""
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
    logger.info(f"Decoded image saved at: {filename}")


@ensure_annotations
def encodeImageIntoBase64(croppedImagePath: str) -> str:
    """Encode image file into base64 string."""
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')


if __name__ == "__main__":
    from pathlib import Path
    test_yaml = Path("config/config.yaml")

    try:
        cfg = read_yaml(test_yaml)
        print(cfg)
    except Exception as e:
        print(f"Error: {e}")
