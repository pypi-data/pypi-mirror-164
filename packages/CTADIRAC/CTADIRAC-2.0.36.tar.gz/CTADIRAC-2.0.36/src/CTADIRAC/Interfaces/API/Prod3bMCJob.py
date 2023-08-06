"""
  Simple Wrapper on the Job class to handle Prod3 MC
"""

__RCSID__ = "$Id$"

# generic imports
import json
import collections
# DIRAC imports
import DIRAC
from DIRAC.Interfaces.API.Job import Job


class Prod3bMCJob(Job):
  """ Job extension class for Prod3 MC simulations,
    takes care of running corsika, 31 simtels and merging
    into 5 data files and 3 tar ball for log files.
  """

  def __init__(self, cpuTime=432000):
    """ Constructor

    Keyword arguments:
    cpuTime -- max cpu time allowed for the job
    """
    Job.__init__(self)
    self.setCPUTime(cpuTime)
    # defaults
    self.setName('Prod3MC_Generation')
    self.package = 'corsika_simhessarray'
    self.version = '2015-07-21'
    self.nShower = 5
    self.start_run_number = '0'
    self.run_number = '10'
    self.array_layout = 'full'
    self.template_tag = '6'
    self.cta_site = 'Paranal'
    self.particle = 'gamma'
    self.pointing_dir = 'South'
    self.zenith_angle = 20.
    self.no_sct = True
    self.inputpath = 'Data/sim_telarray/cta-prod3/0.0deg'
    self.basepath = '/vo.cta.in2p3.fr/MC/PROD3/scratch'
    self.catalogs = json.dumps(['DIRACFileCatalog', 'TSCatalog'])

  def setPackage(self, package):
    """ Set package name : e.g. 'corsika_simhessarray'

    Parameters:
    package -- corsika_simhessarray
    """
    self.package = package

  def setVersion(self, version):
    """ Set software version number : e.g. 2015-07-21

    Parameters:
    version -- corsika+simtel package version number
    """
    self.version = version

  def setNShower(self, nshow):
    """ Set the number of corsika showers,
        5 is enough for testing
        20000 in production usually.

    Parameters:
    nshow -- number of corsika primary showers to generate
    """
    self.nShower = nshow

  def setRunNumber(self, runNb):
    """ Set the corsika run number, passed as a string
        because may be a TS parameter

    Parameters:
    runNb -- run number as a string, used as a corsika seed
    """
    self.run_number = runNb

  def setStartRunNumber(self, startrunNb):
    """ Set the corsika start run number (to be added to the run_number), passed as a string
        because may be a TS parameter

    Parameters:
    startrunNb -- to be added to the run number
    """
    self.start_run_number = startrunNb

  def setArrayLayout(self, layout):
    """ Set the array layout type

    Parameters:
    layout -- a string for the array layout, hex or square
    """
    if layout in ['full']:
      DIRAC.gLogger.info('Set Simtel layout to: %s' % layout)
      self.array_layout = layout
    else:
      DIRAC.gLogger.error('Unknown layout: : %s' % layout)
      DIRAC.exit(-1)

  def setSite(self, site):
    """ Set the site to simulate

    Parameters:
    site -- a string for the site name (Paranal)
    """
    self.cta_site = site

  def setParticle(self, particle):
    """ Set the corsika primary particle

    Parameters:
    particle -- a string for the particle type/name
    """
    if particle in ['gamma', 'gamma-diffuse', 'electron', 'proton', 'helium']:
      DIRAC.gLogger.info('Set Corsika particle to: %s' % particle)
      self.particle = particle
    else:
      DIRAC.gLogger.error('Corsika does not know particle type: %s' % particle)
      DIRAC.exit(-1)

  def setPointingDir(self, pointing):
    """ Set the pointing direction, North or South

    Parameters:
    pointing -- a string for the pointing direction
    """
    if pointing in ['North', 'South', 'East', 'West']:
      DIRAC.gLogger.info('Set Pointing dir to: %s' % pointing)
      self.pointing_dir = pointing
    else:
      DIRAC.gLogger.error('Unknown pointing direction: %s' % pointing)
      DIRAC.exit(-1)

  def setZenithAngle(self, zenith):
    """ Set the pointing direction, North or South

    Parameters:
    zenith -- a string for the zenith angle
    """
    self.zenith_angle = zenith

  def setNoSCTFlag(self, no_sct):
    """ Set the no sct flag to true or false

    Parameters:
    no_sct -- a bool set to true if you do not want to simulate SCTs
    """
    self.no_sct = no_sct

  def setupWorkflow(self, debug=False):
    """ Setup job workflow by defining the sequence of all executables
        All parameters shall have been defined before that method is called.
    """
    # step 1 -- to be removed -- debug only
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
    self.start_run_number = 0
    if self.no_sct:
      corsika_args = ''
    else:
      corsika_args = '--with-sct'

    corsika_args += ' --start_run %s --run %s %s %s %s %s %s' % \
                    (self.start_run_number, self.run_number,
                     self.array_layout, self.cta_site,
                     self.particle, self.pointing_dir, self.zenith_angle)

    csStep = self.setExecutable('./dirac_prod3b_corsika',
                                arguments=corsika_args,
                                logFile='Corsika_Log.txt')

    csStep['Value']['name'] = 'Step%i_Corsika' % iStep
    csStep['Value']['descr_short'] = 'Run Corsika'
    iStep += 1

    # step 4
    csvStep = self.setExecutable('cta-prod-verifysteps',
                                 arguments='corsika 2 100',
                                 logFile='Verify_Corsika_Log.txt')
    csvStep['Value']['name'] = 'Step%i_VerifyCorsika' % iStep
    csvStep['Value']['descr_short'] = 'Verify the Corsika run'
    iStep += 1

    # step 5
    stStep = self.setExecutable('./dirac_prod3b_simtel',
                                arguments='--start_run %s --run %s %s %s %s %s' %
                                (self.start_run_number, self.run_number,
                                 self.cta_site, self.particle,
                                 self.pointing_dir, self.zenith_angle),
                                logFile='Simtels_Log.txt')
    stStep['Value']['name'] = 'Step%i_Simtel' % iStep
    stStep['Value']['descr_short'] = 'Run several simtel_array configurations sequentially'
    iStep += 1

    # step 6 verify non SCT data
    stvStep = self.setExecutable('cta-prod-verifysteps',
                                 arguments="generic 3 1000 'Data/tmp/TmpData/Data/*simtel.gz'",
                                 logFile='Verify_Simtel_noSCT_Log.txt')
    stvStep['Value']['name'] = 'Step%i_VerifySimtel' % iStep
    stvStep['Value']['descr_short'] = 'Verify simtel runs'
    iStep += 1

    # step 6b verify SCT data
    if not self.no_sct:
      stvStep = self.setExecutable('cta-prod-verifysteps',
                                   arguments="generic 1 1000 'Data/sim_telarray/cta-prod3/0.0deg/Data/*SCT*.simtel.gz'",
                                   logFile='Verify_Simtel_SCT_Log.txt')
      stvStep['Value']['name'] = 'Step%i_VerifySimtelSCT' % iStep
      stvStep['Value']['descr_short'] = 'Verify simtel sct run'
      iStep += 1

    # step 7
    cleanStep = self.setExecutable('cta-prod3-cleandata',
                                   arguments="%s %s" %
                                   ('Data/corsika', '*/*.corsika.gz'),
                                   logFile='CleanData_Log.txt')
    cleanStep['Value']['name'] = 'Step%i_CleanData' % iStep
    cleanStep['Value']['descr_short'] = 'Remove corsika files'
    iStep += 1

    # step 8
    mgStep = self.setExecutable('./dirac_prod3b_merge',
                                arguments='--start_run %s --run %s' %
                                (self.start_run_number, self.run_number),
                                logFile='Merging_Log.txt')
    mgStep['Value']['name'] = 'Step%i_Merging' % iStep
    mgStep['Value']['descr_short'] = 'Merge simtel output'
    iStep += 1

    # step 9 verify merged data
    mgvStep = self.setExecutable(
        'cta-prod-verifysteps',
        arguments="generic 1 1000 'Data/sim_telarray/cta-prod3/0.0deg/Data/*merged*.simtel.gz'",
        logFile='Verify_Merging_Log.txt')
    mgvStep['Value']['name'] = 'Step%i_VerifyMerging' % iStep
    mgvStep['Value']['descr_short'] = 'Verify merging of simtel files'
    iStep += 1

    # step 11
    # the order of the metadata dictionary is important,
    # since it's used to build the directory structure
    metadata = collections.OrderedDict()
    metadata['array_layout'] = self.array_layout
    metadata['site'] = self.cta_site
    metadata['particle'] = self.particle
    if self.pointing_dir == 'North':
      metadata['phiP'] = 180
    if self.pointing_dir == 'South':
      metadata['phiP'] = 0
    metadata['thetaP'] = float(self.zenith_angle)
    metadata['tel_sim_prog'] = 'simtel'
    metadata['tel_sim_prog_version'] = self.version
    # new meta data introduced after Prod3b
    metadata['data_level'] = 0
    metadata['configuration_id'] = -1
    mdjson = json.dumps(metadata)

    metadatafield = {'array_layout': 'VARCHAR(128)',
                     'site': 'VARCHAR(128)',
                     'particle': 'VARCHAR(128)', 'phiP': 'float',
                     'thetaP': 'float',
                     'tel_sim_prog': 'VARCHAR(128)',
                     'tel_sim_prog_version': 'VARCHAR(128)',
                     'data_level': 'int', 'configuration_id': 'int'}

    mdfieldjson = json.dumps(metadatafield)

    filemetadata = {'runNumber': self.run_number}

    fmdjson = json.dumps(filemetadata)

    # Temporary fix: since the deployed script does not have the correct format for arguments
    #    dmStep = self.setExecutable('cta-prod3-managedata',
    dmStep = self.setExecutable('../CTADIRAC/Core/scripts/cta-prod3-managedata.py',
                                arguments="'%s' '%s' '%s' %s %s %s '%s'" %
                                (mdjson, mdfieldjson, fmdjson, self.inputpath,
                                 self.basepath, self.start_run_number, self.catalogs),
                                logFile='DataManagement_Log.txt')
    dmStep['Value']['name'] = 'Step%i_DataManagement' % iStep
    dmStep['Value']['descr_short'] = 'Save files to SE and register them in DFC'

    # set env variables valid within the whole workflow
    if self.no_sct:
      self.setExecutionEnv({'NSHOW': '%s' % self.nShower})
    else:
      self.setExecutionEnv({'NSHOW': '%s' % self.nShower, 'WITH_SCT': 1})
