from librosa import load, resample, power_to_db
from librosa.feature import melspectrogram
import numpy as np

def compute_mel_spectrogram(song_path):
    '''
    Computes the log-mel spectrogram of a .ogg file

    ~~~~ INPUTS ~~~~
    -   song_path (str | Path): path to .ogg file
    
    ~~~~ OUTPUTS ~~~~
    -   spec : 2D numpy array containing log-mel spectrogram.
        -   dimensions = [frequency, time], frequency dimension is always 512
        -   each time slice represents 10 milliseconds
        -   log-scale, so max(spec) = 0, min(spec) = -80
    '''
    audio, sr = load(str(song_path))
    resampled = resample(audio, sr, 44100)
    spec = melspectrogram(resampled, 44100, n_fft=2048*2, hop_length=441, 
                          n_mels=512, power=2, fmax = sr/2)
    spec = power_to_db(spec, ref=np.max)
    return spec

