#!/usr/bin/env python
""" Simple data management script for Analysis PROD3 MC
    create DFC MetaData structure
    put and register files in DFC
"""

__RCSID__ = "$Id$"

# generic imports
import os
import glob
import json

# DIRAC imports
import DIRAC
from DIRAC.Core.Base import Script
Script.parseCommandLine()

# Specific DIRAC imports
from CTADIRAC.Core.Workflow.Modules.ProdDataManager import ProdDataManager


def getRunNumber(filename, package):
    if filename[-9:] == '.logs.tgz':
        run_number = int(filename.split('/')[-1].split('_')[-1].split('.')[0])
    elif package in ['chimp', 'mars', 'corsika_simhessarray', 'corsika_simtelarray']:
        run_number = int(filename.split('run')[1].split('___cta')[0])
    elif package == 'evndisplay':
        if filename[-8:] in ['DL1.root', 'DL2.root']:
            run_number = int(filename.split('run')[1].split('___cta')[0])
        elif filename[-10:] in ['DL1.tar.gz', 'DL2.tar.gz']:
            run_number = int(filename.split('run')[1].split('___cta')[0])
        else:
            run_number = int(filename.split('-')[0])  # old default
    elif package == 'ctapipe':
        run_number = filename.split('run')[1].split('.h5')[0]
        if '-' in run_number:
          run_number = run_number.split('-')[0]
    return str(run_number)

####################################################
def main():
    """ simple wrapper to put and register all analysis files

    Keyword arguments:
    args -- a list of arguments in order []
    """
    args = Script.getPositionalArgs()
    metadata = args[0]
    metadatafield = args[1]
    filemetadata = args[2]
    basepath = args[3]
    outputpattern = args[4]
    package = args[5]
    program_category = args[6]
    catalogs = args[7]
    catalogsjson = json.loads( catalogs )
    if len(args)==8:
      outputType='Data'
    else:
      outputType='Log'

    # # Create MD structure
    prod3dm = ProdDataManager( catalogsjson )
    res = prod3dm.createMDStructure( metadata, metadatafield, basepath, program_category)
    if res['OK']:
      path = res['Value']
    else:
      return res

    # # Upload data files
    res = prod3dm._checkemptydir( outputpattern )
    if not res['OK']:
      return res

    for localfile in glob.glob( outputpattern ):
      filename = os.path.basename( localfile )
      run_number = getRunNumber( filename, package )
      runpath = prod3dm._getRunPath( run_number )
      lfn = os.path.join( path, outputType, runpath, filename )
      res = prod3dm.putAndRegister( lfn, localfile, filemetadata, package )
      if not res['OK']:
        return res

    DIRAC.exit()

####################################################
if __name__ == '__main__':
  main()