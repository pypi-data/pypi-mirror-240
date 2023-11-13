import re
import cv2
import numexpr
from a_cv_imwrite_imread_plus import open_image_in_cv
import numpy as np
import pandas as pd
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
from flatten_everything import flatten_everything
from more_itertools import chunked
pd_add_apply_ignore_exceptions()

def detect_shape(approx, boundingrect):
    shape = ""
    if len(approx) == 3:
        shape = "triangle"

    # Square or rectangle
    elif len(approx) == 4:
        (x, y, w, h) = boundingrect
        ar = w / float(h)

        # A square will have an aspect ratio that is approximately
        # equal to one, otherwise, the shape is a rectangle
        shape = "square" if 0.95 <= ar <= 1.05 else "rectangle"

    # Pentagon
    elif len(approx) == 5:
        shape = "pentagon"

    elif len(approx) == 6:
        shape = "hexagon"

    elif len(approx) == 7:
        shape = "heptagon"
    # elif len(approx) == 8:
    #     shape = "octagon"
    # Otherwise assume as circle or oval
    else:
        (x, y, w, h) = boundingrect
        ar = w / float(h)
        shape = "circle" if 0.95 <= ar <= 1.05 else "oval"

    return shape
def get_rotated_rectangle(cnt):
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    return box

def get_enclosing_circle(cnt):
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    return center, radius
def draw_results(df,im,min_area=10,shapes=('rectangle', 'triangle','circle','pentagon','hexagon','oval'),cv2show=True):
    image = open_image_in_cv(im,channels_in_output=3).copy()
    for name, group in df.groupby("aa_h3"):
        if name == 0:
            continue
        fabb = (
            np.random.randint(50, 250),
            np.random.randint(50, 250),
            np.random.randint(50, 250),
        )
        for key, item in group.loc[(group.aa_area > min_area) & (group.aa_shape.isin([*shapes])) ].iterrows():

            image = cv2.drawContours(
                image, item.aa_convexHull, -1, color=fabb, thickness=5, lineType=cv2.LINE_AA
            )
            image = cv2.rectangle(
                image,
                (item.aa_bound_start_x, item.aa_bound_start_y),
                (item.aa_bound_end_x, item.aa_bound_end_y),
                (0, 0, 0),
                3,
            )
            image = cv2.rectangle(
                image,
                (item.aa_bound_start_x, item.aa_bound_start_y),
                (item.aa_bound_end_x, item.aa_bound_end_y),
                fabb,
                2,
            )
            image = cv2.putText(
                image,
                f'{str(item.aa_shape)} - {name}',
                (item.aa_bound_start_x, item.aa_bound_start_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                (0, 0, 0),
                2,
                cv2.LINE_AA,
            )
            image = cv2.putText(
                image,
                f'{str(item.aa_shape)} - {name}',
                (item.aa_bound_start_x, item.aa_bound_start_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                fabb,
                1,
                cv2.LINE_AA,
            )

    if cv2show:
        while True:
            cv2.imshow("CV2 WINDOW", image)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cv2.destroyAllWindows()
    return image

def find_canny_shapes(image, threshold1=10, threshold2=90,    approxPolyDPvar=0.01):

    def canny_edge_blur(image, threshold1=10, threshold2=90):
        image = open_image_in_cv(image, channels_in_output=4)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray_image, threshold1=threshold1, threshold2=threshold2)
        mask = np.zeros_like(image)
        mask[
            numexpr.evaluate("""edges != 0""", global_dict={}, local_dict={"edges": edges})
        ] = 255
        return  open_image_in_cv(mask, channels_in_output=2)

    hcom=re.compile(r"^h\d+$")
    shotiter=canny_edge_blur(image=image, threshold1=threshold1,
                    threshold2=threshold2)
    threshg=shotiter.astype(np.uint8)
    contours, hierachy = cv2.findContours(threshg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    coordsall = [
        (
            pd.DataFrame(
                tuple(tuple(y) for y in chunked(flatten_everything(x), 2))
            ).assign(cv2stuff=[[p] for p in x], **{f"h{k}": v for k, v in enumerate(h)})
        )
        for x, h in zip(contours, hierachy[0])if len(x) >= 3
        ]
    imgray2=open_image_in_cv(image, channels_in_output=3)
    alldata = []
    rows, cols = imgray2.shape[:2]
    hcols = [
        _
        for _ in coordsall[0].columns.to_list()
        if hcom.search( str(_))
    ]

    for dafr in coordsall:
        try:
            cnts = np.array([x[0] for x in dafr.cv2stuff])
            try:
                arclength = cv2.arcLength(cnts, True)
            except Exception:
                arclength = pd.NA
            cas = cv2.approxPolyDP(cnts, approxPolyDPvar * arclength, True)
            try:
                k = cv2.isContourConvex(cas)
            except Exception:
                k = pd.NA
            x = pd.NA
            y = pd.NA
            try:
                M = cv2.moments(cnts)
                if M["m00"] != 0.0:
                    x = int(M["m10"] / M["m00"])
                    y = int(M["m01"] / M["m00"])
            except Exception:
                x = pd.NA
                y = pd.NA
            try:
                area = cv2.contourArea(cas)
            except Exception:
                area = pd.NA
            try:

                boundingrect = cv2.boundingRect(cas)
            except Exception:
                boundingrect = pd.NA
            try:
                hull = cv2.convexHull(cas)
            except Exception:
                hull = pd.NA
            try:
                shap = detect_shape(approx=cas, boundingrect=boundingrect)
            except Exception:
                shap = pd.NA
            try:
                rotarect = get_rotated_rectangle(cas)
            except Exception:
                rotarect = pd.NA
            try:
                center, radius = get_enclosing_circle(cas)
            except Exception:
                center, radius = pd.NA, pd.NA
            try:
                ellipse = cv2.fitEllipse(cas)
            except Exception:
                ellipse = pd.NA
            try:
                [vx, vy, x, y] = cv2.fitLine(cas, cv2.DIST_L2, 0, 0.01, 0.01)
                lefty = int((-x * vy / vx) + y)
                righty = int(((cols - x) * vy / vx) + y)
                coordsforline = (cols - 1, righty), (0, lefty)
            except Exception:
                coordsforline = pd.NA

            alldata.append( (
                arclength,
                k,
                x,
                y,
                area,
                boundingrect,
                hull,
                len(hull),
                len(cas),
                shap,
                rotarect,
                center,
                radius,
                ellipse,
                coordsforline,
            *[dafr[mu].iloc[0] for mu in hcols]))
        except Exception as fe:
            continue
    df2 = pd.DataFrame(alldata,columns= [
        "arcLength",
        "isContourConvex",
        "center_x",
        "center_y",
        "area",
        "boundingRect",
        "convexHull",
        "len_convexHull",
        "len_cnts",
        "shape",
        "rotated_rectangle",
        "minEnclosingCircle_center",
        "minEnclosingCircle_radius",
        "fitEllipse",
        "fitLine",
    ] + hcols)
    df2.center_x = df2.center_x.ds_apply_ignore(pd.NA,lambda x: int(x[0])).astype(np.uint64)
    df2.center_y = df2.center_y.ds_apply_ignore(pd.NA,lambda x: int(x[0])).astype(np.uint64)
    boundingre = df2.boundingRect.ds_apply_ignore([pd.NA,pd.NA,pd.NA,pd.NA,pd.NA,pd.NA,pd.NA,pd.NA,],
        lambda x: ([x[0], x[1], x[0] + x[2], x[1] + x[3], x[2], x[3]])
    ).ds_apply_ignore(pd.Series([pd.NA,pd.NA,pd.NA,pd.NA,pd.NA,pd.NA,pd.NA,pd.NA,]), pd.Series).rename(
        columns={
            0: "bound_start_x",
            1: "bound_start_y",
            2: "bound_end_x",
            3: "bound_end_y",
            4: "bound_width",
            5: "bound_height",
        }
    )
    df2 = pd.concat(
        [df2[[l for l in df2.columns if l != "boundingRect"]], boundingre],
        axis=1,
    )

    df2.columns = [f"aa_{x}" for x in df2.columns]
    return df2


