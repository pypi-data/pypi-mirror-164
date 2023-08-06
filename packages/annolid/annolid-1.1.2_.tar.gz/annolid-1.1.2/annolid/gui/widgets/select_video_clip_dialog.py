import os
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        video_widget = QtMultimediaWidgets.QVideoWidget()
        self.setCentralWidget(video_widget)
        self.player = QtMultimedia.QMediaPlayer(
            self, QtMultimedia.QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(video_widget)
        # period of time that the change of position is notified
        self.player.setNotifyInterval(1)
        self.player.positionChanged.connect(self.on_positionChanged)

    def setInterval(self, path, start, end):
        """
            path: path of video
            start: time in ms from where the playback starts
            end: time in ms where playback ends
        """
        self.player.stop()
        self.player.setMedia(QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(path)))
        self.player.setPosition(start)
        self._end = end
        self.player.play()

    @QtCore.pyqtSlot('qint64')
    def on_positionChanged(self, position):
        if self.player.state() == QtMultimedia.QMediaPlayer.PlayingState:
            if position > self._end:
                self.player.stop()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    video_file = "/Users/chenyang/Downloads/HighF-07.mov"
    w.setInterval(video_file, 30*1000, 33*1000)
    w.show()
    sys.exit(app.exec_())
