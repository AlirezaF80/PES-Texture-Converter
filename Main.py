import wx
import TextureConverter

# global variables
WINDOW_TITLE = 'PES Texture Converter by AlirezaF'
WINDOW_SIZE = (300, 300)


class FileDrop(wx.FileDropTarget):
    def __init__(self, frame):
        wx.FileDropTarget.__init__(self)
        self.window = frame

    def OnDropFiles(self, x, y, file_paths):
        TextureConverter.convert_textures(file_paths)
        return True

    pass


class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super(MyFrame, self).__init__(parent, title=title, size=size,
                                      style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        gridSizer = wx.GridSizer(1, 1, 5, 5)

        label = wx.StaticText(self, label='Drop your texture(s) here\n(.ftex or .dds)\n\nMade by AlirezaF',
                              style=wx.ALIGN_CENTER)
        font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        label.SetFont(font)

        gridSizer.Add(label, 0, wx.ALIGN_CENTER)

        self.SetSizer(gridSizer)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title=WINDOW_TITLE, size=WINDOW_SIZE)
        fileDrop = FileDrop(self.frame)
        self.frame.SetDropTarget(fileDrop)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
