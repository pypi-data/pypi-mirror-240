# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:34:04 2020

@author: MCARAYA
"""

__version__ = '0.1.0'
__release__ = 20220113
__all__ = ['NexusDesktopCSV']

from .mainObject import SimResult as _SimResult
from .vipObject import VIP as _VIP
from .._common.inout import _extension, _verbose
# from datafiletoolbox._common.functions import _mainKey
# from datafiletoolbox._common.stringformat import date as _strDate
# from datafiletoolbox._common.stringformat import _getnumber
from .._dictionaries import UniversalKeys as _UniversalKeys  #, VIPTypesToExtractVectors as _VIPTypesToExtractVectors
from .._common.keywordsConversions import fromECLtoVIP as _fromECLtoVIP, fromCSVtoECL as _fromCSVtoECL, fromECLtoCSV as _fromECLtoCSV  #, fromVIPtoECL
# from datafiletoolbox.dictionaries import ECL2VIPtype, ECL2VIPkey, VIP2ECLtype, VIP2ECLkey
# from datafiletoolbox._dictionaries import ECL2CSVtype, ECL2CSVkey, CSV2ECLtype, CSV2ECLkey
# from datafiletoolbox._common.functions import wellFromAttribute

from datetime import timedelta
import pandas as pd
import numpy as np
import os


class NexusDesktopCSV(_VIP):
    """
    object to contain simulation results read from .CSV file exported from NexusDesktop SimResults application
    """
    def __init__(self, inputFile=None, verbosity=2) :
        _SimResult.__init__(self, verbosity=verbosity)
        self.kind = NexusDesktopCSV
        self.ECLstyle=True
        self.VIPstyle=False
        self.keysECL = ()
        self.keysVIP = ()
        self.keysCSV = ()
        self.CSV = False
        self.results = {}
        self.LPGcorrected = False
        self.CSV_Variable2Verbose = {}
        self.CSV_Verbose2Variable = {}
        self.VIPnotECL = []
        if type(inputFile) == str and len(inputFile.strip()) > 0 :
            self.selectLoader(inputFile)
        self.initialize()

    def initialize(self) :
        """
        run intensive routines, to have the data loaded and ready
        """
        self.CSVextractBacis()
        self.CSVextractHeaders()
        self.set_FieldTime()
        self.get_Wells(reload=True)
        # self.CSVextractBacis()
        self.strip_units()
        self.fill_field_basics()
        self.prepareWellData()
        self.get_Attributes(reload=True)
        self.complete_Units()
        # self.regionNumber = self.extract_Region_Numbers()
        self.buldSalinityVectors()
        self.get_TotalReservoirVolumes()
        _SimResult.initialize(self)

    def selectLoader(self, inputFile) :
        if type(inputFile) == str and len(inputFile.strip()) > 0 :
            inputFile = inputFile.strip()
        if _extension(inputFile)[0].upper() == '.CSV' :
            self.loadCSV(inputFile)
        # elif _extension(inputFile)[0].upper() == '.SSS' :
        #     self.loadSSS(inputFile)

    def use_ECLstyle(self):
        if len(self.keysECL) == 0 :
            _verbose( self.speak, 0, ' ECL style keys: ' + str( self.extract_Keys() ) )
        if len(self.keysECL) > 0 :
            self.keys = self.keysECL
            _verbose( self.speak, 0, 'attributes as ECL style: ' + str( self.get_Attributes() ) )
            self.ECLstyle = True
            self.VIPstyle = False
            _verbose( self.speak, 3, ' Using ECL style keys')
        else :
            self.VIPstyle = 'ERROR'
            _verbose( self.speak, 3, ' Unable to convert to ECL style keys')
            if type(self.ECLstyle) == bool :
                self.use_VIPstyle()
        self.complete_Units()

    def use_VIPstyle(self):
        if len(self.keysVIP) == 0 :
            _verbose( self.speak, 0, ' VIP style keys: ' + str( self.extract_Keys() ) )
        if len(self.keysVIP) > 0 :
            self.keys = self.keysVIP
            _verbose( self.speak, 0, 'attributes as VIP style: ' + str( self.get_Attributes() ) )
            self.ECLstyle = False
            self.VIPstyle = True
            _verbose( self.speak, 3, ' Using VIP style keys')
        else :
            self.ECLstyle = 'ERROR'
            _verbose( self.speak, 3, ' Unable to get VIP style keys.')
            if type(self.VIPstyle) == bool :
                self.use_ECLstyle()
        self.complete_Units()

    def get_Style(self) :
        if self.VIPstyle == True and self.ECLstyle == False :
            return 'using VIP style'
        if self.ECLstyle == True and self.VIPstyle == False :
            return 'using ECL style'
        return 'error in style, highly recommended to regenerate style'

    def loadCSV(self, CSVFilePath):
        """
        load data from CSV file exported from SimResults applicaion of the Nexus Desktop suite.
        """
        if type(CSVFilePath) == str and len(CSVFilePath.strip()) > 0 :
            CSVFilePath = CSVFilePath.strip()
        if os.path.isfile( CSVFilePath ) == False :
            raise FileNotFoundError('No such file found for: ' + str(CSVFilePath) )
        else :
            Temporal = self.CSVread( CSVFilePath )
            if Temporal != {} :
                if self.CSV == False :
                    self.CSV = {}
                self.CSV[_extension(CSVFilePath)[1]] = Temporal
                self.get_Vector('DATE')


    # def loadSSS(self, SSSFilePath):
    #     if type(SSSFilePath) == str :
    #         SSSFilePath = SSSFilePath.strip()
    #         if self.path is None :
    #             self.path = SSSFilePath

    #         self.SSSfiles = self.SSSparts( SSSFilePath )
    #         self.name = _extension(SSSFilePath)[1]
    #         for file in self.SSSfiles :
    #             self.results[ _extension(file)[1] + _extension(file)[0] ] = self.SSSread( file )
    #         self.strip('NAME')
    #         self.set_FieldTime()
    #         self.get_Vector('DATE')
    #         self.get_Wells(reload=True)
    #         self.get_Groups(reload=True)
    #         self.get_Regions(reload=True)
    #         self.get_Keys(reload=True)
    #         self.units = self.get_Unit(self.keys)
    #         _verbose( self.speak, 1, 'simulation runs from ' +  str( self.get_Dates()[0] ) + ' to ' + str( self.get_Dates()[-1] ) )
    #     else :
    #         print("SummaryFilePath must be a string")

    # def correction_for_LPG_from_VIPsss(self) :
    #     if self.LPGcorrected :
    #         _verbose( self.speak, 2, 'LPG correction for VIP sss reports is already applied.')
    #     else :
    #         for LPGkey in ( 'LPG LIQ RATE', 'FULPGLR'  ) :
    #             if self.is_Key( LPGkey ) :
    #                 Before = self.get_Vector(LPGkey)[LPGkey]
    #                 Corrected = Before * 0.1292 / 33.4962
    #                 self.set_Vector( LPGkey, Corrected, self.get_Unit(LPGkey), DataType='float', overwrite=True )
    #                 self.LPGcorrected = True
    #                 _verbose( self.speak, 2, 'Successfully applied LPG correction for VIP sss reports.')

    def CSVread(self, CSVFilePath) :
        """
        extract the data from the CSV file exported from SimResults applicaion of the Nexus Desktop suite.
        Pandas doesn't read this kind of CSV correctly.'
        """
        if self.path is None :
            self.path = CSVFilePath
        CSVfile = open(CSVFilePath, 'r')
        CSVlines = CSVfile.read()
        CSVfile.close()
        CSVlines = CSVlines.split('\n')

        row = 0
        section = ''
        CSVdict = {}

        while row < len(CSVlines) :
            cell0 = CSVlines[ row ].split(', ')[0].split('=')[0]
            if cell0 == '[S3INFO]' :
                section = cell0
                CSVdict[section] = {}

            elif cell0 == '[HEADERS]' :
                section = cell0
                CSVdict[section] = {}

            elif cell0 == '[DATA]' :
                section = cell0
                CSVdict[section] = []
                if '[' in ', '.join( CSVlines[row+1:] ) and ']' in ', '.join( CSVlines[row+1:] ) :
                    segmentEnd =', '.join( CSVlines[row+1:] ).index('[')
                    CSVdict[section] = ', '.join( CSVlines[row+1:] )[: segmentEnd ].split(', ')
                    dataRows = len( CSVdict[section] ) / len( CSVdict['[HEADERS]']['VARIABLE'] )
                    if int(dataRows) == dataRows :
                        row = row + dataRows
                    else :
                        pass
                else :
                    CSVdict[section] = ', '.join( CSVlines[row+1:] ).split(', ')
                    row = len(CSVlines)
            else :
                if '[' in CSVlines[ row ].split(', ')[0].split('=')[0][0] and ']' in CSVlines[ row ].split(', ')[0].split('=')[0][-1] :
                    section = CSVlines[ row ].split(', ')[0].split('=')[0]
                else :
                    CSVdict[section][ cell0 ] = [ CSVlines[ row ].split(', ')[0].split('=')[1] ] + CSVlines[ row ].split(', ')[1:]
            row += 1
        return CSVdict

    def CSVextractBacis(self, CSVname='' ) :
        if CSVname == '' :
            CSVname = list( self.CSV.keys() )[-1]

        if self.name is None :
            try:
                self.name = self.CSV[CSVname]['[S3INFO]']['ORIGIN'][0]
            except :
                pass
        if self.start is None :
            try :
                self.start = np.datetime64( pd.to_datetime( self.CSV[CSVname]['[S3INFO]']['DATE'][0] ), 's')
            except:
                pass
        else :
            try :
                if self.start > np.datetime64( pd.to_datetime( self.CSV[CSVname]['[S3INFO]']['DATE'][0] ), 's') :
                    self.start = np.datetime64( pd.to_datetime( self.CSV[CSVname]['[S3INFO]']['DATE'][0] ), 's')
            except :
                pass
        try :
            self.null = self.CSV[CSVname]['[S3INFO]']['NULLVALUE'][0]
            nullSet = True
        except :
            nullSet = False
        if nullSet == True :
            try :
                self.null = int(self.null)
            except :
                try :
                    self.null = float(self.null)
                except:
                    pass

    def CSVextractHeaders(self, CSVname='' ):
        if CSVname == '' :
            CSVname = list( self.CSV.keys() )[-1]

        CSVkeys = []
        ECLkeys = []
        VIPkeys = []
        CSVwells = []
        for i in range( len( self.CSV[CSVname]['[HEADERS]']['VARIABLE'] ) ):
            if len( self.CSV[CSVname]['[HEADERS]']['MEMBER'][i].strip() ) > 0 :
                self.units[ self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i] + ':' + self.CSV[CSVname]['[HEADERS]']['MEMBER'][i] ] = self.CSV[CSVname]['[HEADERS]']['UNITS'][i]
                if self.CSV[CSVname]['[HEADERS]']['CLASS'][i].strip().upper() == 'WELL' :
                    CSVwells += [ self.CSV[CSVname]['[HEADERS]']['MEMBER'][i].strip() ]
            else :
                self.units[ self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i] ] = self.CSV[CSVname]['[HEADERS]']['UNITS'][i]
            self.CSV_Variable2Verbose[ self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i] ] = self.CSV[CSVname]['[HEADERS]']['VERBOSE'][i]
            self.CSV_Verbose2Variable[ self.CSV[CSVname]['[HEADERS]']['VERBOSE'][i] ] = self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i]
            CSVkeys += [ self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i] +':' + self.CSV[CSVname]['[HEADERS]']['MEMBER'][i] ]
            ECLkey = _fromCSVtoECL( variableORkey=self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i], CLASStype=self.CSV[CSVname]['[HEADERS]']['CLASS'][i], MEMBER=self.CSV[CSVname]['[HEADERS]']['MEMBER'][i], speak=self.speak )
            if ECLkey is not None :
                ECLkeys += [ ECLkey ]
                VIPkey, keyType, keyName = _fromECLtoVIP( ECLkey, self.speak )
                VIPkeys += [ VIPkey + ':' + keyName ]

            fullName = self.CSV[CSVname]['[HEADERS]']['CLASS'][i] + ':' + self.CSV[CSVname]['[HEADERS]']['MEMBER'][i] + ':' + self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i]
            self.pandasColumns[fullName] = [ self.CSV[CSVname]['[HEADERS]']['CLASS'][i], self.CSV[CSVname]['[HEADERS]']['MEMBER'][i], self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i], self.CSV[CSVname]['[HEADERS]']['UNITS'][i], self.CSV[CSVname]['[HEADERS]']['VERBOSE'][i] ]

        CSVwells = list ( set( list( self.wells ) + list( set( CSVwells ) ) ) )
        CSVwells.sort()
        self.wells = tuple ( CSVwells )
        self.keysCSV = tuple ( set( list( self.keysCSV ) + list( set( CSVkeys ) ) ) )
        self.keysVIP = tuple ( set(  list( self.keysVIP ) + list( set( VIPkeys ) ) ) )
        self.keysECL = tuple ( set(  list( self.keysECL ) + list( set( ECLkeys ) ) ) )
        if self.ECLstyle :
            self.keys = self.keysECL
        elif self.VIPstyle :
            self.keys = self.keysVIP

    def CSVextractVectors(self, CSVname ):
        numHeaders = len( self.CSV[CSVname]['[HEADERS]']['VARIABLE'] )

        for i in range( numHeaders ) :
            if len( self.CSV[CSVname]['[HEADERS]']['MEMBER'][i].strip() ) > 0 :
                CSVkey = self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i] + ':' + self.CSV[CSVname]['[HEADERS]']['MEMBER'][i]
            else :
                CSVkey = self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i]
            ECLkey = _fromCSVtoECL( variableORkey=self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i], CLASStype=self.CSV[CSVname]['[HEADERS]']['CLASS'][i], MEMBER=self.CSV[CSVname]['[HEADERS]']['MEMBER'][i], speak=self.speak )
            Vector = self.CSV[CSVname]['[DATA]'][i::numHeaders]
            while len(Vector) > 0 and Vector[-1] == '' :
                Vector = Vector[:-1]
            if len(Vector) > 0 :
                Unit = self.CSV[CSVname]['[HEADERS]']['UNITS'][i]
                _verbose( self.speak, 1, ' Setting vector for CSV key ' + CSVkey )
                self.set_Vector(key=CSVkey, vector_data=Vector, units=Unit, data_type='auto', overwrite=True)
                if ECLkey is not None and len(ECLkey) > 0 :
                    _verbose( self.speak, 1, ' Setting vector for ECL key ' + ECLkey )
                    self.set_Vector(key=ECLkey, vector_data=Vector, units=Unit, data_type='auto', overwrite=True)

        if 'TIME' in self.CSV[CSVname]['[HEADERS]']['VARIABLE'] :
            iTIME = self.CSV[CSVname]['[HEADERS]']['VARIABLE'].index('TIME')
            start = np.datetime64( pd.to_datetime( self.CSV[CSVname]['[S3INFO]']['DATE'][0] ), 's')
            TIME = self.CSV[CSVname]['[DATA]'][iTIME::numHeaders]
            while len(TIME) > 0 and TIME[-1] == '' :
                TIME = TIME[:-1]
            DATE = np.empty(len(TIME), dtype='datetime64[s]')
            for i in range(len(TIME)) :
                DATE[i] = start + np.timedelta64( timedelta(days=TIME[i]) )

    def get_csvVector(self, CSVname=None, CLASS='', MEMBER='', VARIABLE='' ):
        if CSVname is None :
            CSVnames = list( self.CSV.keys() )
        elif type(CSVname) == str :
            CSVnames = [ CSVname ]
        Results = {}
        # Unit = None
        # Verbose = None
        Data = None
        Vector = None
        for CSVname in CSVnames :
            _verbose( self.speak, 1, ' looking into the CSV ' + CSVname )
            numHeaders = len( self.CSV[CSVname]['[HEADERS]']['VARIABLE'] )

            # headers = {'CLASS' : [], 'MEMBER' : [], 'VARIABLE' : []}
            Results[CSVname] = {}
            for col in range( numHeaders ) :
                CLASSflag = False
                MEMBERflag = False
                VARIABLEflag = False

                if CLASS != '' and self.CSV[CSVname]['[HEADERS]']['CLASS'][col].strip() == MEMBER :
                    _verbose( self.speak, 1, 'mathcing CLASS')
                    CLASSflag = True
                elif CLASS == '' :
                    CLASSflag = True
                if MEMBER != '' and self.CSV[CSVname]['[HEADERS]']['MEMBER'][col].strip() == MEMBER :
                    _verbose( self.speak, 1, 'mathcing MEMBER')
                    MEMBERflag = True
                elif MEMBER == '' :
                    MEMBERflag = True
                if VARIABLE != '' and self.CSV[CSVname]['[HEADERS]']['VARIABLE'][col].strip() == MEMBER :
                    _verbose( self.speak, 1, 'mathcing VARIABLE')
                    VARIABLEflag = True
                elif VARIABLE == '' :
                    VARIABLEflag = True

                if CLASSflag * MEMBERflag * VARIABLEflag == 1 :
                    _verbose( self.speak, 1, '\nVECTOR ' + CLASS + ':' + MEMBER + ':' + VARIABLE + ' FOUND!\n')
                    Data = self.CSV[CSVname]['[DATA]'][col::numHeaders]
                    Data = tuple(Data)
                    Vector = list(Data)
                    while len(Vector) > 0 and Vector[-1] == '' :
                        Vector = Vector[:-1]
                    if len(Vector) > 0 :
                        Temp = []
                        Failed = True
                        if '.' in ' '.join(Vector) or 'E-' in ' '.join(Vector) or 'E+' in ' '.join(Vector):
                            for v in range(len(Vector)) :
                                try :
                                    Temp.append( float(Vector[v]) )
                                    Failed = False
                                except:
                                    break
                        else :
                            for v in range(len(Vector)) :
                                try :
                                    if Vector[v].isdigit() :
                                        Temp.append( int(Vector[v]) )
                                        Failed = False
                                    else :
                                        try :
                                            Temp.append( float(Vector[v]) )
                                            Failed = False
                                        except:
                                            break
                                except:
                                    break
                        if not Failed :
                            Vector = np.array(Temp)
                        else :
                            Vector = np.array(Vector)
                    if CSVname not in Results :
                        Results[CSVname] = {}
                    Results[CSVname][col] = {}
                    Results[CSVname][col]['CLASS'] = self.CSV[CSVname]['[HEADERS]']['CLASS'][col]
                    Results[CSVname][col]['MEMBER'] = self.CSV[CSVname]['[HEADERS]']['MEMBER'][col]
                    Results[CSVname][col]['VARIABLE'] = self.CSV[CSVname]['[HEADERS]']['VARIABLE'][col]
                    Results[CSVname][col]['UNITS'] = self.CSV[CSVname]['[HEADERS]']['UNITS'][col]
                    Results[CSVname][col]['VERBOSE'] = self.CSV[CSVname]['[HEADERS]']['VERBOSE'][col]
                    Results[CSVname][col]['DATA'] = Data
                    Results[CSVname][col]['NumpyArray'] = Vector
        tot = 0
        for CSVname in CSVnames :
            tot += len( list( Results[CSVname].keys() ) )
        _verbose( self.speak, 2, ' ' + str(tot) + ' matches found for ' + CLASS + ':' + MEMBER + ':' + VARIABLE + '.')
        return Results

    def CSVloadVector(self, key, VIPkey='', keyType='', keyName='', CSVname=None ):

        key = key.strip().upper()

        if key in ( 'DATE', 'DATES' ) :
            DATEflag = key
            key = 'TIME'
        else :
            DATEflag = False

        keyword = key

        if CSVname is None :
            CSVnames = list( self.CSV.keys() )
        elif type(CSVname) == str :
            CSVnames = [ CSVname ]

        if keyName == '' :
            if ':' in key and len(key.split(':')[1])>0 :
                keyName = key.split(':')[1]
        else :
            keyName = keyName.strip()

        if keyType == '' :
            if ':' in key :
                if key.split(':')[1] in self.get_Wells() :
                    keyType = 'WELL'
            elif ':' in VIPkey :
                if VIPkey.split(':')[1] in self.get_Wells() :
                    keyType = 'WELL'
            elif key[0] == 'F' :
                keyType = 'FIELD'
                keyName = 'FIELD'
            elif key[0] == 'W' :
                keyType = 'WELL'

        Variable, Class, Member = _fromECLtoCSV( key )

        if key in _UniversalKeys or VIPkey in _UniversalKeys :
            keyType = 'MISCELLANEOUS'
            keyName = ''
            if key in _UniversalKeys :
                keyword = key
            else :
                keyword = VIPkey

        elif key in ( 'BHP', 'THP' ) or VIPkey in ( 'BHP', 'THP' ) :
            keyType == 'WELL'

        if keyName == 'ROOT' :
            keyName = 'FIELD'

        FOUNDflag = False
        for CSVname in CSVnames :
            numHeaders = len( self.CSV[CSVname]['[HEADERS]']['VARIABLE'] )
            _verbose( self.speak, 1, ' looking for vector for key: ' + str(key) + ' where variable=' + Variable + ', class=' + Class + ' or ' + keyType + ' and member=' + Member + ' or ' + keyName )
            for col in range( numHeaders ) :
                if ( self.CSV[CSVname]['[HEADERS]']['CLASS'][col] == keyType or self.CSV[CSVname]['[HEADERS]']['CLASS'][col] == Class ) and \
                   ( self.CSV[CSVname]['[HEADERS]']['MEMBER'][col] == keyName or self.CSV[CSVname]['[HEADERS]']['MEMBER'][col] == Member ) and \
                   ( self.CSV[CSVname]['[HEADERS]']['VARIABLE'][col] == Variable or self.CSV[CSVname]['[HEADERS]']['VARIABLE'][col] == keyword ) :
                    _verbose( self.speak, 1, ' found vector for key: ' + str(key) + ' where variable=' + self.CSV[CSVname]['[HEADERS]']['VARIABLE'][col] + ', class=' + self.CSV[CSVname]['[HEADERS]']['CLASS'][col] + ' and member=' + self.CSV[CSVname]['[HEADERS]']['MEMBER'][col] + '.' )
                    if len( self.CSV[CSVname]['[HEADERS]']['MEMBER'][col] ) > 0 :
                        CSVkey = self.CSV[CSVname]['[HEADERS]']['VARIABLE'][col] + ':' + self.CSV[CSVname]['[HEADERS]']['MEMBER'][col]
                    else :
                        CSVkey = self.CSV[CSVname]['[HEADERS]']['VARIABLE'][col]
                    ECLkey = _fromCSVtoECL( variableORkey=self.CSV[CSVname]['[HEADERS]']['VARIABLE'][col], CLASStype=self.CSV[CSVname]['[HEADERS]']['CLASS'][col], MEMBER=self.CSV[CSVname]['[HEADERS]']['MEMBER'][col], speak=self.speak )
                    Vector = self.CSV[CSVname]['[DATA]'][col::numHeaders]
                    while len(Vector) > 0 and Vector[-1] == '' :
                        Vector = Vector[:-1]
                    if len(Vector) > 0 :
                        Temp = []
                        Failed = True
                        if '.' in ' '.join(Vector) or 'E-' in ' '.join(Vector) or 'E+' in ' '.join(Vector):
                            for i in range(len(Vector)) :
                                try :
                                    Temp.append( float(Vector[i]) )
                                    Failed = False
                                except:
                                    break
                        else :
                            for i in range(len(Vector)) :
                                try :
                                    if Vector[i].isdigit() :
                                        Temp.append( int(Vector[i]) )
                                        Failed = False
                                    else :
                                        try :
                                            Temp.append( float(Vector[i]) )
                                            Failed = False
                                        except:
                                            break
                                except:
                                    break
                        if not Failed :
                            Vector = np.array(Temp)
                        else :
                            Vector = np.array(Vector)
                        Unit = self.CSV[CSVname]['[HEADERS]']['UNITS'][col]
                        _verbose( self.speak, 1, ' Setting vector for CSV key ' + CSVkey )
                        self.set_Vector(key=CSVkey, vector_data=Vector, units=Unit, data_type='auto', overwrite=True)
                        if ECLkey is not None and len(ECLkey) > 0 :
                            _verbose( self.speak, 1, ' Setting vector for ECL key ' + ECLkey )
                            self.set_Vector(key=ECLkey, vector_data=Vector, units=Unit, data_type='auto',
                                            overwrite=True)
                        FOUNDflag = True
                        if type(DATEflag) == str  :
                            _verbose( self.speak, 1, ' Creating date vector for CSV key ' + DATEflag )
                            start = np.datetime64( pd.to_datetime( self.CSV[CSVname]['[S3INFO]']['DATE'][0] ), 's' )
                            TIME = self.vectors['TIME']
                            DATE = np.empty(len(TIME), dtype='datetime64[s]')
                            for i in range(len(TIME)) :
                                DATE[i] = start + np.timedelta64( timedelta(days=TIME[i]) )
                            self.vectors[DATEflag] = DATE
                            self.units[DATEflag] = 'DATE'
                        break

        if FOUNDflag == False :
            _verbose( self.speak, 2, 'vector corresponding to key ' + key + ' not found in CSV data.')
        else :
            if type(DATEflag) == str :
                return DATE
            else:
                return Vector

    def CSVgenerateResults(self) :
        for CSVname in list( self.CSV.keys() ) :
            self.CSV[CSVname] = self.CSV[CSVname]
            numHeaders = len( self.CSV[CSVname]['[HEADERS]']['VARIABLE'] )
            numRows = int( len( self.CSV[CSVname]['[DATA]'] ) / numHeaders )

            # generate the diccionaries for every CLASS:
            _verbose( self.speak, 3, ' generating raw data dictionary from CSV table, \n  > preparing results dictionary\n    ... please wait ...')
            for sss in list( set( self.CSV[CSVname]['[HEADERS]']['CLASS'] ) ) :
                if sss not in self.results.keys() :
                    self.results[ str(sss) + '@' + _extension(self.path)[1]+_extension(self.path)[0] ] = ( str(sss), { 'Data':{}, 'Units':{} } )

            # generate Units dictionary
            _verbose( self.speak, 3, '  > loading units\n    ... please wait ...')
            for i in range( numHeaders ) :
                self.results[ self.CSV[CSVname]['[HEADERS]']['CLASS'][i] + '@' + _extension(self.path)[1]+_extension(self.path)[0] ][1]['Units'][ self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i] ] = self.CSV[CSVname]['[HEADERS]']['UNITS'][i]

            # load the series from [DATA] into results dictionary
            _verbose( self.speak, 3, '  > transforming and loading data series\n    ... please wait ...')
            for i in range( numHeaders ) :
                Vector = self.CSV[CSVname]['[DATA]'][i::numHeaders]
                while len( Vector ) > 0 and Vector[-1] == '' :
                    Vector = Vector[:-1]
                if len(Vector) != numRows :
                    print('issue with rows', len(Vector), numRows )
                if len( self.CSV[CSVname]['[HEADERS]']['MEMBER'][i] ) > 0 :
                    Name = self.CSV[CSVname]['[HEADERS]']['MEMBER'][i]
                else :
                    Name = 'ROOT'
                self.results[ self.CSV[CSVname]['[HEADERS]']['CLASS'][i] + '@' + _extension(self.path)[1]+_extension(self.path)[0] ][1]['Data'][ self.CSV[CSVname]['[HEADERS]']['VARIABLE'][i]+':'+Name ] = Vector
            _verbose( self.speak, 3, '  > DONE! results dictionary generated.')

        _verbose( self.speak, 3, '  > checking the transformed data\n    ... please wait ...')
        OK = True
        for CSV in list( self.results.keys() ) :
            KEYsLenght = []
            for KEY in list( self.results[CSV][1]['Data'].keys() ) :
                KEYsLenght.append( len( self.results[CSV][1]['Data'][KEY] ) )
            if max(KEYsLenght) == min(KEYsLenght) :
                _verbose( self.speak, 3, '  > ' + str(CSV) + ' properly created with ' + str( numHeaders ) + ' columns and ' + str( max(KEYsLenght) ) + ' rows.')
            else :
                print( max(KEYsLenght), min(KEYsLenght), numRows)
                _verbose( self.speak, -1, '  > ' + str(CSV) + ' issue: ' + str( numHeaders ) + ' columns and ' + str( max(KEYsLenght) ) + ' rows.')
                OK = False

        if OK :
            _verbose( self.speak, 3, '  > DONE! results dictionary generated.')
        else :
            _verbose( self.speak, -1, '  > results dictionary generated with issues.')

    def reload(self) :
        # if self.CSV == False :
        #     self.loadSSS(self.path)
        # else :
        #     self.loadCSV(self.path)
        self.loadCSV(self.path)

    # def strip(self, VIPkey, stringToStrip=' ') :
    #     """
    #     applies .strip() method to every item in a Key of the results dictionaries
    #     """
    #     for sss in self.results.keys() :
    #         for i in range(len( self.results[sss][1]['Data'][ VIPkey ] )) :
    #             if type( self.results[sss][1]['Data'][ VIPkey ][i] ) == str :
    #                 self.results[sss][1]['Data'][ VIPkey ][i] = self.results[sss][1]['Data'][ VIPkey ][i].strip(stringToStrip)

    # def SSSparts(self, SSSFilePath):
    #     SSSfiles = []
    #     expectedParts = [ ( '_field.sss', '_area.sss', '_flow.sss', '_gather.sss', '_region.sss', '_well.sss' ),
    #                       ( '_FIELD.SSS', '_AREA.SSS', '_FLOW.SSS', '_GATHER.SSS', '_REGION.SSS', '_WELL.SSS' ) ]
    #     if _extension(SSSFilePath)[0].upper() == '.SSS' :
    #         for Case in expectedParts :
    #             for part in Case :
    #                 if part in SSSFilePath and SSSFilePath[SSSFilePath.index(part):] == part:
    #                     SSSroot = SSSFilePath[:SSSFilePath.index(part)]
    #                     break
    #             for part in Case :
    #                 if os.path.isfile(SSSroot + part) :
    #                     SSSfiles.append(SSSroot + part)
    #             if len( SSSfiles ) > 0 :
    #                 return tuple( SSSfiles )
    #         if os.path.isfile(SSSFilePath) : # if this line is reached, implicitly len( SSSfiles ) == 0
    #             return tuple ( SSSFilePath )
    #         else :
    #             raise FileNotFoundError('No such file or related VIP files found for: ' + str(SSSFilePath) )

    #     else : # if _extension(SSSFilePath)[0] != '.SSS' :
    #         SSSroot = _extension(SSSFilePath)[2] + _extension(SSSFilePath)[1]
    #         for Case in expectedParts :
    #             for part in Case :
    #                 if os.path.isfile(SSSroot + part) :
    #                     SSSfiles.append(SSSroot + part)
    #             if len( SSSfiles ) > 0 :
    #                 return tuple( SSSfiles )

    #     if len( SSSfiles ) == 0 :
    #         raise FileNotFoundError('No such file or related VIP files found for: ' + str(SSSFilePath) )

    # def SSSread(self, sssPath) :
    #     _verbose( self.speak, 1, '\nREADING ' + str(sssPath) )
    #     sssfile = open(sssPath, 'r')
    #     sss = sssfile.read()
    #     sssfile.close()
    #     sss = sss.split('\n')

    #     sssType = sss[0].split()[0]
    #     _verbose( self.speak, 1, 'Type of data in this input file: ' + str(sssType) )

    #     sssColumns = sss[1].split('\t')
    #     for i in range(len(sssColumns)):
    #         sssColumns[i] = sssColumns[i].strip()

    #     sssUnits = sss[2].split('\t')
    #     for i in range(len(sssUnits)):
    #         sssUnits[i] = sssUnits[i].strip()

    #     sssClean = []
    #     for i in range(len(sss[3:])) :
    #         if len(sss[3+i].strip()) > 0 :
    #             sssClean.append(sss[3+i])

    #     sssData = []
    #     sssData = '\t'.join(sssClean).split('\t')

    #     sssDict = { 'Data' : {}, 'Units' : {} }

    #     for i in range(len(sssColumns)) :
    #         sssDict['Data'][sssColumns[i]] = sssData[i::len(sssColumns)]
    #     for i in range(len(sssColumns)) :
    #         sssDict['Units'][sssColumns[i]] = sssUnits[i]

    #     if self.speak !=0 :
    #         _verbose( self.speak, 1, ' data found in the ' + str(sssType) + ' summary file:')
    #         for each in sssDict['Data'] :
    #             _verbose( self.speak, 1, '  > ' + str(each) + str( ' ' * (16-len(str(each))) ) + ' with ' + str(len(sssDict['Data'][each])) + ' rows with units: ' + str( sssDict['Units'][each] ) )

    #     return ( sssType, sssDict )

    # support functions for get_Vector:
    def loadVector(self, key, SSStype=[], forceVIP=False) :
        """
        internal function to load a numpy vector from the CSV files
        """
    #     """
    #     internal function to load a numpy vector from the summary files
    #     """

        def alreadyVIP(key, SSStype):
            wellVIPkeys = ('BHP', 'THP')
            if ':' in key :
                VIPkey = key[:key.index(':')]
                keyName = key[key.index(':')+1:]
            else :
                VIPkey = key
                if key in wellVIPkeys :
                    keyName = list(self.get_Wells())
                    SSStype = ['WELL']
                elif VIPkey in _UniversalKeys :
                    keyName = 'ROOT'
                    SSStype = ['FIELD']
                else :
                    keyName = 'ROOT'
            if len( SSStype ) > 1 :
                if keyName == 'ROOT' :
                    keyType = 'FIELD'
                else :
                    _verbose( self.speak, 2, 'none or more than one type summary were selected, ')
                    keyType = SSStype
            else :
                keyType = SSStype[0]

            _verbose( self.speak, 1, 'identified VIP key ' + VIPkey + ' for ' + str(keyType) + ' summary for the item ' + keyName )
            return VIPkey, keyType, keyName

      ####################### end of auxiliar functions #######################

        if SSStype == [] : # and self.CSV == False:
            # for sss in list(self.results.keys()) :
            #     SSStype += [self.results[sss][0]]
            SSStype = ['FIELD', 'WELL']
        elif type(SSStype) == str :
            SSStype = [SSStype]

        key = str(key).strip().upper()
        if forceVIP :
            _verbose( self.speak, 1, 'forced to use inputs as VIP keywords')
        if self.ECLstyle == True and forceVIP == False:
            # if key in self.keysECL :
            try :
                VIPkey, keyType, keyName = _fromECLtoVIP( key, self.speak )
            except :
                try :
                    VIPkey, keyType, keyName = alreadyVIP(key, SSStype)
                except :
                    pass

        else : # VIP style first
            try :
                VIPkey, keyType, keyName = alreadyVIP(key, SSStype)
            except :
                try :
                    VIPkey, keyType, keyName = _fromECLtoVIP( key, self.speak )
                except :
                    pass

        if type(keyType) == str :
            keyTypeList = tuple([keyType])
        else :
            keyTypeList = tuple(keyType[:])


        ###### in case of CSV load :
        # if self.CSV != False :
        return self.CSVloadVector( key, VIPkey, keyType, keyName )
        ###### in case of CSV load.

    #     for keyType in keyTypeList :

    #         if keyType in SSStype :
    #             if keyType == 'FIELD' :
    #                 for sss in list(self.results.keys()) :
    #                     if self.results[sss][0] == keyType :
    #                         if VIPkey in self.results[sss][1]['Data'].keys() :
    #                             RawCol = np.array( self.results[sss][1]['Data'][ VIPkey ] )
    #                             _verbose( self.speak, 1, 'extracted ' + VIPkey + ' from ' + keyType + ' with lenght ' + str(len(RawCol)) )
    #                             try :
    #                                 RawCol = RawCol.astype(int)
    #                                 _verbose( self.speak, 1, 'the values were converted to integer type')
    #                             except :
    #                                 try :
    #                                     RawCol = RawCol.astype(float)
    #                                     _verbose( self.speak, 1, 'the values were converted to floating point type')
    #                                 except :
    #                                     _verbose( self.speak, 1, 'the values are treated as string type')
    #                             return RawCol
    #             else :
    #                 for sss in list(self.results.keys()) :
    #                     if self.results[sss][0] == keyType :
    #                         if VIPkey in self.results[sss][1]['Data'].keys() :
    #                             RawCol = np.array( self.results[sss][1]['Data'][ VIPkey ] )
    #                             NameCol = np.array( self.results[sss][1]['Data'][ 'NAME' ] )
    #                             TimeCol = np.array( self.results[sss][1]['Data'][ 'TIME' ] )
    #                             _verbose( self.speak, 1, 'extracted ' + VIPkey + ' from ' + keyType + ' with lenght ' + str(len(RawCol)) )
    #                             _verbose( self.speak, 0, 'extracted ' + 'NAME' + ' from ' + keyType + ' with lenght ' + str(len(NameCol)) )
    #                             _verbose( self.speak, 0, 'extracted ' + 'TIME' + ' from ' + keyType + ' with lenght ' + str(len(NameCol)) )
    #                             try :
    #                                 RawCol = RawCol.astype(int)
    #                                 _verbose( self.speak, 1, 'the values were converted to integer type')
    #                             except :
    #                                 try :
    #                                     RawCol = RawCol.astype(float)
    #                                     _verbose( self.speak, 1, 'the values were converted to floating point type')
    #                                 except :
    #                                     _verbose( self.speak, 1, 'the values are treated as string type')

    #                             if type(keyName) == str :
    #                                 _verbose( self.speak, 1, 'filtering data for item: ' + keyName)
    #                                 CleanCol = np.extract( np.char.equal( NameCol, keyName ), RawCol )
    #                                 CleanTime = np.extract( np.char.equal( NameCol, keyName ), TimeCol )
    #                                 _verbose( self.speak, 1, 'extracting ' + VIPkey + ' with lenght ' + str(len(CleanCol))  + ' for item ' + keyName + '.')
    #                             elif len(keyName) == 1 :
    #                                 keyName = keyName[0]
    #                                 _verbose( self.speak, 2, 'the item name was not especified by only one options ( ' + keyName + ' ) has been found for the key : ' + key )
    #                                 _verbose( self.speak, 1, 'filtering data for item: ' + keyName )
    #                                 CleanCol = np.extract( np.char.equal( NameCol, keyName ), RawCol )
    #                                 CleanTime = np.extract( np.char.equal( NameCol, keyName ), TimeCol )
    #                                 _verbose( self.speak, 1, 'cleaned ' + VIPkey + ' with lenght ' + str(len(CleanCol)) + ' for item ' + keyName + '.' )
    #                             else :
    #                                 _verbose( self.speak, 2, 'multiple ( ' + str(len(keyName)) + ' ) item options found for the key : ' + key + ':\n' + str(keyName) )
    #                                 CleanCol = np.array([], dtype='float')
    #                                 CleanTime = np.array([], dtype='float')

    #                             if len(CleanCol) > 0 :
    #                                 CleanCol = self.fillZeros( CleanCol, CleanTime )

    #                             return CleanCol

    # def set_FieldTime(self) :
    #     if len( self.get_Restart() ) > 0 :
    #         FieldTime = self.checkRestarts('TIME')['TIME']
    #     else :
    #         FieldTime = self.loadVector('TIME', SSStype=['FIELD'])
    #     if FieldTime is None :
    #         if self.get_Vector('TIME')['TIME'] is not None :
    #             FieldTime = self.get_Vector('TIME')['TIME']
    #     if FieldTime is not None :
    #         self.fieldtime = ( min(FieldTime), max(FieldTime), FieldTime )

    # def get_Dates(self) :
    #     try :
    #         DateVector = _strDate( list( self.loadVector('DATE', 'FIELD', True) ), speak=(self.speak==1))
    #     except :
    #         DateVector = _strDate( list( self.loadVector('DATE', 'FIELD', True) ), formatIN='DD-MM-YYYY', speak=(self.speak==1))
    #     self.set_Vector( 'DATES', np.array( pd.to_datetime( DateVector ), dtype='datetime64[s]'), self.get_Unit('DATE'), DataType='datetime64', overwrite=True )
    #     #self.set_Vector( 'DATES', np.array( pd.to_datetime( self.get_Vector('DATE')['DATE'] ), dtype='datetime64[s]'), self.get_Unit('DATE'), DataType='datetime64', overwrite=True )
    #     self.set_Vector( 'DATE', self.get_Vector('DATES')['DATES'], self.get_Unit('DATES'), overwrite=True )
    #     self.start = min( self.get_Vector('DATE')['DATE'] )
    #     self.end = max( self.get_Vector('DATE')['DATE'] )
    #     return self.get_Vector('DATE')['DATE']

    def extract_wells(self) : #, pattern=None) :
        # preparing object attribute
        wellsList = list( self.wells )
        # if self.CSV == False :
        #     for sss in self.results :
        #         if self.results[sss][0] == 'WELL' :
        #             wellsList += ( ' '.join( self.results[sss][1]['Data']['NAME'] ).split() )
        # else :
        #     for CSVname in self.CSV :
        #         for i in range( len( self.CSV[CSVname]['[HEADERS]']['VARIABLE'] ) ):
        #             if len( self.CSV[CSVname]['[HEADERS]']['MEMBER'][i].strip() ) > 0 :
        #                 if self.CSV[CSVname]['[HEADERS]']['CLASS'][i].strip().upper() == 'WELL' :
        #                     wellsList += [ self.CSV[CSVname]['[HEADERS]']['MEMBER'][i].strip() ]
        for CSVname in self.CSV :
            for i in range( len( self.CSV[CSVname]['[HEADERS]']['VARIABLE'] ) ):
                if len( self.CSV[CSVname]['[HEADERS]']['MEMBER'][i].strip() ) > 0 :
                    if self.CSV[CSVname]['[HEADERS]']['CLASS'][i].strip().upper() == 'WELL' :
                        wellsList += [ self.CSV[CSVname]['[HEADERS]']['MEMBER'][i].strip() ]
        wellsList = list( set( wellsList ) )
        wellsList.sort()
        self.wells = tuple( wellsList )

        return self.wells

    # def extract_Groups(self, pattern=None, reload=False) :
    #     """
    #     Will return a list of all the group names in case.

    #     If the pattern variable is different from None only groups
    #     matching the pattern will be returned; the matching is based
    #     on fnmatch(), i.e. shell style wildcards.
    #     """
    #     if len(self.groups) == 0 or reload == True :
    #         self.groups = tuple( self.extract_Areas(pattern) )
    #     if pattern is None :
    #         return self.groups
    #     else:
    #         return tuple( self.extract_Areas(pattern) )

    def extract_areas(self, pattern=None) :
        # preparing object attribute
        areaList = list( self.groups )
        # for sss in self.results :
        #     if self.results[sss][0] == 'AREA' :
        #         areaList += ( ' '.join( self.results[sss][1]['Data']['NAME'] ).split() )
        areaList = list( set( areaList ) )
        areaList.sort()
        self.groups = tuple( areaList )
        # preparing list to return
        if pattern is not None :
            areaList = []
            for group in self.groups :
                if pattern in group :
                    areaList.append(group)
            return tuple(areaList)
        else :
            return self.groups

    def extract_regions(self, pattern=None) :
        # preparing object attribute
        regionsList = list( self.regions )
        # if self.CSV == False :
        #     for sss in self.results :
        #         if self.results[sss][0] == 'REGION' :
        #             regionsList += ( ' '.join( self.results[sss][1]['Data']['NAME'] ).split() )
        # else :
        #     pass
        regionsList = list( set( regionsList ) )
        regionsList.sort()
        self.regions = tuple( regionsList )
        # preparing list to return
        if pattern is not None :
            regionsList = []
            for region in self.regions :
                if pattern in region :
                    regionsList.append(region)
            return tuple(regionsList)
        else :
            return self.regions

    # def directSSS(self, Key, SSStype):
    #     """
    #     returns the string column from the SSS file for the required Key.
    #     """
    #     SSStype = SSStype.strip()
    #     if type(SSStype) is str :
    #         SSS = None
    #         for SSS in self.SSSfiles :
    #             if _extension(SSS)[1].upper().endswith( SSStype.upper() ) :
    #                 break
    #         if SSS is None :
    #             print('SSS type ' + SSStype + ' not found')
    #             return None

    #     SSS = _extension(SSS)[1] + _extension(SSS)[0]
    #     Key = Key.strip()
    #     if type(Key) is str :
    #         if Key in self.results[SSS][1]['Data'] :
    #             return self.results[SSS][1]['Data'][Key]
    #         else :
    #             print("Key '" + Key + "' not found in SSS " + SSStype )
    #             return None

    # def get_VIPkeys(self, SSStype=None) :
    #     """
    #     returns a dictinary with the SSStype as keys and the kewords found in each SSS file.
    #     """

    #     if type(SSStype) is str :
    #         SSStype = SSStype.strip()
    #         SSS = None
    #         for Sfile in self.SSSfiles :
    #             if _extension(Sfile)[1].upper().endswith( SSStype.upper() ) :
    #                 SSS = Sfile
    #                 break
    #         if SSS is None :
    #             print('SSS type ' + SSStype + ' not found')
    #             return {}
    #         else :
    #             SSS = [ _extension(SSS)[1] + _extension(SSS)[0] ]
    #     elif SSStype is None :
    #         SSS = []
    #         for Sfile in self.SSSfiles :
    #             SSS += [ _extension(Sfile)[1] + _extension(Sfile)[0] ]
    #     elif type(SSStype) is list or type(SSStype) is tuple :
    #         SSS = []
    #         for Stype in SSStype :
    #             for Sfile in self.SSSfiles :
    #                 if _extension(Sfile)[1].upper().endswith( Stype.upper() ) :
    #                     SSS += [ _extension(Sfile)[1] + _extension(Sfile)[0] ]
    #         if SSS == [] :
    #             print('SSS type ' + SSStype + ' not found')
    #             return {}

    #     output = {}
    #     for each in SSS :
    #         output[ _extension(each)[1].split('_')[-1].upper() ] = list( self.results[each][1]['Data'].keys() )
    #     return output

    # def SSSkeys_asECL(self) :
    #     """
    #     returns a list of the keys in the SSS file converted to ECL style
    #     """
    #     Kdicts = fromVIPtoECL( self.get_VIPkeys() )
    #     output = []
    #     for S in Kdicts :
    #         output += Kdicts[S]
    #     return output

    # def extract_Region_Numbers(self) :
    #     """
    #     reads the region numbers from the SSS file and creates a dictionary for
    #     regiond names and number.
    #     """
    #     Numbers = self.directSSS('#', 'REGION')
    #     Names = self.directSSS('NAME', 'REGION')
    #     regNum = {}

    #     if len(Names) != len(Numbers) :
    #         print("lenght doesn't match!")
    #     for i in range(len(Names)) :
    #         regNum[Names[i].strip()] = _getnumber(Numbers[i])
    #     return regNum

    # def buldSalinityVectors(self) :
    #     """
    #     creates the ECL style salinity vectors WWIR and WWPR from
    #     the SALINITY vector from VIP and production and injection rates.
    #     """
    #     if self.is_Attribute('WSALINITY') :
    #         if self.is_Attribute('WWIR') :
    #             if self.is_Attribute('WWPR') :
    #                 prod = self[['WWPR']]
    #             elif self.is_Attribute('WOPR') :
    #                 prod = self[['WOPR']]
    #             elif self.is_Attribute('WGPR') :
    #                 prod = self[['WGPR']]
    #             else :
    #                 self['WSIR'] = 'WSALINITY'
    #                 self.set_Unit('WSIT', 'CONCENTRATION')
    #                 return None
    #         inje = self[['WWIR']]
    #         salt = self[['WSALINITY']]

    #         for DF in [salt, prod, inje] :
    #             DF.rename( columns = wellFromAttribute(DF.columns) )

    #         self['WSIR'] = ( salt * inje>0 ), self.get_Unit('WSALINITY')
    #         # self.set_Unit('WSIR', self.get_Unit('WSALINITY') )
    #         self['WSPR'] = ( salt * prod>0 ), self.get_Unit('WSALINITY')
    #         # self.set_Unit('WSPR', self.get_Unit('WSALINITY') )

    # def add_Key(self, Key, SSStype=None) :
    #     if type(Key) == str :
    #         Key = Key.strip()
    #         if self.ECLstyle :
    #             self.keys = tuple( set( list(self.get_Keys()) + [Key] ) )
    #             self.keysECL = tuple( set( list(self.get_Keys()) + [Key] ) )
    #             VIPkey, keyType, keyName = _fromECLtoVIP( Key, self.speak )
    #             self.keysVIP = tuple( set( list(self.get_Keys()) + [ VIPkey +':'+ keyName ] ) )
    #         else :
    #             self.keys = tuple( set( list(self.get_Keys()) [Key] ) )
    #             self.keysVIP = tuple( set( list(self.get_Keys()) + [Key] ) )
    #             ECLkey = fromVIPtoECL(Key, SSStype, self.speak)
    #             self.keysECL = tuple( set( list(self.get_Keys()) + [ECLkey] ) )

    #     else :
    #         raise TypeError('Key must be string')

    # def list_Keys(self, pattern=None, reload=False) :
    #     """
    #     Return a StringList of summary keys matching @pattern.

    #     The matching algorithm is ultimately based on the fnmatch()
    #     function, i.e. normal shell-character syntax is used. With
    #     @pattern == "WWCT:*" you will get a list of watercut keys for
    #     all wells.

    #     If pattern is None you will get all the keys of summary
    #     object.
    #     """
    #     if self.ECLstyle :
    #         self.keys = self.keysECL
    #     else :
    #         self.keys = self.keysVIP

    #     if len(self.keys) == 0 or reload == True :
    #         self.keys = []
    #         self.keys +=  list( self.extract_Keys(pattern) )
    #         for extra in ( 'TIME', 'DATE', 'DATES' ) :
    #             if extra not in self.keys :
    #                 self.keys.append(extra)
    #         self.keys = tuple( self.keys )
    #     if pattern is None :
    #         if self.ECLstyle == True :
    #             return self.keysECL
    #         elif self.VIPstyle == True :
    #             return self.keysVIP
    #         else :
    #             return self.keys
    #     else:
    #         return tuple( self.extract_Keys(pattern) )

    # def extract_Keys(self, pattern=None, SSStoExtract=None) :
    #     # preparing object attribute
    #     keysList = list( self.keys )
    #     keysListVIP = list( self.keysVIP )
    #     keysListECL = list( self.keysECL )

    #     if SSStoExtract is None :
    #         SSStoExtract = list(self.results.keys())
    #     for sss in SSStoExtract :
    #         if self.results[sss][0] in VIPTypesToExtractVectors :
    #             names = list(set( ' '.join( self.results[sss][1]['Data']['NAME'] ).split() ))
    #             atts = list( self.results[sss][1]['Data'].keys() )

    #             for att in atts :
    #                 attECL = fromVIPtoECL( att, self.results[sss][0], self.speak )
    #                 if attECL is None :
    #                     _SimResult.VIPnotECL.append( self.results[sss][0] + ' : ' + att )
    #                     attECL = ''
    #                 for name in names :
    #                     keysListVIP.append( att + ':' + name )
    #                     if self.results[sss][0] == 'FIELD' and attECL != '' :
    #                         keysListECL.append( attECL )
    #                     elif self.results[sss][0] in VIP2ECLtype and attECL != '' :
    #                         keysListECL.append( attECL + ':' + name )

    #     if len(_SimResult.VIPnotECL) > 0 :
    #         _verbose( self.speak, -1, '\nsome VIP attributes was not recognized as ECL style attributes, \nto get a report of these attributes use the method:\n  .report_VIP_AttributesNotTo_ECL() \n')
    #     keysListVIP = list( set( keysListVIP ) )
    #     keysListVIP.sort()
    #     self.keysVIP = tuple( keysListVIP )
    #     keysListECL = list( set( keysListECL ) )
    #     keysListECL.sort()
    #     self.keysECL = tuple( keysListECL )
    #     # preparing list to return
    #     if pattern is not None :
    #         keysList = []
    #         for key in self.keysVIP :
    #             if pattern in key :
    #                 keysList.append(key)
    #         if len(keysList) > 0 :
    #             return tuple(keysList)
    #         keysList = [] # redundante
    #         for key in self.keysECL :
    #             if pattern in key :
    #                 keysList.append(key)
    #         if len(keysList) > 0 :
    #             return tuple(keysList)
    #     else :
    #         if self.ECLstyle == True :
    #             return self.keysECL
    #         elif self.VIPstyle == True :
    #             return self.keysVIP
    #         else :
    #             return self.keys

    # def get_Unit(self, Key='--EveryType--') :
    #     """
    #     returns a string identifiying the unit of the requested Key

    #     Key could be a list containing Key strings, in this case a dictionary
    #     with the requested Keys and units will be returned.
    #     the Key '--EveryType--' will return a dictionary Keys and units
    #     for all the keys in the results file

    #     """
    #     if type(Key) is str and Key.strip() != '--EveryType--' :
    #         Key = Key.strip().upper()
    #         if Key in self.units :
    #             if self.units[Key] is not None:
    #                 return self.units[Key]
    #             else : # if self.units[Key] is None:
    #                 if ':' in Key :
    #                     if mainKey(Key) in self.units :
    #                         if self.units[ mainKey(Key) ] is not None :
    #                             return self.units[ mainKey(Key) ]
    #                         else :
    #                             return self.extract_Unit(Key)
    #         if Key == 'DATES' or Key == 'DATE' :
    #                 self.units[Key] = 'DATE'
    #                 return 'DATE'
    #         if Key in self.keys :
    #             return self.extract_Unit(Key)
    #         else:
    #             if Key[0] == 'W' :
    #                 UList=[]
    #                 for W in self.get_Wells() :
    #                     if Key+':'+W in self.units :
    #                         UList.append(self.units[Key+':'+W])
    #                     elif Key+':'+W in self.keys :
    #                         UList.append( self.extract_Unit(Key+':'+W) )
    #                 if len(set(UList)) == 1 :
    #                     self.units[Key] = UList[0]
    #                     return UList[0]
    #                 else :
    #                     return None
    #             elif Key[0] == 'G' :
    #                 UList=[]
    #                 for G in self.get_Groups() :
    #                     if Key+':'+G in self.units :
    #                         UList.append(self.units[Key+':'+G])
    #                     elif Key+':'+G in self.keys :
    #                         UList.append( self.extract_Unit(Key+':'+G) )
    #                 if len(set(UList)) == 1 :
    #                     self.units[Key] = UList[0]
    #                     return UList[0]
    #                 else :
    #                     return None
    #             elif Key[0] == 'R' :
    #                 UList=[]
    #                 for R in self.get_Regions() :
    #                     if Key+':'+R in self.units :
    #                         UList.append(self.units[Key+':'+R])
    #                     elif Key+':'+R in self.keys :
    #                         UList.append( self.extract_Unit(Key+':'+R) )
    #                 if len(set(UList)) == 1 :
    #                     self.units[Key] = UList[0]
    #                     return UList[0]
    #                 else :
    #                     return None
    #             UList = None

    #     elif type(Key) is str and Key.strip() == '--EveryType--' :
    #         Key = []
    #         KeyDict = {}
    #         for each in self.keys :
    #             if ':' in each :
    #                 Key.append( mainKey(each) )
    #                 KeyDict[ mainKey(each) ] = each
    #             else :
    #                 Key.append(each)
    #         Key = list( set (Key) )
    #         Key.sort()
    #         tempUnits = {}
    #         for each in Key :
    #             if each in self.units :
    #                 tempUnits[each] = self.units[each]
    #             elif each in self.keys and ( each != 'DATES' and each != 'DATE' ) :
    #                 tempUnits[each] = self.extract_Unit(each)
    #             elif each in self.keys and ( each == 'DATES' or each == 'DATE' ) :
    #                 tempUnits[each] = 'DATE'
    #             else :
    #                 if KeyDict[each] in self.units :
    #                     tempUnits[each] = self.units[KeyDict[each]]
    #                 elif KeyDict[each] in self.keys :
    #                     if self.extract_Unit(KeyDict[each]) is None :
    #                         tempUnits[each] = self.extract_Unit(KeyDict[each])
    #                     else :
    #                         tempUnits[each] = self.extract_Unit(KeyDict[each]).strip('( )').strip("'").strip('"')
    #         return tempUnits
    #     elif type(Key) == list or type(Key) == tuple :
    #         tempUnits = {}
    #         for each in Key :
    #             if type(each) == str and each.strip() in self.units :
    #                 tempUnits[each] = self.units[each.strip()]
    #             if type(each) == str and ( each.strip() == 'DATES' or each.strip() == 'DATE' ) :
    #                 tempUnits[each] = 'DATE'
    #             elif type(each) == str and each.strip() in self.keys :
    #                 if self.extract_Unit(each.strip()) is None :
    #                     tempUnits[each] = self.extract_Unit(each.strip())
    #                 else :
    #                     tempUnits[each] = self.extract_Unit(each.strip()).strip('( )').strip("'").strip('"')
    #         return tempUnits

    # def extract_Unit(self, Key, SSStype='FIELD') :
    #     for sss in list(self.results.keys()) :
    #         for Vector in list(self.results[sss][1]['Units'].keys()) :
    #             if Vector == 'DATE' or Vector == 'DATES' :
    #                 self.units[Vector] = 'DATE'
    #             else :
    #                 if self.ECLstyle == True :
    #                     ECLkey = fromVIPtoECL( Vector, self.results[sss][0], self.speak )
    #                     if ECLkey is not None :
    #                         self.units[ ECLkey ] = self.results[sss][1]['Units'][Vector].strip('( )').strip("'").strip('"')
    #                 if self.VIPstyle == True :
    #                     self.units[Vector] = self.results[sss][1]['Units'][Vector].strip('( )').strip("'").strip('"')
    #     Key = Key.strip()
    #     if self.ECLstyle == True :
    #         if Key in self.units :
    #             return self.units[Key]
    #         elif Key in ECL2VIPkey and ECL2VIPkey[Key] in self.units :
    #             return self.units[ _fromECLtoVIP( Key, self.speak ) ]
    #     if self.VIPstyle == True :
    #         if Key.strip() in self.units :
    #             return self.units[Key]
    #         elif Key in VIP2ECLkey and VIP2ECLkey[Key] in self.units :
    #             return self.units[ fromVIPtoECL( Key, SSStype, self.speak ) ]

    # def complete_Units(self) :
    #     for key in list(self.units.keys()) :
    #         if self.units[key] is None :
    #             if ':' in key :
    #                 self.units[key] = self.extract_Unit(key)
    #                 if self.units[key] is None :
    #                     self.units[key] = self.extract_Unit(key[:key.index(':')])
    #                     if self.units[key] is None :
    #                         VIPkey = _fromECLtoVIP( key, self.speak )
    #                         for sss in self.results :
    #                             self.units[key] = self.results[ VIPkey[1] ][1]['Units'][ VIPkey[0] ].strip('( )').strip("'").strip('"')
    #                             if self.units[key] is None :
    #                                 break
    #                 if self.units[key] is None :
    #                     _verbose( self.speak, 3, 'impossible to found unit system for key ' + key )
    #                 else :
    #                     _verbose( self.speak, 1, 'found unit system ' + self.units[key] + ' for key ' + key )
    #             else :
    #                 self.units[key] = self.extract_Unit(key)
    #                 if self.units[key] is None :
    #                     VIPkey = _fromECLtoVIP( key, self.speak )
    #                     for sss in self.results :
    #                         self.units[key] = self.results[ VIPkey[1] ][1]['Units'][ VIPkey[0] ].strip('( )').strip("'").strip('"')
    #                         if self.units[key] is None :
    #                                 break
    #                 if self.units[key] is None :
    #                     _verbose( self.speak, 3, 'impossible to found unit system for key ' + key )
    #                 else :
    #                     _verbose( self.speak, 1, 'found unit system ' + self.units[key] + ' for key ' + key )

    # def OUTPAVG(self, KeyArguments=None, ECLkey=None) :
    #     if ECLkey is not None :
    #         if type(ECLkey) is str :
    #             ECLkey = ECLkey.strip()
    #             if self.is_Key(ECLkey) :
    #                 print(" WARNING: the keyword '" + ECLkey + "' already exists here, do you want to overwrite?" )
    #                 user = ''
    #                 while user.upper() not in ['Y', 'YES', 'N', 'NO', 'NOT', 'SI', 'SÍ', 'OUI'] :
    #                     user = input('please write YES or NO: ')
    #                 if user in ['Y', 'YES', 'SI', 'SÍ', 'OUI'] :
    #                     if ':' in ECLkey :
    #                         if self.is_Key( 'WBP:'+ECLkey.split(':')[1] ) :
    #                             self.set_Vector( Key=ECLkey, VectorData=self('WBP:'+ECLkey.split(':')[1]), Units=self.get_Unit('WBP:'+ECLkey.split(':')[1]), DataType='float', overwrite=True )
    #                         else :
    #                             _verbose( self.speak, -1, " the corresponding well for the key '" + mainKey(ECLkey) + "' does not have WBP here.")
    #                     else :
    #                         _verbose( self.speak, -1, " the well name can not be found in the key '" + ECLkey + "'\n use .set_Vector() method to set an especific key")
    #             elif self.is_Att(ECLkey) :
    #                 print(" WARNING: the attribute '" + ECLkey + "' already exists here, do you want to overwrite this attribute for all the wells?" )
    #                 user = ''
    #                 while user.upper() not in ['Y', 'YES', 'N', 'NO', 'NOT', 'SI', 'SÍ', 'OUI'] :
    #                     user = input('please write YES or NO: ')
    #                 if user in ['Y', 'YES', 'SI', 'SÍ', 'OUI'] :
    #                     for W in self.get_Wells() :
    #                         self.set_Vector( Key=W, VectorData=self('WBP:'+W), Units=self.get_Unit('WBP:'+W), DataType='float', overwrite=True )
    #             else :
    #                 for W in self.get_Wells() :
    #                     self.set_Vector( Key=W, VectorData=self('WBP:'+W), Units=self.get_Unit('WBP:'+W), DataType='float', overwrite=True )
    #     elif KeyArguments is not None :
    #         if type(KeyArguments) is str and len(KeyArguments) > 0 :
    #             KeyArguments = KeyArguments.strip()
    #             if len(KeyArguments).split() == 1 :
    #                 if KeyArguments.upper() != 'WELL' and KeyArguments[0] == 'W' :
    #                     _verbose( self.speak, 2, " the KeyArguments '" + KeyArguments + "' seems to be a ECL style keyword...")
    #                     self.OUTPAVG(ECLkey=KeyArguments)
    #             else :
    #                 KeyArguments = KeyArguments.split()
    #                 WPAVE = ['WPAVE', '1st', '2nd', '3rd', '4th']

    #                 if KeyArguments[0].upper() == 'OUTPAVG' :
    #                     _verbose( self.speak, 1, " VIP CARD '" + KeyArguments.pop(0) + "' found")

    #                 if KeyArguments[0].upper() == 'STD' :
    #                     # Alpha label indicating that the mobility-weighted datum pressure average is to be computed. This is the default.
    #                     _verbose( self.speak, 3, " IMPORTANT: in VIP the mobility-weighted datum pressure average was computed, the most similar behaviour in eclipse could be to set " + WPAVE[2] + " item of keyword '" + WPAVE[0] + "' to 1.0 (purely connection factor weighted).")
    #                 elif KeyArguments[0].upper() == 'WELL' :
    #                     # Alpha label indicating that a pattern is being assigned to each well in the well list.
    #                     WellList = KeyArguments[-2]
    #                     WPAVE = ['WWPAVE', '2nd', '3rd', '4th', '5th']
    #                     _verbose( self.speak, 3, " IMPORTANT: notice that 'WWPAVE' should be used in eclipse, not 'WPAVE', in order to be compilant with the well list: " + WellList )
    #                 elif KeyArguments[0].upper() == 'PATTERN' :
    #                     # Alpha label indicating one of the possible patterns is to be used to compute the well average pressure.
    #                     if KeyArguments[-1].isdecimal() :
    #                         if int(KeyArguments[-1]) == 1 :
    #                             # Square pattern of size 1 gridblock by 1 gridblock
    #                             WBPkey = 'WBP'
    #                             _verbose( self.speak, 3, " IMPORTANT: be sure that the " + WPAVE[1] + " item of keyword '" + WPAVE[0] + "' is set to a negative value, like '-1', in your eclipse simulation.")
    #                         elif int(KeyArguments[-1]) == 2 :
    #                             # 5-spot pattern
    #                             WBPkey = 'WBP5'
    #                             _verbose( self.speak, 3, " IMPORTANT: be sure that the " + WPAVE[1] + " item of keyword '" + WPAVE[0] + "' is set to a negative value, like '-1', in your eclipse simulation.")
    #                         elif int(KeyArguments[-1]) == 3 :
    #                             # Square pattern of size 3 gridblocks by 3 gridblocks
    #                             WBPkey = 'WBP9'
    #                             _verbose( self.speak, 3, " IMPORTANT: be sure that the " + WPAVE[1] + " item of keyword '" + WPAVE[0] + "' is set to a negative value, like '-1', in your eclipse simulation.")
    #                         elif int(KeyArguments[-1]) in [ 5, 7, 9 ] :
    #                             # Square pattern of size N gridblocks by N gridblocks
    #                             WBPkey = 'WBP'+ KeyArguments[-1] + 'x' + KeyArguments[-1]
    #                             _verbose(self.speak, -1, " there is not eclipse keyword that matched this VIP configuration, \n this VIP average pressure will be loaded as '" + WBPkey + "'")
    #                         elif int(KeyArguments[-1]) == 0 :
    #                             # Exclude this layer from the calculation.
    #                             WBPkey = 'WBP0'
    #                             _verbose( self.speak, 3, " IMPORTANT: this layer has been excluded from the average pressure calculation")

    #                 elif KeyArguments[0].upper() == 'ACTIVE' :
    #                     # Alpha label indicating that only active perforations are used in the calculation. This is the default.
    #                     _verbose( self.speak, 3, " IMPORTANT: be sure that the " + WPAVE[4] + " item of keyword '" + WPAVE[0] + "' is set to 'OPEN' in your eclipse simulation.")
    #                 elif KeyArguments[0].upper() == 'ALL' :
    #                     # Alpha label indicating that all perforations, including inactive or shut-in perforations, are used in the calculation.
    #                     _verbose( self.speak, 3, " IMPORTANT: be sure that the " + WPAVE[4] + " item of keyword '" + WPAVE[0] + "' is set to 'ALL' in your eclipse simulation.")
    #                 elif KeyArguments[0].upper() == 'DATUM' :
    #                     # Alpha label indicating that the well average datum pressure is to be computed. This is the default for a pattern calculation.
    #                     _verbose( self.speak, 3, " IMPORTANT: be sure that the " + WPAVE[3] + " item of keyword '" + WPAVE[0] + "' is set to 'WELL' in your eclipse simulation.")
    #                 elif KeyArguments[0].upper() == 'GRIDBLOCK' :
    #                     # Alpha label indicating that the well average gridblock pressure is to be computed.
    #                     _verbose( self.speak, 3, " IMPORTANT: be sure that the " + WPAVE[3] + " item of keyword '" + WPAVE[0] + "' is set to 'NONE' in your eclipse simulation.")

    #     if WPAVE == "WPAVE" :
    #         return self.OUTPAVG(ECLkey=WBPkey)
    #     if WPAVE == "WWPAVE" :
    #         for W in self.get_Wells( WellList ) :
    #             self.OUTPAVG(ECLkey=WBPkey+':'+W)
    #         return None

    # def get_TotalReservoirVolumes(self) :

    #     for IP in ['I', 'P'] :
    #         for TR in ['R', 'T'] :
    #             # for FIELD
    #             for OGW in ['O', 'G', 'W'] :
    #                 rv = []
    #                 key = 'FV'+IP+TR+OGW
    #                 if self.is_Key( key ) :
    #                     rv.append( key )

    #             key = 'FV'+IP+TR
    #             if len(rv) > 0 :
    #                 _verbose( self.speak, 1, 'adding up reservoir volumes for ' + key )

    #             if len(rv) == 1 :
    #                 self[key] = self(rv[0]), self.get_Units(rv[0])
    #             elif len(rv) == 2 :
    #                 self[key] = self(rv[0]) + self(rv[1]), self.get_Units(rv[0])
    #             elif len(rv) == 3 :
    #                 self[key] = self(rv[0]) + self(rv[1]) + self(rv[2]), self.get_Units(rv[0])

    #             # for WELL, GROUP, REGION
    #             for T in ['W', 'G', 'R'] :
    #                 for OGW in ['O', 'G', 'W'] :
    #                     rv = []
    #                     key = T+'V'+IP+TR+OGW
    #                     if self.is_Attribute( key ) :
    #                         rv.append( key )

    #                 key = T+'V'+IP+TR
    #                 if len(rv) > 0 :
    #                     _verbose( self.speak, 1, 'adding up reservoir volumes for ' + key )

    #                 if len(rv) == 1 :
    #                     df = self[[rv[0]]]
    #                     df.rename( columns=wellFromAttribute(df.columns), inplace=True )
    #                     self[key] = df, self.get_Units(rv[0])
    #                 elif len(rv) == 2 :
    #                     df0 = self[[rv[0]]]
    #                     df0.rename( columns=wellFromAttribute(df0.columns), inplace=True )
    #                     df1 = self[[rv[1]]]
    #                     df1.rename( columns=wellFromAttribute(df1.columns), inplace=True )
    #                     self[key] = df0 + df1, self.get_Units(rv[0])
    #                 elif len(rv) == 3 :
    #                     df0 = self[[rv[0]]]
    #                     df0.rename( columns=wellFromAttribute(df0.columns), inplace=True )
    #                     df1 = self[[rv[1]]]
    #                     df1.rename( columns=wellFromAttribute(df1.columns), inplace=True )
    #                     df2 = self[[rv[2]]]
    #                     df2.rename( columns=wellFromAttribute(df2.columns), inplace=True )
    #                     self[key] = df0 + df1 + df2, self.get_Units(rv[0])

    def prepareWellData(self) :
        prevSpeak = self.speak
        if self.speak != 1 :
            self.speak = 0
        for W in self.wells :
            self('WGOR:'+W)
            self('WWCT:'+W)
            for F in ['O', 'G', 'W'] :
                for S in ['I', 'P'] :
                    for C in ['R', 'T'] :
                        self('W'+F+S+C+':'+W)
        self.speak = prevSpeak
