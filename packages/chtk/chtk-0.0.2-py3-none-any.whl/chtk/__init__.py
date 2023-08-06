__version__ = '0.0.1'

from .chtk import compute_mel_spectrogram, \
                  load_song, \
                  simplify_notes_array 

from .chart import chart_to_array


# Defines what gets imported by `from chtk import *`
__all__ = ['compute_mel_spectrogram', 'load_song', 'simplify_notes_array',
           'chart_to_array']
                  
# from .chtk import *