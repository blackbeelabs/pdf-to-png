import os
from os import path

import fitz  # pip install PyMuPDF


def _get_project_dir_folder():
    return path.dirname(path.dirname(__file__))


def main():
    print("Start: main()")

    extraction_zoom = 2
    ASSETS_FP = path.join(_get_project_dir_folder(), "assets")

    downloaded_folder_path = path.join(ASSETS_FP, "downloaded_pdfs")
    preprocessed_folder_path = path.join(ASSETS_FP, "preprocessed_pngs")
    pdfs = os.listdir(downloaded_folder_path)
    for pdf in pdfs:
        files = [
            f
            for f in os.listdir(path.join(downloaded_folder_path, y))
            if ("paper 2" in f.lower() and f.endswith("pdf"))
        ]

        for i in files:
            filepath = path.join(downloaded_folder_path, y, i)
            print(f"INPUT: {filepath}")
            doc = fitz.open(filepath)
            j = 0
            mat = fitz.Matrix(extraction_zoom, extraction_zoom)
            for page in doc:  # Total number of pages
                outfilepath = path.join(
                    preprocessed_folder_path,
                    f"{y}-{i[:-4]}-pg{j}.png",
                )
                print(f"OUTPUT: {outfilepath}")
                pix = page.get_pixmap(matrix=mat)
                pix.save(outfilepath)
                j += 1
            print()

    print("Done: main()")


if __name__ == "__main__":

    main()
