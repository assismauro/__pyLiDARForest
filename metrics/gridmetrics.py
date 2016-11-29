import pyLASTools
import pyForestLASTools 
import argparse
import sys

def Header():
    print('Calculate gridmetrics using LASTools v0.8')
    print

def ParseCmdLine():
#   D:\CCST\Paper\transects\069\NP_T-069.LAS -step 20 -lp c:\lastools\bin -metrics "-p 5 10 25 50 75 90 -b 5 10 25 50 75 90 -min -max- avg -std -ske -kur -qav -cov -dns -c 0.5 2 4 10 20 50 -d 0.5 2 4 10 20 50" -co 0 -v 1
#   D:\CCST\Paper\transects\069\NP_T-069.LAS -o D:\CCST\Paper\transects\069\069LTmetrics.csv  -lp 'c:\lastools\bin' -co 0 -v 1  
    parser = argparse.ArgumentParser(description='Generate CHM model.')
    parser.add_argument('inputfname',help='File mask to be processed.')
    parser.add_argument('-o','--outputfname',help='Output file name.',default="")
    parser.add_argument('-df','--destinationformat',help='CSV, BIL, ASC, IMG, TIF, XYZ, FLT, or DTM format, default CSV.', default = 'CSV')
    parser.add_argument('-lp','--lastoolspath',help=r'LASTools bin path, default c:\lastools\bin', default = r'c:\lastools\bin')
    parser.add_argument('-s','--step',help='Side length of grid',type=float, default = 20)
    parser.add_argument('-m','--metrics', help = 'Metrics to be calculated.',default="")
    parser.add_argument('-opt','--options', help = 'Additional options.',default="")
    parser.add_argument('-co','--commandonly', type=int, help = 'Just show commands, withou run it.',default=0)
    parser.add_argument('-v','--verbose', type=int, help = 'Show intermediate messages.',default=0)

    try:
        return parser.parse_args()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    Header()

args=ParseCmdLine()
forestLT = pyForestLASTools.pyForestLASTools(inputfname=args.inputfname,rootdir="",\
    lastoolspath=args.lastoolspath,commandonly=args.commandonly,verbose=args.verbose)
try:
    if args.metrics == "":
        ametrics="-p 5 10 25 50 75 90 -b 5 10 25 50 75 90 -min -max -avg -std -ske -kur -qav -cov -dns -c 0.5 2 4 10 20 50 -d 0.5 2 4 10 20 50"
    else:
        ametrics=""
    forestLT.gridmetrics(outputfname=args.outputfname,extension=args.destinationformat,step=args.step,metrics=ametrics,options=args.options)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

'''
outputfname=args.outputfname,extension=args.destinationformat,step=args.step,metrics=args.metrics,otions=args.options
    if args.metrics == "":
        ametrics="-p 5 10 25 50 75 90 -b 5 10 25 50 75 90 -min -max- avg -std -ske -kur -qav -cov -dns -c 0.5 2 4 10 20 50 -d 0.5 2 4 10 20 50"
    else:
        ametrics=""
'''