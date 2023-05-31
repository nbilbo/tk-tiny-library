from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

import ttkbootstrap as ttk
from PIL import Image


def get_system_date(ftime: str = '%m/%d/%Y') -> str:
    return datetime.now().strftime(ftime)


def get_system_time(ftime: str = '%Y:%M:%S') -> str:
    return datetime.now().strftime(ftime)


def get_system_datetime(ftime: str = '%m/%d/%Y %H:%M:%S') -> str:
    return datetime.now().strftime(ftime)


def load_image_tk(
    path: Path, geometry: Optional[Tuple[int, int]] = None
) -> ttk.ImageTk.PhotoImage:
    image = Image.open(path)

    if geometry is not None:
        return ttk.ImageTk.PhotoImage(image.resize(geometry))

    return ttk.ImageTk.PhotoImage(image)
