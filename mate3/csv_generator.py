from pathlib import Path

import matplotlib.pyplot as plt
import camelot

PDF_PATH = "/Users/adam/Desktop/axs_app_note.pdf"
CSV_DESTINATION = Path(__file__).parent.parent / 'registry_data'

if __name__ == "__main__":
    tables = camelot.read_pdf(
        PDF_PATH,
        flavor="lattice",
        pages="all",
        compress=False,
        strip_text=" ",
        layout_kwargs={"detect_vertical": False},
        # Sometimes camelot will merge two cells together because it is
        # trying to be smart. Don't allow it because it doesn't happen
        # anywhere, and because it can happen in cells with close-together text
        split_text=True,
    )

    for old_file in CSV_DESTINATION.glob('*.csv'):
        old_file.unlink()

    tables.export(CSV_DESTINATION / 'registry-data.csv', f='csv', compress=False)
