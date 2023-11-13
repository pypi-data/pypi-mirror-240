import os
import cv2
from a_cv_imwrite_imread_plus import open_image_in_cv
import numexpr
import numpy as np
from a_cv2_easy_resize import add_easy_resize_to_cv2
from typing import Union, Any
from multicv2resize import resize_image
from multiprocca import start_multiprocessing
from multiprocca.proclauncher import MultiProcExecution
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
import pandas as pd
pd_add_apply_ignore_exceptions()
add_easy_resize_to_cv2()


def get_difference_of_2_pics(
        first: Any,
        second: Any,
        percent_resize,
        orig_image: Any,
        draw_output: bool = False,
        draw_color: Union[tuple, list] = (255, 255, 0),
        thickness: int = 2,
        thresh: int = 3,
        maxval: int = 255,
) -> tuple:
    colz = [
        "start_x",
        "start_y",
        "end_x",
        "end_y",
        "center_x",
        "center_y",
        "width",
        "height",
        "area",
    ]
    exec("""import cv2""", globals())
    exec("""import numexpr""", globals())
    exec("""import numpy as np""", globals())
    out = np.array([], dtype=np.uint16)

    gray = numexpr.evaluate(
        f"abs(first-second)",
        global_dict={},
        local_dict={"first": first, "second": second},
    ).astype(np.uint8)
    dilated = gray.copy()
    for i in range(0, 3):
        dilated = cv2.dilate(dilated, None, iterations=i + 1)

    (T, thresh) = cv2.threshold(dilated, thresh, maxval, cv2.THRESH_BINARY)
    cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if draw_output:
        out = orig_image
    allresults = []
    if len(cnts) == 2:
        cnts = cnts[0]
    elif len(cnts) == 3:
        cnts = cnts[1]
    for cc in cnts:
        box = cv2.boundingRect(cc)
        (x, y, w, h) = [int(x / (percent_resize / 100)) for x in box]
        allresults.append(
            dict(zip(colz, (x, y, x + w, y + h, x + (w // 2), y + (h // 2), w, h, w * h)))
        )
        if draw_output:
            cv2.rectangle(
                out, (x, y), (x + w, y + h), tuple(reversed(draw_color)), thickness
            )
            yva = y
            for key1, item1 in allresults[-1].items():
                yva = yva + 20
                cv2.putText(
                    out,
                    f"{key1}: {item1}",
                    (x, yva),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    (1 / 2),
                    (0, 0, 0),
                    3,
                )
                cv2.putText(
                    out,
                    f"{key1}: {item1}",
                    (x, yva),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    (1 / 2),

                    draw_color,
                    1,
                )
    return allresults, out


def finddifferences(singlepicture, picturelist,
                    percentage=10,

                    interpolation=cv2.INTER_NEAREST,
                    cpus=5,
                    chunks=1,
                    draw_output=True,
                    usecache=True,
                    print_stdout=False,

                    print_stderr=True,
                    draw_color=(255, 255, 0),
                    thickness=2,
                    thresh=3,
                    maxval=255,
                    save_folder=None
                    ):
    r"""
        finddifferences - Detect Differences Between a Single Image and a List of Images

        This function compares a single reference image to a list of target images using OpenCV and multiprocessing.
        It identifies and highlights differences between the reference image and each target image, producing a DataFrame
        with detailed information about the differences.

        Parameters:
        - `singlepicture` (str): The file path of the reference image.
        - `picturelist` (list of str): A list of file paths of target images to compare against the reference image.
        - `percentage` (int, optional): Percentage by which to resize the images for comparison. Default is 10%. - the smaller, the faster
        - `interpolation` (int, optional): Interpolation method for resizing images. Default is cv2.INTER_NEAREST.
        - `cpus` (int, optional): Number of CPU cores to use for multiprocessing. Default is 5.
        - `chunks` (int, optional): Number of chunks to split the image processing into. Default is 1.
        - `draw_output` (bool, optional): Whether to draw the output images with highlighted differences. Default is True.
        - `usecache` (bool, optional): Whether to use caching for image processing results. Default is True.
        - `print_stdout` (bool, optional): Whether to print standard output during multiprocessing. Default is False.
        - `print_stderr` (bool, optional): Whether to print standard error during multiprocessing. Default is True.
        - `draw_color` (tuple, optional): RGB color for drawing differences. Default is (255, 255, 0).
        - `thickness` (int, optional): Thickness of the drawn rectangles. Default is 2.
        - `thresh` (int, optional): Threshold for image binarization. Default is 3.
        - `maxval` (int, optional): Maximum value for image binarization. Default is 255.
        - `save_folder` (str, optional): Folder path to save the output images. If None, images are not saved. Default is None.

        Returns:
        - `pd.DataFrame`: A DataFrame containing information about the differences, including bounding box coordinates,
          centers, widths, heights, areas, and the index of the corresponding target image.

        Example:
            import cv2
            from multiwhacamole import finddifferences
            picturelist = [
                r"C:\Users\hansc\Downloads\dfsdfsdf\0.png",
                r"C:\Users\hansc\Downloads\dfsdfsdf\1.png",
                r"C:\Users\hansc\Downloads\dfsdfsdf\2.png",

            ]
            singlepicture = r"C:\Users\hansc\Downloads\dfsdfsdf\0.png"
            df = finddifferences(singlepicture, picturelist,
                                 percentage=10,

                                 interpolation=cv2.INTER_NEAREST,
                                 cpus=5,
                                 chunks=1,
                                 draw_output=True,
                                 usecache=True,
                                 print_stdout=False,
                                 print_stderr=True,
                                 draw_color=(255, 255, 0),
                                 thickness=2,
                                 thresh=3,
                                 maxval=255,
                                 save_folder='c:\\testrecognition'
                                 )

            print(df)

            #   aa_start_x aa_start_y aa_end_x aa_end_y aa_center_x aa_center_y aa_width aa_height aa_area                    aa_screenshot  aa_img_index
            # 0       <NA>       <NA>     <NA>     <NA>        <NA>        <NA>     <NA>      <NA>    <NA>  [[[253 249 247]\n  [253 249 247             0
            # 1         60        780      200      900         130         840      140       120   16800  [[[253 249 247]\n  [253 249 247             1
            # 2        620        740      750      870         685         805      130       130   16900  [[[253 249 247]\n  [253 249 247             1
            # 3         70        640      200      770         135         705      130       130   16900  [[[253 249 247]\n  [253 249 247             1
            # 4       1060        370     1600      710        1330         540      540       340  183600  [[[253 249 247]\n  [253 249 247             1
            # 5         10          0      250       90         130          45      240        90   21600  [[[253 249 247]\n  [253 249 247             1
            # 6        580        640      620      750         600         695       40       110    4400  [[[  0 255 255]\n  [  0 255 255             2
            # 7          0        300     1600      900         800         600     1600       600  960000  [[[  0 255 255]\n  [  0 255 255             2
            # 8        900          0     1040       80         970          40      140        80   11200  [[[  0 255 255]\n  [  0 255 255             2
            # 9          0          0      810       90         405          45      810        90   72900  [[[  0 255 255]\n  [  0 255 255             2

    """
    singlepicoriginal = open_image_in_cv(singlepicture, channels_in_output=3)
    singlepic = open_image_in_cv(singlepicoriginal, channels_in_output=2)

    picsonv = cv2.easy_resize_image(
        singlepic,
        width=None,
        height=None,
        percent=percentage,
        interpolation=interpolation,
    )
    height, width, *_ = picsonv.shape
    pics2 = [{'img': open_image_in_cv(x, channels_in_output=2), 'width': width, 'height': height, 'percent': None,
              'interpolation': interpolation} for x in picturelist]
    pics2conv = resize_image(pics2, processes=cpus, chunks=chunks, print_stderr=print_stderr, print_stdout=print_stdout)

    if save_folder:
        os.makedirs(save_folder, exist_ok=True)
    f = [
        MultiProcExecution(
            fu=get_difference_of_2_pics,
            args=(
                picsonv,
                pic,
                percentage, singlepicoriginal, draw_output,
                draw_color, thickness, thresh, maxval

            ),
            kwargstuple=(),
        )
        for keypic, pic in pics2conv.items()
    ]

    formatteddata, raw_data = start_multiprocessing(
        it=f,
        usecache=usecache,
        processes=cpus,
        chunks=chunks,
        print_stdout=print_stdout,
        print_stderr=print_stderr,
    )
    del raw_data
    if save_folder:
        for k, v in formatteddata.items():
            cv2.imwrite(os.path.normpath(os.path.join(save_folder, str(k) + '.png')), v[-1])
    df = pd.DataFrame(formatteddata).T.explode(0)
    df['img_index'] = df.index.__array__().copy()
    df.rename(columns={1: 'screenshot'}, inplace=True)
    df.reset_index(drop=True, inplace=True)
    nandata = ['start_x',
               'start_y',
               'end_x',
               'end_y',
               'center_x',
               'center_y',
               'width',
               'height',
               'area']
    nandataseries = pd.Series([pd.NA for x in nandata], index=nandata)
    dfdata = df[0].ds_apply_ignore(nandataseries, lambda x: pd.Series(x) if not pd.isna(x) else nandataseries)
    df.drop(columns=0, inplace=True)
    df = pd.concat([dfdata, df], axis=1)
    df.columns = [f'aa_{x}' for x in df.columns]
    return df


