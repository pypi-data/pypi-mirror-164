""" EvnDisp Script to create a Transformation with Input Data
"""

import json
from DIRAC.Core.Base import Script
Script.setUsageMessage('\n'.join([__doc__.split('\n')[1],
                                  'Usage:',
                                  '  %s transName' % Script.scriptName,
                                  'Arguments:',
                                  '  transName: name of the transformation',
                                  '\ne.g: %s evndisp-gamma-N' % Script.scriptName,
                                  ]))

Script.parseCommandLine()

import DIRAC
from DIRAC.TransformationSystem.Client.Transformation import Transformation
from CTADIRAC.Interfaces.API.EvnDisp3MSCWRefJob import EvnDisp3MSCWRefJob
from DIRAC.Core.Workflow.Parameter import Parameter


def submitTS(job, transName, mqJson):
  """ Create a transformation executing the job workflow
  This is using a file mask so that files be added on the fly.
  """
  DIRAC.gLogger.notice('submitTS')

  # Initialize JOB_ID
  job.workflow.addParameter(Parameter("JOB_ID", "000000", "string", "", "",
                                      True, False, "Temporary fix"))

  t = Transformation()
  t.setTransformationName(transName)  # this must be unique
  t.setType("DataReprocessing")
  t.setDescription("EvnDisp3MSCW example")
  t.setLongDescription("EvnDisplay stereo reconstruction")  # mandatory
  t.setBody(job.workflow.toXML())
  t.setGroupSize(100)
  t.setFileMask(mqJson)  # catalog query is defined here
  t.addTransformation()  # transformation is created here
  t.setStatus("Active")
  t.setAgentType("Automatic")
  trans_id = t.getTransformationID()
  return trans_id


def runEvnDisp3MSCW(args=None):
  """ Simple wrapper to create a EvnDisp3RefJob and setup parameters
      from positional arguments given on the command line.

      Parameters:
      args -- infile mode
  """
  DIRAC.gLogger.notice('runEvnDisp3MSCW')
  # get arguments
  transName = args[0]

  ################################
  job = EvnDisp3MSCWRefJob(cpuTime=432000)  # to be adjusted!!

  ### Main Script ###
  # override for testing
  job.setName('EvnDisp3MSCW')
  # add for testing
  job.setType('EvnDisp3')

  # defaults
  # job.setLayout( "Baseline")
  ## package and version
  # job.setPackage( 'evndisplay' )
  # job.setVersion( 'prod3b_d20170602' )

  # change here for Paranal or La Palma
  job.setPrefix("CTA.prod3Nb")
  job.setPointing(180)  # must match table
  job.setDispSubDir('BDTdisp.Nb.3AL4-BN15.T1')
  job.setRecId('0,1,2')  # 0 = all teltescopes, 1 = LST only, 2 = MST only
  #  set calibration file and parameters file, must match pointing
  job.setTableFile('tables_CTA-prod3b-LaPalma-NNq05-NN-ID0_180deg-d20160925m4-Nb.3AL4-BN15.root')

  # set meta-data to the product of the transformation
  # set query to add files to the transformation
  MDdict = {'MCCampaign': 'PROD3', 'particle': 'gamma',
            'array_layout': 'Baseline', 'site': 'LaPalma',
            'outputType': 'Data', 'data_level': {"=": 1},
            'configuration_id': {"=": 0},
            'calibimgreco_prog': 'evndisp',
            'calibimgreco_prog_version': 'prod3b_d20170602',
            'thetaP': {"=": 20}, 'phiP': {"=": 0.0}}
  job.setEvnDispMD(MDdict)

  # add the sequence of executables
  job.setTSTaskId('@{JOB_ID}')  # dynamic
  job.setupWorkflow(debug=True)

  # output
  job.setOutputSandbox(['*Log.txt'])

  # submit the workflow to the TS
  res = submitTS(job, transName, json.dumps(MDdict))

  return res


#########################################################
if __name__ == '__main__':

  args = Script.getPositionalArgs()
  if (len(args) != 1):
    Script.showHelp()

  res = runEvnDisp3MSCW(args)
  if not res['OK']:
    DIRAC.gLogger.error(res['Message'])
    DIRAC.exit(-1)
  else:
    DIRAC.gLogger.notice('Done')
