from pywinauto.application import Application
app = Application().start("notepad.exe")
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)