from .libs import WinForms


def info(window, title, message):
    WinForms.MessageBox.Show(message, title)


def question(window, title, message):
    result = WinForms.MessageBox.Show(message, title, WinForms.MessageBoxButtons.YesNo)
    return result == WinForms.DialogResult.Yes


def confirm(window, title, message):
    result = WinForms.MessageBox.Show(message, title, WinForms.MessageBoxButtons.OKCancel)
    return result == WinForms.DialogResult.OK


def error(window, title, message):
    WinForms.MessageBox.Show(message, title, WinForms.MessageBoxButtons.OK, WinForms.MessageBoxIcon.Error)


def stack_trace(window, title, message, content, retry=False):
    raise NotImplementedError()


def save_file(window, title, suggested_filename, file_types):
    saveFileDialog1 = WinForms.OpenFileDialog()


    saveFileDialog1.Title = title
    saveFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*"
    saveFileDialog1.FilterIndex = 1
    saveFileDialog1.RestoreDirectory = True
    saveFileDialog1.ShowHelp = True

    if (saveFileDialog1.ShowDialog() == WinForms.DialogResult.OK):
        return ""

