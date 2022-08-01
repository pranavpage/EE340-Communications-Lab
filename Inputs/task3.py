#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Equalizer
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
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class task3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Equalizer")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Equalizer")
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

        self.settings = Qt.QSettings("GNU Radio", "task3")

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
        self.samp_rate = samp_rate = 48000
        self.band5 = band5 = 1
        self.band4 = band4 = 1
        self.band3 = band3 = 1
        self.band2 = band2 = 1
        self.band1 = band1 = 1

        ##################################################
        # Blocks
        ##################################################
        self._band5_range = Range(0, 10, 1, 1, 200)
        self._band5_win = RangeWidget(self._band5_range, self.set_band5, 'band5', "counter_slider", float)
        self.top_layout.addWidget(self._band5_win)
        self._band4_range = Range(0, 10, 1, 1, 200)
        self._band4_win = RangeWidget(self._band4_range, self.set_band4, 'band4', "counter_slider", float)
        self.top_layout.addWidget(self._band4_win)
        self._band3_range = Range(0, 10, 1, 1, 200)
        self._band3_win = RangeWidget(self._band3_range, self.set_band3, 'band3', "counter_slider", float)
        self.top_layout.addWidget(self._band3_win)
        self._band2_range = Range(0, 10, 1, 1, 200)
        self._band2_win = RangeWidget(self._band2_range, self.set_band2, 'band2', "counter_slider", float)
        self.top_layout.addWidget(self._band2_win)
        self._band1_range = Range(0, 10, 1, 1, 200)
        self._band1_win = RangeWidget(self._band1_range, self.set_band1, 'band1', "counter_slider", float)
        self.top_layout.addWidget(self._band1_win)
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
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/media/pranav/page/Laptop data/Coursework/Semester 9/EE340/Inputs/Bach.wav', True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_0_0_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                band5,
                samp_rate,
                9000,
                15000,
                10,
                firdes.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_0_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                band4,
                samp_rate,
                6000,
                9000,
                10,
                firdes.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                band3,
                samp_rate,
                3000,
                6000,
                10,
                firdes.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                band2,
                samp_rate,
                500,
                3000,
                10,
                firdes.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                band1,
                samp_rate,
                20,
                500,
                10,
                firdes.WIN_RECTANGULAR,
                6.76))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_0_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.band_pass_filter_0_0_0_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.band1, self.samp_rate, 20, 500, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.band2, self.samp_rate, 500, 3000, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(self.band3, self.samp_rate, 3000, 6000, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(self.band4, self.samp_rate, 6000, 9000, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_0_0_0_0.set_taps(firdes.band_pass(self.band5, self.samp_rate, 9000, 15000, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_band5(self):
        return self.band5

    def set_band5(self, band5):
        self.band5 = band5
        self.band_pass_filter_0_0_0_0_0.set_taps(firdes.band_pass(self.band5, self.samp_rate, 9000, 15000, 10, firdes.WIN_RECTANGULAR, 6.76))

    def get_band4(self):
        return self.band4

    def set_band4(self, band4):
        self.band4 = band4
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(self.band4, self.samp_rate, 6000, 9000, 10, firdes.WIN_RECTANGULAR, 6.76))

    def get_band3(self):
        return self.band3

    def set_band3(self, band3):
        self.band3 = band3
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(self.band3, self.samp_rate, 3000, 6000, 10, firdes.WIN_RECTANGULAR, 6.76))

    def get_band2(self):
        return self.band2

    def set_band2(self, band2):
        self.band2 = band2
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.band2, self.samp_rate, 500, 3000, 10, firdes.WIN_RECTANGULAR, 6.76))

    def get_band1(self):
        return self.band1

    def set_band1(self, band1):
        self.band1 = band1
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.band1, self.samp_rate, 20, 500, 10, firdes.WIN_RECTANGULAR, 6.76))





def main(top_block_cls=task3, options=None):

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
