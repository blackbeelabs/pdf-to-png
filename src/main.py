import os
from os import path

import fitz  # pip install PyMuPDF


def _get_project_dir_folder():
    return path.dirname(path.dirname(__file__))


def main():
    print("Start: main()")

    extraction_zoom = 2  # This can take a value between 1 and 10. Refer to https://github.com/GipsyPotter/PDFtoPNG/blob/main/mainpdf.py

    ASSETS_FP = path.join(_get_project_dir_folder(), "assets")

    downloaded_folder_path = path.join(ASSETS_FP, "downloaded_pdfs")
    preprocessed_folder_path = path.join(ASSETS_FP, "preprocessed_pngs")

    pdfs = [f for f in os.listdir(downloaded_folder_path) if f.endswith(".pdf")]
    for pdf in pdfs:
        filepath = path.join(downloaded_folder_path, pdf)
        print(f"INPUT: {filepath}")

        doc = fitz.open(filepath)
        mat = fitz.Matrix(extraction_zoom, extraction_zoom)
        j = 0
        for page in doc:  # Total number of pages
            outfilepath = path.join(
                preprocessed_folder_path,
                f"{pdf[:-4]}-pg{j}.png",
            )
            print(f"OUTPUT: {outfilepath}")
            pix = page.get_pixmap(matrix=mat)
            pix.save(outfilepath)
            j += 1
        print()

    print("Done: main()")


if __name__ == "__main__":

    main()
