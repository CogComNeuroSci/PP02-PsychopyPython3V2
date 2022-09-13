# Code for Stroop task randomization
# Blocked randomization

from psychopy import data


# constants

## number of blocks
nBlocks = 10

## number of trials per block
nBlockTrials = 80

## number of design repetitions per block
nReps = int(nBlockTrials/(4*4))


# make the design based on the core trial characteristics

## make the 4-by-4 factorial design
colors = ["red","blue","green","yellow"]
Design = data.createFactorialTrialList({"ColorWord": colors, "FontColor": colors})


# make the trial stucture for the entire experiment
 
## Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = "CE8_1_output_handlers")


## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    # make the design for one block
    
    ## completely random trial order
    blockTrials = data.TrialHandler(Design, nReps = nReps, method = "fullRandom")
    
    ## add the block to the ExperimentHandler
    thisExp.addLoop(blockTrials)
    
    for trial in blockTrials:
        
        ## store the block number
        blockTrials.addData("Block", blocki+1)
        
        ## proceed to the next triall
        thisExp.nextEntry()


# Validation and export

## Note that we can't validate the design before executing it, we can only look at the output file
