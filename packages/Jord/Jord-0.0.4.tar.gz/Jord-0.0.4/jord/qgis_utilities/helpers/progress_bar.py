from qgis.PyQt import QtGui
from qgis.PyQt import QtWidgets
from typing import List, Tuple

__all__ = ["dialog_progress_bar"]


def dialog_progress_bar(
    progress: int = 0, *, minimum_width: int = 300
) -> Tuple[QtWidgets.QDialog, QtWidgets.QProgressBar]:
    """
    Create a progress bar dialog.

    :param progress: The progress to display.
    :param minimum_width: The minimum width of the dialog.
    :return: The dialog.
    """
    dialog = QtGui.QProgressDialog()
    dialog.setWindowTitle("Progress")
    dialog.setLabelText("text")
    bar = QtWidgets.QProgressBar(dialog)
    bar.setTextVisible(True)
    bar.setValue(progress)
    dialog.setBar(bar)
    dialog.setMinimumWidth(minimum_width)
    dialog.show()
    return dialog, bar


if __name__ == "__main__":

    def calc(x, y):
        from time import sleep

        dialog, bar = dialog_progress_bar(0)
        bar.setValue(0)
        bar.setMaximum(100)
        sum = 0
        for i in range(x):
            for j in range(y):
                k = i + j
                sum += k
            i += 1
            bar.setValue((float(i) / float(x)) * 100)
            sleep(0.1)
        print(sum)

    # calc(10000, 2000)
