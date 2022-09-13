# Code for Stroop task randomization
# Blocked randomization with two instructions

import pandas
import numpy


# constants

## number of blocks
nBlocks = 10

## number of trials per block
nBlockTrials = 80


# make the design based on the core trial characteristics

## declare all levels of the factor
ColorOptions = numpy.array(["red","blue","green","yellow"])

## determine the number of levels for the factor
Ncolors = len(ColorOptions)
Nunique = Ncolors * Ncolors

## determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

## make the 4-by-4 factorial design
ColorWord = numpy.floor(UniqueTrials / Ncolors)
FontColor = numpy.floor(UniqueTrials / 1) %  Ncolors

## combine arrays in trial matrix
Design = numpy.column_stack([ColorWord, FontColor])


# make the design for one block

## number of design repetitions per block
nReps = int(nBlockTrials/Nunique)

## repeat the 4-by-4 design five times
blockTrials = numpy.tile(Design, (nReps, 1))


# make the trial stucture for the entire experiment

## number of trials in the experiment
ntrials = nBlocks * nBlockTrials

## make empty trial matrix
trials = numpy.ones((ntrials,5)) * numpy.nan


# fill in the random trial order per block

## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## randomize the trial order
    numpy.random.shuffle(blockTrials)
    
    ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    
    ## store the trials for this block in the experiment array
    trials[currentTrials, 0:2] = blockTrials
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 2] = blocki+1
    
    ## store the instructions
    trials[currentTrials, 3] = (blocki+1)%2
    
    ## store the correct response
    if (blocki+1)%2 == 0:
        trials[currentTrials, 4] = trials[currentTrials, 0]     ## correct answer determined by color word
    else:
        trials[currentTrials, 4] = trials[currentTrials, 1]     ## correct answer determined by font color


# Validation and export

## creating pandas dataframe from numpy array
trials = pandas.DataFrame.from_records(trials)

## name the columns
trials.columns = ["ColorWord", "FontColor", "Block", "Instruction", "CorAns"]

## cross table validation
print("Block randomization")
print(pandas.crosstab(trials.ColorWord, [trials.FontColor, trials.Block]))
print("Block instructions")
print(pandas.crosstab(trials.Instruction, trials.Block))
print("Correct answers")
print(pandas.crosstab(trials.CorAns, [trials.Instruction, trials.FontColor]))
print(pandas.crosstab(trials.CorAns, [trials.Instruction, trials.ColorWord]))

## export
trials.to_csv(path_or_buf = "CE8_2_output_arrays.csv", index = False)
