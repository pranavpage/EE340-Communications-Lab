#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: pranav
# GNU Radio version: 3.8.3.1

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import audio
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

from gnuradio import qtgui

class task1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "task1")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.g = g = 392
        self.f = f = 349
        self.e = e = 329
        self.d = d = 293
        self.c_ = c_ = 523
        self.c = c = 262
        self.a_ = a_ = 466
        self.a = a = 440

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_f((c, c, d, c, f, e, c, c, d, c, g, f, c, c ,c_, a, f, e, d, a_, a_, a, f, g, f), True, 1, [])
        self.blocks_vco_f_0 = blocks.vco_f(samp_rate, 6.2832, 0.5)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, 8000)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_repeat_0, 0), (self.blocks_vco_f_0, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_repeat_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_g(self):
        return self.g

    def set_g(self, g):
        self.g = g
        self.blocks_vector_source_x_0_0.set_data((self.c, self.c, self.d, self.c, self.f, self.e, self.c, self.c, self.d, self.c, self.g, self.f, self.c, self.c ,self.c_, self.a, self.f, self.e, self.d, self.a_, self.a_, self.a, self.f, self.g, self.f), [])

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.blocks_vector_source_x_0_0.set_data((self.c, self.c, self.d, self.c, self.f, self.e, self.c, self.c, self.d, self.c, self.g, self.f, self.c, self.c ,self.c_, self.a, self.f, self.e, self.d, self.a_, self.a_, self.a, self.f, self.g, self.f), [])

    def get_e(self):
        return self.e

    def set_e(self, e):
        self.e = e
        self.blocks_vector_source_x_0_0.set_data((self.c, self.c, self.d, self.c, self.f, self.e, self.c, self.c, self.d, self.c, self.g, self.f, self.c, self.c ,self.c_, self.a, self.f, self.e, self.d, self.a_, self.a_, self.a, self.f, self.g, self.f), [])

    def get_d(self):
        return self.d

    def set_d(self, d):
        self.d = d
        self.blocks_vector_source_x_0_0.set_data((self.c, self.c, self.d, self.c, self.f, self.e, self.c, self.c, self.d, self.c, self.g, self.f, self.c, self.c ,self.c_, self.a, self.f, self.e, self.d, self.a_, self.a_, self.a, self.f, self.g, self.f), [])

    def get_c_(self):
        return self.c_

    def set_c_(self, c_):
        self.c_ = c_
        self.blocks_vector_source_x_0_0.set_data((self.c, self.c, self.d, self.c, self.f, self.e, self.c, self.c, self.d, self.c, self.g, self.f, self.c, self.c ,self.c_, self.a, self.f, self.e, self.d, self.a_, self.a_, self.a, self.f, self.g, self.f), [])

    def get_c(self):
        return self.c

    def set_c(self, c):
        self.c = c
        self.blocks_vector_source_x_0_0.set_data((self.c, self.c, self.d, self.c, self.f, self.e, self.c, self.c, self.d, self.c, self.g, self.f, self.c, self.c ,self.c_, self.a, self.f, self.e, self.d, self.a_, self.a_, self.a, self.f, self.g, self.f), [])

    def get_a_(self):
        return self.a_

    def set_a_(self, a_):
        self.a_ = a_
        self.blocks_vector_source_x_0_0.set_data((self.c, self.c, self.d, self.c, self.f, self.e, self.c, self.c, self.d, self.c, self.g, self.f, self.c, self.c ,self.c_, self.a, self.f, self.e, self.d, self.a_, self.a_, self.a, self.f, self.g, self.f), [])

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a
        self.blocks_vector_source_x_0_0.set_data((self.c, self.c, self.d, self.c, self.f, self.e, self.c, self.c, self.d, self.c, self.g, self.f, self.c, self.c ,self.c_, self.a, self.f, self.e, self.d, self.a_, self.a_, self.a, self.f, self.g, self.f), [])





def main(top_block_cls=task1, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
