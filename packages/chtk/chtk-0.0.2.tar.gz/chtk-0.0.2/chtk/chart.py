import numpy as np
import pickle
from pathlib import Path

# Load constants
with open(Path.cwd() / 'resources' / 'COMBO_DICT.pkl', 'rb') as f:
    COMBO_DICT = pickle.load(f)
with open(Path.cwd() / 'resources' / 'INTERMEDIATE_NOTE_MAP.pkl', 'rb') as f:
    INTERMEDIATE_NOTE_MAP = pickle.load(f)
    
def chart_to_array(path, print_release_notes=False):
    '''
    Converts a .chart file to a notes array
    
    Args:
        path (Path): Path top .chart file
    
    Returns:
        notes_array (1D numpy array): notes array
    '''
    coded_notes = __chart_to_one_hot(path, print_release_notes)

    if coded_notes == None:
        print('\nThe chart at {} is not in .chart format'.format(path))
        return None

    notes_array = np.zeros(max(coded_notes.keys()))
    for k, v in coded_notes.items():
        notes_array[k-1] = v   # This could potentially offset all notes by 10ms
    return notes_array

def __chart_to_one_hot(path, print_release_notes=False):
    '''
    Takes .chart file located at path and generates a dictionary with key value 
    pairs being (tick : note event)

    TODO: See documentation for one hot to note event key.
    
    See Tensor-Hero/Prototyping/archive/chart_to_one_hot.ipynb for more info.
    
    Args:
        path (Path): path to .chart file
        print_release_notes (bool) = if True, will output a feed of release 
            notes that had to be bumped forward due to overlap with the start of
            a new note
    
    Returns:
        coded_notes_3 (dict): Dictionary containing ticks and note events for 
            the whole .chart file at path.
            -   {tick : one hot encoded note event}
    '''
    notes, song_metadata, time_signatures, BPMs = __chart_to_dict(path)
    notes = __shift_ticks(notes, song_metadata, time_signatures, BPMs)

    if notes == None:  # If the chart file is not in .chart format
        return None

    # Create a dictionary where the keys are the tick values and the values
    # are a list of notes corresponding to the data
    coded_notes_0 = {}

    # Loop through song one note at a time, processing along the way
    for i in range(len(notes['tick'])):
        # NOTE: If star power is ever tracked, we can check it here
        # if notes['N_S'] == 'S':
        #   <do something>

        # If the key is not in the dictionary
        if notes['tick'][i] not in coded_notes_0:  
            coded_notes_0[notes['tick'][i]] = []   # Create empty list

        # If the note is not held
        if notes['duration'][i] == 0 \
            or int(notes['note'][i]) == 5 \
            or int(notes['note'][i]) == 6:              
            # Add note to list
            coded_notes_0[notes['tick'][i]].append(int(notes['note'][i]))  
        else:   # If the note is held 
            # If the key is not in the dictionary
            if (notes['tick'][i] + notes['duration'][i]) not in coded_notes_0:  
                # Create empty list
                coded_notes_0[notes['tick'][i] + notes['duration'][i]] = []     

            # Add hold modifier to note index
            # Hold modifier is the code of the note + 10 (see Prototyping file
            # mentioned in docstring)
            coded_notes_0[notes['tick'][i]].append(int(notes['note'][i]) + 10)

            # Add a release modifier to note index at release
            # Release key is the code of the note + 20 (see prototyping file 
            # mentioned in docstring)
            coded_notes_0[notes['tick'][i] + notes['duration'][i]]\
                .append(int(notes['note'][i]) + 20)    
    
        # Sometimes there are notes with conflicting force/tap flags. 
        # Allow tap flag to override force flag
        if 5 in coded_notes_0[notes['tick'][i]] \
            and 6 in coded_notes_0[notes['tick'][i]]:              
            # print('Force AND tap flag at tick {}'.format(notes['tick'][i]))
            coded_notes_0[notes['tick'][i]].remove(5)

        # Check for duplicate values, multiple notes written at the same tick
        if coded_notes_0[notes['tick'][i]] \
            != list(set(coded_notes_0[notes['tick'][i]])):  
            if len(coded_notes_0[notes['tick'][i]]) > 2:
                # print('Duplicate notes present in chart at tick {}'\
                    # .format(notes['tick'][i]))
                # print('Old notes: ', coded_notes_0[notes['tick'][i]])
                coded_notes_0[notes['tick'][i]] \
                    = list(set(coded_notes_0[notes['tick'][i]]))
                # print('New notes: ', coded_notes_0[notes['tick'][i]])

    # coded_notes_1 will hold intermediate values of coded_notes
    coded_notes_1 = {}

    for x in coded_notes_0.keys():
        if 5 in coded_notes_0[x]:    # If a force note
            # print('coded_notes_0[x]: ', coded_notes_0[x])
            coded_notes_0[x].remove(5)
            # print('coded_notes_0[x]: ', coded_notes_0[x])
            coded_notes_1[x] = __map_notes(coded_notes_0[x], 'force')
        elif 6 in coded_notes_0[x]:  # If a tap note
            coded_notes_0[x].remove(6)
            coded_notes_1[x] = __map_notes(coded_notes_0[x], 'tap')
        else:                        # If a regular note
            coded_notes_1[x] = __map_notes(coded_notes_0[x], 'regular')

    # coded_notes_2 will map the coded_notes_1 values into the syntax of the 
    # values described by all_combinations in the prototyping file
    coded_notes_2 = {}

    # Create notestring, an intermediate representation of note events. 
    # Described in prototyping file mentioned in the docstring above.
    for x in coded_notes_1.keys():
        notestring = ''
        if sorted(coded_notes_1[x]) != coded_notes_1[x]:
            coded_notes_1[x] = sorted(coded_notes_1[x])
        for note_event in coded_notes_1[x]:
            notestring += str(note_event)  
        coded_notes_2[x] = notestring

    # Holds the final {tick : one hot note event} representation of chart
    coded_notes_3 = {} 
    
    # replaced keeps track of ticks that had releases and new notes at the same
    # tick, new notes are pushed forward to the nearest unoccupied tick.
    replaced = {'x' : [],  
                'replacement_digits' : [],
                'y' : [],
                'release_digits' : []}
    
    # Convert the notestring representation to one hot representation
    # See prototyping file mentioned in docstring for more information
    for x in coded_notes_2.keys():
        try:
            # COMBO_DICT maps notestrings to one hot representations
            coded_notes_3[x] = COMBO_DICT[coded_notes_2[x]]
        except: # TODO: Specify this except statement
            # If released note and new note coincide on a tick
            if __check_for_release_notes(x, coded_notes_2):  
                y = x+1 # new tick to push coinciding note to1
                while y in coded_notes_2:  # Choose an unoccupied tick after x
                    y+=1
                
                # Parse the string and strip away release indicators
                replacement_digits = ''
                release_digits = ''
                code = ''
                for digit in coded_notes_2[x]:
                    # print('coded_notes_2[x]: ', coded_notes_2[x])
                    if not code:
                        code = digit
                        continue
                    if len(code) < 2:
                        code += digit
                    else:
                        code = digit
                        continue
                    if code in ['16', '23', '30', '37', '44']:
                        if code not in release_digits:
                            release_digits += code
                    else:
                        replacement_digits += code

                # Replace note
                replaced['x'].append(x)
                replaced['y'].append(y)
                replaced['release_digits'].append(release_digits)
                replaced['replacement_digits'].append(replacement_digits)
                if print_release_notes:            
                    print('Release Notes Coincided at tick', x, \
                          ': bumped to tick', y)
                    print('Full replaced dictionary: ', replaced)
                

    for i in range(len(replaced['x'])):
        coded_notes_2[replaced['x'][i]] = replaced['replacement_digits'][i]
        coded_notes_2[replaced['y'][i]] = replaced['release_digits'][i]
        try:
            # If the error was flagged as a new note coinciding with a release
            if replaced['replacement_digits'][i] \
                and replaced['release_digits'][i]:                  
                coded_notes_3[replaced['x'][i]] \
                    = COMBO_DICT[coded_notes_2[replaced['x'][i]]]
                coded_notes_3[replaced['y'][i]] \
                    = COMBO_DICT[coded_notes_2[replaced['y'][i]]]
            # If the error was flagged as a new note coinciding with a new note
            if replaced['replacement_digits'][i] \
                and not replaced['release_digits'][i]:  
                codes = []
                code = ''
                for digit in replaced['replacement_digits'][i]:
                    # print('replaced[\'replacement_digits\'][i]: ', \
                        # replaced['replacement_digits'][i])
                    if not code:
                        code = digit
                        continue
                    if len(code) < 2:
                        code += digit
                        codes.append(int(code))
                    else:
                        code = digit
                        continue
                code = max(codes)
                # print('max code = ', code)
                replaced['replacement_digits'][i] = str(code)
                coded_notes_2[replaced['x'][i]] \
                    = replaced['replacement_digits'][i]
                coded_notes_3[replaced['x'][i]] \
                    = COMBO_DICT[coded_notes_2[replaced['x'][i]]]
                # coded_notes_3[replaced['y'][i]] \
                    # = COMBO_DICT[coded_notes_2[replaced['y'][i]]]
        except:
            try:
                codes = []
                code = ''
                for digit in replaced['replacement_digits'][i]:
                    # print('replaced[\'replacement_digits\'][i]: ', \
                        # replaced['replacement_digits'][i])
                    if not code:
                        code = digit
                        continue
                    if len(code) < 2:
                        code += digit
                        codes.append(int(code))
                    else:
                        code = digit
                        continue
                code = max(codes)
                # print('max code = ', code)
                replaced['replacement_digits'][i] = str(code)
                coded_notes_2[replaced['x'][i]] \
                    = replaced['replacement_digits'][i]
                coded_notes_3[replaced['x'][i]] \
                    = COMBO_DICT[coded_notes_2[replaced['x'][i]]]
                # coded_notes_3[replaced['y'][i]] \
                    # = COMBO_DICT[coded_notes_2[replaced['y'][i]]]
            except:
                raise NameError('Release notes are not in combo dictionary')
    
    return coded_notes_3

    
def __chart_to_dict(path):
    '''
    Reads the raw .chart file at path and mines information into several 
    descriptive dictionaries. Data is not modified in this function, just read.

    Args:
        path (Path): path to .chart file

    Returns:
        notes (dict): Contains four arrays describing the tick, note, star power
            indicator, and duration for each note event. The arrays are:
            - tick (list of int): tick of each note
            - N_S (list of str): 'N' or 'S' where N is note and S is star power
            - note (list of int): note event where notes are described as:
                • 0-4 : Green-Orange
                • 5 : force flag
                • 6 : tap note flag
                • 7 : open note
            - duration (list of int): durations of notes measured in ticks
        song_metadata (dict): Contains the same metadata present at the
            beginning of every .chart file. All key:value pairs are (str:str)
            - Name : name of song
            - Artist : song artist
            - Charter : writer of GH chart
            - Offset : offset from beginning of audio
            - Resolution : ticks per measure
            - Genre : genre of song
            - MediaType : ??
            - MusicStream : name of audio file corresponding to chart
        time_signatures (dict): Contains two arrays describing time signature
            changes throughout the chart
            - tick (list of int): ticks where each time signature starts
            - TS (list of int): time signature
        BPMs (dict): Contains two arrays describing BPM changes throughout the
            chart
            - tick (list of int): ticks where each BPM starts
            - BPM (list of int): BPM
    '''
    # Read chart into array
    try:
        with open(path, 'r') as file:
            raw_chart = file.readlines()
        file.close()
    # This will happen when the chart is not in .chart format
    except Exception as err:  
        print(f'Exception: {err}')
        print(f'input path: {path}')
        return None, None, None, None

    # Strip lines of \n character
    for i in range(len(raw_chart)):
        raw_chart[i] = raw_chart[i].replace('\n', '')

    # Create lists to hold sections of the chart file
    song = []
    synctrack = []
    expertsingle = []

    # Parse chart file, populating lists
    i = 0
    for data in raw_chart:
        if '[Song]' in data:
            i = 1
        elif data == '[SyncTrack]':
            i = 2
        elif data in ['[Events]', '[EasySingle]', '[MediumSingle]', 
                      '[HardSingle]']:
            i = 3
        elif data == '[ExpertSingle]':
            i = 4
        
        if data in ['{', '}', '[Song]', 'ï»¿[Song]', '[SyncTrack]', 
                    '[Events]', '[ExpertSingle]']:
            continue
        if data[0] == ' ':
            if i == 1:
                song.append(data[2:])
            elif i == 2:
                synctrack.append(data[2:])
            elif i == 3:
                continue
            elif i == 4:
                expertsingle.append(data[2:])
        else:
            if i == 1:
                song.append(data[0:].strip('\t'))
            elif i == 2:
                synctrack.append(data[0:].strip('\t'))
            elif i == 3:
                continue
            elif i == 4:
                expertsingle.append(data[0:].strip('\t'))

    time_signatures = {'tick' : [],
                       'TS' : []}
    BPMs = {'tick' : [],
            'BPM' : []}

    for event in synctrack:
        line = event.split(' ')
        if line[2] == 'TS':
            time_signatures['tick'].append(int(line[0]))
            time_signatures['TS'].append(int(line[3]))
        elif line[2] == 'R':
            raise NameError('Error - Resolution changes during this song')
        else:
            try:
                BPMs['tick'].append(int(line[0]))
                BPMs['BPM'].append(int(line[3]))
            except:
                # print(line)
                # print(expertsingle)
                # print(time_signatures)
                raise NameError('Chart file may have improper indentation')

    # Parse the 'expertsingle' section of the .chart file for note information
    notes = {'tick' : [],       # What tick the note is at
            'N_S' : [],         # Whether it is a note (N) or star power (S)
            'note' : [],        # What the note is 
            'duration': []}     # tick duration of the note or star power

    for note in expertsingle:
        line = note.split(' ')
        if len(line) < 2:
            break
        if line[2] == 'E':       # skip the lines that mark events
            continue
        else:
            if "=" in line:
                notes['tick'].append(int(line[0]))
                notes['N_S'].append(line[2])
                notes['note'].append(line[3])
                notes['duration'].append(int(line[4]))
            else:
                notes['tick'].append(int(line[0]))
                notes['N_S'].append(line[1])
                notes['note'].append(line[2])
                notes['duration'].append(int(line[3]))

    # Parse the 'song' section of the .chart file to get relevent information
    song_metadata = {'Name' : '',
                     'Artist' : '',
                     'Charter' : '',
                     'Offset' : '',
                     'Resolution' : '',
                     'Genre' : '',
                     'MediaType' : '',
                     'MusicStream' : ''}
    if song:
        for data in song:
            line = data.split(' ')
            if line[0] in song_metadata.keys():
                song_metadata[line[0]] = line[-1]
        song_metadata['Offset'] = int(float(song_metadata['Offset']))
        song_metadata['Resolution'] = int(float(song_metadata['Resolution']))
    else:
        print('song metadata lost')
        print(song)
        song_metadata['Resolution'] = 192

    return notes, song_metadata, time_signatures, BPMs

def __shift_ticks(notes, song_metadata, time_signatures, BPMs):
    '''
    Helper function for __chart_to_one_hot()
    
    Converts the note representation gathered by __chart_to_dict() and converts
    the notes so they have a single time signature (4) and BPM (31.25). These
    values are chosen because they cause ticks to correspond to 10ms slots.
    
    Args:
        All args are output from __chart_to_dict(), see docstring for details
    
    Returns:
        shifted_notes (dict): same format as the notes dict (see
        __chart_to_dict() docstring) but with ticks changed to account for new 
        uniform time signature and BPM
    '''
    # Split the song into bins corresponding to time signatures and BPMs
    
    # First, assemble some lists from the preprocessing step
    # note_keys organized as (tick, 'N_S', note)
    note_keys = list(zip(notes['tick'], notes['N_S'], 
                    notes['note'], notes['duration']))
    # TS_events organized as (tick, TS)                    
    TS_events = list(zip(time_signatures['tick'], time_signatures['TS']))
    # BPM_events organized as (tick, BPM)
    BPM_events = list(zip(BPMs['tick'], BPMs['BPM']))

    # Append None at the end of these lists so the loop knows where to stop
    TS_events.append(None)
    BPM_events.append(None)

    # Loop through all the notes in the song
    TS_index = 0
    BPM_index = 0

    cur_TS = TS_events[TS_index]                # Current time signature
    cur_BPM = BPM_events[BPM_index]             # Current BPM
    next_TS = None                              # Next time signature
    next_BPM = None                             # Next BPM
    if len(TS_events) > 1:
        next_TS = TS_events[TS_index + 1]
    if len(BPM_events) > 1:
        next_BPM = BPM_events[BPM_index + 1]


    # bins['TS'][0] corresponds to the time signature of bin 0
    # bins['notes'] is a list of lists of notes in each bin
    bins = {
        'TS' : [],              # time signature
        'BPM' : [],             # BPM
        'shift_tick' : [],      # The first tick where the TS / BPM combo starts
        'notes' : [[]],         # The notes in the bin
    }

    # Append the first element of each array before looping
    event_index = 0     # Counts how many times either BPM or TS change
    bins['TS'].append(cur_TS[1])
    bins['BPM'].append(cur_BPM[1])
    bins['shift_tick'].append(cur_BPM[0])
    bins['notes'][event_index].append(note_keys[0])

    # Initialize ticks
    cur_TS_tick = cur_TS[0]
    if next_TS != None:
        next_TS_tick = next_TS[0]
    else:
        next_TS_tick = None
    cur_BPM_tick = cur_BPM[0]
    if next_BPM != None:
        next_BPM_tick = next_BPM[0]
    else:
        next_BPM_tick = None

    for i in range(1, len(note_keys)):
        if next_BPM_tick == None and next_TS_tick == None:     # If in the last bin
            bins['notes'][-1].append(note_keys[i])             # Add notes until there are no more to add
            continue
        
        if next_TS_tick != None:                        # If there is a time signature change in the future
            if note_keys[i][0] >= next_TS_tick:         # If the current note is past that change                            
                if next_BPM_tick != None:                   # If there is a BPM change in the future
                    if note_keys[i][0] >= next_BPM_tick:    # If the current note is past that change
                        TS_index += 1                       # Update time signature and BPM, they changed at the same time
                        cur_TS = TS_events[TS_index]
                        cur_TS_tick = cur_TS[0]
                        next_TS = TS_events[TS_index + 1]
                        if next_TS != None:
                            next_TS_tick = next_TS[0]
                        else:
                            next_TS_tick = None

                        BPM_index += 1
                        cur_BPM = BPM_events[BPM_index]
                        cur_BPM_tick = cur_BPM[0]
                        next_BPM = BPM_events[BPM_index + 1]
                        if next_BPM != None:
                            next_BPM_tick = next_BPM[0]
                        else:
                            next_BPM_tick = None

                        bins['TS'].append(cur_TS[1])
                        bins['BPM'].append(cur_BPM[1])
                        bins['shift_tick'].append(min(cur_TS[0], cur_BPM[0]))
                        bins['notes'].append([])
                        bins['notes'][-1].append(note_keys[i])
                        continue

                    else:                                   # If the time signature changed but the BPM didn't
                        TS_index += 1                       # Update the time signature, but not the BPM
                        cur_TS = TS_events[TS_index]
                        cur_TS_tick = cur_TS[0]
                        next_TS = TS_events[TS_index + 1]
                        if next_TS != None:
                            next_TS_tick = next_TS[0]
                        else:
                            next_TS_tick = None

                        bins['TS'].append(cur_TS[1])
                        bins['BPM'].append(cur_BPM[1])
                        bins['shift_tick'].append(min(cur_TS[0], cur_BPM[0]))
                        bins['notes'].append([])
                        bins['notes'][-1].append(note_keys[i])
                        continue

                else:                               # If the next BPM tick = None but the note tick is past the time signature
                    TS_index += 1                   # Update the time signature, but not the BPM
                    cur_TS = TS_events[TS_index]
                    cur_TS_tick = cur_TS[0]
                    next_TS = TS_events[TS_index + 1]
                    if next_TS != None:
                        next_TS_tick = next_TS[0]
                    else:
                        next_TS_tick = None       

                    bins['TS'].append(cur_TS[1])
                    bins['BPM'].append(cur_BPM[1])
                    bins['shift_tick'].append(cur_TS[0])
                    bins['notes'].append([])
                    bins['notes'][-1].append(note_keys[i])
                    continue

            else:  # If there is a time signature change in the future but the note is not past it
                if next_BPM_tick != None:                   # If there is a BPM change in the future
                    if note_keys[i][0] >= next_BPM_tick:    # If the note is past that BPM change    
                        BPM_index += 1                      # Update the BPM but not the time signature
                        cur_BPM = BPM_events[BPM_index]
                        cur_BPM_tick = cur_BPM[0]
                        next_BPM = BPM_events[BPM_index + 1]
                        if next_BPM != None:
                            next_BPM_tick = next_BPM[0]
                        else:
                            next_BPM_tick = None

                        bins['TS'].append(cur_TS[1])
                        bins['BPM'].append(cur_BPM[1])
                        bins['shift_tick'].append(cur_BPM[0])
                        bins['notes'].append([])
                        bins['notes'][-1].append(note_keys[i])
                        continue

                    else:  # If the time signature did not change and the BPM also did not change
                        bins['notes'][-1].append(note_keys[i])  # Add note and continue
                        continue

        #-------------------------------------------------------------------------------------------------------#
        # The second half of the ifzilla:
        # If there is not a time signature change in the future

        else:                        # If there is NOT a time signature change in the future                              
            if next_BPM_tick != None:                   # If there is a BPM change in the future
                if note_keys[i][0] >= next_BPM_tick:    # If the current note is past that change
                    BPM_index += 1                      # Update the BPM
                    cur_BPM = BPM_events[BPM_index]
                    cur_BPM_tick = cur_BPM[0]
                    next_BPM = BPM_events[BPM_index + 1]
                    if next_BPM != None:
                        next_BPM_tick = next_BPM[0]
                    else:
                        next_BPM_tick = None

                    bins['TS'].append(cur_TS[1])
                    bins['BPM'].append(cur_BPM[1])
                    bins['shift_tick'].append(cur_BPM[0])
                    bins['notes'].append([])
                    bins['notes'][-1].append(note_keys[i])
                    continue

                else:  # If the current note is not past the BPM change
                    bins['notes'][-1].append(note_keys[i])  # Add note and continue
                    continue

            else:                               # If the next BPM tick = None and the next TS tick = None
                                                # Then the if statement at the beginning of this thing should have fired off
                raise NameError('Error: Tick Conversion Failure')

    bins['X'] = []                # Tick conversion factor
    bins['sync_tick'] = []        # The tick value that the first note in 'notes' should have
    res = song_metadata['Resolution']
    BPM_new = int(60000 / (res*0.01))

    # Populate 'X' and 'sync_tick' field of bins
    for i in range(len(bins['shift_tick'])):
        bins['X'].append(BPM_new / bins['BPM'][i])  # 31250 = 31.25 beats/minute 

        if i == 0:
            bins['sync_tick'].append(0)
        else:
            bins['sync_tick'].append(round(bins['notes'][i][0][0] * bins['X'][i-1]))

    # Create array in bins for 'shift'
    bins['shift'] = [0]  # Don't shift the first bin

    # Convert note ticks to using conversion factor X
    for i in range(len(bins['shift_tick'])):
        for j in range(len(bins['notes'][i])):
            bins['notes'][i][j] = list(bins['notes'][i][j])  # Convert to list
            
            # Construct shift length
            if j == 0 and i != 0:
                bins['shift'].append(round((bins['shift_tick'][i] * bins['X'][i])) \
                    - (round((bins['shift_tick'][i] * bins['X'][i-1])) \
                        - bins['shift'][i-1]))

            bins['notes'][i][j][0] = round(bins['notes'][i][j][0]*bins['X'][i])  # Scale tick mark
            bins['notes'][i][j][3] = round(bins['notes'][i][j][3]*bins['X'][i])  # Scale duration
            bins['notes'][i][j][0] -= bins['shift'][i]                           # Shift

    # Convert back to dictionary format
    shifted_notes = {'tick' : [],       # What tick the note is at
                    'N_S' : [],         # Whether it is a note (N) or star power (S)
                    'note' : [],        # What the note is 
                    'duration': []}     # tick duration of the note or star power

    for T_bin in bins['notes']:
        for n in T_bin:
            shifted_notes['tick'].append(n[0])
            shifted_notes['N_S'].append(n[1])
            shifted_notes['note'].append(n[2])
            shifted_notes['duration'].append(n[3])

    return shifted_notes


def get_configuration(path):
    '''
    Gets metadata from the song.ini file within a song's directory

    Args:
        path (Path): path to song folder

    Returns:
        configuration (dict): metadata values from song.ini
    '''
    # Read chart into array
    with open(path / 'song.ini', 'r') as f:
        raw_chart = f.readlines()

    # Configuration is held in a dictionary
    configuration = {}
    # Strip lines of \n character
    for i in range(1, len(raw_chart)-1):
        raw_chart[i] = raw_chart[i].replace('\n', '')
        split_string = raw_chart[i].split('=')
        configuration[split_string[0]] = split_string[-1]

        # Turn int values into ints if possible
        try:
            int(split_string[-1])
            configuration[split_string[0]] = int(split_string[-1])
        except:
            pass

    # Turn int values into ints
    return configuration



def __map_notes(note_array, note_type):
    '''
    Helper function for __chart_to_one_hot()
    
    Takes the initial extracted note representation from __chart_to_dict() and
    creates an intermediate representation that is useful to determine the
    final notes array.

    Args:
        note_array (list of int): Array of notes for each tick as presented in
            coded_notes_0
        note_type (str): Either regular, force, or tap
    
    Returns:
        note_array(list of int): New note array with converted format suitable
            for coded_notes_1
    '''
    assert note_type in ['regular', 'force', 'tap'], \
        'note_type should be "regular", "force", or "tap"'
    
    # Behold, the great elif statement that should have been a dictionary.
    for i in range(len(note_array)):
        if note_array[i] in INTERMEDIATE_NOTE_MAP.keys():
            note_array[i] = INTERMEDIATE_NOTE_MAP[note_array[i]] 
        else:
            print(note_array)
            print('The erroneous note in note_array at index {} is {}'\
                .format(i, note_array[i]))
            raise NameError('Error: note encoded incorrectly')

        if note_type == 'force':
            note_array[i] += 1
        elif note_type == 'tap':
            note_array[i] += 2

    return note_array

def __check_for_release_notes(x, coded_notes_2):
    '''
    Checks to see if there is a released note at tick x. Utilized by 
    __chart_to_one_hot() to avoid overlap between note events at discrete ticks
    
    Args:
        x (int): tick to check
        coded_notes_2 (dict): Medial representation of ticks and note events.
            -   {tick : encoded note event}
    
    Returns:
        r_in_x (bool): True if the note at x indicates the release of a held
            note.
    '''
    r_notes = ['16', '23', '30', '37', '44']
    r_in_x = []
    for r in (r_notes):
        if r in coded_notes_2[x]:
            r_in_x.append(r)

    if not r_in_x:
        return False
    else:
        return r_in_x