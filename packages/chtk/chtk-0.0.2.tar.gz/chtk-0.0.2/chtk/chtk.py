from librosa import load, resample, power_to_db
from librosa.feature import melspectrogram
import numpy as np
import pickle
from pathlib import Path
from .chart import chart_to_array

# Import constants
with open(Path.cwd() / 'resources' / 'SIMPLIFIED_NOTE_DICT.pkl', 'rb') as f:
    SIMPLIFIED_NOTE_DICT = pickle.load(f)

# ---------------------------------------------------------------------------- #
#                                 PREPROCESSING                                #
# ---------------------------------------------------------------------------- #

def load_song(song_dir):
    '''Loads audio, sr, and notes array from song_dir, returns audio and notes 
    array sliced into 4 second chunks

    Args:
        song_dir (Path): Path to song directory containing both notes.chart and 
        other.wav
    
    Returns:
        notes_arrays (2D numpy array): Matrix of numpy arrays where each row is 
            a 4 second notes array
        audio_segments (2D numpy array): Matrix of raw audio arrays where each 
            row is 4 seconds of audio
        sr (int): sample rate
    '''
    # Get simplified notes array and audio
    notes_array = chart_to_array(song_dir / 'notes.chart')
    notes_array = __remove_modifiers(__remove_release_keys(notes_array))
    audio, sr = load(str(song_dir / 'other.wav'))
 
    return notes_array, audio, sr

def compute_mel_spectrogram(song_path):
    '''
    Computes the log-mel spectrogram of a .ogg file

    Args:
        song_path (str | Path): path to .ogg file
    
    Returns:
        spec (2D numpy array): log-mel spectrogram
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

def simplify_notes_array(notes_array):
    '''
    Removes all modifiers and released notes from a notes array.

    Args:
        notes_array (1D numpy array): notes array with modifiers and released
            notes one hot encoded

    Returns:
        simplified_notes_array (1D numpy array): notes array with released notes
            removed and modifiers changed from held or tapped to regular.
    '''
    return __remove_modifiers(__remove_release_keys(notes_array))
# ---------------------------------------------------------------------------- #
#                               HELPER FUNCTIONS                               #
# ---------------------------------------------------------------------------- #

def __remove_release_keys(notes_array):
    '''
    Removes all notes corresponding to releases from notes_array
   
    Args:
        notes_array (1D numpy array): notes array including release keys
   
    Returns:
        1D numpy array: new notes array with release keys removed (converted to zeros)
    '''
    new_notes = np.zeros(notes_array.size)
    changed_notes = []
    for x in range(notes_array.size):
        if notes_array[x] not in list(range(187,218)):
            new_notes[x] = notes_array[x]
        else:
            changed_notes.append(x)
    return new_notes

def __remove_modifiers(notes_array):
    '''
    Maps modified and held notes to their regular counterparts

    Args:
        notes_array (1D numpy array): any notes array
    '''
    new_notes = np.zeros(notes_array.size)
    for x in range(notes_array.size):
        if notes_array[x]:
            new_notes[x] = SIMPLIFIED_NOTE_DICT[notes_array[x]]
    return new_notes
