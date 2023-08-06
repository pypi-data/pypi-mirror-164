#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Max Hodak
@date: 20101102
@license: GNU GPLv3 <https://gitlab.com/malfatti/SciScripts/raw/master/LICENSE>
@homepage: https://gitlab.com/Malfatti/SciScripts

Fixed, modified to increase speed using numpy, Alex Chubykin, 06 June 2012

###############################
### This is a modified copy ###
###############################

Original was once avaliable for download at http://intantech.com/downloads.html

Modified by T. Malfatti to:
    - Work in python3;
    - Load a folder with .int files;
    - Improve performance by replacing struct by numpy
"""

import sys
import numpy as np
from glob import glob


## Level 0
def ReadData(filename, verbose = False, describe_only = False):
    """
    Example:

      from sciscripts.IO.Intan import ReadData
      mydata = ReadData("spikes_101029_011129.int")

    mydata looks like:
      {
        "duration": 60,                             # seconds
        "channel_count": 17,                        # number of amps
        "analog": [((-0.2594, -0.1502, ...), ...],  # voltage data
        "aux": [((0, 1, 1, 1, 0, 0, ...), ...],     # aux data
      }

    len(mydata['analog']) is approximately mydata['duration']*25000 and
    len(mydata['analog'][i]) = mydata['channel_count'] for i < mydata['duration']*25000
    (ish, unless the fpga was dropping frames or such such).  ReadData always returns a dict
    for extensability reasons.  For example, other lines may be added later.
    If the int file is of an improper format, or something else goes wrong, an exception is thrown.
    """
    with open(filename, mode='rb') as f:
        data = f.read()
        if verbose: print('data length',len(data))

        header = data[0:3]
        version, major_version, minor_version = np.frombuffer(header, np.uint8)

        if version != 128:
            raise Exception("Improper data file format.")
        if (major_version != 1 or minor_version != 1):
            print("Datafile may not be compatible with this script.")

        sr = 25000            # Fixed on Intan RHA
        header_size = 67
        num_amps = sum([np.frombuffer(data[i+2:i+3], np.uint8)[0] for i in range(1,64)])
        t_count = int((len(data) - header_size) / (1+4*num_amps))
        t_max = t_count/sr
        BLOCK_SIZE = 4*num_amps+1

        description = {"duration": t_max, "channel_count": num_amps}

        if verbose:
            print('Data file contains %0.2f seconds of data from %d amplifier channel(s)' % (t_max, num_amps))

        if describe_only: return(description)

        data = data[header_size:] # Throw away the header.
        aux = np.frombuffer(data[BLOCK_SIZE-1::BLOCK_SIZE], np.int8)
        data = bytearray(data)
        del data[BLOCK_SIZE-1::BLOCK_SIZE]

        try:
            analog = np.frombuffer(data, np.float32).reshape((t_count, num_amps))
        except ValueError:
            analog = np.frombuffer(data[:-(len(data)%4)], np.float32)
            analog = analog[:-(analog.shape[0]%num_amps)]
            analog = analog.reshape((analog.shape[0]//num_amps, num_amps))
            minlen = min((_.shape[0] for _ in (analog,aux)))
            analog, aux = analog[:minlen,:], aux[:minlen]

    description.update({'analog': analog, 'aux': aux})
    return(description)


## Level 1
def Load(File, ChannelMap=[], Verbose=False):
    Data = ReadData(File, verbose=Verbose)

    try: len(Data['aux'][0])
    except TypeError: Data['aux'] = Data['aux'].reshape((Data['aux'].shape[0], 1))

    Data = np.hstack((Data['analog'], Data['aux']))

    if ChannelMap:
        ChannelMap = [_-1 for _ in ChannelMap]
        Data[:, (range(len(ChannelMap)))] = Data[:, ChannelMap]

    Rate = 25000

    return(Data, Rate)


## Level 2
def FolderLoad(Folder, ChannelMap=[], Verbose=False):
    Rate = 25000
    Data = {str(F): Load(File, ChannelMap, Verbose)[0]
            for F,File in enumerate(sorted(glob(Folder+'/*int')))}

    return(Data, Rate)


if __name__ == '__main__':
    a=ReadData(sys.argv[1], verbose = True, describe_only = False) # a is a dictionary with the data, a["analog"] returns the 2xD np array with the recordings
    print(a)

