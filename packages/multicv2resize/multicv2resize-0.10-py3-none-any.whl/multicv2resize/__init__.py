import cv2
from multiprocnomain import start_multiprocessing
from a_cv2_easy_resize import add_easy_resize_to_cv2
import numpy as np
from a_cv_imwrite_imread_plus import add_imwrite_plus_imread_plus_to_cv2,open_image_in_cv

def _resize_image(img, width=None, height=None, percent=None, interpolation=cv2.INTER_AREA):
    exec("""import cv2""", globals())
    exec("""from a_cv2_easy_resize import add_easy_resize_to_cv2""", globals())
    add_easy_resize_to_cv2()
    return cv2.easy_resize_image(
        img, width=width, height=height, percent=percent, interpolation=interpolation
    )

def resize_image(pics,processes=5,chunks=1,print_stderr=True, print_stdout=False):
    r"""
    Parallelized image resizing function using OpenCV and multiprocessing.

    This function utilizes the `multiprocnomain` library for parallelizing the resizing process of a batch of images.
    The resizing parameters for each image in the batch are specified in a list of dictionaries,
    allowing for flexibility in resizing options.

    Parameters:
        - pics (list): A list of dictionaries, each containing the following keys:
            - 'img' (Any): Accepts almost any image format
            - 'width' (int, optional): The target width of the resized image. If None, the original width is maintained. - IMPORTANT: (pass either width, height, width and height, or percentage)
            - 'height' (int, optional): The target height of the resized image. If None, the original height is maintained. - IMPORTANT: (pass either width, height, width and height, or percentage)
            - 'percent' (int, optional): The percentage by which to scale the image.  - IMPORTANT: (pass either width, height, width and height, or percentage)
            - 'interpolation' (int, optional): The interpolation method to use during resizing.
              Defaults to cv2.INTER_AREA.

        - processes (int, optional): The number of parallel processes to use for resizing. Defaults to 5.

        - chunks (int, optional): The number of chunks to divide the resizing tasks into for better load balancing. Defaults to 1.

        - print_stderr (bool, optional): If True, prints stderr messages during the resizing process. Defaults to True.

        - print_stdout (bool, optional): If True, prints stdout messages during the resizing process. Defaults to False.

    Returns:
        - dict: A dictionary containing resized images corresponding to the input batch. The keys are generated based on the input image paths.

    Example:

        pics0 = [{'img':r"C:\Users\hansc\Pictures\cgea.png",'width':None,'height':None,'percent':percentage,'interpolation':cv2.INTER_AREA} for percentage in range(50,150,1)]
        pics1 = [{'img':r"C:\Users\hansc\Pictures\cgea.png",'width':100+addwidth,'height':100,'percent':None,'interpolation':cv2.INTER_AREA} for addwidth in range(50,150,1)]
        pics=pics0+pics1

        pic=resize_image(pics,processes=5,chunks=1,print_stderr=True, print_stdout=False)
        for k, v in pic.items():
            cv2.imwrite(rf'C:\resi\{k}.png', v)

    """
    cachedict = {

    }

    for p in pics:
        if not isinstance(p['img'],np.ndarray):
            try:
                p['img'] = cachedict[p['img']]
            except Exception:
                imgpath=p['img']
                p['img'] = open_image_in_cv(p['img'])
                try:
                    cachedict[imgpath] =   p['img']
                except Exception:
                    continue
    return start_multiprocessing(
        fu=_resize_image, it=pics, processes=int(processes), chunks=int(chunks), print_stderr=print_stderr,
        print_stdout=print_stdout
    )



