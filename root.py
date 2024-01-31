import data
from libaries import *
import primary
import popup


#maybe add a option to redo going back, ie an command+] to pair the command+[

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #load the data
        
        #the base widget for EVERYTHING
        self.root = QGroupBox ()
        self.root.setStyleSheet ("border: 0; background-color: #1c1c1c;")

        #set up the scrollbar of primary
        self.scroll = QScrollArea()
        #set up scrollbar properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        #self.scroll.setStyleSheet ("max-width: 0px;")
        
        

        #set up the layout so that stuff on root can be stacked
        self.rootLayout = QGridLayout ()
        #self.root.setAlignment (Qt.AlignmentFlag.AlignHCenter)
        #self.rootLayout.setAlignment (Qt.AlignmentFlag.AlignHCenter)
        self.rootLayout.setContentsMargins(0,0,0,0)
        

        self.primary = primary.main ()
        #set the widget that is in the scrollbar to be the primary
        self.scroll.setWidget(self.primary)

        #connect for signal from adding subject
        self.primary.addElement.connect (self.setAddElementMode)
        self.primary.editElement.connect (self.setEditElementMode)
        self.primary.moveElement.connect (self.moveElement)
        self.primary.sizeElement.connect (self.sizeElement)
        #connect for opening an element
        self.primary.openElement.connect (self.openElement)
        self.primary.showImage.connect (self.imagePopup)
        self.primary.back.connect (self.back)

        #add the primary (scroll) to the root
        self.rootLayout.addWidget (self.scroll, 0,0)

        #set the root layout
        self.root.setLayout (self.rootLayout)

        #set the root widget as the main widget
        self.setCentralWidget(self.root)

        #set the size of the window
        self.setGeometry(0, 0, 1440, 800)

    def openElement (self, path):
        
        data.path = path
        data.updateCurrentDisplay ()
        self.displayChange()
        
        
    def openElementRelative (self, index):
        for i in index:
            data.path.append (i)
        data.updateCurrentDisplay ()
        self.displayChange()
    def back (self):
        data.path.pop ()
        #add code here for if the element is an element group or timeline
        if data.getElement (data.path).type == "group" or data.getElement (data.path).type == "timeline":
            data.path.pop ()
        data.updateCurrentDisplay ()
        self.displayChange ()

    def displayChange (self):
        self.primary.displayChange()
        self.primary.reload()
        self.refresh ()
        self.scroll.verticalScrollBar().setValue(0)
        
        
    def moveElement (self, direction, path):
        data.moveElement (direction, path)
        self.primary.reload ()
        self.refresh()
        pass
    def sizeElement (self, size, path):
        data.changeElementSize (size, path)
        self.primary.reload ()
        self.refresh()

    def setAddElementMode (self, type, path):
        if data.mode == "popup":
            return (False)
        data.mode = "popup"
        #print (type)
        match type:
            case "subject":
                self.popup = popup.subject ("add")
            case "element":
                self.popup = popup.element ("add")
            case "group":
                self.popup = popup.group ("add")
            case "image":
                self.popup = popup.image ("add")
            case "unit":
                self.popup = popup.unit ("add")
        try:
            self.popup.submit.connect (self.popup.confirm)
        except:
            pass
        self.popup.submit.connect (lambda: data.addElement (path, self.popup.getInfo()))

        self.popup.submit.connect (self.primary.reload)
        self.popup.submit.connect (self.setNormalMode)
        self.popup.submit.connect (self.refresh)

        self.popup.submitAndOpen.connect (lambda: data.addElement (path, self.popup.getInfo()))
        self.popup.submitAndOpen.connect (lambda: self.openElementRelative ([len(data.getElement (path).subelement) - 1]))
        self.popup.submitAndOpen.connect (self.setNormalMode)


        self.popup.cancel.connect (self.setNormalMode)
        
        self.rootLayout.addWidget (self.popup, 0, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.popup.focus()

    def setEditElementMode (self, type, path):
        data.mode = "editElement"
        match type:
            case "subject":
                self.popup = popup.subject ("edit")
            case "element":
                self.popup = popup.element ("edit")
            case "group":
                self.popup = popup.group ("edit")
            case "image":
                self.popup = popup.image ("edit")
            case "unit":
                self.popup = popup.unit ("edit")
                
        elementPath = data.getElement (path)
        self.popup.setText(elementPath)
        
        self.popup.submit.connect (lambda: data.editElement (path, self.popup.getInfo()))

        self.popup.submit.connect (self.primary.reload)
        self.popup.submit.connect (self.setNormalMode)
        self.popup.submit.connect (self.refresh)

        self.popup.submitAndOpen.connect (lambda: data.editElement (path, self.popup.getInfo()))
        self.popup.submitAndOpen.connect (lambda: self.openElement (path))
        self.popup.submitAndOpen.connect (self.setNormalMode)

        self.popup.cancel.connect (self.setNormalMode)
        #print (path)
        self.popup.delete.connect (lambda: data.deleteElement(path))
        self.popup.delete.connect (self.primary.reload)
        self.popup.delete.connect (self.setNormalMode)
        self.popup.delete.connect (self.refresh)

        self.rootLayout.addWidget (self.popup, 0, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.popup.focus()
    def refresh (self):
        #print (data.currentDisplay.subelement)
        self.primary.update ()
        self.root.update ()
        self.update ()
    def imagePopup (self, image):
        self.popup = popup.photoDisplay (image)

        self.popup.back.connect (self.setNormalMode)
        
        self.rootLayout.addWidget (self.popup, 0, 0, alignment=Qt.AlignmentFlag.AlignHCenter)

    def setNormalMode (self):
        data.mode = "normal"
        self.popup.hide ()
        

        

        



app = QApplication(sys.argv)
qss = data.filepath ("style.qss")

with open(qss,"r") as fh:
    app.setStyleSheet(fh.read())
window = MainWindow()
   



window.show()
app.exec()