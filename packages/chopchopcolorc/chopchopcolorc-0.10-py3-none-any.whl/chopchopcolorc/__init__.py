import sys
import numpy as np
import cv2
from locate_pixelcolor_c import search_colors
from a_cv_imwrite_imread_plus import open_image_in_cv
from multiprocca import start_multiprocessing
from multiprocca.proclauncher import MultiProcExecution

def _color_search_c(pic, colors):

    try:
        exec("""import sys""", globals())
        exec("""import numpy as np""", globals())
        exec("""import cv2""", globals())
        exec("""from locate_pixelcolor_c import search_colors""", globals())
        exec("""from a_cv_imwrite_imread_plus import open_image_in_cv""", globals())
        colorsrev = np.array([list(q) for q in (map(reversed, colors))], dtype=np.uint8)


        pic = open_image_in_cv(pic, channels_in_output=3)
        sc = search_colors(pic=pic, colors=colorsrev)
        if len(sc) == 1:
            if np.sum(sc) == 0:
                if not ((pic[0, 0])) in colorsrev:
                    sc = np.array([[-1, -1]], dtype=np.int32)
        return sc
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.stderr.flush()
        return np.array([[-1, -1]], dtype=np.int32)


def color_search_c(
    pics, rgb_tuples, cpus=5, chunks=1, print_stderr=True, print_stdout=False, usecache=True,
):
    r"""

This module provides functions for parallel color search in a collection of images.
It utilizes multiprocessing and a code written in C to efficiently process images concurrently.

Functions:
1. **_color_search_c(pic, colors):**
    - Internal function for color search in a single image.
    - Utilizes the 'locate_pixelcolor_c' module to search for specified colors.
    - Returns an array of coordinates where the colors are found.

2. **color_search_c(pics, rgb_tuples, cpus=5, chunks=1, print_stderr=True, print_stdout=False, usecache=True):**
    - Executes parallel color search on a list of images using multiprocessing.
    - Utilizes '_color_search_c' for each image in parallel.
    - Returns a dictionary with image indices mapped to their corresponding color search results.

Example Usage:
    from chopchopcolorc import color_search_c
    from list_all_files_recursively import get_folder_file_complete_path # optional
    folder=r"C:\testfolderall"
    colors2find = (
        (69, 71, 66),
        (255, 255, 255),
        (153, 155, 144),
        (55, 57, 52),
        (136, 138, 127),
        (56, 58, 53),
        (54, 56, 51),
        (0, 180, 252),
    )
    allpi = [
        x.path
        for x in get_folder_file_complete_path(folder)
        if x.ext == ".png"
    ]


    colorresults=color_search_c(pics=allpi, rgb_tuples=colors2find, cpus=6, chunks=1, print_stderr=True,
    print_stdout=False, usecache=True,)
    print(colorresults)

    """

    f = [
        MultiProcExecution(fu=_color_search_c, args=(pic, rgb_tuples), kwargstuple=())
        for pic in pics
    ]
    formatted_results, raw_data = start_multiprocessing(
        it=f,
        usecache=usecache,
        processes=cpus,
        chunks=chunks,
        print_stdout=print_stdout,
        print_stderr=print_stderr,
    )
    return formatted_results




