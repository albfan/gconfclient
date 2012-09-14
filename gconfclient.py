import gtk
import sys
from gconfviewer import AbstractGConfViewer

class GConfViewerCLI(AbstractGConfViewer):

    def __init__(self, dirkey, keyName):
        AbstractGConfViewer.__init__(self, dirkey)
        self.keyName = keyName

    def getKeyName(self):
        return self.keyName

    def setResult(self, result):
        print result

if __name__ == '__main__':
    GConfViewerCLI(sys.argv[1], sys.argv[2])
    gtk.main()
