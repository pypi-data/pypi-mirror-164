from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pickle

# viz_dict maps one hot indices to their corresponding .chart representation
with open(Path.cwd() / 'resources' / 'VIZ_DICT.pkl', 'rb') as f:
    VIZ_DICT = pickle.load(f)

note_idx_to_y = { # Note index to y position on plots
    1 : 5,
    2 : 4,
    3 : 3,
    4 : 2,
    5 : 1
}
note_idx_to_c = { # Colors of notes
    1 : 'g',
    2 : 'r',
    3 : 'y',
    4 : '#4a68ff',
    5 : '#ff9100'
}

def slice_notes(notes, start=0, end=2):
    '''
    Takes a notes array or spectrogram and slices it between start and end in 
    seconds
    
    Args:
        notes (1D numpy array or 2D numpy array): notes array or spectrogram
        start (int): start of slice relative to beginning of song in seconds
        end (int): end of slice relative to beginning of song in seconds
   
    Returns:
        notes (1D numpy array or 2D numpy array): notes array or spectrogram 
        sliced between start and end
    '''
    assert start < end, "Error: start value must be less than end value"
    start_tick, end_tick = start*100, end*100  # ticks are in 10ms bins
    if len(notes.shape) == 1:
        return notes[start_tick:end_tick]
    else:
        return notes[:, start_tick:end_tick]

def plot_chart(ground_truth=None, candidate=None, audio=None, SHOW=True):
    '''
    Plots Guitar Hero charts and spectrograms using matplotlib.
    
    Can also be used to plot spectrograms without notes, just fill in the audio 
    arg without ground_truth or candidate.

    Args:
        ground_truth (list of int): ground truth notes array
        candidate (list of int): candidate notes array
        audio (2D numpy matrix): spectrogram
        SHOW (bool): If true, will show the generated plot in place

    Returns:
        fig (matplotlib figure): contains the full generated plot
    '''
    num_subplots = int(ground_truth is not None) + int(candidate is not None) \
                   + int(audio is not None)
    assert num_subplots > 0, 'ERROR, plot_chart was called without input'
    
    fig, axes = plt.subplots(num_subplots)
    if ground_truth is not None:
        fig.set_size_inches(min(len(ground_truth)/40, 900), 2*num_subplots)
    elif candidate is not None:
        fig.set_size_inches(min(len(candidate)/40, 900), 2*num_subplots)
    ax_idx = 0

    if num_subplots == 1:
        axes = [axes]

    # ground truth plot
    if ground_truth is not None:
        __create_scatter_axes(ground_truth, axes[ax_idx])
        axes[ax_idx].set_title('Ground Truth')
        ax_idx += 1

    # candidate plot
    if candidate is not None:
        __create_scatter_axes(candidate, axes[ax_idx])
        axes[ax_idx].set_title('Candidate')
        ax_idx += 1

    if audio is not None:
        axes[ax_idx].imshow(audio, aspect='auto', origin='lower')
    
    fig.align_xlabels(axes)
    
    if SHOW:
        plt.show()

    return fig

def __create_scatter_axes(notes, ax=None):
    '''
    Helper function for plot_chart(), creates a matplotlib axis from a notes 
    array.

    Args:
        notes (list of int): notes arrays. The longer the notes array, the wider 
            the plot.
        ax (matplotlib ax): 

    Returns:
        ax (matplotlib ax): holds entire plot of the input notes array
    '''
    x = [] # x position of scatter points for each note in notes
    y = [] # y position of scatter points for each note in notes
    c = [] # color array of scatter points
    x_lines = [] # x position of open notes
    scaler = 1 # scales the note placement on the y dimension up or down

    for idx, note in enumerate(notes):  # Parse notes to populate ax
        if not note: # skip empty time bins
            continue

        chord = VIZ_DICT[note]
        for n in chord: # chords are arranged as list of int, GRY = [1, 2, 3]
            if n != 6:  # If not an open note
                x.append(idx)
                y.append(note_idx_to_y[n]*scaler)
                c.append(note_idx_to_c[n])
            else:
                x_lines.append(idx)

    # Generate coordinates for open notes
    coords = [] # maps start and end point of purple bars
    for tick in x_lines:
        coords.append(([tick, tick], [0, 6])) # -> bar b/w (x,0) and (x,6)

    # Plot GRYBO notes
    if ax is None:
        ax = plt.gca()

    # Plot and format GRYBO notes
    ax.set_ylim((0,6))
    ax.set_xlabel('Ticks', fontsize=15)
    ax.set_yticks(np.arange(0,7,1))
    ax.grid(axis= 'y', which='both')
    ax.set_axisbelow(True)
    ax.set_yticklabels([])
    ax.set_xlim(0, len(notes))
    ax.scatter(x, y, edgecolors='k', color=c, s=160)

    # Plot and format open notes
    for coord in coords:
        ax.plot(coord[0], coord[1], linewidth=3, color='#c000eb')

    return ax
