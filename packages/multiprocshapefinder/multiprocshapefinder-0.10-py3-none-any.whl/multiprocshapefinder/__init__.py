from multiprocca import start_multiprocessing
from multiprocca.proclauncher import MultiProcExecution
import pandas as pd
from .multishapemain import find_canny_shapes, draw_results


def find_all_shapes(images, threshold1=10, threshold2=90, approxPolyDPvar=0.01, cpus=5,
                    chunks=1, print_stderr=True, print_stdout=False,usecache=True):
    f = [
        MultiProcExecution(
            fu=find_canny_shapes,
            args=(
                pic,
                threshold1,
                threshold2,
                approxPolyDPvar,

            ),
            kwargstuple=(),
        )
        for pic in images
    ]


    formatteddata, raw_data = start_multiprocessing(
        it=f,
        usecache=usecache,
        processes=cpus,
        chunks=chunks,
        print_stdout=print_stdout,
        print_stderr=print_stderr,
    )

    return pd.concat([x[1].assign(aa_img_index=x[0]) for x in formatteddata.items()], ignore_index=True)

