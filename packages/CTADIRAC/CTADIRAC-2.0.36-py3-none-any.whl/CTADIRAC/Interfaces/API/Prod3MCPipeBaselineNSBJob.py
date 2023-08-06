"""
  Wrapper on the Job class to handle Prod3 MC
  piping corsika into 3 simtels
  created for Prod3 NSB tests with reference base line
  for both Paranal
			JB,LA September 2017
"""

__RCSID__ = "$Id$"

# generic imports
import json
import collections
# DIRAC imports
import DIRAC
# Base class
from CTADIRAC.Interfaces.API.Prod3MCPipeBaselineJob import Prod3MCPipeBaselineJob


class Prod3MCPipeBaselineNSBJob(Prod3MCPipeBaselineJob):
  """ Job extension class for Prod3 MC NSB simulations,
      takes care of running corsika piped into simtel
      3 output files are created
      Most code is inherited from the Prod3MCPipeBaselineJob class
  """

  def __init__(self, cpuTime=259200):
    """ Constructor takes almosst everything from base class

    Keyword arguments:
    cpuTime -- max cpu time allowed for the job
    """
#    super(Prod3MCPipeBaselineJob, self).__init__()
    Prod3MCPipeBaselineJob.__init__(self, cpuTime)
#    self.inputpath = 'Data/sim_telarray/cta-prod3-demo/0.0deg'
    self.N_output_files = 3

  def setupWorkflow(self, debug=False):
    """ Override the base class job workflow to adapt to NSB test simulations
        All parameters shall have been defined before that method is called.
    """
    # step 1 - debug only
    iStep = 1
    if debug:
      lsStep = self.setExecutable('/bin/ls -alhtr', logFile='LS_Init_Log.txt')
      lsStep['Value']['name'] = 'Step%i_LS_Init' % iStep
      lsStep['Value']['descr_short'] = 'list files in working directory'
      iStep += 1

    # step 2
    swStep = self.setExecutable('cta-prod3-setupsw',
                                arguments='%s %s' % (self.package, self.version),
                                logFile='SetupSoftware_Log.txt')
    swStep['Value']['name'] = 'Step%i_SetupSoftware' % iStep
    swStep['Value']['descr_short'] = 'Setup software'
    iStep += 1

    # step 3
    if self.cta_site == 'Paranal':
      prod_script = './dirac_prod3_paranal_baseline'
    elif self.cta_site == 'LaPalma':
      prod_script = './dirac_prod3_lapalma_baseline'
    else:
      DIRAC.gLogger.error('Unknown site: %s' % self.cta_site)
      DIRAC.gLogger.error('No shell script associated')
      DIRAC.exit(-1)

    csStep = self.setExecutable(prod_script,
                                arguments='--start_run %s --run %s %s %s %s %s' %
                                (self.start_run_number, self.run_number,
                                 self.cta_site,
                                 self.particle, self.pointing_dir, self.zenith_angle),
                                logFile='CorsikaSimtel_Log.txt')
    csStep['Value']['name'] = 'Step%i_CorsikaSimtel' % iStep
    csStep['Value']['descr_short'] = 'Run Corsika piped into simtel'
    iStep += 1

    # step 4 verify merged data
    mgvStep = self.setExecutable('ta-prod-verifysteps',
                                 arguments="generic %0d 1000 '%s/Data/*.simtel.gz'" %
                                 (self.N_output_files, self.inputpath),
                                 logFile='Verify_Simtel_Log.txt')
    mgvStep['Value']['name'] = 'Step%i_VerifySimtel' % iStep
    mgvStep['Value']['descr_short'] = 'Verify simtel files'
    iStep += 1

    # step 5 - debug only
    if debug:
      lsStep = self.setExecutable('/bin/ls -alhtr Data/sim_telarray/*/*/*', logFile='LS_End_Log.txt')
      lsStep['Value']['name'] = 'Step%i_LS_End' % iStep
      lsStep['Value']['descr_short'] = 'list files in working directory and sub-directory'
      iStep += 1

    # step 6
    # meta data
    # ## the order of the metadata dictionary is important, since it's used to build the directory structure
    metadata = collections.OrderedDict()
    metadata['array_layout'] = self.array_layout
    metadata['site'] = self.cta_site
    metadata['particle'] = self.particle
    if self.pointing_dir == 'North':
      metadata['phiP'] = 180
    if self.pointing_dir == 'South':
      metadata['phiP'] = 0
    metadata['thetaP'] = float(self.zenith_angle)
    metadata[self.program_category + '_prog'] = 'simtel'
    metadata[self.program_category + '_prog_version'] = self.version
    metadata['data_level'] = self.output_data_level
    metadata['configuration_id'] = self.configuration_id
    mdjson = json.dumps(metadata)

    # meta data field
    metadatafield = {'array_layout': 'VARCHAR(128)', 'site': 'VARCHAR(128)',
                     'particle': 'VARCHAR(128)', 'phiP': 'float',
                     'thetaP': 'float',
                     self.program_category + '_prog': 'VARCHAR(128)',
                     self.program_category + '_prog_version': 'VARCHAR(128)',
                     'data_level': 'int', 'configuration_id': 'int'}
    mdfieldjson = json.dumps(metadatafield)

    # register Data NSB 1x
    # file meta data
    filemetadata = {'runNumber': self.run_number, 'nsb': 1}
    file_md_json = json.dumps(filemetadata)
    outputpattern = './Data/sim_telarray/*/*/Data/*baseline.simtel.gz'
    if self.particle == 'gamma-diffuse':
      outputpattern = './Data/sim_telarray/*/*/Data/*baseline_cone10.simtel.gz'
    dmStep = self.setExecutable('cta-analysis-managedata',
                                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s'" %
                                (mdjson, mdfieldjson, file_md_json, self.basepath,
                                 outputpattern, self.package, self.program_category, self.catalogs),
                                logFile='DataManagement_NSB1x_Log.txt')
    dmStep['Value']['name'] = 'Step%i_DataManagement_1' % iStep
    dmStep['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
    iStep += 1
    # log file
    outputpattern = './Data/sim_telarray/*/*/Log/*baseline.log.gz'
    if self.particle == 'gamma-diffuse':
      outputpattern = './Data/sim_telarray/*/*/Log/*baseline_cone10.log.gz'
    dmStep = self.setExecutable('cta-analysis-managedata',
                                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
                                (mdjson, mdfieldjson, file_md_json, self.basepath,
                                 outputpattern, self.package, self.program_category, self.catalogs),
                                logFile='Log_DataManagement_NSB1x_Log.txt')
    dmStep['Value']['name'] = 'Step%i_Log_DataManagement' % iStep
    dmStep['Value']['descr_short'] = 'Save log files to SE and register them in DFC'
    iStep += 1
    # histogram
    outputpattern = './Data/sim_telarray/*/*/Histograms/*baseline.hdata.gz'
    if self.particle == 'gamma-diffuse':
      outputpattern = './Data/sim_telarray/*/*/Histograms/*baseline_cone10.hdata.gz'
    dmStep = self.setExecutable('cta-analysis-managedata',
                                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Histograms" %
                                (mdjson, mdfieldjson, file_md_json, self.basepath,
                                 outputpattern, self.package, self.program_category, self.catalogs),
                                logFile='Histo_DataManagement_NSB1x_Log.txt')
    dmStep['Value']['name'] = 'Step%i_Histo_DataManagement' % iStep
    dmStep['Value']['descr_short'] = 'Save hitograms files to SE and register them in DFC'
    iStep += 1

    # register Data NSB 5x
    # file meta data
    filemetadata = {'runNumber': self.run_number, 'nsb': 5}
    file_md_json = json.dumps(filemetadata)
    outputpattern = './Data/sim_telarray/*/*/Data/*baseline-5x*.simtel.gz'
    dmStep = self.setExecutable('cta-analysis-managedata',
                                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s'" %
                                (mdjson, mdfieldjson, file_md_json, self.basepath,
                                 outputpattern, self.package, self.program_category, self.catalogs),
                                logFile='DataManagement_NSB5x_Log.txt')
    dmStep['Value']['name'] = 'Step%i_DataManagement_1' % iStep
    dmStep['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
    iStep += 1
    # log file
    outputpattern = './Data/sim_telarray/*/*/Log/*baseline-5x*.log.gz'
    dmStep = self.setExecutable('cta-analysis-managedata',
                                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
                                (mdjson, mdfieldjson, file_md_json, self.basepath,
                                 outputpattern, self.package, self.program_category, self.catalogs),
                                logFile='Log_DataManagement_NSB5x_Log.txt')
    dmStep['Value']['name'] = 'Step%i_Log_DataManagement' % iStep
    dmStep['Value']['descr_short'] = 'Save log files to SE and register them in DFC'
    iStep += 1
    # histogram
    outputpattern = './Data/sim_telarray/*/*/Histograms/*baseline-5x*.hdata.gz'
    dmStep = self.setExecutable('cta-analysis-managedata',
                                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Histograms" %
                                (mdjson, mdfieldjson, file_md_json, self.basepath,
                                 outputpattern, self.package, self.program_category, self.catalogs),
                                logFile='Histo_DataManagement_NSB5x_Log.txt')
    dmStep['Value']['name'] = 'Step%i_Histo_DataManagement' % iStep
    dmStep['Value']['descr_short'] = 'Save histogram files to SE and register \
                                      them in DFC'
    iStep += 1

    # register Data NSB 30x for Paranal only
    if self.cta_site == 'Paranal':
      # file meta data
      filemetadata = {'runNumber': self.run_number, 'nsb': 30}
      file_md_json = json.dumps(filemetadata)
      outputpattern = './Data/sim_telarray/*/*/Data/*baseline-30x*.simtel.gz'
      dmStep = self.setExecutable('cta-analysis-managedata',
                                  arguments="'%s' '%s' '%s' %s '%s' %s %s '%s'" %
                                  (mdjson, mdfieldjson, file_md_json, self.basepath,
                                   outputpattern, self.package, self.program_category, self.catalogs),
                                  logFile='DataManagement_NSB30x_Log.txt')
      dmStep['Value']['name'] = 'Step%i_DataManagement_1' % iStep
      dmStep['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
      iStep += 1
      # log file
      outputpattern = './Data/sim_telarray/*/*/Log/*baseline-30x*.log.gz'
      dmStep = self.setExecutable('cta-analysis-managedata',
                                  arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
                                  (mdjson, mdfieldjson, file_md_json, self.basepath,
                                   outputpattern, self.package, self.program_category, self.catalogs),
                                  logFile='Log_DataManagement_NSB30x_Log.txt')
      dmStep['Value']['name'] = 'Step%i_Log_DataManagement' % iStep
      dmStep['Value']['descr_short'] = 'Save log files to SE and register them in DFC'
      iStep += 1
      # histogram
      outputpattern = './Data/sim_telarray/*/*/Histograms/*baseline-30x*.hdata.gz'
      dmStep = self.setExecutable('cta-analysis-managedata',
                                  arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Histograms" %
                                  (mdjson, mdfieldjson, file_md_json, self.basepath,
                                   outputpattern, self.package, self.program_category, self.catalogs),
                                  logFile='Histo_DataManagement_NSB30x_Log.txt')
      dmStep['Value']['name'] = 'Step%i_Histo_DataManagement' % iStep
      dmStep['Value']['descr_short'] = 'Save histograms files to SE and\
                                          register them in DFC'
      iStep += 1

    # Number of showers is passed via an environment variable
    self.setExecutionEnv({'NSHOW': '%s' % self.nShower})
