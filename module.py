import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.signal import spectrogram






def params(file):
    params = file.getparams()
    signal_wave = file.readframes(params[3])
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    envelope = np.abs(scipy.signal.hilbert(signal_array))
    #設定聲音震幅閾值
    threshold = 5000
    #抓出大於閾值的部分
    mask = envelope > threshold
    #讓音頻陣列化
    frames = file.getnframes()#採樣點數
    freq = file.getframerate()#採樣率
    
    signal_array = signal_array.copy()
    signal_array[~mask] = 0#將小於閾值的部分設為0
    amplitude = np.abs(signal_array)#振福的變量
    return signal_array , freq , amplitude


def stft(signal_array, freq , nperseg , noverlap , window):
    fs, t , Zxx = spectrogram(signal_array , fs = freq, nperseg= nperseg , noverlap= noverlap , window='hann')#Zxx:頻譜密度、t:時間、fs:frames
    return Zxx