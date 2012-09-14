#! /usr/bin/python

import gtk
import gtk.glade
from gconfviewer import AbstractGConfViewer

class GConfViewerGUI(AbstractGConfViewer):

    def __init__(self, dirkey):
        AbstractGConfViewer.__init__(self, dirkey)

        gui = gtk.glade.XML('view/viewer.glade')
        self.entry = gui.get_widget('entry')
        self.textview = gui.get_widget('textview')
        self.buffer = self.textview.get_buffer()
        gui.get_widget('window').show_all()

    def getKeyName(self):
        return self.entry.get_text()

    def setResult(self, result):
        self.buffer.insert_at_cursor(result)


if __name__ == '__main__':
    GConfViewerGUI('/desktop/gnome/keybindings')
    gtk.main()

