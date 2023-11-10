#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:14:32 2020

@author: Martin Carlos Araya
"""

__version__ = '0.80.16'
__release__ = 20230619
__all__ = ['SimSeries', 'SimDataFrame', 'read_excel', 'concat', 'znorm', 'minmaxnorm']

from sys import getsizeof
from io import StringIO
from shutil import get_terminal_size
from pandas._config import get_option
from pandas.io.formats import console
from pandas.core import indexing
from os.path import commonprefix
import pandas as pd
import fnmatch
import warnings
from pandas import Series, DataFrame, DatetimeIndex, Timestamp, Index
# from pandas.core.groupby.generic import DataFrameGroupBy
# from pandas.core.window.rolling import Rolling
import numpy as np
import datetime as dt
from warnings import warn
import matplotlib.pyplot as plt
from .._common.units import unit  # to use unit.isUnit method
from .._common.units import convertUnit, unitProduct, unitDivision, convertible as convertibleUnits, unitBase
from .._common.slope import slope as _slope


try:
    from datafiletoolbox import multisplit, isDate, strDate
except:
    try:
        from .._common.stringformat import multisplit, isDate, date as strDate
    except:
        raise ImportError("please install 'datafiletoolbox'.")

_SERIES_WARNING_MSG = """\
    You are passing unitless data to the SimSeries constructor. Currently,
    it falls back to returning a pandas Series. But in the future, we will start
    to raise a TypeError instead."""


def concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True, squeeze=True):
    """
    wrapper of pandas.concat enhaced with units support

    Return:
        SimDataFrame
    """
    if type(objs) is not list:
        raise TypeError("objs must be a list of DataFrames or SimDataFrames")
    if len(objs) == 1:
        print("WARNING: only 1 DataFrame received.")
        return [objs][0]

    merged_units = merge_units([ob for ob in objs if type(ob) in (SimDataFrame,SimSeries)])
    merged_SimParameters = merge_SimParameters([ob for ob in objs if type(ob) in (SimDataFrame,SimSeries)])

    dfobjs = [ (ob.to(merged_units).as_Pandas() if type(ob) in (SimSeries, SimDataFrame) else ob) for ob in objs ]

    if 'units' in merged_SimParameters:
        del merged_SimParameters['units']

    df = pd.concat(dfobjs, axis=axis, join=join, ignore_index=ignore_index, keys=keys, levels=levels, names=names, verify_integrity=verify_integrity, sort=sort, copy=copy)
    sdf = SimDataFrame(data=df , units=merged_units, **merged_SimParameters )

    if squeeze:
        return sdf.squeeze()
    else:
        return sdf


def read_excel(io, sheet_name=None, header=0, names=None, index_col=None, usecols=None, squeeze=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, decimal='.', comment=None, skipfooter=0, convert_float=None, mangle_dupe_cols=True, storage_options=None,
units=1, speak=False, indexName=None, indexUnits=None, nameSeparator=None, intersectionCharacter='∩', autoAppend=False, transposed=False, operatePerName=False, *args, **kwargs):
    """
    wrapper of pandas.read_excel enhanced with units support

    Return:
        SimDataFrame
    """
    import pandas

    dateunits = ['date']  #,'fecha']
    speak = bool(speak)

    if type(units) is int:
        if units < 0:
            raise ValueError("'units' parameter must be positive")
        if type(header) is int:
            if header == units:
                if speak:
                    print(" > same row will be used as header and as units.")
            else:
                header = [header, units]
        elif type(header) is list:
            if len(header) == 1 and units in header:
                if speak:
                    print(" > same row will be used as header and as units.")
                header = header[0]
            else:
                header += [units]

    excelread = pandas.read_excel(io, sheet_name=sheet_name, header=header, names=names, index_col=index_col, usecols=usecols, dtype=dtype, engine=engine, converters=converters, true_values=true_values, false_values=false_values, skiprows=skiprows, nrows=nrows, na_values=na_values, keep_default_na=keep_default_na, na_filter=na_filter, verbose=verbose, parse_dates=parse_dates, date_parser=date_parser, thousands=thousands, comment=comment, skipfooter=skipfooter, mangle_dupe_cols=mangle_dupe_cols, storage_options=storage_options)  # convert_float=convert_float, decimal=decimal

    if type(excelread) is not dict:
        excelread = {'onesheet':excelread}

    output = {}
    for name, df in excelread.items():

        if type(units) is list:
            if len(units) == len(df.columns):
                dataunits = {df.columns[i]:units[i] for i in len(units)}
            else:
                raise ValueError("if 'units' is a list, it must be same length as the columns of the dataframe")
        elif type(units) is str:
            dataunits = units
        elif type(units) is int:
            if type(header) is list:
                if len(header) == 2:
                    # dataunits = {}
                    # newcols = []
                    # for col in df.columns:
                    #     if str(col[-1]).startswith('Unnamed:'):
                    #         nc = str(col[0]).strip()
                    #         dataunits[nc] = 'unitless'
                    #         newcols.append(nc)
                    #     else:
                    #         nc = str(col[0]).strip()
                    #         dataunits[nc] = str(col[-1]).strip()
                    #         newcols.append(nc)
                    dataunits = {str(col[0]).strip(): 'unitless' if str(col[-1]).startswith('Unnamed:') else str(col[-1]).strip() for col in df.columns}
                    newcols = list(dataunits.keys())
                elif len(header) > 2:
                    # dataunits = {}
                    # newcols = []
                    # for col in df.columns:
                    #     if str(col[-1]).startswith('Unnamed:'):
                    #         nc = col[:-1]
                    #         dataunits[nc] = 'unitless'
                    #         newcols.append(nc)
                    #     else:
                    #         nc = col[:-1]
                    #         dataunits[nc] = str(col[-1]).strip()
                    #         newcols.append(nc)
                    dataunits = {col[:-1]: 'unitless' if str(col[-1]).startswith('Unnamed:') else str(col[-1]).strip() for col in df.columns}
                    newcols = pandas.MultiIndex.from_tuples(list(dataunits.keys()))
                df.columns = newcols
            elif type(header) is int:
                dataunits = {c:str(c) for c in df.columns}

        elif units is None:
            dataunits = None
        else:
            dataunits = units

        if isinstance(df,pandas.DataFrame):
            for colN in range(len(df.columns)):
                if str(df.iloc[:,colN].dtype).startswith('date'):
                    col = df.columns[colN]
                    if type(dataunits) is not dict:
                        dataunits = {c:dataunits for c in df.columns}
                    if col in dataunits:
                        if str(dataunits[col]).lower().strip() not in dateunits:
                            dataunits[col] = 'date'
                    else:
                        dataunits[col] = 'date'
        elif isinstance(df,pandas.Series):
            if str(df.dtype).startswith('date'):
                if df.name is not None:
                    dataunits = {df.name:'date'}
        if str(df.index.dtype).startswith('date'):
            if str(indexUnits).lowrt().strip() not in dateunits:
                indexUnits = 'date'

        output[name] = SimDataFrame(data=df, units=dataunits, speak=speak, indexName=indexName, indexUnits=indexUnits, nameSeparator=nameSeparator, intersectionCharacter=intersectionCharacter, autoAppend=autoAppend, transposed=transposed, operatePerName=operatePerName, *args, **kwargs)

        if bool(squeeze):
            output[name] = output[name].squeeze('columns')

    if len(output) == 1:
        return output[name]
    else:
        return output


def _simseries_constructor_with_fallback(data=None, index=None, units=None, **kwargs):
    """
    A flexible constructor for SimSeries._constructor, which needs to be able
    to fall back to a Series(if a certain operation does not produce
    units)
    """
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message=_SERIES_WARNING_MSG,
                category=FutureWarning,
                module="SimPandas[.*]",
            )
            return SimSeries(data=data, index=index, units=units, **kwargs)
    except TypeError:
        return Series(data=data, index=index, **kwargs)


def _Series2Frame(aSimSeries):
    """
    when a row is extracted from a DataFrame, Pandas returns a Series in wich
    the columns of the DataFrame are converted to the indexes of the Series and
    the extracted index from the DataFrame is set as the Name of the Series.

    This function returns the proper DataFrame view of such Series.

    Works with SimSeries as well as with Pandas standard Series
    """
    if isinstance(aSimSeries, DataFrame):
        return aSimSeries
    if type(aSimSeries) is SimSeries:
        try:
            return SimDataFrame(data=dict(zip(list(aSimSeries.index), aSimSeries.to_list())), units=aSimSeries.get_Units(), index=aSimSeries.columns, speak=aSimSeries.speak, indexName=aSimSeries.index.name, indexUnits=aSimSeries.indexUnits, nameSeparator=aSimSeries.nameSeparator, intersectionCharacter=aSimSeries.intersectionCharacter, autoAppend=aSimSeries.autoAppend, operatePerName=aSimSeries.operatePerName)
        except:
            return aSimSeries
    if type(aSimSeries) is Series:
        try:
            return DataFrame(data=dict(zip(list(aSimSeries.index), aSimSeries.to_list())), index=aSimSeries.columns)
        except:
            return aSimSeries

def _cleanAxis(axis=None):
    if axis is None:
        return 0
    if type(axis) is str and axis.lower() in ['row', 'rows', 'ind', 'index']:
        return 0
    if type(axis) is str and axis.lower() in ['col', 'cols', 'column', 'columns']:
        return 1
    if type(axis) is bool:
        return int(axis)
    if type(axis) is float:
        return int(axis)
    return axis

def jitter(df,std=0.10):
    import numpy as np
    jit = np.random.randn(len(df),len(df.columns))
    jit = ( jit * std ) + 1
    return df*jit

def _stringNewName(newName):
    if len(newName) == 1:
        return list(newName.values())[0]
    else:
        return '∩'.join(map(str,set(newName.values())))

def typeOfFrame(frame):
    try:
        if frame._isSimSeries:
            return SimSeries
    except:
        try:
            if frame._isSimDataFrame:
                return SimDataFrame
        except:
            if type(frame) is Series:
                return Series
            elif type(frame) is DataFrame:
                return DataFrame
            else:
                raise TypeError('frame is not an instance of Pandas or SimPandas Frames')


class _SimLocIndexer(indexing._LocIndexer):
    def __init__(self, *args):
        self.spd = args[1]
        super().__init__(*args)

    def __getitem__(self, *args):
        result = super().__getitem__(*args)
        if isinstance(result,(Series,DataFrame)):
            if type(self.spd) is SimSeries:
                return self.spd._class(data=result, **self.spd._SimParameters)

            elif type(self.spd) is SimDataFrame and type(*args) is not tuple and isinstance(result,Series):
                return self.spd._class(data=dict(zip(result.index,result.values)),index=[result.name], **self.spd._SimParameters)
            elif type(self.spd) is SimDataFrame and type(*args) is not tuple and isinstance(result,DataFrame):
                return self.spd._class(data=result, **self.spd._SimParameters)
            elif type(self.spd) is SimDataFrame and type(*args) is tuple and len(*args) > 1 and type(args[0][-1]) in (list,tuple,slice) and isinstance(result,DataFrame):
                return self.spd._class(data=result, **self.spd._SimParameters)
            else:
                result = self.spd._class(data=result.values,index=result.index, **self.spd._SimParameters)
                result.rename(columns=dict(zip(result.columns,self.spd[[args[0][-1]]].columns)),inplace=True)
                result.set_units(self.spd.get_units(self.spd[[args[0][-1]]].columns))
                return result
        else:
            return result

    def __setitem__(self, key, value):  #, units=None):
        if type(value) in (SimSeries,SimDataFrame):
            value = value.to(self.spd.get_Units())
        if type(value) is SimDataFrame and len(value.index) == 1:
            value = value.to_SimSeries()

        # check if received value is tuple (value,units)
        newUnits = False
        if type(value) is tuple and len(value) == 2:
            if key[1] not in self.spd.columns or not isinstance(self.spd.loc[key],(Series,SimSeries,DataFrame,SimDataFrame)) or (
                    isinstance(self.spd.loc[key],(Series,SimSeries,DataFrame,SimDataFrame)) and type(value[0]) is not str and hasattr(value[0],'__iter__') and len(self.spd.loc[key]) == len(value[0])):
                value, units = value[0], value[1]
                if key[1] not in self.spd.columns or self.spd.get_Units(key[1])[key[1]] is None or self.spd.get_Units(
                        key[1])[key[1]].lower() in ('dimensionless', 'unitless', 'none', ''):
                    newUnits = True
                else:
                    if units == self.spd.get_Units(key[1])[key[1]]:
                        pass
                    elif convertibleUnits(units, self.spd.get_Units(key[1])[key[1]]):
                        value = convertUnit(value, units, self.spd.get_Units(key[1])[key[1]], self.spd.speak)
                    else:
                        warn(' Not able to convert ' + str(units) + ' to ' + str(self.spd.get_Units(key[1])[key[1]]))
        super().__setitem__(key, value)
        if newUnits:
            self.spd.set_Units({key[1]: units})


# class _iSimLocIndexer(indexing._iLocIndexer):
#     def __init__(self, *args):
#         self.spd = args[1]
#         super().__init__(*args)

#     def __getitem__(self, *args):
#         result = super().__getitem__(*args)
#         if isinstance(result,(Series,DataFrame)):
#             if type(self.spd) is SimSeries:
#                 return self.spd._class(data=result, **self.spd._SimParameters)

#             elif type(self.spd) is SimDataFrame and type(*args) is not tuple and isinstance(result,Series):
#                 return self.spd._class(data=dict(zip(result.index,result.values)),index=[result.name], **self.spd._SimParameters)
#             elif type(self.spd) is SimDataFrame and type(*args) is not tuple and isinstance(result,DataFrame):
#                 return self.spd._class(data=result, **self.spd._SimParameters)
#             elif type(self.spd) is SimDataFrame and type(*args) is tuple and len(*args) > 1 and type(args[0][-1]) in (list,tuple,slice) and isinstance(result,DataFrame):
#                 return self.spd._class(data=result, **self.spd._SimParameters)
#             else:
#                 result = self.spd._class(data=result.values,index=result.index, **self.spd._SimParameters)
#                 result.rename(columns=dict(zip(result.columns,self.spd[[args[0][-1]]].columns)),inplace=True)
#                 result.set_units(self.spd.get_units(self.spd[[args[0][-1]]].columns))
#                 return result
#         else:
#             return result

#     def __setitem__(self, key, value):  #, units=None):
#         if type(value) in (SimSeries,SimDataFrame):
#             value = value.to(self.spd.get_Units())
#         if type(value) is SimDataFrame and len(value.index) == 1:
#             value = value.to_SimSeries()

#         # check if received value is tuple (value,units)
#         if type(value) is tuple and len(value) == 2:
#             if not isinstance(self.spd.loc[key],(Series,SimSeries,DataFrame,SimDataFrame)) or (
#                     isinstance(self.spd.loc[key],(Series,SimSeries,DataFrame,SimDataFrame)) and type(value[0]) is not str and not hasattr(value[0],'__iter__') and len(self.spd.loc[key]) == len(value[0])):
#                 value, units = value[0], value[1]
#                 if key[1] not in self.spd.columns or self.spd.get_Units(key[1])[key[1]] is None or self.spd.get_Units(key[1])[key[1]].lower() in ('dimensionless', 'unitless', 'none', ''):
#                     newUnits = True
#                 else:
#                     newUnits = False
#                     if convertibleUnits(units, self.spd.get_Units(key[1])):
#                         value = convertUnits(value,units,self.spd.get_Units(key[1]))
#         super().__setitem__(key, value)
#         if newUnits:
#             self.spd.set_Units({key[1]:units})


# class SimRolling(Rolling):
#     def __init__(self, df, window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None, method='single', SimParameters=None):
#         super().__init__(window, min_periods=min_periods, center=center, win_type=win_type, on=on, axis=axis, closed=closed, method=method)
#         self.params =  SimParameters

#     def _resolve_output(self, out: DataFrame, obj: DataFrame) -> DataFrame:
#         from pandas.core.base import DataError
#         """Validate and finalize result."""
#         if out.shape[1] == 0 and obj.shape[1] > 0:
#             raise DataError("No numeric types to aggregate")
#         elif out.shape[1] == 0:
#             return obj.astype("float64")

#         self._insert_on_column(out, obj)
#         if self.params is not None:
#             out =  SimDataFrame(out, **self.params)
#         return out


class SimSeries(Series):
    """
    A Series object designed to store data with units.

    Parameters
    ----------
    data : array-like, dict, scalar value
        The data to store in the SimSeries.
    index : array-like or Index
        The index for the SimSeries.
    units : string or dictionary of units(optional)
        Can be any string, but only units acepted by the UnitConverter will
        be considered when doing arithmetic calculations with other SimSeries
        or SimDataFrames.

    kwargs
        Additional arguments passed to the Series constructor,
         e.g. ``name``.

    See Also
    --------
    SimDataFrame
    pandas.Series

    """
    _metadata = ["units", "speak", 'indexUnits', 'nameSeparator', 'intersectionCharacter', 'autoAppend', 'spdLocator', 'operatePerName']  #, 'spdiLocator']

    def __init__(self, data=None, units=None, index=None, name=None, speak=False, indexName=None, indexUnits=None, nameSeparator=None, intersectionCharacter='∩' , autoAppend=False, operatePerName=False, *args, **kwargs):
        Uname = None
        Udict = None
        self.units = None
        self.speak = bool(speak)
        self.indexUnits = None
        self.nameSeparator = None
        self.intersectionCharacter = '∩'
        self.autoAppend = False
        self.operatePerName = False
        self.spdLocator = _SimLocIndexer("loc", self)
        # self.spdiLocator = _iSimLocIndexer("iloc", self)

        # validaton
        if isinstance(data, DataFrame) and len(data.columns)>1:
            raise ValueError("'data' paramanter can be an instance of DataFrame but must have only one column.")

        indexInput = None
        # catch index keyword from input parameters
        if index is not None:
            indexInput = index
        elif 'index' in kwargs and kwargs['index'] is not None:
            indexInput = kwargs['index']
        elif len(args) >= 3 and args[2] is not None:
            indexInput = args[2]
        # if index is a Series, get the name
        elif isinstance(indexInput, Series):
            if type(indexInput.name) is str:
                indexInput = indexInput.name
        # if index is None and data is SimSeries or SimDataFrame get the name
        elif type(data) in [SimSeries, SimDataFrame] and type(data.index.name) is str and len(data.index.name)>0:
            indexInput = data.index.name
            self.indexUnits = data.indexUnits.copy() if type(data.indexUnits) is dict else data.indexUnits

        # catch units or get from data if it is SimDataFrame or SimSeries
        if type(units) is dict and len(units) > 0:
            Udict, units = units, None
            if len(Udict) == 1:
                if type(Udict[ list(Udict.keys())[0] ] ) is str:
                    Uname = list(Udict.keys())[0]
                    units = Udict[ Uname ]
        elif type(units) is str:
            self.units = units
        elif (units is None or (type(units) is dict and len(units) > 0)) and (type(data) is SimSeries and data.units is not None):
            if type(data.units) is str:
                units = data.units
                if indexUnits is None:
                    indexUnits = data.indexUnits
                    self.indexUnits = indexUnits
            elif type(data.units) is dict:
                units = data.units.copy()
                if data.index.name not in units:
                        units[data.index.name] = data.indexUnits
        else:
            self.units = 'UNITLESS'


        # remove arguments not known by Pandas
        kwargsB = kwargs.copy()
        if name is not None and 'name' in kwargs:
            kwargs.pop('name',None)
        kwargs.pop('columns',None)
        kwargs.pop('indexName', None)
        kwargs.pop('indexUnits', None)
        kwargs.pop('nameSeparator', None)
        kwargs.pop('autoAppend', None)
        kwargs.pop('operatePerName',None)
        kwargs.pop('transposed',None)
        # convert to pure Pandas
        if type(data) in [ SimDataFrame, SimSeries ]:
            self.nameSeparator = data.nameSeparator
            data = data.to_Pandas()
        super().__init__(data=data, index=index, *args, **kwargs)

        # set the name of the index
        if (self.index.name is None or(type(self.index.name) is str and len(self.index.name)==0 ) ) and (type(indexInput) is str and len(indexInput)>0 ):
            self.index.name = indexInput
        # overwrite the index.name with input from the argument indexName
        if indexName is not None and type(indexName) is str and len(indexName.strip())>0:
            self.set_indexName(indexName)
        elif 'indexName' in kwargsB and type(kwargsB['indexName']) is str and len(kwargsB['indexName'].strip())>0:
            self.set_indexName(kwargsB['indexName'])

        # set the name
        if self.name is None and Uname is not None:
            self.name = Uname
        # set the units
        if self.name is not None and self.units is None and Udict is not None:
            if self.name in Udict:
                self.units = Udict[ self.name ]
            else:
                for each in self.index:
                    if each in Udict:
                        if type(self.units) is dict:
                            self.units[each] = Udict[each]
                        else:
                            self.units = { each:Udict[each] }
                    else:
                        if type(self.units) is dict:
                            self.units[each] = 'UNITLESS'
                        else:
                            self.units = { each:'UNITLESS' }
        if Udict is not None and self.index.name is not None and self.index.name in Udict:
            self.indexUnits = Udict[self.index.name]
        # overwrite the indexUnits with input from the argument indexName
        if indexUnits is not None and type(indexUnits) is str and len(indexUnits.strip())>0:
            self.indexUnits = indexUnits
        if 'indexUnits' in kwargsB and type(kwargsB['indexUnits']) is str and len(kwargsB['indexUnits'].strip())>0:
            self.indexUnits = kwargsB['indexUnits']
        elif 'indexUnits' in kwargsB and type(kwargsB['indexUnits']) is dict and len(kwargsB['indexUnits'])>0:
            self.indexUnits = kwargsB['indexUnits'].copy()
        if self.indexUnits is not None and self.index.name is not None and len(self.index.name) > 0 and type(self.units) is dict and self.index.name not in self.units:
            self.units[self.index.name] = self.indexUnits

        # get separator for the column names, 'partA'+'separator'+'partB'
        if nameSeparator is not None and type(nameSeparator) is str and len(nameSeparator.strip())>0:
            self.nameSeparator = nameSeparator
        elif 'nameSeparator' in kwargsB and type(kwargsB['nameSeparator']) is str and len(kwargsB['nameSeparator'].strip())>0:
            self.set_NameSeparator(kwargsB['nameSeparator'])
        elif (self.nameSeparator is None or self.nameSeparator == '' or self.nameSeparator is False ) and (type(self.name) is str and ':' in self.name ):
            self.nameSeparator = ':'
        elif self.nameSeparator is None or self.nameSeparator == '' or self.nameSeparator is False:
            self.nameSeparator = ''
        elif self.nameSeparator is True:
            self.nameSeparator = ':'
        else:
            self.nameSeparator = ':'

        if intersectionCharacter is not None and type(intersectionCharacter) is str:
            self.intersectionCharacter = intersectionCharacter

        # catch autoAppend from kwargs
        if autoAppend is not None:
            self.autoAppend = bool(autoAppend)
        elif 'autoAppend' in kwargsB and kwargsB['autoAppend'] is not None:
            self.autoAppend = bool(kwargs['autoAppend'] )

        # catch operatePerName from kwargs
        if operatePerName is not None:
            self.operatePerName = bool(operatePerName)
        elif 'operatePerName' in kwargsB and kwargsB['operatePerName'] is not None:
            self.operatePerName = bool(kwargs['operatePerName'] )

        # set the provided name
        #if self.name is None and name is not None:
        if name is not None:
            self.name = name
        if self.name is None and 'columns' in kwargsB and type(kwargsB['columns']) is not str and hasattr(kwargsB['columns'],'__iter__') and type(kwargsB['columns']) is not dict and len(kwargsB['columns']) == 1:
            self.name = kwargsB['columns'][0]
        if self.name is None and 'columns' in kwargsB and type(kwargsB['columns']) is str and len(kwargsB['columns'].strip()) > 0:
            self.name = kwargsB['columns'].strip()

    @property
    def _constructor(self):
        return _simseries_constructor_with_fallback
    @property
    def _constructor_expanddim(self):
        # from datafiletoolbox.SimPandas.simframe import SimDataFrame
        return SimDataFrame

    @property
    def _SimParameters(self):
        return {'units':self.units.copy() if type(self.units) is dict else self.units,
                'name':self.name,
                'speak':self.speak if hasattr(self,'speak') else False,
                'indexName':self.index.name,
                'indexUnits':self.indexUnits if hasattr(self,'indexUnits') else None,
                'nameSeparator':self.nameSeparator if hasattr(self,'nameSeparator') else None,
                'intersectionCharacter':self.intersectionCharacter if hasattr(self,'intersectionCharacter') else '∩',
                'autoAppend':self.autoAppend if hasattr(self,'autoAppend') else False,
                'operatePerName':self.operatePerName if hasattr(self,'operatedPerName') else False,
                }

    @property
    def loc(self) -> _SimLocIndexer:
        """
        wrapper for .loc indexing
        """
        return self.spdLocator

    # @property
    # def iloc(self) -> _iSimLocIndexer:
    #     """
    #     wrapper for .iloc indexing
    #     """
    #     return self.spdiLocator

    @property
    def _class(self):
        return SimSeries

    def __getitem__(self, key=None):
        if key is None:
            return self
        if type(key) is str and key.strip() == self.name and not key.strip() in self.index:
            return self
        else:
            try:
                return self.loc[key]
            except:
                try:
                    return self.iloc[key]
                except:
                    raise KeyError("the requested Key is not a valid index or name: "+str(key))

    def __contains__(self, item):
        if item in self.columns:
            return True
        elif item in self.index:
            return True
        else:
            return False

    def set_index(self, name):
        self.set_indexName(name)

    def describe(self,*args,**kwargs):
        return self._class(data=self.to_Pandas().describe(*args,**kwargs),**self._SimParameters)

    def set_indexName(self, name):
        if type(name) is str and len(name.strip())>0:
            self.index.name = name.strip()

    def set_indexUnits(self, units):
        if type(units) is str and len(units.strip())>0:
            self.indexUnits = units.strip()
        elif type(units) is dict and len(units)>0:
            self.indexUnits = units

    def set_NameSeparator(self, separator):
        if type(separator) is str and len(separator) > 0:
            self.nameSeparator = separator

    def get_NameSeparator(self):
        if self.nameSeparator in [None, '', False]:
            warn(" NameSeparator is not defined.")
            return ''
        else:
            return self.nameSeparator

    def transpose(self):
        return self

    @property
    def T(self):
        return self.transpose()

    def as_Pandas(self):
        return self.to_Series()

    def to_Pandas(self):
        return self.to_Series()

    def to_pandas(self):
        return self.to_Series()

    def to_Series(self):
        return Series(self).copy()

    def as_Series(self):
        return Series(self)

    def to_SimDataFrame(self):
        if type(self.units) is str:
            return SimDataFrame(data=self)
        elif type(self.units) is dict:
            return SimDataFrame(data=self.values.reshape(1,self.values.size), index=[self.name], columns=self.index, **self._SimParameters)

    @property
    def sdf(self):
        return self.to_SimDataFrame()

    @property
    def SDF(self):
        return self.to_SimDataFrame()

    @property
    def df(self):
        return self.to_SimDataFrame().to_DataFrame()

    @property
    def DF(self):
        return self.to_SimDataFrame().to_DataFrame()

    @property
    def Series(self):
        return self.as_Series()

    @property
    def s(self):
        return self.as_Series()

    @property
    def S(self):
        return self.as_Series()

    def squeeze(self,axis=None):
        """
        wrapper of pandas.squeeze

        SimSeries with a single element and no units (or unitless) are squeezed to a scalar.
        SimSeries without units or unitless are squeezed to a Series.

        Parameters
        ----------
        axis : {0 or ‘index’, 1 or ‘columns’, None}, default None
            A specific axis to squeeze. By default, all length-1 axes are squeezed., optional

        Returns
        -------
        SimSeries, Series, or scalar
            The projection after squeezing axis or all the axes. and units

        """
        if len(self) == 1:
            if len(self.get_Units()) == 0 or np.array([(u is None or str(u).lower().strip() in ['unitless','dimensionless']) for u in self.get_Units().values()]).all():
                return self.iloc[0]
        elif len(self.get_Units()) == 0 or np.array([(u is None or str(u).lower().strip() in ['unitless','dimensionless']) for u in self.get_Units().values()]).all():
            return self.as_Series()
        elif type(self.get_Units()) is dict and len(set(self.get_Units(self.index).values())) == 1:
            params = self._SimParameters.copy()
            params['units'] = list(set(self.get_Units(self.index).values()))[0]
            return SimSeries(self.to_Series(), **params)
        else:
            return self

    @property
    def columns(self):
        return Index([self.name] )

    @property
    def right(self):
        if self.nameSeparator is None or self.nameSeparator is False or self.nameSeparator in ['']:
            return tuple(self.columns)
        objs = []
        for each in list(self.columns):
            if each is None:
                objs += [each]
            elif self.nameSeparator in each:
                objs += [each.split(self.nameSeparator)[-1]]
            else:
                objs += [each]
        return tuple(set(objs))

    @property
    def left(self):
        if self.nameSeparator is None or self.nameSeparator is False or self.nameSeparator in ['']:
            return tuple(self.columns)
        objs = []
        for each in list(self.columns):
            if each is None:
                objs += [each]
            elif self.nameSeparator in each:
                objs += [each.split(self.nameSeparator)[0]]
            else:
                objs += [each]
        return tuple(set(objs))

    def to_excel(self, excel_writer, split_by=None, sheet_name=None, na_rep='', float_format=None, columns=None,
                 header=True, units=True, index=True, index_label=None, startrow=0, startcol=0, engine=None,
                 merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, sort=None,
                 format_header=True):
        """
        Wrapper of .to_excel method from Pandas.
        On top of Pandas method this method is able to split the data into different
        sheets based on the column names. See paramenters `split_by´ and `sheet_name´.

        Write {klass} to an Excel sheet.
        To write a single {klass} to an Excel .xlsx file it is only necessary to
        specify a target file name. To write to multiple sheets it is necessary to
        create an `ExcelWriter` object with a target file name, and specify a sheet
        in the file to write to.
        Multiple sheets may be written to by specifying unique `sheet_name`.
        With all data written to the file it is necessary to save the changes.
        Note that creating an `ExcelWriter` object with a file name that already
        exists will result in the contents of the existing file being erased.

        Parameters
        ----------
        excel_writer : str or ExcelWriter object from Pandas.
            File path or existing ExcelWriter.
        split_by: None, positive or negative integer or str 'left', 'right' or 'first'. Default is None
            If is string 'left' or 'right', creates a sheet grouping the columns by
            the corresponding left:right part of the column name.
            If is string 'first', creates a sheet grouping the columns by
            the first character of the column name.
            If None, all the columns will go into the same sheet.
            if integer i > 0, creates a sheet grouping the columns by the 'i' firsts
            characters of the column name indicated by the integer.
            if integer i < 0, creates a sheet grouping the columns by the 'i' last
            the number characters of the column name indicated by the integer.
        sheet_name : None or str, default None
            Name of sheet which will contain DataFrame.
            If None:
                the `left` or `right` part of the name will be used if is unique,
                or 'FIELD', 'WELLS', 'GROUPS' or 'REGIONS' if all the column names
                start with 'F', 'W', 'G' or 'R'.
            else 'Sheet1' will be used.
        na_rep : str, default ''
            Missing data representation.
        float_format : str, optional
            Format string for floating point numbers. For example
            ``float_format="%.2f"`` will format 0.1234 to 0.12.
        columns : sequence or list of str, optional
            Columns to write.
        header : bool or list of str, default True
            Write out the column names. If a list of string is given it is
            assumed to be aliases for the column names.
        units : bool, default True
            Write the units of the column under the header name.
        index : bool, default True
            Write row names(index).
        index_label : str or sequence, optional
            Column label for index column(s) if desired. If not specified, and
            `header` and `index` are True, then the index names are used. A
            sequence should be given if the DataFrame uses MultiIndex.
        startrow : int, default 0
            Upper left cell row to dump data frame.
        startcol : int, default 0
            Upper left cell column to dump data frame.
        engine : str, optional
            Write engine to use, 'openpyxl' or 'xlsxwriter'. You can also set this
            via the options ``io.excel.xlsx.writer``, ``io.excel.xls.writer``, and
            ``io.excel.xlsm.writer``.
        merge_cells : bool, default True
            Write MultiIndex and Hierarchical Rows as merged cells.
        encoding : str, optional
            Encoding of the resulting excel file. Only necessary for xlwt,
            other writers support unicode natively.
        inf_rep : str, default 'inf'
            Representation for infinity(there is no native representation for
            infinity in Excel).
        verbose : bool, default True
            Display more information in the error logs.
        freeze_panes : tuple of int(length 2), optional
            Specifies the one-based bottommost row and rightmost column that
            is to be frozen.
        sort: None, bool or int
            if None, default behaviour depends on split_by parameter:
                if split_by is None will keep the current order of the columns in the SimDataFrame.
                if split_by is not None will sort alphabetically ascending the names of the columns.
            if True (bool) will sort the columns alphabetically ascending.
            if False (bool) will maintain the current order.
            if int > 0 will sort the columns alphabetically ascending.
            if int < 0 will sort the columns alphabetically descending.
            if int == 0 will keep the current order of the columns.

        """
        return self.to_SimDataFrame().to_excel(excel_writer, split_by=split_by, sheet_name=sheet_name, na_rep=na_rep,
                                               float_format=float_format, columns=columns, header=header, units=units,
                                               index=index, index_label=index_label, startrow=startrow,
                                               startcol=startcol, engine=engine, merge_cells=merge_cells,
                                               encoding=encoding, inf_rep=inf_rep, verbose=verbose,
                                               freeze_panes=freeze_panes, sort=sort, format_header=format_header)

    def renameRight(self, inplace=False):
        if self.nameSeparator in [None, '', False]:
            return self  # raise ValueError("name separator must not be None")
        objs = {}
        for each in list(self.columns):
            if each is None:
                objs[each] = each
            elif self.nameSeparator in each:
                objs[each] = each.split(self.nameSeparator )[-1]
                # self.units[ each.split(self.nameSeparator )[-1] ] = self.units[ each ]
                # del(self.units[each])
            else:
                objs[each] = each
        if len(self.columns) == 1:
            objs = list(objs.values())[0]
        if inplace:
            self.rename(objs, inplace=True)
        else:
            return self.rename(objs, inplace=False)

    def renameLeft(self, inplace=False):
        if self.nameSeparator in [None, '', False]:
            return self  # raise ValueError("name separator must not be None")
        objs = {}
        for each in list(self.columns):
            if each is None:
                objs[each] = each
            elif self.nameSeparator in each:
                objs[each] = each.split(self.nameSeparator)[0]
                # self.units[ each.split(self.nameSeparator )[0] ] = self.units[ each ]
                # del(self.units[each])
            else:
                objs[each] = each
        if len(self.columns) == 1:
            objs = list(objs.values())[0]
        if inplace:
            self.rename(objs, inplace=True)
        else:
            return self.rename(objs, inplace=False)

    def _CommonRename(self, SimSeries1, SimSeries2=None, LR=None):
        SDF1, SDF2 = SimSeries1, SimSeries2

        cha = self.intersectionCharacter

        if LR is not None:
            LR = LR.upper()
            if LR not in 'LR':
                LR = None

        if SDF2 is None:
            SDF1, SDF2 = self, SDF1

        if type(SDF1) is not SimSeries:
            raise TypeError("both series to be compared must be SimSeries.")
        if type(SDF2) is not SimSeries:
            raise TypeError("both series to be compared must be SimSeries.")

        if SDF1.nameSeparator is None or SDF2.nameSeparator is None:
            raise ValueError("the 'nameSeparator' must not be empty in both SimSeries.")

        if LR == 'L' or (LR is None and len(SDF1.left) == 1 and len(SDF2.left) == 1 ):
            SDF2C = SDF2.copy()
            SDF2C.renameRight(inplace=True)
            SDF1C = SDF1.copy()
            SDF1C.renameRight(inplace=True)
            commonNames = {}
            for c in SDF1C.columns:
                if c in SDF2C.columns:
                    commonNames[c] = str(SDF1.left[0]) + str(cha) + str(SDF2.left[0]) + str(SDF1.nameSeparator) + str(c)
                else:
                    commonNames[c] = str(SDF1.left[0]) + str(SDF1.nameSeparator) + str(c)
            for c in SDF2C.columns:
                if c not in SDF1C.columns:
                    commonNames[c] = str(SDF2.left[0]) + str(SDF1.nameSeparator) + str(c)
            if LR is None and len(commonNames) > 1:
                alternative = self._CommonRename(SDF1, SDF2, LR='R')
                if len(alternative[2]) < len(commonNames):
                    return alternative

        elif LR == 'R' or (LR is None and len(SDF1.right) == 1 and len(SDF2.right) == 1 ):
            SDF2C = SDF2.copy()
            SDF2C.renameLeft(inplace=True)
            SDF1C = SDF1.copy()
            SDF1C.renameLeft(inplace=True)
            commonNames = {}
            for c in SDF1C.columns:
                if c in SDF2C.columns:
                    commonNames[c] = str(c) + str(SDF1.nameSeparator) + str(SDF1.right[0]) + str(cha) + str(SDF2.right[0])
                else:
                    commonNames[c] = str(c) + str(SDF1.nameSeparator) + str(SDF1.right[0])
            for c in SDF2C.columns:
                if c not in SDF1C.columns:
                    commonNames[c] = str(c) + str(SDF1.nameSeparator) + str(SDF2.right[0])
            if LR is None and len(commonNames) > 1:
                alternative = self._CommonRename(SDF1, SDF2, LR='L')
                if len(alternative[2]) < len(commonNames):
                    return alternative

        # check if proposed names are not repetitions of original names
        for name in commonNames:
            if self.nameSeparator  is str and len(self.nameSeparator) > 0 and self.nameSeparator in commonNames[name]:
                if commonNames[name].split(self.nameSeparator)[0] == commonNames[name].split(self.nameSeparator)[1] and commonNames[name].split(self.nameSeparator)[0] == name:
                    commonNames[name] = name
        return SDF1C, SDF2C, commonNames

    def rename(self, index=None, *, axis=None, copy=True, inplace=False, level=None, errors='ignore'):
        """
        wrapper of rename function from Pandas.

        Alter Series index labels or name.

        Function / dict values must be unique (1-to-1).
        Labels not contained in a dict / Series will be left as-is.
        Extra labels listed don’t throw an error.

        Alternatively, change Series.name with a scalar value.

        See the user guide for more.

        Parameters
        axis{0 or “index”}
        Unused. Accepted for compatibility with DataFrame method only.

        indexscalar, hashable sequence, dict-like or function, optional
        Functions or dict-like are transformations to apply to the index.
        Scalar or hashable sequence-like will alter the Series.name attribute.

        **kwargs
        Additional keyword arguments passed to the function. Only the “inplace” keyword is used.

        Returns
        Series or None
        Series with index labels or name altered or None if inplace=True.
        """
        if type(index) is dict:
            if len(index) == 1 and list(index.keys()) not in self.index:
                return self.rename(list(index.values())[0], axis=axis, copy=copy, inplace=inplace, level=level, errors=errors)
            cBefore = list(self.index)
            if inplace:
                super().rename(index=index, axis=axis, copy=copy, inplace=inplace, level=level, errors=errors)
                cAfter = list(self.index)
            else:
                catch = super().rename(index=index, axis=axis, copy=copy, inplace=inplace, level=level, errors=errors)
                cAfter = list(catch.index)

            newUnits = {}
            for i in range(len(cBefore)):
                newUnits[cAfter[i]] = self.units[cBefore[i]]
            if inplace:
                self.units = newUnits
                self.spdLocator = _SimLocIndexer("loc", self)
                return None
            else:
                catch.units = newUnits
                catch.spdLocator = _SimLocIndexer("loc", catch)
                return catch
        elif type(index) is str:
            if inplace:
                self.name = index.strip()
                self.spdLocator = _SimLocIndexer("loc", self)
                return None
            else:
                catch = self.copy()
                catch.name = index
                catch.spdLocator = _SimLocIndexer("loc", catch)
                return catch

    def to(self, units):
        """
        returns the series converted to the requested units if possible,
        else returns None
        """
        return self.convert(units)

    def convert(self, units):
        """
        returns the series converted to the requested units if possible,
        else returns None
        """
        if type(units) is str and type(self.units) is str:
            if convertibleUnits(self.units, units):
                params = self._SimParameters
                params['units'] = units
                return SimSeries(data=convertUnit(self.S, self.units, units, self.speak), **params)
        if type(units) is str and type(self.units) is dict and len(set(self.units.values())) == 1:
            params = self._SimParameters
            params['units'] = units
            return SimSeries(data=convertUnit(self.S, list(set(self.units.values()))[0], units, self.speak ), **params )
        if type(units) is dict :  # and type(self.units) is dict:
            return self.to_SimDataFrame().convert(units).to_SimSeries()

    # def resample(self, rule, axis=0, closed=None, label=None, convention='start', kind=None, loffset=None, base=None, on=None, level=None, origin='start_day', offset=None):
    #     axis = _cleanAxis(axis)
    #     return SimSeries(data=self.S.resample(rule, axis=axis, closed=closed, label=label, convention=convention, kind=kind, loffset=loffset, base=base, on=on, level=level, origin=origin, offset=offset), **self._SimParameters )

    def reindex(self, index=None, **kwargs):
        """
        wrapper for pandas.Series.reindex

        index : array-like, optional
            New labels / index to conform to, should be specified using keywords.
            Preferably an Index object to avoid duplicating data.
        """
        return SimSeries(data=self.S.reindex(index=index, **kwargs), **self._SimParameters )


    def dropna(self, axis=0, inplace=False, how=None):
        axis = _cleanAxis(axis)
        if inplace:
            super().dropna(axis=axis, inplace=inplace, how=how)
            return None
        else:
            return SimSeries(data=self.S.dropna(axis=axis, inplace=inplace, how=how), **self._SimParameters )

    def drop(self, labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise'):
        axis = _cleanAxis(axis)
        if inplace:
            super().drop(labels=labels, axis=axis, index=index, columns=columns, level=level, inplace=inplace, errors='errors')
            return None
        else:
            return SimSeries(data=self.S.drop(labels=labels, axis=axis, index=index, columns=columns, level=level, inplace=inplace, errors='errors'), **self._SimParameters )

    @property
    def wells(self):
        objs = []
        if type(self.name) is str:
            if self.nameSeparator in self.name and self.name[0] == 'W':
                objs = [self.name.split(self.nameSeparator)[-1]]
        elif type(self.index[-1]) is str:
            for each in list(self.index):
                if self.nameSeparator in each and each[0] == 'W':
                    objs += [each.split(self.nameSeparator)[-1]]
        return tuple(set(objs))

    # @property
    # def items(self):
    #     return self.left

    def get_Wells(self, pattern=None):
        """
        Will return a tuple of all the well names in case.

        If the pattern variable is different from None only wells
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq

        """
        if pattern is not None and type(pattern ) is not str:
            raise TypeError('pattern argument must be a string.')
        if pattern is None:
            return tuple(self.wells)
        else:
            return tuple(fnmatch.filter(self.wells, pattern ) )

    @property
    def groups(self):
        if self.nameSeparator in [None, '', False]:
            return []
        objs = []
        if type(self.name) is str:
            if self.nameSeparator in self.name and self.name[0] == 'G':
                objs = [self.name.split(self.nameSeparator )[-1]]
        elif type(self.index[-1]) is str:
            for each in list(self.index ):
                if self.nameSeparator in each and each[0] == 'G':
                    objs += [each.split(self.nameSeparator )[-1]]
        return tuple(set(objs))

    def get_Groups(self, pattern=None):
        """
        Will return a tuple of all the group names in case.

        If the pattern variable is different from None only groups
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq

        """
        if pattern is not None and type(pattern ) is not str:
            raise TypeError('pattern argument must be a string.')
        if pattern is None:
            return self.groups
        else:
            return tuple(fnmatch.filter(self.groups, pattern ) )

    @property
    def regions(self):
        if self.nameSeparator in [None, '', False]:
            return []
        objs = []
        if type(self.name) is str:
            if self.nameSeparator in self.name and self.name[0] == 'R':
                objs = [self.name.split(self.nameSeparator )[-1]]
        elif type(self.index[-1]) is str:
            for each in list(self.index ):
                if self.nameSeparator in each and each[0] == 'R':
                    objs += [each.split(self.nameSeparator )[-1]]
        return tuple(set(objs))

    def get_Regions(self, pattern=None):
        """
        Will return a tuple of all the region names in case.

        If the pattern variable is different from None only regions
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq
        """
        if pattern is not None and type(pattern ) is not str:
            raise TypeError('pattern argument must be a string.')
        if pattern is None:
            return self.regions
        else:
            return tuple(fnmatch.filter(self.regions, pattern ) )

    @property
    def attributes(self):
        if self.nameSeparator in [None, '', False]:
            return { col:[] for col in self.columns }
        atts = {}
        for each in list(self.get_Keys() ):
            if self.nameSeparator in each:
                if each.split(self.nameSeparator )[0] in atts:
                    atts[each.split(self.nameSeparator )[0]] += [each.split(self.nameSeparator )[-1]]
                else:
                    atts[each.split(self.nameSeparator )[0]] = [each.split(self.nameSeparator )[-1]]
            else:
                if each not in atts:
                    atts[each] = []
        for att in atts:
            atts[att] = list(set(atts[att]))
        return atts

    @property
    def properties(self):
        if len(self.attributes.keys()) > 0:
            return tuple(self.attributes.keys())
        else:
            return tuple()

    def get_Attributes(self, pattern=None):
        """
        Will return a dictionary of all the attributes names in case as keys
        and their related items as values.

        If the pattern variable is different from None only attributes
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq
        """
        if pattern is None:
            return tuple(self.attributes.keys())
        else:
            return tuple(fnmatch.filter(tuple(self.attributes.keys()), pattern ) )

    def get_Keys(self, pattern=None):
        """
        Will return a tuple of all the key names in case.

        If the pattern variable is different from None only keys
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq

        """
        if pattern is not None and type(pattern ) is not str:
            raise TypeError('pattern argument must be a string.\nreceived '+str(type(pattern))+' with value '+str(pattern))
        if type(self.name) is str:
            keys =(self.name, )
        else:
            keys = tuple(self.index )
        if pattern is None:
            return keys
        else:
            return tuple(fnmatch.filter(keys, pattern ) )

    def diff(self, periods=1, forward=False):
        if type(periods) is bool:
            periods, forward = 1, periods
        if forward:
            return SimSeries(data=-1*self.S.diff(periods=-1*periods), **self._SimParameters )
        else:
            return SimSeries(data=self.S.diff(periods=periods), **self._SimParameters )

    def __neg__(self):
        result = -self.as_Series()
        return SimSeries(data=result, **self._SimParameters )

    def __add__(self, other):
        params = self._SimParameters
        # both SimSeries
        if isinstance(other, SimSeries):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimSeries are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")
            if type(self.units) is str and type(other.units) is str:
                newName = _stringNewName(self._CommonRename(other)[2])
                if self.units == other.units:
                    result = self.S.add(other.S, fill_value=0)
                elif convertibleUnits(other.units, self.units ):
                    otherC = convertUnit(other, other.units, self.units, self.speak )
                    result = self.S.add(otherC.S, fill_value=0)
                elif convertibleUnits(self.units, other.units ):
                    selfC = convertUnit(self, self.units, other.units, self.speak )
                    result = other.S.add(selfC.S, fill_value=0)
                    params['units'] = other.units
                else:
                    result = self.S.add(other.S, fill_value=0)
                    params['units'] = self.units+'+'+other.units
                try:
                    params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
                except ValueError:
                    params['dtype'] = result.dtype
                except TypeError:
                    params['dtype'] = result.dtype
                params['name'] = newName
                return SimSeries(data=result, **params)
            else:
                raise NotImplementedError

        # other is Pandas Series
        elif isinstance(other, Series):
            result = self.S.add(other, fill_value=0)
            newName = _stringNewName(self._CommonRename(SimSeries(other, **self._SimParameters))[2])
            try:
                params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
            except ValueError:
                params['dtype'] = result.dtype
            params['name'] = newName
            return SimSeries(data=result, **params)

        # let's Pandas deal with other types, maintain units, dtype and name
        result = self.as_Series() + other
        try:
            params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
        except ValueError:
            params['dtype'] = result.dtype
        return SimSeries(data=result, **params)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        params = self._SimParameters
        # both SimSeries
        if isinstance(other, SimSeries):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimSeries are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")
            if type(self.units) is str and type(other.units) is str:
                newName = _stringNewName(self._CommonRename(other)[2])
                if self.units == other.units:
                    result = self.sub(other, fill_value=0)
                elif convertibleUnits(other.units, self.units ):
                    otherC = convertUnit(other, other.units, self.units, self.speak)
                    result = self.sub(otherC, fill_value=0)
                elif convertibleUnits(self.units, other.units ):
                    selfC = convertUnit(self, self.units, other.units, self.speak)
                    result = selfC.sub(other, fill_value=0)
                    params['units'] = other.units
                else:
                    result = self.sub(other, fill_value=0)
                    params['units'] = self.units+'-'+other.units
                try:
                    params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
                except ValueError:
                    params['dtype'] = result.dtype
                except TypeError:
                    params['dtype'] = result.dtype
                params['name'] = newName
                return SimSeries(data=result, **params)
            else:
                raise NotImplementedError

        # other is Pandas Series
        elif isinstance(other, Series):
            result = self.S.sub(other, fill_value=0)
            newName = _stringNewName(self._CommonRename(SimSeries(other, **self._SimParameters))[2])
            try:
                params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
            except ValueError:
                params['dtype'] = result.dtype
            params['name'] = newName
            return SimSeries(data=result, **params)

        # let's Pandas deal with other types, maintain units and dtype
        result = self.as_Series() - other
        try:
            params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
        except ValueError:
            params['dtype'] = result.dtype
        return SimSeries(data=result, **params)

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        params = self._SimParameters
        # both SimSeries
        if isinstance(other, SimSeries):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimSeries are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")
            if type(self.units) is str and type(other.units) is str:
                params['units'] = unitProduct(self.units, other.units)
                newName = _stringNewName(self._CommonRename(other)[2])
                if self.units == other.units:
                    result = self.mul(other)
                elif convertibleUnits(other.units, self.units):
                    otherC = convertUnit(other, other.units, self.units, self.speak )
                    result = self.mul(otherC)
                elif convertibleUnits(self.units, other.units):
                    selfC = convertUnit(self, self.units, other.units, self.speak )
                    result = other.mul(selfC)
                    params['units'] = unitProduct(other.units, self.units)
                elif convertibleUnits(other.units, unitBase(self.units)):
                    otherC = convertUnit(other, other.units, unitBase(self.units), self.speak )
                    result = self.mul(otherC)
                elif convertibleUnits(self.units, unitBase(other.units)):
                    selfC = convertUnit(self, self.units, unitBase(other.units), self.speak )
                    result = other.mul(selfC)
                    params['units'] = unitProduct(other.units, self.units)
                else:
                    result = self.mul(other)
                    params['units'] = self.units + '*' + other.units
                try:
                    params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
                except ValueError:
                    params['dtype'] = result.dtype
                except TypeError:
                    params['dtype'] = result.dtype
                params['name'] = newName
                return SimSeries(data=result, **params)
            else:
                raise NotImplementedError

        # let's Pandas deal with other types(types with no units), maintain units and dtype
        result = self.as_Series() * other
        params['dtype'] = self.dtype if (result.astype(self.dtype).equals(result)) else result.dtype
        return SimSeries(data=result, **params )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        params = self._SimParameters
        # both SimSeries
        if isinstance(other, SimSeries):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimSeries are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")
            if type(self.units) is str and type(other.units) is str:
                newName = _stringNewName(self._CommonRename(other)[2])
                params['units'] = unitDivision(self.units, other.units)
                if self.units == other.units:
                    result = self.truediv(other)
                elif convertibleUnits(other.units, self.units):
                    otherC = convertUnit(other, other.units, self.units, self.speak )
                    result = self.truediv(otherC)
                elif convertibleUnits(self.units, other.units):
                    selfC = convertUnit(self, self.units, other.units, self.speak )
                    result = selfC.truediv(other)
                    params['units'] = unitDivision(other.units, self.units)
                elif convertibleUnits(other.units, unitBase(self.units)):
                    otherC = convertUnit(other, other.units, unitBase(self.units), self.speak )
                    result = self.truediv(otherC)
                elif convertibleUnits(self.units, unitBase(other.units)):
                    selfC = convertUnit(self, self.units, unitBase(other.units), self.speak )
                    result = selfC.truediv(other)
                    params['units'] = unitDivision(other.units, self.units)
                else:
                    result = self.truediv(other)
                    params['units'] = self.units + '/' + other.units
                try:
                    params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
                except ValueError:
                    params['dtype'] = result.dtype
                except TypeError:
                    params['dtype'] = result.dtype
                params['name'] = newName
                return SimSeries(data=result, **params)
            else:
                raise NotImplementedError

        # let's Pandas deal with other types(types with no units), maintain units and dtype
        result = self.as_Series() / other
        try:
            params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
        except ValueError:
            params['dtype'] = result.dtype
        return SimSeries(data=result, **params)

    def __rtruediv__(self, other):
        return self.__pow__(-1).__mul__(other)

    def __floordiv__(self, other):
        params = self._SimParameters
        # both SimSeries
        if isinstance(other, SimSeries):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimSeries are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")
            if type(self.units) is str and type(other.units) is str:
                params['units'] = unitDivision(self.units, other.units)
                newName = _stringNewName(self._CommonRename(other)[2])
                if self.units == other.units:
                    result = self.floordiv(other)
                elif convertibleUnits(other.units, self.units ):
                    otherC = convertUnit(other, other.units, self.units, self.speak )
                    result = self.floordiv(otherC)
                elif convertibleUnits(self.units, other.units ):
                    selfC = convertUnit(self, self.units, other.units, self.speak )
                    result = other.floordiv(selfC)
                    params['units'] = unitDivision(other.units, self.units)
                elif convertibleUnits(other.units, unitBase(self.units) ):
                    otherC = convertUnit(other, other.units, unitBase(self.units), self.speak )
                    result = self.floordiv(otherC)
                elif convertibleUnits(self.units, unitBase(other.units)):
                    selfC = convertUnit(self, self.units, unitBase(other.units), self.speak )
                    result = other.floordiv(selfC)
                    params['units'] = unitDivision(other.units, self.units)
                else:
                    result = self.floordiv(other)
                    params['units'] = self.units + '/' + other.units
                params['dtype'] = result.dtype  # self.dtype if result.astype(self.dtype).equals(result) else result.dtype
                params['name'] = newName
                return SimSeries(data=result, **params)
            else:
                raise NotImplementedError

        # let's Pandas deal with other types(types with no units), maintain units and dtype
        result = self.as_Series() // other
        params['dtype'] = result.dtype
        return SimSeries(data=result, **params)

    def __rfloordiv__(self, other):
        return self.__pow__(-1).__mul__(other).__int__()

    def __mod__(self, other):
        params = self._SimParameters
        # both are SimSeries
        if isinstance(other, SimSeries):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimSeries are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")
            if type(self.units) is str and type(other.units) is str:
                newName = _stringNewName(self._CommonRename(other)[2])
                if self.units == other.units:
                    result = self.mod(other)
                elif convertibleUnits(other.units, self.units ):
                    otherC = convertUnit(other, other.units, self.units, self.speak )
                    result = self.mod(otherC)
                elif convertibleUnits(self.units, other.units ):
                    selfC = convertUnit(self, self.units, other.units, self.speak )
                    result = other.mod(selfC)
                    params['units'] = other.units
                else:
                    result = self.mod(other)
                try:
                    params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
                except ValueError:
                    params['dtype'] = result.dtype
                except TypeError:
                    params['dtype'] = result.dtype
                params['name'] = newName
                return SimSeries(data=result, **params)
            else:
                raise NotImplementedError

        # let's Pandas deal with other types, maintain units and dtype
        result = self.as_Series() % other
        try:
            params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
        except ValueError:
            params['dtype'] = result.dtype
        return SimSeries(data=result, **params)

    def __pow__(self, other):
        params = self._SimParameters
        # both SimSeries
        if isinstance(other, SimSeries):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimSeries are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")
            if type(self.units) is str and type(other.units) is str:
                params['units'] = self.units+'^'+other.units
                newName = _stringNewName(self._CommonRename(other)[2])
                if self.units == other.units:
                    result = self.pow(other)
                elif convertibleUnits(other.units, self.units ):
                    otherC = convertUnit(other, other.units, self.units, self.speak )
                    result = self.pow(otherC)
                    params['units'] = self.units+'^'+self.units
                elif convertibleUnits(self.units, other.units ):
                    selfC = convertUnit(self, self.units, other.units, self.speak )
                    result = other.pow(selfC)
                    params['units'] = other.units+'^'+other.units
                else:
                    result = self.pow(other)
                try:
                    params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
                except ValueError:
                    params['dtype'] = result.dtype
                except TypeError:
                    params['dtype'] = result.dtype
                params['name'] = newName
                return SimSeries(data=result, **params )
            else:
                raise NotImplementedError

        # let's Pandas deal with other types(types with no units), maintain units and dtype
        result = self.as_Series() ** other
        try:
            params['dtype'] = self.dtype if result.astype(self.dtype).equals(result) else result.dtype
        except ValueError:
            params['dtype'] = result.dtype
        return SimSeries(data=result, **params)

    def __int__(self):
        if self.isna().any():
            notNA = ~self.isna()
            NA = self.isna()
            return (self[notNA].append(self[NA])).sort_index()
        else:
            return SimSeries(data=self.S.astype(int), **self._SimParameters)

    def __abs__(self):
        return SimSeries(data=abs(self.S), **self._SimParameters)

    def avg(self, axis=0, **kwargs):
        return self.mean(axis=axis, **kwargs)

    def avg0(self, axis=0, **kwargs):
        return self.mean0(axis=axis, **kwargs)

    def average(self, axis=0, **kwargs):
        return self.mean(axis=axis, **kwargs)

    def average0(self, axis=0, **kwargs):
        return self.mean0(axis=axis, **kwargs)

    def count0(self, **kwargs):
        return self.replace(0,np.nan).count(**kwargs)

    def max0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).max(axis=axis, **kwargs)

    def mean0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).mean(axis=axis, **kwargs)

    def median0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).median(axis=axis, **kwargs)

    def min0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).min(axis=axis, **kwargs)

    def mode0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).mode(axis=axis, **kwargs)

    def prod0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).prod(axis=axis, **kwargs)

    def quantile0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).quantile(axis=axis, **kwargs)

    def rms(self, axis=0, **kwargs):
        return (self**2).mean(axis=axis, **kwargs)**0.5

    def rms0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).rms(axis=axis, **kwargs)

    def std0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).std(axis=axis, **kwargs)

    def sum0(self, axis=0, **kwargs):
        return self.sum(axis=axis, **kwargs)

    def var0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).var(axis=axis, **kwargs)

    def znorm(self):
        """
        return standard normalization

        """
        return znorm(self)

    def znorm0(self):
        """
        return standard normalization ignoring zeroes

        """
        return znorm(self.replace(0,np.nan))

    def minmaxnorm(self):
        """
        return min-max normalization
        """
        return minmaxnorm(self)

    def minmaxnorm(self):
        """
        return min-max normalization
        """
        return minmaxnorm(self.replace(0,np.nan))
        return minmaxnorm(self)

    def __repr__(self) -> str:
        """
        Return a string representation for a particular Series, with Units.
        """
        # from Pandas Series
        buf = StringIO("")
        width, height = get_terminal_size()
        max_rows =(
            height
            if get_option("display.max_rows") == 0
            else get_option("display.max_rows")
        )
        min_rows =(
            height
            if get_option("display.max_rows") == 0
            else get_option("display.min_rows")
        )
        show_dimensions = get_option("display.show_dimensions")

        self.to_string(
            buf=buf,
            name=self.name,
            dtype=self.dtype,
            min_rows=min_rows,
            max_rows=max_rows,
            length=show_dimensions,
        )
        result = buf.getvalue()

        if type(self.units) is str:
            return result + ', Units: ' + self.units
        elif type(self.units) is dict:
            result = result.split('\n')
            for n in range(len(result)-1):
                keys = result[n] + ' '
                i, f = 0, 0
                while i < len(keys):
                    f = keys.index(' ', i)
                    key = keys[i:f]
                    if key == '...':
                        i = len(keys)
                        continue
                    while key not in self.index and f <= len(keys):
                        f = keys.index(' ', f+1) if ' ' in keys[f+1:] else len(keys)+1
                        key = keys[i:f]
                    if key not in self.index:
                        i = len(keys)
                        continue
                    if key in self.units and self.units[key] is not None:
                        result[n] += '    ' + self.units[key].strip()
                    i = len(keys)
            result = '\n'.join(result)
            return '\n' + result
        else:
            return result

    def get_units(self, items=None):
        return self.get_Units()

    def get_Units(self, items=None):
        """
        returns the units for the selected 'items' or for all the columns in the SimDataFrame.

        Parameters
        ----------
        items : str or list of str, optional
            Ignored, this parameter is kept for compatibility with SimDataFrame. The default is None.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        if self.units is None:
            return 'UNITLESS'
        elif type(self.units) is str and type(self.name) is str:
            uDic = { str(self.name) : self.units }
        elif type(self.units) is dict:
            uDic = {}
            for each in self.index:
                if each in self.units:
                    uDic[each] = self.units[each]
                else:
                    uDic[each] = 'UNITLESS'
        else:
            return self.units.copy() if type(self.units) is dict else self.units
        return uDic

    def set_units(self,units,item=None):
        """
        Alias of .set_Units method.
        This method can be used to define the units related to the values of a column (item).

        Parameters
        ----------
        units : str or list of str
            the units to be assigned
        item : str, optional
            The name of the column to apply the units.
            The default is None. In this case the unit

        Raises
        ------
        ValueError
            when units can't be applied.
        TypeError
            when units or item has the wrong format.

        Returns
        -------
        None.

        """
        return self.set_Units(units=units,item=item)

    def set_Units(self,units,item=None):
        """
        This method can be used to define the units related to the values of a column (item).

        Parameters
        ----------
        units : str or list of str
            the units to be assigned
        item : str, optional
            The name of the column to apply the units.
            The default is None. In this case the unit

        Raises
        ------
        ValueError
            when units can't be applied.
        TypeError
            when units or item has the wrong format.

        Returns
        -------
        None.

        """
        if item is not None and type(item) in (str, int, float) and item not in self.columns:
            raise ValueError("the required item '" + str(item) + "' is not in this SimSeries")

        if self.units is None or type(self.units) is str:
            if units is None:
                self.units = None
            elif type(units) is str:
                self.units = units.strip()
            elif type(units) is dict:
                old_units = self.units
                try:
                    self.units = {}
                    return self.set_Units(units)
                except:
                    self.units = old_units
                    raise ValueError("not able to process dictionary of units.")
            else:
                raise TypeError("units must be a string.")

        elif type(self.units) is dict:
            if type(units) not in (str,dict) and hasattr(units,'__iter__'):
                if item is not None and type(item) not in (str,dict) and hasattr(item,'__iter__'):
                    if len(item) == len(units):
                        return self.set_Units( dict(zip(item,units)) )
                    else:
                        raise ValueError("both units and item must have the same length.")
                elif item is None:
                    if len(units) == len(self.columns):
                        return self.set_Units( dict(zip(list(self.columns),units)) )
                    else:
                        raise ValueError("units list must be the same length of columns in the SimSeries or must be followed by a list of items.")
                else:
                    raise TypeError("if units is a list, items must be a list of the same length.")
            elif type(units) is dict:
                for k,u in units.items():
                    self.set_Units(u,k)
            elif type(units) is str:
                if item is None:
                    self.units = units.strip()
                else:
                    if type(item) not in (str,dict) and hasattr(item,'__iter__'):
                        units = units.strip()
                        for i in item:
                            if i in self.units:
                                self.units[i] = units
                    elif type(item) not in dict:
                        if item in self.units:
                            self.units[item] = units

            if item is None and len(self.columns) > 1:
                raise ValueError("More than one column in this SimSeries, item must not be None")
            elif item is None and len(self.columns) == 1:
                return self.set_Units(units,[list(self.columns)[0]])
            elif item is not None:
                if item in self.columns:
                    if units is None:
                        self.units[item] = None
                    elif type(units) is str:
                        self.units[item] = units.strip()
                    else:
                        raise TypeError("units must be a string.")
                if item == self.index.name:
                    self.indexUnits = units.strip()
                    self.units[item] = units.strip()
                if item in self.index.names:
                    self.units[item] = units.strip()

    def get_UnitsString(self, items=None):
        if len(self.get_Units(items)) == 1:
            return list(self.get_Units(items).values())[0]
        elif len(set(self.get_Units(items).values() )) == 1:
            return list(set(self.get_Units(items).values() ))[0]

    def copy(self):
        if type(self.units) is dict:
            params = self._SimParameters
            params['units'] = self.units.copy()
            return SimSeries(data=self.as_Series().copy(True), **params)
        return SimSeries(data=self.as_Series().copy(True), **self._SimParameters )

    def filter(self, conditions=None, **kwargs):
        """
        Returns a filtered SimSeries based on conditions argument.

        To filter over the series simply define the
        condition:
            '>0'

        To set several conditions together the operatos 'and' and 'or'
        are accepted:
            '>0 and <1000'

        To filter only over the index set the condition directly:
            '>0'
        or use the key '.index' or '.i' to refer to the index of the SimSeries.

        To remove null values append '.notnull' to the column name:
            'NAME.notnull'
        To keep only null values append '.null' to the column name:
            'NAME'.null
        """
        returnString = False
        if 'returnString' in kwargs:
            returnString = bool(kwargs['returnString'] )
        returnFilter = False
        if 'returnFilter' in kwargs:
            returnFilter = bool(kwargs['returnFilter'] )
        returnFrame = False
        if 'returnFrame' in kwargs:
            returnFrame = bool(kwargs['returnFrame'] )
        if 'returnSeries' in kwargs:
            returnFrame = bool(kwargs['returnSeries'] )
        if not returnFilter and not returnString and('returnSeries' not in kwargs or 'returnFrame' not in kwargs ):
            returnFrame = True

        specialOperation = ['.notnull', '.null', '.isnull', '.abs']
        numpyOperation = ['.sqrt', '.log10', '.log2', '.log', '.ln']
        pandasAggregation = ['.any', '.all']
        PandasAgg = ''

        def KeyToString(filterStr, key, PandasAgg):
            if len(key) > 0:
                # catch particular operations performed by Pandas
                foundSO, foundNO = '', ''
                if key in specialOperation:
                    if filterStr[-1] == ' ':
                        filterStr = filterStr.rstrip()
                    filterStr += key+'()'
                else:
                    for SO in specialOperation:
                        if key.strip().endswith(SO):
                            key = key[:-len(SO)]
                            foundSO =(SO if SO != '.null' else '.isnull' ) + '()'
                            break
                # catch particular operations performed by Numpy
                if key in numpyOperation:
                    raise ValueError("wrong syntax for '"+key+"(blank space before) in:\n   "+conditions)
                else:
                    for NO in numpyOperation:
                        if key.strip().endswith(NO):
                            key = key[:-len(NO)]
                            NO = '.log' if NO == '.ln' else NO
                            filterStr += 'np' + NO + '('
                            foundNO = ' )'
                            break
                # catch aggregation operations performed by Pandas
                if key in pandasAggregation:
                    PandasAgg = key+'(axis=1)'
                else:
                    for PA in pandasAggregation:
                        if key.strip().endswith(PA):
                            PandasAgg = PA+'(axis=1)'
                            break
                # if key is the index
                if key in ['.i', '.index']:
                    filterStr = filterStr.rstrip()
                    filterStr += ' self.S.index'
                # if key is a column
                elif key in self.columns:
                    filterStr = filterStr.rstrip()
                    filterStr += " self.S['"+key+"']"
                # key might be a wellname, attribute or a pattern
                elif len(self.find_Keys(key)) == 1:
                    filterStr = filterStr.rstrip()
                    filterStr += " self.S['"+ self.find_Keys(key)[0] +"']"
                elif len(self.find_Keys(key)) > 1:
                    filterStr = filterStr.rstrip()
                    filterStr += " self.S["+ str(list(self.find_Keys(key)) ) +"]"
                    PandasAgg = '.any(axis=1)'
                else:
                    filterStr += ' ' + key
                filterStr = filterStr.rstrip()
                filterStr += foundSO + foundNO
                key = ''
            return filterStr, key, PandasAgg

        if type(conditions) is not str:
            if type(conditions) is not list:
                try:
                    conditions = list(conditions)
                except:
                    raise TypeError('conditions argument must be a string.')
            conditions = ' and '.join(conditions)

        conditions = conditions.strip() + ' '

        # find logical operators and translate to correct key
        AndOrNot = False
        if ' and ' in conditions:
            conditions = conditions.replace(' and ', ' & ')
        if ' or ' in conditions:
            conditions = conditions.replace(' or ', ' | ')
        if ' not ' in conditions:
            conditions = conditions.replace(' not ', ' ~ ')
        if '&' in conditions:
            AndOrNot = True
        elif '|' in conditions:
            AndOrNot = True
        elif '~' in conditions:
            AndOrNot = True

        # create Pandas compatible condition string
        filterStr =  ' ' + '('*AndOrNot
        key = ''
        cond, oper = '', ''
        i = 0
        while i < len(conditions):

            # catch logital operators
            if conditions[i] in ['&', "|", '~']:
                filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                filterStr = filterStr.rstrip()
                filterStr += ' )' + PandasAgg + ' ' + conditions[i] + '('
                PandasAgg = ''
                i += 1
                continue

            # catch enclosed strings
            if conditions[i] in ['"', "'", '[']:
                if conditions[i] in ['"', "'"]:
                    try:
                        f = conditions.index(conditions[i], i+1 )
                    except:
                        raise ValueError('wring syntax, closing ' + conditions[i] + ' not found in:\n   '+conditions)
                else:
                    try:
                        f = conditions.index(']', i+1 )
                    except:
                        raise ValueError("wring syntax, closing ']' not found in:\n   "+conditions)
                if f > i+1:
                    key = conditions[i+1:f]
                    filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                    i = f+1
                    continue

            # pass blank spaces
            if conditions[i] == ' ':
                filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                if len(filterStr) > 0 and filterStr[-1] != ' ':
                    filterStr += ' '
                i += 1
                continue

            # pass parenthesis
            if conditions[i] in ['(', ')']:
                filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                filterStr += conditions[i]
                i += 1
                continue

            # catch conditions
            if conditions[i] in ['=', '>', '<', '!']:
                cond = ''
                f = i+1
                while conditions[f] in ['=', '>', '<', '!']:
                    f += 1
                cond = conditions[i:f]
                if cond == '=':
                    cond = '=='
                elif cond in ['=>', '=<', '=!']:
                    cond = cond[::-1]
                elif cond in ['><', '<>']:
                    cond = '!='
                filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                filterStr = filterStr.rstrip()
                filterStr += ' ' + cond
                i += len(cond)
                continue

            # catch operations
            if conditions[i] in ['+', '-', '*', '/', '%', '^']:
                oper = ''
                f = i+1
                while conditions[f] in ['+', '-', '*', '/', '%', '^']:
                    f += 1
                oper = conditions[i:f]
                oper = oper.replace('^', '**')
                filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                filterStr = filterStr.rstrip()
                filterStr += ' ' + oper
                i += len(oper)
                continue

            # catch other characters
            else:
                key += conditions[i]
                i += 1
                continue

        # clean up
        filterStr = filterStr.strip()
        # check missing key, means .index by default
        if filterStr[0] in ['=', '>', '<', '!']:
            filterStr = 'self.S.index ' + filterStr
        elif filterStr[-1] in ['=', '>', '<', '!']:
            filterStr = filterStr + ' self.S.index'
        # close last parethesis and aggregation
        filterStr += ' )' * bool(AndOrNot + bool(PandasAgg) ) + PandasAgg
        # open parenthesis for aggregation, if needed
        if not AndOrNot and bool(PandasAgg):
            filterStr = '(' + filterStr

        retTuple = []

        if returnString:
            retTuple += [ filterStr ]
        filterArray = eval(filterStr )
        if returnFilter:
            retTuple += [ filterArray ]
        if returnFrame:
            retTuple += [ self.S[ filterArray ] ]

        if len(retTuple ) == 1:
            return retTuple[0]
        else:
            return tuple(retTuple )

    def sort_values(self, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None):
        if inplace:
            super().sort_values(axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key)
            return None
        else:
            return SimSeries(data=self.S.sort_values(axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key), **self._SimParameters)

    def head(self,n=5):
        """
        Return the first n rows.

        This function returns first n rows from the object based on position. It is useful for quickly verifying data, for example, after sorting or appending rows.

        For negative values of n, this function returns all rows except the last n rows, equivalent to df[n:].

        Parameters:
        ----------
            n : int, default 5
            Number of rows to select.

        Returns
        -------
            type of caller
            The first n rows of the caller object.
        """
        return SimSeries(data=self.S.head(n),**self._SimParameters)

    def tail(self,n=5):
        """
        Return the last n rows.

        This function returns last n rows from the object based on position. It is useful for quickly verifying data, for example, after sorting or appending rows.

        For negative values of n, this function returns all rows except the first n rows, equivalent to df[n:].

        Parameters:
        ----------
            n : int, default 5
            Number of rows to select.

        Returns
        -------
            type of caller
            The last n rows of the caller object.
        """
        return SimSeries(data=self.S.tail(n),**self._SimParameters)

    def cumsum(self, skipna=True, *args, **kwargs):
        """
        Return cumulative sum over a SimDataFrame.

        Returns a SimDataFrame or SimSeries of the same size containing the cumulative sum.

        Parameters:
            axis : {0 or ‘index’, 1 or ‘columns’}, default 0
                The index or the name of the axis. 0 is equivalent to None or ‘index’.

        skipna: bool, default True
            Exclude NA/null values. If an entire row/column is NA, the result will be NA.

        *args, **kwargs
            Additional keywords have no effect but might be accepted for compatibility with NumPy.

        Returns
            SimSeries or SimDataFrame
            Return cumulative sum of Series or DataFrame.
        """
        return SimSeries(data=self.S.cumsum(skipna=skipna, *args, **kwargs),**self._SimParameters)

    def jitter(self,std=0.10):
        """
        add jitter the values of the SimSeries
        """
        return jitter(self,std)

    def daily(self, outBy='mean', datetimeIndex=False, **kwargs):
        """
        return a Series with a single row per day.
        index must be a date type.

        available gropuing calculations are:
            first : keeps the fisrt row per day
            last : keeps the last row per day
            max : returns the maximum value per year
            min : returns the minimum value per year
            mean or avg : returns the average value per year
            median : returns the median value per month
            std : returns the standard deviation per year
            sum : returns the summation of all the values per year
            count : returns the number of rows per year
        """
        return self.to_SimDataFrame().daily(outBy=outBy, datetimeIndex=datetimeIndex, **kwargs).to_SimSeries()

    def monthly(self, outBy='mean', datetimeIndex=False, **kwargs):
        """
        return a dataframe with a single row per month.
        index must be a date type.

        available gropuing calculations are:
            first : keeps the fisrt row per month
            last : keeps the last row per month
            max : returns the maximum value per month
            min : returns the minimum value per month
            mean or avg : returns the average value per month
            median : returns the median value per month
            std : returns the standard deviation per month
            sum : returns the summation of all the values per month
            count : returns the number of rows per month

        datetimeIndex : bool
            if True the index will converted to DateTimeIndex with Day=1 for each month
            if False the index will be a MultiIndex (Year,Month)
        """
        return self.to_SimDataFrame().monthly(outBy=outBy, datetimeIndex=datetimeIndex, **kwargs).to_SimSeries()

    def yearly(self, outBy='mean', datetimeIndex=False, **kwargs):
        """
        return a dataframe with a single row per year.
        index must be a date type.

        available gropuing calculations are:
            first : keeps the fisrt row
            last : keeps the last row
            max : returns the maximum value per year
            min : returns the minimum value per year
            mean or avg : returns the average value per year
            median : returns the median value per month
            std : returns the standard deviation per year
            sum : returns the summation of all the values per year
            count : returns the number of rows per year

        datetimeIndex : bool
            if True the index will converted to DateTimeIndex with Day=1 and Month=1 for each year
            if False the index will be a MultiIndex (Year,Month)
        """
        return self.to_SimDataFrame().yearly(outBy=outBy, datetimeIndex=datetimeIndex, **kwargs).to_SimSeries()

    def DaysInYear(self,column=None):
        """
        returns a SimSeries with the number of days in a particular year

        Parameters
        ----------
        column : str
            The selected column must be an of dtype integer, date, datetime containing
            the year to calculate the number of day.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        return self.daysInYear(column=column)

    def daysinyear(self,column=None):
        """
        returns a SimSeries with the number of days in a particular year

        Parameters
        ----------
        column : str
            The selected column must be an of dtype integer, date, datetime containing
            the year to calculate the number of day.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        return self.daysInYear(column=column)

    def daysInYear(self,column=None):
        """
        returns a SimSeries with the number of days in a particular year

        Parameters
        ----------
        column : str
            The selected column must be an of dtype integer, date, datetime containing
            the year to calculate the number of day.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        params = self._SimParameters
        if 'units' in params:
            if type(params['units']) is str:
                params['units'] = 'days'
            else:
                params['units']['DaysInYear'] = 'days'
        else:
            params['units'] = 'days'
        params['name'] = 'DaysInYear'
        params['index']=self.index
        if column is not None:
            if type(column) is str and column in self.columns:
                if self[column].dtype in ('int','int64') and self[column].min() > 0:
                    return SimSeries(data=daysInYear(self[column].values), **params)
                elif 'datetime' in str(self[column].dtype):
                    return daysInYear(self[column])
                else:
                    raise ValueError('selected column is not a valid date or year integer')
            elif type(column) is str and column not in self.columns:
                raise ValueError('the selected column is not in this SimDataFrame')
            elif hasattr(column,'__iter__'):
                result = self.SimDataFrame(data={}, index=self.index, **self._SimParameters)
                for col in column:
                    if col in self.columns:
                        result[col] = daysInYear(self[col])
                return result
        else:
            if self.dtype in ('int','int64') and self.min() > 0:
                return SimSeries(data=list(daysInYear(self.values)), **params)
            elif 'datetime' in str(self.dtype):
                return daysInYear(self)
            elif self.index.dtype in ('int','int64') and self.index.min() > 0:
                # params['units'] = self.units.copy() if type(self.units) is dict else self.units
                # params['name'] = self.name
                # params['indexName'] = 'DaysInYear'
                # params['indexUnits'] = 'days'
                return SimSeries(data=list(daysInYear(self.index.to_numpy())), **params)
            elif 'datetime' in str(self.index.dtype):
                # params['units'] = self.units.copy() if type(self.units) is dict else self.units
                # params['name'] = self.name
                # params['indexName'] = 'DaysInYear'
                # params['indexUnits'] = 'days'
                return SimSeries(data=list(daysInYear(self.index)), **params)
            else:
                raise ValueError('index is not a valid date or year integer')

    def RealYear(self,column=None):
        return self.realYear(column)

    def realyear(self,column=None):
        return self.realYear(column)

    def realYear(self,column=None):
        """
        returns a SimSeries with the year and cumulative days as fraction

        Parameters
        ----------
        column : str
            The selected column must be a datetime array.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        params = self._SimParameters
        params['index'] = self.index
        params['name'] = 'realYear'
        params['units'] = 'Years'
        if column is not None:
            if type(column) is str and column in self.columns:
                if 'datetime' in str(self[column].dtype):
                    return realYear(self[column])
                else:
                    raise ValueError('selected column is not a valid date format')
            elif type(column) is str and column not in self.columns:
                raise ValueError('the selected column is not in this SimDataFrame')
            elif hasattr(column,'__iter__'):
                result = SimDataFrame(data={}, index=self.index, **self._SimParameters)
                for col in column:
                    if col in self.columns:
                        result[col] = daysInYear(self[col])
                return result
        else:
            if 'datetime' in str(self.index.dtype):
                return SimSeries(data=list(realYear(self.index)), **params)
            else:
                raise ValueError('index is not a valid date or year integer')

    def integrate(self, method='trapz', at=None):
        """
        Calculates numerical integration, using trapezoidal method,
        or constant value of the columns values over the index values.

        method parameter can be: 'trapz' to use trapezoidal method
                                 'const' to constant vale multiplied
                                         by delta-index

        Returns a new SimSeries
        """
        return self.SDF.integrate(method=method, at=at).to_SimSeries()

    def differenciate(self, na_position='last'):
        """
        Calculates numerical differentiation of the columns values over the index values.

        Returns a new SimDataFrame
        """
        return self.SDF.differenciate(na_position=na_position).to_SimSeries()

    def plot(self, y=None, x=None, others=None,**kwargs):
        """
        wrapper of Pandas plot method, with some superpowers

        Parameters
        ----------
        y : string, list or index; optional
            column name to plot. The default is None.
        x : string, optional
            the columns to be used for x coordinates. The default is the index.
        others : SimDataFrame, SimSeries, DataFrame or Series; optional
            other Frames to include in the plot, for the same selected columns. The default is None.
        **kwargs : TYPE
            any other keyword argument for matplolib.

        Returns
        -------
        matplotlib AxesSubplot.
        """
        return self.sdf.plot(y=y, x=x, others=others, **kwargs)

    def info(self,*args,**kwargs):
        """
        .info method implemented for SimSeries for compatibility with SimDataFrame.
        """
        return self.SDF.info()

    def slope(self, x=None, y=None, window=None, slope=True, intercept=False):
        """
        calculates the slope of the series vs its index.

        Calculates the slope of column Y vs column X or vs index if 'x' is None

        Parameters
        ----------
        window : int, float or str, optional
            The half-size of the rolling window to calculate the slope.
            if None : the slope will be calculated from the entire dataset.
            if int : window rows before and after of each row will be used to calculate the slope
            if float : the window size will be variable, with window values of X arround each row's X. Not compatible with datetime columns
            if str : the window string will be used as timedelta arround the datetime X
            The default is None.
        slope : bool, optional
            Set it True to return the slope of the linear fit. The default is True.
        intercept : bool, optional
            Set it True to return the intersect of the linear fit. The default is False.
        if both slope and intercept are True, a tuple of both results will be returned

        x : kept for compatibility with SimDataFrame
        y : kept for compatibility with SimDataFrame

        Returns
        -------
        numpy array
            The array containing the desired output.

        """
        if window is None and x is not None and y is None:
            window, x = x, None
        params = self._SimParameters
        if self.name is not None and len(self.get_Units(self.name)) == 1 and self.indexUnits is not None:
            if type(params['units']) is dict:
                params['units'][self.name] = str(self.get_Units(self.name)[self.name]) + '/' + str(self.indexUnits)
            else:
                params['units'] = str(self.get_Units(self.name)[self.name]) + '/' + str(self.indexUnits)
        params['name'] = 'slope_of_' + (self.name)
        slopeS = _slope(df=self, x=x, y=y, window=window, slope=slope, intercept=intercept)
        return SimSeries(data=slopeS, index=self.index, **params)


class SimDataFrame(DataFrame):
    """
    A SimDataFrame object is a pandas.DataFrame that units associated with to
    each column. In addition to the standard DataFrame constructor arguments,
    SimDataFrame also accepts the following keyword arguments:

    Parameters
    ----------
    units : string or dictionary of units(optional)
        Can be any string, but only units acepted by the UnitConverter will
        be considered when doing arithmetic calculations with other SimSeries
        or SimDataFrames.

    See Also
    --------
    SimSeries
    pandas.DataFrame

    """
    _metadata = ["units", "speak", "indexUnits", "nameSeparator", "intersectionCharacter", "autoAppend", "spdLocator", "transposed", "operatePerName"]  #, "spdiLocator"]

    def __init__(self, data=None, units=None, index=None, speak=False, indexName=None, indexUnits=None, nameSeparator=None, intersectionCharacter='∩', autoAppend=False, transposed=False, operatePerName=False, *args, **kwargs):
        self.units = None
        self.speak = bool(speak)
        self.indexUnits = None
        self.nameSeparator = None
        self.intersectionCharacter = '∩'
        self.autoAppend = False
        self.operatePerName = False
        self.spdLocator = _SimLocIndexer("loc", self)
        # self.spdiLocator = _iSimLocIndexer("iloc", self)
        self.transposed = bool(transposed)


        indexInput = None
        # catch index keyword from input parameters
        if index is not None:
            indexInput = index
        elif 'index' in kwargs and kwargs['index'] is not None:
            indexInput = kwargs['index']
        elif len(args) >= 3 and args[2] is not None:
            indexInput = args[2]
        # if index is a Series, get the name
        elif isinstance(indexInput, Series):
            if type(indexInput.name) is str:
                indexInput = indexInput.name
        # if index is None and data is SimSeries or SimDataFrame get the name
        elif type(data) in [SimSeries, SimDataFrame] and type(data.index.name) is str and len(data.index.name)>0:
            indexInput = data.index.name
            self.indexUnits = data.indexUnits.copy() if type(data.indexUnits) is dict else data.indexUnits

        # if units is None data is SimDataFrame or SimSeries get the units
        if units is None:
            if type(data) is SimDataFrame:
                if type(data.units) is dict:
                    units = data.units.copy()
            elif type(data) is SimSeries:
                if type(data.units) is dict:
                    units = data.units.copy()
                    if data.index.name not in units:
                        units[data.index.name] = data.indexUnits
                elif type(data.name) is str and type(data.units) is str:
                    units = {data.name:data.units , data.index.name:data.indexUnits}

        # remove arguments not known by Pandas
        kwargsB = kwargs.copy()
        kwargs.pop('name', None)
        kwargs.pop('indexName', None)
        kwargs.pop('indexUnits', None)
        kwargs.pop('nameSeparator', None)
        kwargs.pop('units', None)
        kwargs.pop('speak', None)
        kwargs.pop('autoAppend', None)
        kwargs.pop('operatePerName',None)
        # convert to pure Pandas
        if type(data) in [ SimDataFrame, SimSeries ]:
            self.nameSeparator = data.nameSeparator
            self.autoAppend = data.autoAppend
            self.operatePerName = data.operatePerName
            data = data.to_Pandas()
        super().__init__(data=data, index=index, *args, **kwargs)

        # set the name of the index
        if(self.index.name is None or(type(self.index.name) is str and len(self.index.name) == 0)) and(type(indexInput) is str and len(indexInput) > 0):
            self.index.name = indexInput
        # overwrite the index.name with input from the argument indexName
        if indexName is not None and type(indexName) is str and len(indexName.strip()) > 0:
            self.set_indexName(indexName)
        elif 'indexName' in kwargsB and type(kwargsB['indexName']) is str and len(kwargsB['indexName'].strip()) > 0:
            self.set_indexName(kwargsB['indexName'])
        # set units of the index
        elif indexUnits is not None and type(indexUnits) is str and len(indexUnits.strip()) > 0:
            self.set_indexUnits(indexUnits)
        elif 'indexUnits' in kwargsB and type(kwargsB['indexUnits']) is str and len(kwargsB['indexUnits'].strip()) > 0:
            self.set_indexUnits(kwargsB['indexUnits'])
        if self.indexUnits is not None and self.index.name is not None and len(self.index.name) > 0 and type(self.units) is dict and self.index.name not in self.units:
            self.units[self.index.name] = self.indexUnits

        # set the units
        if type(units) is str:
            if self.transposed:
                self.transposed = False
            # self.units = {}
            # for key in list(self.columns):
            #     self.units[ key ] = units
            self.units = dict(zip(list(self.columns), [units]*len(list(self.columns))))
        elif hasattr(units,'__iter__') and type(units) not in (str,dict):
            if self.transposed:
                if len(units) == len(self.index):
                    self.units = dict(zip(list(self.index), units))
            elif not self.transposed:
                if len(units) == len(self.columns):
                    self.units = dict(zip(list(self.columns), units))
                else:
                    raise ValueError('The number of items in the iterable provided by units argument must coincide with the number of columns.')
        elif type(units) is str:
            if self.transposed:
                if len(self.index) == 1:
                    self.units = {self.index[0]:units}
            elif not self.transposed:
                if len(self.columns) == 1:
                    self.units = {self.columns[0]:units}
        elif type(units) is dict and len(units) > 0:
            self.units = {}
            if self.transposed:
                for key in list(self.index):
                    if key is not None and key in units:
                        self.units[key] = units[key]
                    else:
                        self.units[key] = 'UNITLESS'
            elif not self.transposed:
                for key in list(self.columns):
                    if key is not None and key in units:
                        self.units[key] = units[key]
                    else:
                        self.units[key] = 'UNITLESS'
            if self.index.name in units:
                self.units[self.index.name] = units[self.index.name]
            for key in self.index.names:
                if key is not None and key in units:
                    self.units[key] = units[key]
        if self.indexUnits is None and self.index.name is not None and units is not None:
            if self.index.name in units:
                self.indexUnits = units[self.index.name]
        if self.indexUnits is None and indexUnits is not None:
            self.indexUnits = indexUnits.strip() if type(indexUnits) is str else indexUnits

        if self.index.name is not None and type(self.units) is dict and self.index.name not in self.units:
            self.units[self.index.name] = '' if self.indexUnits is None else self.indexUnits

        # get separator for the column names, 'partA'+'separator'+'partB'
        if nameSeparator is not None and type(nameSeparator) is str and len(nameSeparator.strip()) > 0:
            self.set_NameSeparator(nameSeparator)
        elif 'nameSeparator' in kwargsB and type(kwargsB['nameSeparator']) is str and len(kwargsB['nameSeparator'].strip()) > 0:
            self.set_NameSeparator(kwargsB['nameSeparator'])
        if self.nameSeparator in [None, '', False] and ':' in ' '.join(list(map(str, self.columns))):
            self.nameSeparator = ':'
        if self.nameSeparator in [None, '', False]:
            self.nameSeparator = ''
        if self.nameSeparator is True:
            self.nameSeparator = ':'

        # set autoAppend if provided as argument
        if autoAppend is not None:
            self.autoAppend = bool(autoAppend)
        elif 'autoAppend' in kwargsB and kwargsB['autoAppend'] is not None:
            self.autoAppend = bool(kwargsB['autoAppend'])

        # set operatePerName if provided as argument
        if operatePerName is not None:
            self.operatePerName = bool(operatePerName)
        elif 'operatePerName' in kwargsB and kwargsB['operatePerName'] is not None:
            self.operatePerName = bool(kwargsB['operatePerName'])

    @property
    def _constructor(self):
        return SimDataFrame

    @property
    def _constructor_sliced(self):
        return SimSeries

    @property
    def loc(self) -> _SimLocIndexer:
        """
        wrapper for .loc indexing
        """
        return self.spdLocator

    # @property
    # def iloc(self) -> _iSimLocIndexer:
    #     """
    #     wrapper for .iloc indexing
    #     """
    #     return self.spdiLocator

    @property
    def _class(self):
        return SimDataFrame

    @property
    def _SimParameters(self):
        return {'units':self.units.copy() if type(self.units) is dict else self.units,
                'speak':self.speak if hasattr(self,'speak') else False,
                'indexName':self.index.name,
                'indexUnits':self.indexUnits if hasattr(self,'indexUnits') else None,
                'nameSeparator':self.nameSeparator if hasattr(self,'nameSeparator') else None,
                'intersectionCharacter':self.intersectionCharacter if hasattr(self,'intersectionCharacter') else '∩',
                'autoAppend':self.autoAppend if hasattr(self,'autoAppend') else False,
                'transposed':self.transposed if hasattr(self,'transposed') else False,
                'operatePerName':self.operatePerName if hasattr(self,'operatedPerName') else False,
                }

    def set_indexName(self, Name):
        if type(Name) is str and len(Name.strip()) > 0:
            self.index.name = Name.strip()

    def set_indexUnits(self, Units):
        if type(Units) is str and len(Units.strip()) > 0:
            self.indexUnits = Units.strip()

    def set_NameSeparator(self, separator):
        if type(separator) is str and len(separator) > 0:
            if separator in ['=', '-', '+', '&', '*', '/', '!', '%']:
                print(" the separator '"+separator+"' could be confused with operators.\n it is recommended to use ':' as separator.")
            self.nameSeparator = separator

    def get_NameSeparator(self):
        if self.nameSeparator in [None, '', False]:
            warn(" NameSeparator is not defined.")
            return ''
        else:
            return self.nameSeparator

    def set_index(self, key, drop=False, append=False, inplace=False, verify_integrity=False, **kwargs):
        if type(key) is list:
            if False in [k in self.columns for k in key]:
                k = [str(k) for k in key if k not in self.columns ]
                raise ValueError("The key '"+', '.join(k)+"' is not a column name of this SimDataFrame.")
        elif key not in self.columns:
            raise ValueError("The key '"+str(key)+"' is not a column name of this SimDataFrame.")
        if inplace:
            indexUnits = self.get_Units(key)
            super().set_index(key, drop=drop, append=append, inplace=inplace, verify_integrity=verify_integrity, **kwargs)
            self.set_indexUnits(indexUnits)
        else:
            params = self._SimParameters
            params['index'] = None
            params['indexName'] = None
            params['indexUnits'] = self.get_Units(key)#[key]
            return SimDataFrame(data=self.DF.set_index(key, drop=drop, append=append, inplace=inplace, verify_integrity=verify_integrity, **kwargs), **params)

    def describe(self,*args,**kwargs):
        return self._class(data=self.to_Pandas().describe(*args,**kwargs),**self._SimParameters)

    def shift(self, periods=1, freq=None, axis=0, fill_value=None):
        """
        wrapper for Pandas shift method

        Shift index by desired number of periods with an optional time freq.

        When freq is not passed, shift the index without realigning the data.
        If freq is passed (in this case, the index must be date or datetime,
        or it will raise a NotImplementedError), the index will be increased using the periods and the freq. freq can be inferred when specified as “infer” as long as either freq or inferred_freq attribute is set in the index.

        Parameters
periodsint
Number of periods to shift. Can be positive or negative.

freqDateOffset, tseries.offsets, timedelta, or str, optional
Offset to use from the tseries module or time rule (e.g. ‘EOM’). If freq is specified then the index values are shifted but the data is not realigned. That is, use freq if you would like to extend the index when shifting and preserve the original data. If freq is specified as “infer” then it will be inferred from the freq or inferred_freq attributes of the index. If neither of those attributes exist, a ValueError is thrown.

axis{0 or ‘index’, 1 or ‘columns’, None}, default None
Shift direction.

fill_valueobject, optional
The scalar value to use for newly introduced missing values. the default depends on the dtype of self. For numeric data, np.nan is used. For datetime, timedelta, or period data, etc. NaT is used. For extension dtypes, self.dtype.na_value is used.

Changed in version 1.1.0.

Returns
SimDataFrame
Copy of input object, shifted.

        """
        return SimDataFrame(data=self.DF.shift(periods=periods, freq=freq, axis=axis, fill_value=fill_value), **self._SimParameters)

    def to_excel(self, excel_writer, split_by=None, sheet_name=None, na_rep='', float_format=None, columns=None,
                 header=True, units=True, index=True, index_label=None, startrow=0, startcol=0, engine=None,
                 merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, sort=None,
                 format_header=True):
        """
        Wrapper of .to_excel method from Pandas.
        On top of Pandas method this method is able to split the data into different
        sheets based on the column names. See paramenters `split_by´ and `sheet_name´.

        Write {klass} to an Excel sheet.
        To write a single {klass} to an Excel .xlsx file it is only necessary to
        specify a target file name. To write to multiple sheets it is necessary to
        create an `ExcelWriter` object with a target file name, and specify a sheet
        in the file to write to.
        Multiple sheets may be written to by specifying unique `sheet_name`.
        With all data written to the file it is necessary to save the changes.
        Note that creating an `ExcelWriter` object with a file name that already
        exists will result in the contents of the existing file being erased.

        Parameters
        ----------
        excel_writer : str or ExcelWriter object from Pandas.
            File path or existing ExcelWriter.
        split_by: None, positive or negative integer or str 'left', 'right' or 'first'. Default is None
            If is string 'left' or 'right', creates a sheet grouping the columns by
            the corresponding left:right part of the column name.
            If is string 'first', creates a sheet grouping the columns by
            the first character of the column name.
            If None, all the columns will go into the same sheet.
            if integer i > 0, creates a sheet grouping the columns by the 'i' firsts
            characters of the column name indicated by the integer.
            if integer i < 0, creates a sheet grouping the columns by the 'i' last
            the number characters of the column name indicated by the integer.
        sheet_name : None or str, default None
            Name of sheet which will contain DataFrame.
            If None:
                the `left` or `right` part of the name will be used if is unique,
                or 'FIELD', 'WELLS', 'GROUPS' or 'REGIONS' if all the column names
                start with 'F', 'W', 'G' or 'R'.
            else 'Sheet1' will be used.
        na_rep : str, default ''
            Missing data representation.
        float_format : str, optional
            Format string for floating point numbers. For example
            ``float_format="%.2f"`` will format 0.1234 to 0.12.
        columns : sequence or list of str, optional
            Columns to write.
        header : bool or list of str, default True
            Write out the column names. If a list of string is given it is
            assumed to be aliases for the column names.
        units : bool, default True
            Write the units of the column under the header name.
        index : bool, default True
            Write row names(index).
        index_label : str or sequence, optional
            Column label for index column(s) if desired. If not specified, and
            `header` and `index` are True, then the index names are used. A
            sequence should be given if the DataFrame uses MultiIndex.
        startrow : int, default 0
            Upper left cell row to dump data frame.
        startcol : int, default 0
            Upper left cell column to dump data frame.
        engine : str, optional
            Write engine to use, 'openpyxl' or 'xlsxwriter'. You can also set this
            via the options ``io.excel.xlsx.writer``, ``io.excel.xls.writer``, and
            ``io.excel.xlsm.writer``.
        merge_cells : bool, default True
            Write MultiIndex and Hierarchical Rows as merged cells.
        encoding : str, optional
            Encoding of the resulting excel file. Only necessary for xlwt,
            other writers support unicode natively.
        inf_rep : str, default 'inf'
            Representation for infinity(there is no native representation for
            infinity in Excel).
        verbose : bool, default True
            Display more information in the error logs.
        freeze_panes : tuple of int(length 2), optional
            Specifies the one-based bottommost row and rightmost column that
            is to be frozen.
        sort: None, bool or int
            if None, default behaviour depends on split_by parameter:
                if split_by is None will keep the current order of the columns in the SimDataFrame.
                if split_by is not None will sort alphabetically ascending the names of the columns.
            if True (bool) will sort the columns alphabetically ascending.
            if False (bool) will maintain the current order.
            if int > 0 will sort the columns alphabetically ascending.
            if int < 0 will sort the columns alphabetically descending.
            if int == 0 will keep the current order of the columns.

        """
        # if header is not requiered and sheet_name is str, directly pass it to Pandas
        if(not header and type(sheet_name) is str ) or(not units and type(sheet_name) is str ):
            self.DF.to_excel(excel_writer, sheet_name=sheet_name, na_rep=na_rep, float_format=float_format, columns=columns, header=False, index=index, index_label=index_label, startrow=startrow, startcol=startcol, engine=engine, merge_cells=merge_cells, encoding=encoding, inf_rep=inf_rep, verbose=verbose, freeze_panes=freeze_panes)

        # helper function
        firstChar = lambda s : str(s)[0]
        lastChar = lambda s : str(s)[-1]
        iChar = lambda s : lambda i : str(s)[:i] if i>0 else str(s)[i:]

        # define the columns to be exported
        if type(columns) is str:
            columns = [columns]
        if columns is None:
            cols = list(self.columns)
        else:
            cols = columns.copy()

        # validate split_by parameter
        if type(split_by) is not str and split_by is not None:
            raise ValueError(" `split_by´ parameter must be 'left', 'right', 'first' or None.")

        if type(split_by) is str:
            split_by = split_by.strip().lower()
        if split_by is not None and(len(split_by) == 0 or split_by == 'none' ):
            split_by = None

        # define the split and sheet(s) name(s)
        if split_by is None : # no split_by, use a single sheet
            if sheet_name is None : # generate the sheet name
                if len(self[cols].left) == 1:
                    names = self[cols].left
                elif len(self[cols].right) == 1:
                    names = self[cols].right
                elif len(set(map(firstChar, cols))) == 1:
                    names = list(set(map(firstChar, cols)))[0]
                    if names == 'F':
                        names =('FIELD', )
                    elif names == 'W':
                        names =('WELLS', )
                    elif names == 'G':
                        names =('GROUPS', )
                    elif names == 'R':
                        names =('REGIONS', )
                    elif names == 'C':
                        names =('CONNECTIONS', )
                    else:
                        names =('Sheet1', )
                else:
                    names =('Sheet1', )
            else: # use the provided sheet_name
                if type(sheet_name) is not str:
                    raise TypeError("'sheet_name' must be a string.")
                if len(sheet_name) > 32 and verbose:
                    print(" the sheet_name '"+sheet_name+"' is longer than 32 characters, \n will be but to the first 32 characters: '"+sheet_name[:32]+"'")
                names =(sheet_name[:32], )

        elif type(split_by) is str:
            if split_by == 'left':
                names = tuple(sorted(self[cols].left))
            elif split_by == 'right':
                names = tuple(sorted(self[cols].right))
            elif split_by == 'first':
                names = tuple(sorted(set(map(firstChar, cols))))
            elif split_by == 'last':
                names = tuple(sorted(set(map(lastChar, cols))))

        elif type(split_by) is int:
            if split_by == 0:
                raise ValueError(" integer `split_by´ parameter must be positive or negative, not zero.")
            else:
                names = tuple(sorted(set([iChar(c)(split_by) for c in cols] )))

        else:
            raise ValueError(" `split_by´ parameter must be 'left', 'right', 'first', 'last', an integer or None.")

        # initialize an instance of ExcelWriter or use the instance provided
        from pandas import ExcelWriter
        if isinstance(excel_writer, ExcelWriter):
            SDFwriter = excel_writer
        elif type(excel_writer) is str:
            if excel_writer.strip().lower().endswith('.xlsx'):
                pass  # ok
            elif excel_writer.strip().lower().endswith('.xls'):
                if verbose:
                    print(" the file")
            SDFwriter = ExcelWriter(excel_writer, engine='xlsxwriter')
        else:
            raise ValueError(" `excel_writer´ parameter must be a string path to an .xlsx file or an ExcelWriter instance.")

        headerRows = 2 if header is True else 0

        if index:
            if self.index.name is None:
                indexName =('', )
            if type(self.index) is pd.core.indexes.multi.MultiIndex:
                indexName = tuple(self.index.names)
            else:
                indexName =(self.index.name, )
            indexUnits = '' if self.indexUnits is None else self.indexUnits
            indexCols = len(self.index.names) if type(self.index) is pd.core.indexes.multi.MultiIndex else 1

        if freeze_panes is None:
            freeze_panes =(startrow+headerRows, startcol+(indexCols if index else 0))

        # if single name, simpy write the output using .to_excel method from Pandas
        for i in range(len(names)):

            # get the columns for this sheet
            if split_by is None:
                if sort is None:
                    colselect = tuple(cols)
                elif int(sort) > 0:
                    colselect = tuple(sorted(cols))
                elif int(sort) < 0:
                    colselect = tuple(sorted(cols)[::-1])
                else:
                    colselect = tuple(cols)

            elif split_by == 'left':
                if sort is None:
                    colselect = tuple(sorted(fnmatch.filter(cols, names[i]+'*' )))
                elif int(sort) > 0:
                    colselect = tuple(sorted(fnmatch.filter(cols, names[i]+'*' )))
                elif int(sort) < 0:
                    colselect = tuple(sorted(fnmatch.filter(cols, names[i]+'*' ))[::-1])
                else:
                    colselect = tuple(fnmatch.filter(cols, names[i]+'*' ))

            elif split_by == 'right':
                if sort is None:
                    colselect = tuple(sorted(fnmatch.filter(cols, '*'+names[i] )))
                elif int(sort) > 0:
                    colselect = tuple(sorted(fnmatch.filter(cols, '*'+names[i] )))
                elif int(sort) < 0:
                    colselect = tuple(sorted(fnmatch.filter(cols, '*'+names[i] ))[::-1])
                else:
                    colselect = tuple(fnmatch.filter(cols, '*'+names[i] ))

            elif split_by == 'first':
                if sort is None:
                    colselect = tuple(sorted(fnmatch.filter(cols, names[i][0]+'*' )))
                elif int(sort) > 0:
                    colselect = tuple(sorted(fnmatch.filter(cols, names[i][0]+'*' )))
                elif int(sort) < 0:
                    colselect = tuple(sorted(fnmatch.filter(cols, names[i][0]+'*' ))[::-1])
                else:
                    colselect = tuple(fnmatch.filter(cols, names[i][0]+'*' ))

            elif split_by == 'last':
                if sort is None:
                    colselect = tuple(sorted(fnmatch.filter(cols, '*'+names[i][-1] )))
                elif int(sort) > 0:
                    colselect = tuple(sorted(fnmatch.filter(cols, '*'+names[i][-1] )))
                elif int(sort) < 0:
                    colselect = tuple(sorted(fnmatch.filter(cols, '*'+names[i][-1] ))[::-1])
                else:
                    colselect = tuple(fnmatch.filter(cols, names[i][0]+'*' ))

            # write the sheet to the ExcelWriter
            self.DF.to_excel(SDFwriter, sheet_name=names[i], na_rep=na_rep, float_format=float_format, columns=colselect,
                             header=not format_header and header, index=index, index_label=index_label,
                             startrow=startrow+headerRows, startcol=startcol, engine=engine, merge_cells=merge_cells,
                             encoding=encoding, inf_rep=inf_rep, verbose=verbose, freeze_panes=freeze_panes)

            # Get the xlsxwriter workbook and worksheet objects.
            SDFworkbook  = SDFwriter.book
            SDFworksheet = SDFwriter.sheets[names[i]]

            if header and format_header:
                header_format = SDFworkbook.add_format({'bold': True, 'font_size': 11})
                units_format = SDFworkbook.add_format({'italic': True})

                # add the index name and units to the header
                if index:
                    colselect = indexName+colselect

                # write the column header, name and units
                for c in range(len(colselect)):
                    colUnit = ''
                    if colselect[c] in self.units:
                        colUnit = self.units[colselect[c]]
                    SDFworksheet.write(startrow, startcol+c, colselect[c], header_format)
                    SDFworksheet.write(startrow+1, startcol+c, colUnit, units_format)

        if isinstance(excel_writer, ExcelWriter):
            return SDFwriter
        elif type(excel_writer) is str:
            SDFwriter.save()

    def transpose(self):
        params = self._SimParameters
        params['transposed'] = not self.transposed
        return SimDataFrame(data=self.DF.T, **params)

    @property
    def T(self):
        return self.transpose()

    def as_Pandas(self):
        return self.to_DataFrame()

    def to_pandas(self):
        return self.to_DataFrame()

    def to_Pandas(self):
        return self.to_DataFrame()

    def to_DataFrameMultiIndex(self):
        return self._DataFrameWithMultiIndex()

    def to_DataFrame(self):
        return DataFrame(self).copy()

    def as_DataFrame(self):
        return DataFrame(self)

    def to_Series(self):
        return self.to_SimSeries().to_Series()

    def to_SimSeries(self):
        if len(self.columns) == 1:
            return self[self.columns[0]]
        if len(self) <= 1:
            return SimSeries(data=Series(self.DF.iloc[0].to_list(), name=self.index[0], index=self.columns.to_list()) , **self._SimParameters)
        raise TypeError('Not possioble to converto to SimSeries')

    @property
    def Series(self):
        return self.to_Series()

    @property
    def SimSeries(self):
        return self.to_SimSeries()

    @property
    def S(self):
        return self.to_SimSeries()

    @property
    def SS(self):
        return self.to_SimSeries()

    @property
    def s(self):
        return self.to_SimSeries()

    @property
    def ss(self):
        return self.to_SimSeries()


    @property
    def DataFrame(self):
        return self.as_DataFrame()

    @property
    def DF(self):
        return self.as_DataFrame()

    @property
    def df(self):
        return self.as_DataFrame()

    def squeeze(self,axis=None):
        """
        wrapper of pandas.squeeze

        SimDataFrame without units or unitless are squeezed to a DataFrame.
        SimDataFrame with a single row or column are squeezed to a SimSeries.
        SimDataFrame with a single row or column and without units or unitless are squeezed to a Series.
        SimDataFrame with a single element and no units (or unitless) are squeezed to a scalar.

        Parameters
        ----------
        axis : {0 or ‘index’, 1 or ‘columns’, None}, default None
            A specific axis to squeeze. By default, all length-1 axes are squeezed., optional

        Returns
        -------
        SimDataFrame, DataFrame, SimSeries, Series, or scalar
            The projection after squeezing axis or all the axes. and units

        """
        if len(self.columns) == 1 or len(self.index) == 1:
            return self.to_SimSeries().squeeze()
        elif len(self.get_Units()) == 0 or np.array([(u is None or str(u).lower().strip() in ['unitless','dimensionless']) for u in self.get_Units().values()]).all():
            return self.as_DataFrame()
        else:
            return self

    def to(self, units):
        """
        returns the dataframe converted to the requested units if possible,
        else returns None
        """
        return self.convert(units)

    @property
    def indexName(self):
        return self.index.name

    def reset_index(self,level=None, drop=False, inplace=False, col_level=0, col_fill=''):
        if inplace:
            indexUnits, indexName = self.indexUnits, None if drop else self.index.name
            super().reset_index(level=level, drop=drop, inplace=inplace, col_level=col_level, col_fill='')
            if type(self.indexUnits) in (str, dict) and indexName is not None:
                self.set_Units(indexUnits,indexName)
            self.index.name = None
        else:
            result = SimDataFrame(
                data=self.DF.reset_index(level=level, drop=drop, inplace=inplace, col_level=col_level, col_fill=''),
                **self._SimParameters)
            if not drop and type(self.indexUnits) in (str, dict) and self.index.name is not None:
                result.set_Units(self.indexUnits, item=self.index.name)
            result.index.name = None
            return result

    def append(self, other, ignore_index=False, verify_integrity=False, sort=False):
        """
        wrapper of Pandas.DataFrame append method considering the units of both Frames

        Append rows of other to the end of caller, returning a new object.

        Parameters
        ----------
        other : SimDataFrame, SimSeries or DataFrame, Series/dict-like object, or list of these
            The data to append.

        ignore_index : bool, default False
            If True, the resulting axis will be labeled 0, 1, …, n - 1.

        verify_integrity: bool, default False
            If True, raise ValueError on creating index with duplicates.

        sort : bool, default False
            Sort columns if the columns of self and other are not aligned.

        Changed in version 1.0.0: Changed to not sort by default.

        Returns
        -------
            SimDataFrame
        """

        if type(other) in (SimDataFrame,SimSeries):
            otherC = other.copy()
            newUnits = self.get_units(self.columns).copy()
            for col, units in self.get_units(self.columns).items():
                if col in otherC.columns:
                    if units != otherC.get_units(col)[col]:
                        if convertibleUnits(otherC.get_units(col)[col], units):
                            otherC[col] = otherC[col].to(units)
                        else:
                            newUnits[col+'_2nd'] = otherC.get_units(col)[col]
                            otherC.rename(columns={col:col+'_2nd'},inplace=True)
            for col in otherC.columns:
                if col not in newUnits:
                    newUnits[col] = otherC.get_units(col)[col]
            params = self._SimParameters
            params['units'] = newUnits
            # return SimDataFrame(data=self.DF.append(otherC), **params)
            return SimDataFrame(data=pd.concat([self.DF, otherC], axis=0), **params)
        else:
            # append and return SimDataFrame
            # return SimDataFrame(data=self.DF.append(other), **self._SimParameters)
            return SimDataFrame(data=pd.concat([self.DF, other], axis=0), **self._SimParameters)

    def convert(self, units):
        """
        returns the dataframe converted to the requested units if possible,
        else returns None
        """
        if self.transposed:
            result = self.transpose().convert(units)
            if result is not None:
                return result.transpose()
            else:
                return None
        if type(units) is str:
            result = self.copy()
            valid = False
            for col in self.columns:
                if convertibleUnits(self.get_Units(col)[col], units ):
                    result[col] = self[col].to(units)
                    valid = True
            if valid:
                return result
        if type(units) not in (str,dict) and hasattr(units,'__iter__'):
            result = self.copy()
            valid = False
            for col in self.columns:
                for ThisUnits in units:
                    if convertibleUnits(self.get_Units(col)[col], ThisUnits ):
                        result[col] = self[col].to(ThisUnits)
                        valid = True
                        break
            if valid:
                return result
            else:
                print('no columns could be to converted to the requested units.')
                return self
        if type(units) is dict:
            # unitsDict = {}
            # for k, v in units.items():
            #     keys = self.find_Keys(k)
            #     if len(keys) > 0:
            #         for each in keys:
            #             unitsDict[each] = v
            unitsDict = { i:v for k,v in units.items() for i in self.find_Keys(k) }
            result = self.copy()
            for col in self.columns:
                if col in unitsDict and convertibleUnits(self.get_Units(col)[col], unitsDict[col] ):
                    result[col] = self[col].to(unitsDict[col]) # convertUnit(self[col].S, self.get_Units(col)[col], unitsDict[col], self.speak ), unitsDict[col]
            return result

    def dropzeros(self,axis='both'):
        """
        alias for .drop_zeros() method
        """
        return self.drop_zeros(axis=axis)

    def drop_zeros(self, axis='both', inplace=False):
        """
        drop the axis(rows or columns) where all the values are zeross.

        axis parameter can be:
            'columns' or 1 : removes all the columns fill with zeroes
            'index' or 'rows' 0 : removes all the rows fill with zeroes
            'both' or 2 : removes all the rows and columns fill with zeroes
        """
        axis = _cleanAxis(axis)
        if inplace:
            if axis in ['both', 2]:
                self.replace(0, np.nan, inplace=True)
                self.dropna(axis='columns', how='all', inplace=True)
                self.dropna(axis='index', how='all', inplace=True)
                self.dropna(axis='columns', how='all', inplace=True)
                self.replace(np.nan, 0, inplace=True)
            elif axis in ['rows', 'row', 'index', 0]:
                self.replace(0, np.nan, inplace=True)
                self.dropna(axis='index', how='all', inplace=True)
                self.replace(np.nan, 0, inplace=True)
            elif axis in ['columns', 'column', 'col', 'cols', 1]:
                self.replace(0, np.nan, inplace=True)
                self.dropna(axis='columns', how='all', inplace=True)
                self.replace(np.nan, 0, inplace=True)
            else:
                raise ValueError(" valid `axis´ argument are 'index', 'columns' or 'both'.")
        else:
            if axis in ['both', 2]:
                return self.replace(0, np.nan).dropna(axis='columns', how='all').dropna(axis='index', how='all').dropna(axis='columns', how='all').replace(np.nan, 0)
            elif axis in ['rows', 'row', 'index', 0]:
                return self.replace(0, np.nan).dropna(axis='index', how='all').replace(np.nan, 0)
            elif axis in ['columns', 'column', 'col', 'cols', 1]:
                return self.replace(0, np.nan).dropna(axis='columns', how='all').replace(np.nan, 0)
            else:
                raise ValueError(" valid `axis´ argument are 'index', 'columns' or 'both'.")


    def dropna(self, axis='index', how='all', thresh=None, subset=None, inplace=False):
        axis = _cleanAxis(axis)
        if subset is not None:
            if type(subset) is str and subset in self.columns:
                pass
            elif len(self.find_Keys(subset)) > 0:
                subset = list(self.find_Keys(subset))

        if inplace:
            super().dropna(axis=axis, how=how, thresh=thresh, subset=subset, inplace=inplace)
            return None
        else:
            return SimDataFrame(data=self.DF.dropna(axis=axis, how=how, thresh=thresh, subset=subset, inplace=inplace), **self._SimParameters)

    def drop(self, labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise'):
        axis = _cleanAxis(axis)
        if labels is not None:
            if axis == 1 and type(labels) is not str and hasattr(labels,'__iter__'):
                labels = list(self.find_Keys(labels))
            elif axis == 1 and labels not in self.columns:
                if len(self.find_Keys(labels)) > 0:
                    labels = list(self.find_Keys(labels))
            elif axis == 0 and labels not in self.index:
                filt = [labels in str(ind) for ind in self.index]
                labels = self.index[filt]
        elif columns is not None:
            if type(columns) is not list and columns not in self.columns:
                if len(self.find_Keys(columns)) > 0:
                    columns = list(self.find_Keys(columns))
        if inplace:
            super().drop(labels=labels, axis=axis, index=index, columns=columns, level=level, inplace=inplace, errors=errors)
            return None
        else:
            return SimDataFrame(data=self.DF.drop(labels=labels, axis=axis, index=index, columns=columns, level=level, inplace=inplace, errors=errors), **self._SimParameters)

    def drop_duplicates(self, subset=None, keep='first', inplace=False, ignore_index=False):
        if inplace:
            super().drop_duplicates(subset=subset, keep=keep, inplace=inplace, ignore_index=ignore_index)
        else:
            return SimDataFrame(data=self.DF.drop_duplicates(subset=subset, keep=keep, inplace=inplace, ignore_index=ignore_index), **self._SimParameters)

    def fillna(self, value=None, method=None, axis='index', inplace=False, limit=None, downcast=None):
        axis = _cleanAxis(axis)
        if inplace:
            super().fillna(value=value, method=method, axis=axis, inplace=inplace, limit=limit, downcast=downcast)
        else:
            return SimDataFrame(data=self.DF.fillna(value=value, method=method, axis=axis, inplace=inplace, limit=limit, downcast=downcast), **self._SimParameters)

    def interpolate(self, method='slinear', axis='index', limit=None, inplace=False, limit_direction=None, limit_area=None, downcast=None, **kwargs):
        axis = _cleanAxis(axis)
        if inplace:
            super().interpolate(method=method, axis=axis, limit=limit, inplace=inplace, limit_direction=limit_direction, limit_area=limit_area, downcast=downcast, **kwargs)
        else:
            return SimDataFrame(data=self.DF.interpolate(method=method, axis=axis, limit=limit, inplace=inplace, limit_direction=limit_direction, limit_area=limit_area, downcast=downcast, **kwargs), **self._SimParameters )

    def replace(self, to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad'):
        if inplace:
            super().replace(to_replace=to_replace, value=value, inplace=inplace, limit=limit, regex=regex, method=method)
        else:
            return SimDataFrame(data=self.DF.replace(to_replace=to_replace, value=value, inplace=inplace, limit=limit, regex=regex, method=method), **self._SimParameters)

    # def groupby(self, by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False, dropna=True):
    #     axis = _cleanAxis(axis)
    #     selfGrouped = self.DF.groupby(by=by, axis=axis, level=level, as_index=as_index, sort=sort, group_keys=group_keys, squeeze=squeeze, observed=observed, dropna=dropna)
    #     return SimDataFrame(data=selfGrouped, **self._SimParameters )

    def daily(self, outBy='mean', datetimeIndex=False, by=None,
              complete_index=False, fillna_method=None, **kwargs):
        """
        return a dataframe with a single row per day.
        index must be a date type.

        available gropuing calculations are:
            first : keeps the fisrt row per day
            last : keeps the last row per day
            max : returns the maximum value per year
            min : returns the minimum value per year
            mean or avg : returns the average value per year
            median : returns the median value per month
            std : returns the standard deviation per year
            sum : returns the summation of all the values per year
            count : returns the number of rows per year

        by :  label or list of labels, optional.
            Used to determine the groups for the groupby.
            If by is a function, it’s called on each value of the object’s index.
            If a dict or Series is passed, the Series or dict VALUES will be used
            to determine the groups (the Series’ values are first aligned; see .align() method).
            If an ndarray is passed, the values are used as-is to determine the groups.
            A label or list of labels may be passed to group by the columns in self.
            Notice that a tuple is interpreted as a (single) key.

        complete_index : bool, optional. Default False
            Will reindex the dataframe to new index containing every day between
            the first and the last dates in the input index.
            If set to True, by default will autocomplete the null values using
            linear interpolation considering the length of time intervals from
            the index.
            This behavior can be changed by setting the `fillna´ parameter.

        fillna_method : str or False, optional. Default is False
            If not False, will fill null values using the indicated method.
            Available method to fill NA are the methods from Pandas fillna and
            Pandas interpolate.
            Methods from fillna:
                'pad' / 'ffill': propagate last valid observation forward to
                                 next valid observation.
                'backfill' / 'bfill': use next valid observation to fill gap.
            Methods from interpolate:
                'linear': Ignore the index and treat the values as equally spaced.
                'time': Works on daily and higher resolution data to interpolate given length of interval.
                'index', 'values': use the actual numerical values of the index.
            Methods from scipy.interpolate.interp1d (passed from interpolate):
                'nearest'
                'zero'
                'slinear'
                'quadratic'
                'cubic'
                'spline'
                'barycentric'
                'polynomial'
                These methods use the numerical values of the index.
                Both 'polynomial' and 'spline' require that you also specify
                an order (int), e.g.
                    df.daily(fillna_method='polynomial', order=5).

        """
        if type(self.index) is not pd.DatetimeIndex:
            raise TypeError('index must be of datetime type.')

        if fillna_method in ['polynomial', 'spline']:
            if 'order' not in kwargs:
                raise ValueError("The '" + fillna_method + "' fillna_method requieres one additional parameter 'order':\n   df.daily(fillna_method='polynomial', order=5)")
            if type(kwargs['order']) is not int:
                raise ValueError("The 'order' parameter must be an integer:\n   df.daily(fillna_method='polynomial', order=5)")

        if type(outBy) is bool and type(datetimeIndex) is bool:
            outBy, datetimeIndex = 'mean', outBy
        elif type(outBy) is bool and type(datetimeIndex) is not bool:
            outBy, datetimeIndex = datetimeIndex, outBy

        if by is None:
            by = []
        elif type(by) is not str and hasattr(by,'__iter__'):
            # newBy = []
            # for each in by:
            #     if each in self.columns:
            #         newBy.append(each)
            # by = newBy
            by = [each for each in by if each in self.columns]
        elif by in self.columns:
            by =  [by]
        else:
            by =  [by]  # raise ValueError(str(by) + ' is not a column in this dataframe')
        userby = by if len(by) > 0 else None
        by = [self.index.year, self.index.month, self.index.day] + by

        result = self.DF.groupby(by=by)
        if outBy == 'first':
            result = result.first()
        elif outBy == 'last':
            result = result.last()
        elif outBy == 'max':
            result = result.max()
        elif outBy == 'min':
            result = result.min()
        elif outBy in ['mean', 'avg']:
            result = result.mean()
        elif outBy == 'median':
            result = result.median()
        elif outBy == 'std':
            result = result.std()
        elif outBy == 'sum':
            result = result.sum()
        elif outBy == 'count':
            result = result.count()
        elif outBy in ['int', 'integrate', 'integral', 'cum', 'cumulative', 'representative']:
            result = self.integrate()
            result = result.DF.groupby(by=by)  # [self.index.year, self.index.month, self.index.day]
            index = DataFrame(data=self.index, index=self.index ).groupby(by=by)  # [self.index.year, self.index.month, self.index.day]
            index = np.append(index.first().to_numpy(), index.last().to_numpy()[-1])
            deltaindex = np.diff(index)
            if isinstance(self.index, DatetimeIndex):
                deltaindex = deltaindex.astype('timedelta64[s]').astype('float64')/60/60/24
            values = result.first().append(result.last().iloc[-1])
            deltavalues = np.diff(values.transpose())
            result = DataFrame(data=(deltavalues/deltaindex).transpose(), index=result.first().index, columns=self.columns)
        else:
            raise ValueError(" outBy parameter is not valid.")

        if complete_index:
            if len(by) > 3:  # user criteria to group by
                indexBackup = pd.MultiIndex.from_tuples([(int(i[0]), int(i[1]), int(i[2])) for i in result.index])
                result.index = pd.MultiIndex.from_tuples([tuple(i[3:]) for i in result.index]) if len(by) > 4 else [i[3] for i in result.index]
                result.index.names = by[3:]
                result = result.reset_index()
            else:
                indexBackup = result.index

            result.index = pd.to_datetime([str(YYYY) + '-' + str(MM).zfill(2)+  '-' + str(DD).zfill(2) for YYYY, MM, DD in indexBackup])
            result.index.name = 'DATE'
            if len(by) == 4:
                newDF = None
                for group in result[by[3]].unique():
                    groupDF = result[result[by[3]] == group]
                    if len(groupDF) == 0:
                        continue
                    daily_index = pd.date_range(min(groupDF.index), max(groupDF.index), freq='D')
                    groupDF = groupDF.reindex(index=daily_index)

                    if fillna_method is False:
                        pass
                    elif fillna_method is None:
                        groupDF = groupDF.interpolate(method='time').fillna(method='pad')
                    elif fillna_method in ['pad', 'ffill', 'backfill', 'bfill']:
                        groupDF = groupDF.fillna(method=fillna_method)
                    elif fillna_method in ['linear', 'time', 'index', 'values', 'nearest',
                                           'zero', 'slinear', 'quadratic', 'cubic', 'barycentric']:
                        groupDF = groupDF.interpolate(method=fillna_method).fillna(method='pad')
                    elif fillna_method in ['polynomial', 'spline']:
                        groupDF = groupDF.interpolate(method=fillna_method, order=kwargs['order']).fillna(method='pad')
                    if newDF is None:
                        newDF = groupDF.copy()
                    else:
                        # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
                        # newDF = newDF.append(groupDF)
                        newDF = pd.concat([newDF, groupDF], axis=0)

            elif len(by) == 3:
                daily_index = pd.date_range(min(result.index), max(result.index), freq='D')
                result = result.reindex(index=daily_index)

                if fillna_method is False:
                    pass
                elif fillna_method is None:
                    result = result.interpolate(method='time')
                elif fillna_method in ['pad', 'ffill', 'backfill', 'bfill']:
                    result = result.fillna(method=fillna_method)
                elif fillna_method in ['linear', 'time', 'index', 'values', 'nearest',
                                       'zero', 'slinear', 'quadratic', 'cubic', 'barycentric']:
                    result = result.interpolate(method=fillna_method)
                elif fillna_method in ['polynomial', 'spline']:
                    result = result.interpolate(method=fillna_method, order=kwargs['order'])
            else:
                raise ValueError('Not able to reindex grouping by more than one column.')

            by = [result.index.year, result.index.month, result.index.day] + by[3:]
            result = result.groupby(by=by).first()

        output = SimDataFrame(data=result, **self._SimParameters)
        if userby is None:
            output.index = pd.MultiIndex.from_tuples([(int(y) ,int(m), int(d)) for y, m, d in output.index])
        elif len(userby) == 1:
            output.index = pd.MultiIndex.from_tuples([(int(i[0]), int(i[1]), int(i[2]),i[3]) for i in output.index])
        else:
            output.index = pd.MultiIndex.from_tuples([(int(i[0]), int(i[1]), int(i[2]),) + tuple(i[3:]) for i in output.index])

        if datetimeIndex:
            if userby is None:
                output.index = pd.to_datetime([str(YYYY) + '-' + str(MM).zfill(2)+  '-' + str(DD).zfill(2) for YYYY, MM, DD in output.index])
                output.index.names = ['DATE']
                output.index.name = 'DATE'
                if 'DATE' not in output.get_Units():
                    output.set_Units('date','DATE')
            elif len(userby) == 1:
                output.index = pd.MultiIndex.from_tuples([(pd.to_datetime(str(i[0]) + '-' + str(i[1]).zfill(2) + '-' + str(i[2]).zfill(2)), i[3]) for i in output.index])
            else:
                output.index = pd.MultiIndex.from_tuples([(pd.to_datetime(str(i[0]) + '-' + str(i[1]).zfill(2) + '-' + str(i[2]).zfill(2)), ) + tuple(i[3:]) for i in output.index])
            if userby is not None:
                output.index.names = ['DATE'] + userby
                output.index.name = 'DATE' + '_' + '_'.join(map(str,userby))
        elif userby is None:
            output.index.names = ['YEAR', 'MONTH', 'DAY']
            output.index.name = 'YEAR_MONTH_DAY'
        else:
            output.index.names = ['YEAR', 'MONTH', 'DAY'] + userby
            output.index.name = 'YEAR_MONTH_DAY' + '_' + '_'.join(map(str,userby))

        if not datetimeIndex:
            if 'YEAR' not in output.get_Units():
                output.set_Units('year','YEAR')
            if 'MONTH' not in output.get_Units():
                output.set_Units('month','MONTH')
            if 'DAY' not in output.get_Units():
                output.set_Units('day','DAY')
        return output

    def monthly(self, outBy='mean', datetimeIndex=False, by=None, day='first'):
        """
        return a dataframe with a single row per month.
        index must be a date type.

        available gropuing calculations are:
            first : keeps the fisrt row per month
            last : keeps the last row per month
            max : returns the maximum value per month
            min : returns the minimum value per month
            mean or avg : returns the average value per month
            median : returns the median value per month
            std : returns the standard deviation per month
            sum : returns the summation of all the values per month
            count : returns the number of rows per month

        datetimeIndex : bool
            if True the index will converted to DateTimeIndex with Day=1 for each month
            if False the index will be a MultiIndex (Year,Month)

        by :  label, or list of labels
            Used to determine the groups for the groupby.
            If by is a function, it’s called on each value of the object’s index.
            If a dict or Series is passed, the Series or dict VALUES will be used
            to determine the groups (the Series’ values are first aligned; see .align() method).
            If an ndarray is passed, the values are used as-is to determine the groups.
            A label or list of labels may be passed to group by the columns in self.
            Notice that a tuple is interpreted as a (single) key.

        day : str or int
            The day of the month to write on the datetime index.
            If integer or string number, this number will be used as the day for the index.
            If string 'first' the first day of the month will be used, always 1.
            If string 'last' the last day of each month will be used.
            Ignored if datetimeIndex is False.
        """
        if day is None:
            day = '01'
        elif type(day) in [int,float]:
            if day > 31 or day < 1:
                raise ValueError("'day' must be between 1 and 31")
            day = str(int(day))
        elif type(day) is str:
            if day.strip().isdigit():
                day = day.strip()
                if int(day) > 31 or int(day) < 1:
                    raise ValueError("'day' must be between 1 and 31")
            elif day.strip().lower() == 'first':
                day = '01'
            elif day.strip().lower() == 'last':
                day = day.strip().lower()
            else:
                raise ValueError("'day' parameter must be an integer or the string 'first'")
        else:
            raise ValueError("'day' parameter must be an integer or the string 'first'")
        day = '-' + day.zfill(2)

        if type(outBy) is bool:
            outBy, datetimeIndex = 'mean', outBy

        if by is None:
            by = []
        elif type(by) is not str and hasattr(by,'__iter__'):
            # newBy = []
            # for each in by:
            #     if each in self.columns:
            #         newBy.append(each)
            # by = newBy
            by = [each for each in by if each in self.columns]
        elif by in self.columns:
            by =  [by]
        else:
            by =  [by]
        userby = by if len(by) > 0 else None
        by = [self.index.year, self.index.month] + by

        try:
            result = self.DF.groupby(by=by)  # [self.index.year, self.index.month]
        except:
            raise TypeError('index must be of datetime type.')
        if outBy == 'first':
            result = result.first()
        elif outBy == 'last':
            result = result.last()
        elif outBy == 'max':
            result = result.max()
        elif outBy == 'min':
            result = result.min()
        elif outBy in ['mean', 'avg']:
            result = result.mean()
        elif outBy == 'median':
            result = result.median()
        elif outBy == 'std':
            result = result.std()
        elif outBy == 'sum':
            result = result.sum()
        elif outBy == 'count':
            result = result.count()
        elif outBy in ['int', 'integrate', 'integral', 'cum', 'cumulative', 'representative']:
            result = self.integrate()
            result = result.DF.groupby(by=by)  # [self.index.year, self.index.month]
            index = DataFrame(data=self.index, index=self.index ).groupby(by=by)  # [self.index.year, self.index.month]
            index = np.append(index.first().to_numpy(), index.last().to_numpy()[-1] )
            deltaindex = np.diff(index)
            if isinstance(self.index, DatetimeIndex):
                deltaindex = deltaindex.astype('timedelta64[s]').astype('float64')/60/60/24
            values = result.first().append(result.last().iloc[-1])
            deltavalues = np.diff(values.transpose())
            result = DataFrame(data=(deltavalues/deltaindex).transpose(), index=result.first().index, columns=self.columns)
        else:
            raise ValueError(" outBy parameter is not valid.")

        output = SimDataFrame(data=result, **self._SimParameters)
        if userby is None:
            output.index = pd.MultiIndex.from_tuples([(int(y),int(m)) for y,m in output.index ])
        elif len(userby) == 1:
            output.index = pd.MultiIndex.from_tuples([(int(i[0]),int(i[1]),i[2]) for i in output.index ])
        else:
            output.index = pd.MultiIndex.from_tuples([(int(i[0]),int(i[1]),) + tuple(i[2:]) for i in output.index ])

        if datetimeIndex:
            if userby is None:
                output.index = pd.to_datetime( [ str(YYYY)+'-'+str(MM).zfill(2)+(day if day != '-last' else '-'+str(daysInMonth(MM,YYYY))) for YYYY,MM in output.index ] )
                output.index.names = ['DATE']
                output.index.name = 'DATE'
                if 'DATE' not in output.get_Units():
                    output.set_Units('date','DATE')
            elif len(userby) == 1:
                #output.index = pd.to_datetime( [ str(i[0])+'-'+str(i[1]).zfill(2)+'-01' for i in output.index ] )
                output.index = pd.MultiIndex.from_tuples([(pd.to_datetime(str(i[0])+'-'+str(i[1]).zfill(2)+ (day if day != '-last' else '-'+str(daysInMonth(i[1],i[0]))) ),i[2],) for i in output.index])
            else:
                output.index = pd.MultiIndex.from_tuples([(pd.to_datetime(str(i[0])+'-'+str(i[1]).zfill(2)+ (day if day != '-last' else '-'+str(daysInMonth(i[1],i[0]))) ),) + tuple(i[2:]) for i in output.index])
            if userby is not None:
                output.index.names = ['DATE'] + userby
                output.index.name = 'DATE' + '_' + '_'.join(map(str,userby))
        elif userby is None:
            output.index.names = ['YEAR', 'MONTH']
            output.index.name = 'YEAR_MONTH'
        else:
            output.index.names = ['YEAR', 'MONTH'] + userby
            output.index.name = 'YEAR_MONTH' + '_' + '_'.join(map(str,userby))
        if not datetimeIndex:
            if 'YEAR' not in output.get_Units():
                output.set_Units('year','YEAR')
            if 'MONTH' not in output.get_Units():
                output.set_Units('month','MONTH')
        return output

    def yearly(self, outBy='mean', datetimeIndex=False, by=None, day='first', month=None):
        """
        return a dataframe with a single row per year.
        index must be a date type.

        available gropuing calculations are:
            first : keeps the fisrt row
            last : keeps the last row
            max : returns the maximum value per year
            min : returns the minimum value per year
            mean or avg : returns the average value per year
            median : returns the median value per month
            std : returns the standard deviation per year
            sum : returns the summation of all the values per year
            count : returns the number of rows per year
            integrate : calculates the numerical integration over the index (a datetime-index) and returns
            representative : calculates the numerical integration of the column over the index (a datetime-index) and then divide it by the elapsed time on between each pair of rows
            cumsum or cumulative : run cumsum over the columns and then return the last value of each year

        datetimeIndex : bool, optional
            if True the index will converted to DateTimeIndex with Day=1 and Month=1 for each year
            if False the index will be a MultiIndex (Year,Month)

        by :  label, or list of labels, optional
            Used to determine the groups for the groupby.
            If by is a function, it’s called on each value of the object’s index.
            If a dict or Series is passed, the Series or dict VALUES will be used
            to determine the groups (the Series’ values are first aligned; see .align() method).
            If an ndarray is passed, the values are used as-is to determine the groups.
            A label or list of labels may be passed to group by the columns in self.
            Notice that a tuple is interpreted as a (single) key.

        day : str or int, optional
            Ignored if datetimeIndex is False.
            The day of the month to write on the datetime index.
            If integer or string number, this number will be used as the day for the index.
            If string 'first' the first day of the 'month' will be used, always 1.
            If string 'last' the last day of 'month' will be used.
            Default is 'first'.

        month : str or int, optional
            Ignored if datetimeIndex is False.
            The month of the year to write on the datetime index.
            If integer or string number, this number will be used as the month for the index.
            If string 'first' the first month of the year will be used, always 1.
            If string 'last' the last month of the year will be used, always 12.
            Default is None.
        """
        monthsnames = {'JAN':1, 'ENE':1, 'GEN':1,
                       'FEB':2,
                       'MAR':3,
                       'APR':4, 'ABR':4,
                       'MAY':5,
                       'JUN':6, 'GIU':6,
                       'JUL':7, 'JLY':7, 'LUG':7,
                       'AUG':8, 'AGO':8,
                       'SEP':9, 'SET':9,
                       'OCT':10, 'OTT':10,
                       'NOV':11,
                       'DEC':12, 'DIC':12, }
        if month is None:
            if str(day).strip().lower() not in ['first','last']:
                raise ValueError("please provide 'month' when requesting a particular day")
        elif type(month) in [int,float]:
            if month > 12 or month < 1:
                raise ValueError("'month' must be between 1 and 12")
            month = str(int(month))
        elif type(month) is str:
            if month.strip().isdigit():
                month = month.strip()
                if int(month) > 12 or int(month) < 1:
                    raise ValueError("'month' must be between 1 and 12")
            elif month.lower() == 'first':
                month = '01'
            elif month.lower() == 'last':
                month = '12'
            elif month.strip().upper()[:3] in monthsnames:
                month = str(monthsnames[month.strip().upper()[:3]])
            else:
                raise ValueError("'month' parameter must be an integer or the string representing a month, or 'first' or 'last'")
        else:
            raise ValueError("'month' parameter must be an integer or the string representing a month, or 'first' or 'last'")
        if day is None:
            day = '01'
        elif type(day) in [int,float]:
            day = str(int(day))
        elif type(day) is str:
            if day.strip().isdigit():
                day = day.strip()
                if int(day) > 31 or int(day) < 1:
                    raise ValueError("'day' must be between 1 and 31")
            elif day.lower() == 'first':
                day = '01'
                if month is None:
                    month = '01'
            elif day.lower() == 'last':
                if month is None:
                    day = '31'
                    month = '12'
                elif int(month) == 2:
                    day = 'last'
                else:
                    day = str(daysInMonth(int(month)))
            else:
                raise ValueError("'day' parameter must be an integer or the string 'first'")
        else:
            raise ValueError("'day' parameter must be an integer or the string 'first'")

        month = '-' + month.zfill(2)
        day = '-' + day.zfill(2)

        if type(outBy) is bool:
            outBy, datetimeIndex = 'mean', outBy

        if by is None:
            by = []
        elif type(by) is not str and hasattr(by,'__iter__'):
            # newBy = []
            # for each in by:
            #     if each in self.columns:
            #         newBy.append(each)
            # by = newBy
            by = [each for each in by if each in self.columns]
        elif by in self.columns:
            by =  [by]
        else:
            by =  [by]
        userby = by if len(by) > 0 else None
        by = [self.index.year] + by
        if len(by) == 1:
            by = by[0]

        try:
            result = self.DF.groupby(by=by)  # self.index.year
        except:
            raise TypeError('index must be of datetime type.')
        if outBy == 'first':
            result = result.first()
        elif outBy == 'last':
            result = result.last()
        elif outBy == 'max':
            result = result.max()
        elif outBy == 'min':
            result = result.min()
        elif outBy in ['mean', 'avg']:
            result = result.mean()
        elif outBy == 'median':
            result = result.median()
        elif outBy == 'std':
            result = result.std()
        elif outBy == 'sum':
            result = result.sum()
        elif outBy == 'count':
            result = result.count()
        elif outBy in ['int', 'integrate', 'integral', 'cum', 'cumulative', 'representative','rep','repr']:
            result = self.integrate()
            result = result.DF.groupby(by=by)  # self.index.year
            index = DataFrame(data=self.index, index=self.index).groupby(by=by)  # self.index.year
            index = np.append(index.first().to_numpy(), index.last().to_numpy()[-1])
            deltaindex = np.diff(index)
            if isinstance(self.index, DatetimeIndex):
                deltaindex = deltaindex.astype('timedelta64[s]').astype('float64')/60/60/24
            # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
            values = result.first().append(result.last().iloc[-1])
            values = pd.concat([result.first(), result.last().iloc[-1]], axis=0)
            deltavalues = np.diff(values.transpose())
            result = DataFrame(data=(deltavalues/deltaindex).transpose(), index=result.first().index, columns=self.columns)
        else:
            raise ValueError(" outBy parameter is not valid.")

        output = SimDataFrame(data=result, **self._SimParameters)
        if userby is None:
            output.index = [ int(y) for y in output.index ]
        elif len(userby) == 1:
            output.index = pd.MultiIndex.from_tuples([(int(i[0]),i[1]) for i in output.index ])
        else:
            output.index = pd.MultiIndex.from_tuples([(int(i[0]),) + tuple(i[1:]) for i in output.index ])

        if datetimeIndex:
            if userby is None:
                output.index = pd.to_datetime( [ str(YYYY)+month+(day if day != '-last' else '-'+str(daysInMonth(month[1:],YYYY))) for YYYY in output.index ] )
                output.index.names = ['DATE']
                output.index.name = 'DATE'
                if 'DATE' not in output.get_Units():
                    output.set_Units('date','DATE')
            elif len(userby) == 1:
                output.index = pd.MultiIndex.from_tuples([(pd.to_datetime(str(i[0])+month+(day if day != '-last' else '-'+str(daysInMonth(month[1:],i[0])))),i[1],) for i in output.index])
            else:
                output.index = pd.MultiIndex.from_tuples([(pd.to_datetime(str(i[0])+month+(day if day != '-last' else '-'+str(daysInMonth(month[1:],i[0])))),) + tuple(i[1:]) for i in output.index])
            if userby is not None:
                output.index.names = ['DATE'] + userby
                output.index.name = 'DATE' + '_' + '_'.join(map(str,userby))
        elif userby is None:
            output.index.names = ['YEAR']
            output.index.name = 'YEAR'
        else:
            output.index.names = ['YEAR',] + userby
            output.index.name = 'YEAR' + '_' + '_'.join(map(str,userby))
        if not datetimeIndex:
            output.set_Units('year','YEAR')
            output.indexUnits = 'year'
        return output

    def aggregate(self, func=None, axis=0, *args, **kwargs):
        axis = _cleanAxis(axis)
        return SimDataFrame(data=self.DF.aggregate(func=func, axis=axis, *args, **kwargs), **self._SimParameters )

    # def resample(self, rule, axis=0, closed=None, label=None, convention='start', kind=None, loffset=None, base=None, on=None, level=None, origin='start_day', offset=None):
    #     axis = _cleanAxis(axis)
    #     return SimDataFrame(data=self.DF.resample(rule, axis=axis, closed=closed, label=label, convention=convention, kind=kind, loffset=loffset, base=base, on=on, level=level, origin=origin, offset=offset), **self._SimParameters )

    def reindex(self, labels=None, index=None, columns=None, axis=None, **kwargs):
        """
        wrapper for pandas.DataFrame.reindex

        labels : array-like, optional
            New labels / index to conform the axis specified by ‘axis’ to.
        index, columns : array-like, optional(should be specified using keywords)
            New labels / index to conform to. Preferably an Index object to avoid duplicating data
        axis : int or str, optional
            Axis to target. Can be either the axis name(‘index’, ‘columns’) or number(0, 1).
        """
        if labels is None and axis is None and index is not None:
            labels = index
            axis = 0
        elif labels is None and axis is None and columns is not None:
            labels = columns
            axis = 1
        elif labels is not None and axis is None and columns is None and index is None:
            if len(labels) == len(self.index):
                axis = 0
            elif len(labels) == len(self.columns):
                axis = 1
            else:
                raise TypeError("labels does not match neither len(index) or len(columns).")
        axis = _cleanAxis(axis)
        return SimDataFrame(data=self.DF.reindex(labels=labels, axis=axis, **kwargs), **self._SimParameters )

    def rename(self, mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore'):
        """
        wrapper of rename function from Pandas.

        Alter axes labels.

        Function / dict values must be unique(1-to-1).
        Labels not contained in a dict / Series will be left as-is.
        Extra labels listed don’t throw an error.

        Parameters:
            mapper: dict-like or function
                Dict-like or functions transformations to apply to that axis’ values.
                Use either mapper and axis to specify the axis to target with mapper,
                or index and columns.

            index: dict-like or function
                Alternative to specifying axis(mapper, axis=0 is equivalent to index=mapper).

            columns: dict-like or function
                Alternative to specifying axis(mapper, axis=1 is equivalent to columns=mapper).

            axis: {0 or ‘index’, 1 or ‘columns’}, default 0
                Axis to target with mapper. Can be either the axis name(‘index’, ‘columns’) or number(0, 1). The default is ‘index’.

            copy: bool, default True
                Also copy underlying data.

            inplace:bool, default False
                Whether to apply the chanes directly in the dataframe.
                Always return a new DataFrame.
                If True then value of copy is ignored.

            level: int or level name, default None
                In case of a MultiIndex, only rename labels in the specified level.

            errors: {‘ignore’, ‘raise’}, default ‘ignore’
                If ‘raise’, raise a KeyError when a dict-like mapper, index, or columns
                contains labels that are not present in the Index being transformed.
                If ‘ignore’, existing keys will be renamed and extra keys will be ignored.
        """
        cBefore = list(self.columns)
        if inplace:
            super().rename(mapper=mapper, index=index, columns=columns, axis=axis, copy=copy, inplace=inplace, level=level, errors=errors)
            cAfter = list(self.columns)
        else:
            catch = super().rename(mapper=mapper, index=index, columns=columns, axis=axis, copy=copy, inplace=inplace, level=level, errors=errors)
            cAfter = list(catch.columns)
        newUnits = {}
        for i in range(len(cBefore)):
            if cBefore[i] in self.units:
                newUnits[cAfter[i]] = self.units[cBefore[i]]
        if inplace:
            self.units = newUnits
            self.spdLocator = _SimLocIndexer("loc", self)
            return None
        else:
            catch.units = newUnits
            catch.spdLocator = _SimLocIndexer("loc", catch)
            return catch

    def rename_item(self, mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore'):
        """
        alias for renameItem method.

        Like the regular rename method but renameItem change all the columns or indexes where the item appears.
        The item is the right part of the column or index name:
                main_part:item_part

        Parameters
        ----------
        mapper : dict, optional
            Dict-like transformations to apply to that axis’ values.
            Use either mapper and axis to specify the axis to target with mapper, or index and columns.
        index : TYPE, optional
            Alternative to specifying axis (mapper, axis=0)
        columns : dict, optional
            Alternative to specifying axis (mapper, axis=1)
        axis : {0 or ‘index’, 1 or ‘columns’}, default 1
            Axis to target with mapper.
            Can be either the axis name (‘index’, ‘columns’) or number (0, 1).
            The default is ‘index’.
        copy : bool, default True
            Also copy underlying data.
        inplace : bool, default False
            Whether to return a new DataFrame. If True then value of copy is ignored.
        level : int or level name, default None
            In case of a MultiIndex, only rename labels in the specified level.
            *** NOT YET IMPLEMENTED ***
        errors : TYPE, optional
            If ‘raise’, raise a KeyError when a dict-like mapper, index, or columns
            contains labels that are not present in the Index being transformed.
            If ‘ignore’, existing keys will be renamed and extra keys will be ignored.

        Returns
        -------
        DataFrame or None
            DataFrame with the renamed axis labels or None if inplace=True.

        """
        return self.renameItem(self, mapper=mapper, index=index, columns=columns, axis=axis, copy=copy, inplace=inplace, level=level, errors=errors)

    def renameItem(self, mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore'):
        """
        Like the regular rename method but renameItem change all the columns or indexes where the item appears.
        The item is the right part of the column or index name:
                main_part:item_part

        Parameters
        ----------
        mapper : dict, optional
            Dict-like transformations to apply to that axis’ values.
            Use either mapper and axis to specify the axis to target with mapper, or index and columns.
        index : TYPE, optional
            Alternative to specifying axis (mapper, axis=0)
        columns : dict, optional
            Alternative to specifying axis (mapper, axis=1)
        axis : {0 or ‘index’, 1 or ‘columns’}, default 1
            Axis to target with mapper.
            Can be either the axis name (‘index’, ‘columns’) or number (0, 1).
            The default is ‘index’.
        copy : bool, default True
            Also copy underlying data.
        inplace : bool, default False
            Whether to return a new DataFrame. If True then value of copy is ignored.
        level : int or level name, default None
            In case of a MultiIndex, only rename labels in the specified level.
            *** NOT YET IMPLEMENTED ***
        errors : TYPE, optional
            If ‘raise’, raise a KeyError when a dict-like mapper, index, or columns
            contains labels that are not present in the Index being transformed.
            If ‘ignore’, existing keys will be renamed and extra keys will be ignored.

        Returns
        -------
        DataFrame or None
            DataFrame with the renamed axis labels or None if inplace=True.

        """
        def _itemColumns(sdf, itemMapper, axis):
            itemsDict = {}
            for item in itemMapper:
                pattern = '*'+sdf.nameSeparator+str(item)
                keys = tuple(fnmatch.filter(map(str,tuple(sdf.columns if axis == 1 else sdf.index)), pattern))
                kMapper = { k:k.replace(sdf.nameSeparator+str(item), sdf.nameSeparator+str(itemMapper[item])) for k in keys }
                itemsDict.update(kMapper)
            return itemsDict

        if mapper is not None:
            if axis is None:
                axis = 1
            elif type(axis) is str:
                axis = {'index':0, 'columns':1}
            mapper = _itemColumns(self, mapper, axis)
        elif index is not None:
            index = _itemColumns(self, index, 0)
        elif columns is not None:
            columns = _itemColumns(self, columns, 1)
        return self.rename(mapper=mapper, index=index, columns=columns, axis=axis, copy=copy, inplace=inplace, level=level, errors=errors)

    @property
    def right(self):
        if self.nameSeparator is None or self.nameSeparator is False or self.nameSeparator in ['']:
            return tuple(self.columns)
        objs = []
        for each in list(self.columns):
            if self.nameSeparator in each:
                objs += [each.split(self.nameSeparator)[-1]]
            else:
                objs += [each]
        return tuple(set(objs))

    @property
    def left(self):
        if self.nameSeparator is None or self.nameSeparator is False or self.nameSeparator in ['']:
            return tuple(self.columns)
        objs = []
        for each in list(self.columns):
            if self.nameSeparator in each:
                objs += [each.split(self.nameSeparator)[0]]
            else:
                objs += [each]
        return tuple(set(objs))

    def renameRight(self, inplace=False):
        if self.nameSeparator in [None, '', False]:
            return self  # raise ValueError("name separator must not be None")
        objs = {}
        for each in list(self.columns ):
            if type(each) is str and self.nameSeparator in each:
                objs[each] = each.split(self.nameSeparator )[-1]
                # self.units[ each.split(self.nameSeparator )[-1] ] = self.units[ each ]
                # del(self.units[each])
            else:
                objs[each] = each
        if len(set(objs.keys())) != len(set(objs.values())):
            objs = dict( zip(objs.keys(),objs.keys()) )
        if inplace:
            self.rename(columns=objs, inplace=inplace)
        else:
            return self.rename(columns=objs, inplace=inplace)

    def renameLeft(self, inplace=False):
        if self.nameSeparator in [None, '', False]:
            return self #  raise ValueError("name separator must not be None")
        objs = {}
        for each in list(self.columns ):
            if type(each) is str and self.nameSeparator in each:
                objs[each] = each.split(self.nameSeparator )[0]
                # self.units[ each.split(self.nameSeparator )[0] ] = self.units[ each ]
                # del(self.units[each])
            else:
                objs[each] = each
        if len(set(objs.keys())) != len(set(objs.values())):
            objs = dict( zip(objs.keys(),objs.keys()) )
        if inplace:
            self.rename(columns=objs, inplace=inplace)
        else:
            return self.rename(columns=objs, inplace=inplace)

    def _CommonRename(self, SimDataFrame1, SimDataFrame2=None, LR=None):
        cha = self.intersectionCharacter

        if LR is not None:
            LR = LR.upper()
            if LR not in 'LR':
                LR = None

        if SimDataFrame2 is None:
            SDF1, SDF2 = self, SimDataFrame1
        else:
            SDF1, SDF2 = SimDataFrame1, SimDataFrame2

        if type(SDF1) is not SimDataFrame:
            raise TypeError("both dataframes to be compared must be SimDataFrames.")
        if type(SDF2) is not SimDataFrame:
            raise TypeError("both dataframes to be compared must be SimDataFrames.")

        if SDF1.nameSeparator is None or SDF2.nameSeparator is None:
            raise ValueError("the 'nameSeparator' must not be empty in both SimDataFrames.")

        if LR == 'L' or (LR is None and len(SDF1.left) == 1 and len(SDF2.left) == 1):
            SDF2C = SDF2.copy()
            SDF2C.renameRight(inplace=True)
            SDF1C = SDF1.copy()
            SDF1C.renameRight(inplace=True)
            commonNames = {}
            for c in SDF1C.columns:
                if c in SDF2C.columns:
                    commonNames[c] = SDF1.left[0] + cha + SDF2.left[0] + SDF1.nameSeparator + c
                else:
                    commonNames[c] = SDF1.left[0] + SDF1.nameSeparator + c
            for c in SDF2C.columns:
                if c not in SDF1C.columns:
                    commonNames[c] = SDF2.left[0] + SDF1.nameSeparator + c
            if LR is None and len(commonNames) > 1:
                alternative = self._CommonRename(SDF1, SDF2, LR='R')
                if len(alternative[2]) < len(commonNames):
                    return alternative

        elif LR == 'R' or (LR is None and len(SDF1.right) == 1 and len(SDF2.right) == 1):
            SDF2C = SDF2.copy()
            SDF2C.renameLeft(inplace=True)
            SDF1C = SDF1.copy()
            SDF1C.renameLeft(inplace=True)
            commonNames = {}
            for c in SDF1C.columns:
                if c in SDF2C.columns:
                    commonNames[c] = c + SDF1.nameSeparator + SDF1.right[0] + cha + SDF2.right[0]
                else:
                    commonNames[c] = c + SDF1.nameSeparator + SDF1.right[0]
            for c in SDF2C.columns:
                if c not in SDF1C.columns:
                    commonNames[c] = c + SDF1.nameSeparator + SDF2.right[0]
            if LR is None and len(commonNames) > 1:
                alternative = self._CommonRename(SDF1, SDF2, LR='L')
                if len(alternative[2]) < len(commonNames):
                    return alternative

        else:
            SDF1C, SDF2C = SDF1, SDF2.copy()
            commonNames = None

        return SDF1C, SDF2C, commonNames

    def _JoinedIndex(self, other, *, drop_duplicates=False, keep='first'):
        return _MergeIndex(self, other, how='outer', drop_duplicates=drop_duplicates, keep=keep)

    def _CommonIndex(self, other, *, drop_duplicates=True, keep='first'):
        return _MergeIndex(self, other, how='inner', drop_duplicates=drop_duplicates, keep=keep)

    def _MergeIndex(self, other, how='outer', *, drop_duplicates=True, keep='first'):
        return _MergeIndex(self, other, how=how, drop_duplicates=drop_duplicates, keep=keep)

    def __contains__(self, item):
        if item in self.columns:
            return True
        elif item in self.index:
            return True
        elif len(self.find_Keys(item)) > 0:
            return True
        else:
            return False

    def __neg__(self):
        result = -self.as_DataFrame()
        return SimDataFrame(data=result, **self._SimParameters)

    def __add__(self, other):
        # both are SimDataFrame
        if isinstance(other, SimDataFrame):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimDataFrames are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")
            notFount = 0

            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()

            for col in otherI.columns:
                if col in selfI.columns:
                    result[col] = selfI[col] + otherI[col]
                else:
                    notFount += 1
                    result[col] = otherI[col]

            if notFount == len(otherI.columns):
                if selfI.nameSeparator is not None and otherI.nameSeparator is not None:
                    selfC, otherC, newNames = selfI._CommonRename(otherI)

                    # if no columns has common names
                    if newNames is None:
                        if len(otherC.columns) == 1 and not self.autoAppend:  # just in case there is only one column in the second operand
                            return selfC + otherC.to_SimSeries()
                        elif not self.autoAppend:
                            raise TypeError("Not possible to operate SimDataFrames if there aren't common columns")
                        else:  # self.autoAppend is True
                            for col in otherI.columns:
                                result[col] = otherI[col]
                    else:
                                
                        if (selfI.columns != selfC.columns).any() or (otherI.columns != otherC.columns).any():
                            resultX = selfC + otherC
                            resultX.rename(columns=newNames, inplace=True)
                        else:
                            resultX = result
                        if self.autoAppend:
                            for col in newNames.values():
                                result[col] = resultX[col]
                        else:
                            result = resultX
            return result

        # other is SimSeries
        elif isinstance(other, (SimSeries,Series)):
            if type(other) is Series:
                other = SimSeries(other, **self._SimParameters)
            selfI, otherI = self._JoinedIndex(other)
            otherI = otherI.to_SimSeries()
            result = selfI.copy()
            if self.operatePerName and otherI.name in selfI.columns:
                result[otherI.name] = selfI[otherI.name] + otherI
            elif selfI.autoAppend:
                result[otherI.name] = otherI
            else:
                for col in selfI.columns:
                    result[col] = selfI[col] + otherI
            return result

        # other is Pandas DataFrame
        elif isinstance(other, DataFrame):
            # result = self.DF.add(other, fill_value=0)
            selfC, otherC, newNames = self._CommonRename(SimDataFrame(other, **self._SimParameters))
            result = selfC + otherC
            return result if newNames is None else result.rename(columns=newNames)

        # let's Pandas deal with other types, maintain units and dtype
        else:
            result = self.as_DataFrame() + other
            return SimDataFrame(data=result, **self._SimParameters)

    def __radd(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        # both are SimDataFrame
        if isinstance(other, SimDataFrame):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimDataFrames are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")
            notFount = 0

            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()

            for col in otherI.columns:
                if col in selfI.columns:
                    result[col] = selfI[col] - otherI[col]
                else:
                    notFount += 1
                    result[col] = otherI[col] if selfI.intersectionCharacter in col else -otherI[col]

            if notFount == len(otherI.columns):
                if selfI.nameSeparator is not None and otherI.nameSeparator is not None:
                    selfC, otherC, newNames = selfI._CommonRename(otherI)

                    # if no columns has common names
                    if newNames is None:
                        if len(otherC.columns) == 1:  # just in case there is only one column in the second operand
                            return selfC - otherC.to_SimSeries()
                        else:
                            raise TypeError("Not possible to operate SimDataFrames if there aren't common columns")

                    resultX = selfC - otherC
                    resultX.rename(columns=newNames, inplace=True)
                    if self.autoAppend:
                        for col in newNames.values():
                            result[col] = resultX[col]
                    else:
                        result = resultX
            return result

        # other is SimSeries
        elif isinstance(other, (SimSeries,Series)):
            if type(other) is Series:
                other = SimSeries(other, **self._SimParameters)
            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()
            if self.operatePerName and otherI.name in selfI.columns:
                result[otherI.name] = selfI[otherI.name] - otherI
            if self.autoAppend :  # elif self.autoAppend:
                result[otherI.name] = -otherI
            else:
                for col in selfI.columns:
                    result[col] = selfI[col] - otherI
            return result

        # other is Pandas DataFrame
        elif isinstance(other, DataFrame):
            # result = self.DF.sub(other, fill_value=0)
            selfC, otherC, newNames = self._CommonRename(SimDataFrame(other, **self._SimParameters))
            result = selfC - otherC
            return result if newNames is None else result.rename(columns=newNames)

        # let's Pandas deal with other types, maintain units and dtype
        else:
            result = self.as_DataFrame() - other
            return SimDataFrame(data=result, **self._SimParameters)

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        # both are SimDataFrame
        if isinstance(other, SimDataFrame):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimDataFrames are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")

            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()

            notFount = 0
            for col in otherI.columns:
                if col in selfI.columns:
                    result[col] = selfI[col] * otherI[col]
                else:
                    notFount += 1

            if notFount == len(otherI.columns):
                if selfI.nameSeparator is not None and otherI.nameSeparator is not None:
                    selfC, otherC, newNames = selfI._CommonRename(otherI)

                    # if no columns has common names
                    if newNames is None:
                        if len(otherC.columns) == 1:  # just in case there is only one column in the second operand
                            return selfC * otherC.to_SimSeries()
                        else:
                            raise TypeError("Not possible to operate SimDataFrames if there aren't common columns")

                    resultX = selfC * otherC
                    resultX.rename(columns=newNames, inplace=True)
                    if self.autoAppend:
                        for col in newNames.values():
                            if self.intersectionCharacter in col :  # intersectionCharacter = '∩'
                                result[col] = resultX[col]
                    else:
                        result = resultX

            return result

        # other is SimSeries
        elif isinstance(other, (SimSeries,Series)):
            if type(other) is Series:
                other = SimSeries(other, **self._SimParameters)
            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()
            if self.operatePerName and otherI.name in selfI.columns:
                result[otherI.name] = self[otherI.name] * otherI
            else:
                for col in selfI.columns:
                    result[col] = selfI[col] * otherI
            return result

        # if other is Pandas DataFrame, convert it to SimDataFrame to be able to deal with
        elif isinstance(other, DataFrame):
            return self.__mul__(SimDataFrame(data=other, **self._SimParameters))

        # let's Pandas deal with other types, maintain units and dtype
        else:
            result = self.as_DataFrame() * other
            return SimDataFrame(data=result, **self._SimParameters)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        # both are SimDataFrame
        if isinstance(other, SimDataFrame):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimDataFrames are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")

            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()

            notFount = 0
            for col in otherI.columns:
                if col in selfI.columns:
                    result[col] = selfI[col] / otherI[col]
                else:
                    notFount += 1

            if notFount == len(otherI.columns):
                if self.nameSeparator is not None and otherI.nameSeparator is not None:
                    selfC, otherC, newNames = selfI._CommonRename(otherI)

                    # if no columns has common names
                    if newNames is None:
                        if len(otherC.columns) == 1:  # just in case there is only one column in the divisor
                            return selfC / otherC.to_SimSeries()
                        else:
                            raise TypeError("Not possible to operate SimDataFrames if there aren't common columns")

                    resultX = selfC / otherC
                    resultX.rename(columns=newNames, inplace=True)
                    if self.autoAppend:
                        for col in newNames.values():
                            if self.intersectionCharacter in col :  # intersectionCharacter = '∩'
                                result[col] = resultX[col]
                    else:
                        result = resultX
            return result

        # other is SimSeries
        elif isinstance(other, (SimSeries,Series)):
            if type(other) is Series:
                other = SimSeries(other, **self._SimParameters)
            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()
            if self.operatePerName and otherI.name in selfI.columns:
                result[otherI.name] = selfI[otherI.name] / otherI
            else:
                for col in selfI.columns:
                    result[col] = selfI[col] / otherI
            return result

        # if other is Pandas DataFrame, convert it to SimDataFrame to be able to deal with
        elif isinstance(other, DataFrame):
            return self.__truediv__(SimDataFrame(data=other, **self._SimParameters))

        # let's Pandas deal with other types, maintain units and dtype
        else:
            result = self.as_DataFrame() / other
            return SimDataFrame(data=result, **self._SimParameters)

    def __rtruediv__(self, other):
        return self.__pow__(-1).__mul__(other)

    def __floordiv__(self, other):
        # both are SimDataFrame
        if isinstance(other, SimDataFrame):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimDataFrames are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")

            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()

            notFount = 0
            for col in otherI.columns:
                if col in selfI.columns:
                    result[col] = selfI[col] // otherI[col]
                else:
                    notFount += 1

            if notFount == len(otherI.columns):
                if selfI.nameSeparator is not None and otherI.nameSeparator is not None:
                    selfC, otherC, newNames = selfI._CommonRename(otherI)

                    # if no columns has common names
                    if newNames is None:
                        if len(otherC.columns) == 1:  # just in case there is only one column in the second operand
                            return selfC // otherC.to_SimSeries()
                        else:
                            raise TypeError("Not possible to operate SimDataFrames if there aren't common columns")

                    resultX = selfC // otherC
                    resultX.rename(columns=newNames, inplace=True)
                    if self.autoAppend:
                        for col in newNames.values():
                            if self.intersectionCharacter in col :  # intersectionCharacter = '∩'
                                result[col] = resultX[col]
                    else:
                        result = resultX
            return result

        # other is SimSeries
        elif isinstance(other, (SimSeries,Series)):
            if type(other) is Series:
                other = SimSeries(other, **self._SimParameters)
            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()
            if self.operatePerName and otherI.name in selfI.columns:
                result[otherI.name] = selfI[otherI.name] // otherI
            else:
                for col in self.columns:
                    result[col] = self[col] // other
            return result

        # if other is Pandas DataFrame, convert it to SimDataFrame to be able to deal with
        elif isinstance(other, DataFrame):
            return self.__floordiv__(SimDataFrame(data=other, **self._SimParameters))

        # let's Pandas deal with other types, maintain units and dtype
        else:
            result = self.as_DataFrame() // other
            return SimDataFrame(data=result, **self._SimParameters)

    def __rfloordiv__(self, other):
        return self.__pow__(-1).__mul__(other).__int__()

    def __mod__(self, other):
        # both are SimDataFrame
        if isinstance(other, SimDataFrame):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimDataFrames are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")

            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()

            notFount = 0
            for col in otherI.columns:
                if col in selfI.columns:
                    result[col] = selfI[col] % otherI[col]
                else:
                    notFount += 1

            if notFount == len(otherI.columns):
                if selfI.nameSeparator is not None and otherI.nameSeparator is not None:
                    selfC, otherC, newNames = selfI._CommonRename(otherI)

                    # if no columns has common names
                    if newNames is None:
                        if len(otherC.columns) == 1:  # just in case there is only one column in the second operand
                            return selfC % otherC.to_SimSeries()
                        else:
                            raise TypeError("Not possible to operate SimDataFrames if there aren't common columns")

                    resultX = selfC % otherC
                    resultX.rename(columns=newNames, inplace=True)
                    if self.autoAppend:
                        for col in newNames.values():
                            if self.intersectionCharacter in col :  # intersectionCharacter = '∩'
                                result[col] = resultX[col]
                    else:
                        result = resultX

            return result

        # other is SimSeries
        elif isinstance(other, (SimSeries,Series)):
            if type(other) is Series:
                other = SimSeries(other, **self._SimParameters)
            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()
            if self.operatePerName and otherI.name in selfI.columns:
                result[otherI.name] = selfI[other.name] % otherI
            else:
                for col in selfI.columns:
                    result[col] = selfI[col] % otherI
            return result

        # if other is Pandas DataFrame, convert it to SimDataFrame to be able to deal with
        elif isinstance(other, DataFrame):
            return self.__mod__(SimDataFrame(data=other, **self._SimParameters))

        # let's Pandas deal with other types, maintain units and dtype
        else:
            result = self.as_DataFrame() % other
            return SimDataFrame(data=result, **self._SimParameters )

    def __pow__(self, other):
        # both are SimDataFrame
        if isinstance(other, SimDataFrame):
            if self.index.name is not None and other.index.name is not None and self.index.name != other.index.name:
                Warning("indexes of both SimDataFrames are not of the same kind:\n   '"+self.index.name+"' != '"+other.index.name+"'")

            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()

            notFount = 0
            for col in otherI.columns:
                if col in selfI.columns:
                    result[col] = selfI[col] ** otherI[col]
                else:
                    notFount += 1

            if notFount == len(otherI.columns):
                if selfI.nameSeparator is not None and otherI.nameSeparator is not None:
                    selfC, otherC, newNames = self._CommonRename(otherI)

                    # if no columns has common names
                    if newNames is None:
                        if len(otherC.columns) == 1:  # just in case there is only one column in the second operand
                            return selfC ** otherC.to_SimSeries()
                        else:
                            raise TypeError("Not possible to operate SimDataFrames if there aren't common columns")

                    resultX = selfC ** otherC
                    resultX.rename(columns=newNames, inplace=True)
                    if self.autoAppend:
                        for col in newNames.values():
                            if self.intersectionCharacter in col :  # intersectionCharacter = '∩'
                                result[col] = resultX[col]
                    else:
                        result = resultX

            return result

        # other is SimSeries
        elif isinstance(other, (SimSeries,Series)):
            if type(other) is Series:
                other = SimSeries(other, **self._SimParameters)
            selfI, otherI = self._JoinedIndex(other)
            result = selfI.copy()
            if self.operatePerName and otherI.name in selfI.columns:
                result[otherI.name] = self[otherI.name] ** otherI
            else:
                for col in selfI.columns:
                    result[col] = selfI[col] ** otherI
            return result

        # if other is Pandas DataFrame, convert it to SimDataFrame to be able to deal with
        elif isinstance(other, DataFrame):
            return self.__pow__(SimDataFrame(data=other, **self._SimParameters))

        # let's Pandas deal with other types, maintain units and dtype
        else:
            result = self.as_DataFrame() ** other
            return SimDataFrame(data=result, **self._SimParameters)

    def __int__(self):
        return SimDataFrame(data=self.DF.astype(int), **self._SimParameters)

    def merge(self, right, how='inner', on=None, left_on=None, right_on=None, left_index=None, right_index=None, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
        if on is None and left_on is None and right_on is None and right_index is None and left_index is None:
            left_index, right_index = True, True
        return merge(self, right, how='inner', on=on, left_on=left_on, right_on=right_on, left_index=left_index, right_index=right_index, sort=sort, suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)

    def avg(self, axis=0, **kwargs):
        return self.mean(axis=axis, **kwargs)

    def avg0(self, axis=0, **kwargs):
        return self.mean0(axis=axis, **kwargs)

    def average(self, axis=0, **kwargs):
        return self.mean(axis=axis, **kwargs)

    def average0(self, axis=0, **kwargs):
        return self.mean0(axis=axis, **kwargs)

    def count(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.count(axis=axis, **kwargs), **self._SimParameters )
        if axis == 1:
            newName = '.count'
            if len(set(self.columns)) == 1:
                newName = list(set(self.columns))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns)) == 1:
                newName = list(set(self.renameRight(inplace=False).columns))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns)) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns))[0]+newName
            data=self.DF.count(axis=axis, **kwargs)
            data.columns=[newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = 'dimensionless'
            return SimDataFrame(data=data, **params)

    def count0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).count(axis=axis, **kwargs)

    def max(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.max(axis=axis, **kwargs), **self._SimParameters )
        if axis == 1:
            newName = '.max'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns)) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns)) == 1:
                newName = list(set(self.renameRight(inplace=False).columns))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns)) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns))[0]+newName
            data=self.DF.max(axis=axis, **kwargs)
            data.columns=[newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def max0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).max(axis=axis, **kwargs)

    def mean(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.mean(axis=axis, **kwargs), **self._SimParameters)
        if axis == 1:
            newName = '.mean'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns ) ) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameRight(inplace=False).columns ))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns ))[0]+newName
            data=self.DF.mean(axis=axis, **kwargs)
            data.columns=[newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def mean0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).mean(axis=axis, **kwargs)

    def median(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.median(axis=axis, **kwargs), **self._SimParameters)
        if axis == 1:
            newName = '.median'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns ) ) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameRight(inplace=False).columns ))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns ))[0]+newName
            data=self.DF.median(axis=axis, **kwargs)
            data.columns=[newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def median0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).median(axis=axis, **kwargs)

    def min(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.min(axis=axis, **kwargs), **self._SimParameters)
        if axis == 1:
            newName = '.min'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns ) ) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameRight(inplace=False).columns ))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns ))[0]+newName
            data=self.DF.min(axis=axis, **kwargs)
            data.columns=[newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def min0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).min(axis=axis, **kwargs)

    def mode(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.mode(axis=axis, **kwargs), **self._SimParameters)
        if axis == 1:
            newName = '.mode'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns ) ) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameRight(inplace=False).columns ))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns ))[0]+newName
            data=self.DF.mode(axis=axis, **kwargs)
            data.columns=[newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def mode0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).mode(axis=axis, **kwargs)

    def prod(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.prod(axis=axis, **kwargs), **self._SimParameters)
        if axis == 1:
            newName = '.prod'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns ) ) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameRight(inplace=False).columns ))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns ))[0]+newName
            data=self.DF.prod(axis=axis, **kwargs)
            data.columns=[newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def prod0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).prod(axis=axis, **kwargs)

    def quantile(self, q=0.5, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.quantile(q=q, axis=axis, **kwargs), **self._SimParameters)
        if axis == 1 and hasattr(q, '__iter__'):  # q is a list
            namedecimals = 1
            if 'namedecimals' in kwargs:
                if type(kwargs['namedecimals']) is int:
                    namedecimals = kwargs['namedecimals']
                del kwargs['namedecimals']
            else:
                namedecimals = len(str(q))-2
            newNameLambda = lambda q : '.Q'+str(round(q*100, namedecimals))
            newName = map(newNameLambda, q)
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns)) == 1:
                newName = [list(set(self.columns))[0] + nm for nm in newName]
            elif len(set(self.renameRight(inplace=False).columns)) == 1:
                newName = [list(set(self.renameRight(inplace=False).columns))[0] + nm for nm in newName]
            elif len(set(self.renameLeft(inplace=False).columns)) == 1:
                newName = [list(set(self.renameLeft(inplace=False).columns))[0] + nm for nm in newName]
            data=self.DF.quantile(q=q, axis=axis, **kwargs).transpose()
            data.columns = newName
            #data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)
        elif axis == 1:
            namedecimals = 1
            if 'namedecimals' in kwargs:
                if type(kwargs['namedecimals']) is int:
                    namedecimals = kwargs['namedecimals']
                del kwargs['namedecimals']
            else:
                namedecimals = len(str(q))-2
            newName = '.Q'+str(round(q*100, namedecimals))
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns)) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns)) == 1:
                newName = list(set(self.renameRight(inplace=False).columns))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns)) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns))[0]+newName
            data=self.DF.quantile(q=q, axis=axis, **kwargs)
            data.columns=[newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def quantile0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).quantile(axis=axis, **kwargs)

    def rms(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            result = SimDataFrame(data=(self.DF**2), **self._SimParameters).mean(axis=axis, **kwargs)
            return SimDataFrame(data=result.DF**0.5, **result._SimParameters)
        if axis == 1:
            newName = '.rms'
            if len(set(self.columns)) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameRight(inplace=False).columns ))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns ))[0]+newName
            data = SimDataFrame(data=(self.DF**2), **self._SimParameters).mean(axis=axis, **kwargs)
            data.rename(columns={data.columns[0]:newName}, inplace=True)
            data.name = newName
            params = data._SimParameters
            params['name'] = newName
            params['columns'] = [newName]
            return SimDataFrame(data=data, **params)

        return (SimDataFrame(data=(self.DF**2), **self._SimParameters).mean(axis=axis, **kwargs))**0.5

    def rms0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).rms(axis=axis, **kwargs)

    def std(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.std(axis=axis, **kwargs), **self._SimParameters)
        if axis == 1:
            newName = '.std'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns ) ) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameRight(inplace=False).columns ))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns ))[0]+newName
            data = self.DF.std(axis=axis, **kwargs)
            data.columns = [newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def std0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).std(axis=axis, **kwargs)

    def sum(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            if len(set(self.get_Units(self.columns).values())) == 1:
                params = self._SimParameters
                params['units'] = list(set(self.get_Units(self.columns).values()))[0]
                return SimDataFrame(data=self.DF.sum(axis=axis, **kwargs).rename('.sum'), **params)
            else:
                params = self._SimParameters
                if type(params['units']) is dict:
                    params['units']['.sum'] = '*units per row'
                return SimDataFrame(data=self.DF.sum(axis=axis, **kwargs).rename('.sum'), **params)
        if axis == 1:
            newName = '.sum'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns)) == 1:
                newName = list(set(self.columns))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns)) == 1:
                newName = list(set(self.renameRight(inplace=False).columns))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns)) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns))[0]+newName
            else:
                commonL = commonprefix(list(self.renameLeft(inplace=False).columns))
                commonR = commonprefix(list(self.renameRight(inplace=False).columns))
                if len(commonL) >= len(commonR):
                    newName = commonL + newName
                else:
                    newName = commonR + newName
            if len(set(self.get_Units(self.columns).values())) == 1:
                data = self.DF.sum(axis=axis, **kwargs)
            else:
                result = self[self.columns[0]]
                units = self.units[self.columns[0]]
                for col in range(1,len(self.columns)):
                    result = result + self[self.columns[col]]
                data = result
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)
        if axis == 2:
            return self.sum(axis=1).sum(axis=0)

    def sum0(self, axis=0, **kwargs):
        return self.sum(axis=axis, **kwargs)

    def var(self, axis=0, **kwargs):
        axis = _cleanAxis(axis)
        if axis == 0:
            return SimDataFrame(data=self.DF.var(axis=axis, **kwargs), **self._SimParameters)
        if axis == 1:
            newName = '.var'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            if len(set(self.columns ) ) == 1:
                newName = list(set(self.columns ))[0]+newName
            elif len(set(self.renameRight(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameRight(inplace=False).columns ))[0]+newName
            elif len(set(self.renameLeft(inplace=False).columns ) ) == 1:
                newName = list(set(self.renameLeft(inplace=False).columns ))[0]+newName
            data=self.DF.var(axis=axis, **kwargs)
            data.columns=[newName]
            data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def var0(self, axis=0, **kwargs):
        return self.replace(0,np.nan).var(axis=axis, **kwargs)

    def round(self, decimals=0, **kwargs):
        return SimDataFrame(data=self.DF.round(decimals=decimals, **kwargs), **self._SimParameters)

    def diff(self,periods=1, axis=0, forward=False):
        axis = _cleanAxis(axis)
        if type(periods) is bool:
            periods, forward = 1, periods
        if axis == 0:
            if forward:
                return SimDataFrame(data=-1*self.DF.diff(periods=-1*periods, axis=axis), **self._SimParameters)
            else:
                return SimDataFrame(data=self.DF.diff(periods=periods, axis=axis), **self._SimParameters)
        if axis == 1:
            # newName = '.diff'
            if len(set(self.get_Units(self.columns).values())) == 1:
                units = list(set(self.get_Units(self.columns).values()))[0]
            else:
                units = 'dimensionless'
            # if len(set(self.columns ) ) == 1:
            #     newName = list(set(self.columns ))[0]+newName
            # elif len(set(self.renameRight(inplace=False).columns ) ) == 1:
            #     newName = list(set(self.renameRight(inplace=False).columns ))[0]+newName
            # elif len(set(self.renameLeft(inplace=False).columns ) ) == 1:
            #     newName = list(set(self.renameLeft(inplace=False).columns ))[0]+newName
            # else:
            #     newName = [c+'.diff' for c in self.columns]
            if forward:
                data=-1*self.DF.diff(periods=-1*periods, axis=axis)
            else:
                data=self.DF.diff(periods=periods, axis=axis)
            # data.columns=newName
            # data.name = newName
            params = self._SimParameters
            params['units'] = units
            return SimDataFrame(data=data, **params)

    def znorm(self):
        """
        return standard normalization

        """
        return znorm(self)

    def znorm0(self):
        """
        return standard normalization ignoring zeroes

        """
        return znorm(self.replace(0,np.nan))

    def minmaxnorm(self):
        """
        return min-max normalization
        """
        return minmaxnorm(self)

    def minmaxnorm(self):
        """
        return min-max normalization
        """
        return minmaxnorm(self.replace(0,np.nan))


    def copy(self, **kwargs):
        return SimDataFrame(data=self.as_DataFrame().copy(True), **self._SimParameters)

    def __call__(self, key=None):
        if key is None:
            key = self.columns

        result = self.__getitem__(key)
        if isinstance(result, SimSeries):
            result = result.to_numpy()
        return result

    def __setitem__(self, key, value, units=None):
        uDic = {}
        if type(key) is str:
            key = key.strip()
        if type(value) is tuple and len(value) == 2 and type(value[1]) in [str,dict] and units is None :  # and type(value[0]) in [SimSeries, Series, list, tuple, np.ndarray,float,int,str]
            value, units = value[0], value[1]
        if type(value) is SimDataFrame and len(value.index) == 1 and type(key) is not slice and ( (key in self.index or pd.to_datetime(key) in self.index) and (key not in self.columns and pd.to_datetime(key) not in self.columns)):
            self.loc[key] = value
            return None
        if units is None:
            if type(value) is SimSeries:
                if type(value.units) is str:
                    uDic = { str(key) : value.units }
                elif type(value.units) is dict:
                    uDic = value.units
                else:
                    uDic = { str(key) : 'UNITLESS' }
                if self.indexUnits is None and value.indexUnits is not None:
                    self.indexUnits = value.indexUnits
            elif isinstance(value, SimDataFrame):
                if len(value.columns) == 1:
                    if value.columns[0] in value.units:
                        uDic = { str(key) : value.units[value.columns[0]] }
                    else:
                        uDic = { str(key) : 'UNITLESS' }
                else:
                    uDic = value.units.copy() if type(value.units) is dict else { str(key) : value.units }
                    if value.index.name not in value.columns and value.index.name in uDic:
                        del uDic[value.index.name]
                    if key not in uDic and len(set(uDic.values())) == 1:
                        uDic[str(key)] = list(set(uDic.values()))[0]
                    if self.indexUnits is None and value.indexUnits is not None:
                        self.indexUnits = value.indexUnits
                    elif self.indexUnits is not None and value.indexUnits is not None and self.indexUnits != value.indexUnits:
                        if convertibleUnits(value.indexUnits, self.indexUnits):
                            try:
                                value.index = convertUnit(value.index, value.indexUnits, self.indexUnits)
                            except:
                                print("WARNING: failed to convert the provided index to the units of this SimDataFrame index.")
                        else:
                            print("WARNING: not able to convert the provided index to the units of this SimDataFrame index.")

            else:
                uDic = { str(key) : 'UNITLESS' }
        elif type(units) is str:
            uDic = { str(key) : units.strip() }
        elif type(units) is dict:
            uDic = units
        else:
            raise NotImplementedError

        if isinstance(value, SimDataFrame):
            if len(value.columns) == 1:
                value = value.to_SimSeries()
            elif len(value.columns) > 2:
                for col in value.columns:
                    self.__setitem__(col,value[col])
                return None


        before = len(self.columns)
        # if len(self.index) == len(value.index) and (self.index == value.index).all():
        #     pass
        # elif self.index.duplicated().sum() > 0 or value.index.duplicated().sum() > 0:
        #     value = value.reindex(self.index)
        super().__setitem__(key, value)
        after = len(self.columns)

        if after == before:
            self.new_Units(key, uDic[key])
        elif after > before:
            for c in range(before, after ):
                if self.columns[c] in self.columns[ before : after ] and self.columns[c] in uDic:
                    self.new_Units(self.columns[c], uDic[ self.columns[c] ])
                else:
                    self.new_Units(self.columns[c], 'UNITLESS')

    def __getitem__(self, key):

        ### if key is boolean filter, return the filtered SimDataFrame
        if isinstance(key, (Series)) or type(key) is np.ndarray:
            if str(key.dtype) == 'bool':
                return SimDataFrame( data=self._getbyFilter(key), **self._SimParameters)

        ### if key is pd.Index or pd.MultiIndex return selected rows or columns
        if isinstance(key, (Index)):
            keyCols = True
            for each in key:
                if each not in self.columns:
                    keyCols = False
                    break
            if keyCols:
                return SimDataFrame(data=self._getbyColumn(key), **self._SimParameters)
            else:
                result = SimDataFrame(data=self._getbyIndex(key), **self._SimParameters)
                if len(result) == 1:
                    result = _Series2Frame(result)
                return result

        ### here below we try to guess what the user is requesting
        byIndex = False
        indexFilter = None
        indexes = None
        slices = None
        result = None  # initialize variable

        ### convert tuple argument to list
        if type(key) is tuple:
            key = list(key)

        ### if key is a string but not a column name, check if it is an item, attribute, pattern, filter or index
        if type(key) is str and key not in self.columns:
            if bool(self.find_Keys(key)) : # catch the column names this key represent
                key = list(self.find_Keys(key))
            elif key == self.indexName:  # key is the name of the index
                result = self.index
            else: # key is not a column name
                try: # to evalue as a filter
                    result = self._getbyCriteria(key)
                except:
                    try: # to evaluate as an index value
                        result = self._getbyIndex(key)
                    except:
                        raise ValueError('requested key is not a valid column name, pattern, index or filter criteria:\n   ' + key)
                if result is None:
                    try:
                        result = self._getbyIndex(key)
                    except:
                        raise ValueError('requested key is not a valid column name, pattern, index or filter criteria:\n   ' + key)

        ### key is a list, have to check every item in the list
        elif type(key) is list:
            keyList, key, filters, indexes, slices = key, [], [], [], []
            for each in keyList:
                ### the key is a column name
                if type(each) is slice:
                    slices += [each]
                elif each in self.columns:
                    key += [each]
                ### if key is a string but not a column name, check if it is an item, attribute, pattern, filter or index
                elif type(each) is str:
                    if bool(self.find_Keys(each) ) : # catch the column names this key represent
                        key += list(self.find_Keys(each) )
                    else: # key is not a column name, might be a filter or index
                        try: # to evalue as a filter
                            _ = self.filter(each, returnFilter=True)
                            filters += [each]
                        except:
                            try: # to evaluate as an index value
                                _ = self._getbyIndex(each)
                                indexes += [each]
                            except:
                                # discard this item
                                print(' the paramenter '+str(each)+' is not valid.')

                ### must be an index, not a column name o relative, not a filter, not in the index
                else:
                    indexes += [each]

            ### get the filter array, if filter criteria was provided
            if bool(filters):
                try:
                    indexFilter = self.filter(filters, returnFilter=True)
                except:
                    raise Warning('filter conditions are not valid:\n   '+ ' and '.join(filters))
                if indexFilter is not None and not indexFilter.any():
                    raise Warning('filter conditions removed every row :\n   '+ ' and '.join(filters))

        ### attempt to get the desired keys, first as column names, then as indexes
        if result is not None:
            params = self._SimParameters
            params['indexName'] = None
            params['units'] =  self.get_Units(key)
            params['columns'] = key if type(key) in (list,Index) else [key]
            result = SimDataFrame(data=result, **params)
        elif bool(key) or key == 0:
            try:
                result = self._getbyColumn(key)
            except:
                result = self._getbyIndex(key)
                if result is not None : byIndex = True
        else:
            result = SimDataFrame(data=self, **self._SimParameters)

        ### convert returned object to SimDataFrame or SimSeries accordingly
        if type(result) is DataFrame:
            resultUnits = self.get_Units(result.columns)
            params = self._SimParameters
            params['units'] = resultUnits
            result = SimDataFrame(data=result, **params)
        elif type(result) is Series:
            if len(self.get_Units()) > 0:
                if result.name is None or result.name not in self.get_Units():
                    # this Series is one index for multiple columns
                    try:
                        resultUnits = self.get_Units(result.index)
                    except:
                        resultUnits = { result.name:'UNITLESS'}
                else:
                    resultUnits = self.get_Units(result.name)
            else:
                resultUnits = { result.name:'UNITLESS'}
            params = self._SimParameters
            params['units'] = resultUnits
            result = SimSeries(data=result, **params)

        ### apply filter array if applicable
        if indexFilter is not None:
            if type(indexFilter) is np.ndarray:
                result = result.iloc[indexFilter]
            else:
                result = result[indexFilter.array]

        ### apply indexes and slices
        if bool(indexes) or bool(slices):
            indexeslices = indexes + slices
            iresult = _Series2Frame(result._getbyIndex(indexeslices[0]))
            if len(indexeslices) > 1:
                for i in indexeslices[1:]:
                    # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
                    # iresult = iresult.append(_Series2Frame(result._getbyIndex(i)))
                    iresult = pd.concat([iresult, _Series2Frame(result._getbyIndex(i))], axis=0)
                    
            try:
                result = iresult.sort_index()
            except:
                result = iresult

        ### if is a single row return it as a DataFrame instead of a Series
        if byIndex:
            result = _Series2Frame(result)

        if type(result) is DataFrame:
            result = SimDataFrame(result, **self._SimParameters)
        elif type(result) is Series:
            result = SimSeries(result, **self._SimParameters)

        return result

    def _getbyFilter(self, key):
        """
        ** helper function to __getitem__ method **

        try to get a filtered DataFrame or Series(.filter[key] )
        """
        if len(key) != len(self.DF):
            raise ValueError('Filter wrong length ' + str(len(key)) + ' instead of ' + str(len(self.DF)) )
        if not isinstance(key, (Series, SimSeries)) and type(key) is not np.ndarray:
            raise TypeError("Filter must be a Series or Array" )
        else:
            if str(key.dtype) != 'bool':
                raise TypeError("Filter dtype must be 'bool'" )

        return self.DF.loc[key]

    def _getbyCriteria(self, key):
        """
        ** helper function to __getitem__ method **

        try to get a filtered DataFrame or Series(.filter[key] )
        """
        return self.filter(key)

    def _getbyColumn(self, key):
        """
        ** helper function to __getitem__ method **

        try to get a column by column name(.__getitem__[key] )
        """
        return self.DF.__getitem__(key)


    def _getbyIndex(self, key):
        """
        ** helper function to __getitem__ method **

        try to get a row by index value(.loc[key] ) or by position(.iloc[key] )
        """
        # if index is date try to undestand key as a date
        if type(self.index) is DatetimeIndex and type(key) not in [DatetimeIndex, Timestamp, int, float, np.ndarray]:
            try:
                return self._getbyDateIndex(key)
            except:
                pass

        # try to find key by index value using .loc
        try:
            return self.DF.loc[key]
        except:
            # try to find key by index position using .loc
            try:
                return self.DF.iloc[key]
            except:
                try:
                    return self.DF.loc[:,key]
                except:
                    try:
                        return self.DF.iloc[:,key]
                    except:
                        raise ValueError(' ' + str(key) + ' is not a valid index value or position.')

    def _getbyDateIndex(self, key):
        """
        ** helper function to __getitem__ method **

        try to get a row by index value(.loc[key] ) or by position(.iloc[key] )
        """
        if type(self.index) is DatetimeIndex:
            if type(key) in [DatetimeIndex, Timestamp, np.datetime64, np.ndarray, dt.date]:
                try:
                    return self.DF.loc[key]
                except:
                    pass

            if type(key) is not str and(isDate(key) or type(key) not in [DatetimeIndex, Timestamp] ):
                try:
                    return self.DF.loc[key]
                except:
                    try:
                        return self.DF.iloc[key]
                    except:
                        pass

            if type(key) is str and len(multisplit(key, ('==', '!=', '>=', '<=', '<>', '><', '>', '<', '=', ' ')) ) == 1 and isDate(key):
                try:
                    key = strDate(key )
                except:
                    try:
                        key = strDate(key, formatIN=isDate(key, returnFormat=True), formatOUT='DD-MMM-YYYY' )
                    except:
                        raise Warning('\n Not able to undertand the key as a date.\n')
                try:
                    return self.DF.loc[key]
                except:
                    pass

            if type(key) is str:
                keyParts = multisplit(key, ('==', '!=', '>=', '<=', '<>', '><', '>', '<', '=', ' '))
                keySearch = ''
                datesDict = {}
                temporal = SimDataFrame(index=self.index, **self._SimParameters)
                datesN = len(self)
                for P in range(len(keyParts)):
                    if isDate(keyParts[P]):
                        keySearch += ' D'+str(P)
                        datesDict['D'+str(P)] = keyParts[P]
                        temporal.__setitem__('D'+str(P), DatetimeIndex([ Timestamp(strDate(keyParts[P], formatIN=isDate(keyParts[P], returnFormat=True), formatOUT='YYYY-MMM-DD')) ] * datesN ).to_numpy() )
                    else:
                        keySearch += ' '+keyParts[P]
                datesFilter = temporal.filter(keySearch, returnFilter=True)
                return self.DF.iloc[datesFilter.array]

            else:
                return self.DF.iloc[key]

    def _columnsNameAndUnits2MultiIndex(self):
        # out = []  # out = {}
        units = self.get_units()
        if units is None or len(units) == 0:
            return self.columns  # there are not units, return column names as they are
        if len(self.columns) == 0:
            return self.columns  # is an empty DataFrame
        # for col in self.columns:
        #     if col in units:
        #         out.append((col,units[col]))  # out[col] = units[col]
        #     else:
        #         out.append((col,None))  # out[col] = None
        out = [(col, units[col]) if col in units else (col, None) for col in self.columns]
        out = pd.MultiIndex.from_tuples(out)  # out = pd.MultiIndex.from_tuples(out.items())
        return out

    def _DataFrameWithMultiIndex(self):
        if self.transposed:
            result = self.DF.copy()
            # units = []
            # for i in result.index:
            #     if i in self.units:
            #         units.append(self.units[i])
            #     else:
            #         units.append('UNITLESS')
            units = [self.units[i] if i in self.units else 'UNITLESS' for i in result.index]
            joker = ('*','@','$','-','%','_',' ')
            for unitsCol in [s + 'units' for s in joker ] + [s + 'units' + s for s in joker ] + [s + 'UNITS' for s in joker ] + [s + 'UNITS' + s for s in joker ]:
                if unitsCol not in result.columns:
                    result[unitsCol] = units
                    break
                elif list(result[unitsCol]) == units:
                    break
            result.index.name = None
            return result
        else:
            result = self.DF.copy()
            newName = self._columnsNameAndUnits2MultiIndex()
            result.columns=newName
            return result

    def _repr_html_(self):
        """
        Return a html representation for a particular DataFrame, with Units.
        """
        return self._DataFrameWithMultiIndex()._repr_html_()

    def __repr__(self) -> str:
        """
        Return a string representation for a particular DataFrame, with Units.
        """
        return self._DataFrameWithMultiIndex().__repr__()

    @property
    def wells(self):
        if self.nameSeparator in [None, '', False]:
            return []
        objs = []
        for each in list(self.columns):
            if type(each) is str and self.nameSeparator in each and each[0] == 'W':
                objs += [each.split(self.nameSeparator )[-1]]
        return tuple(set(objs))

    # @property
    # def items(self):
    #     return self.left

    def get_Wells(self, pattern=None):
        """
        Will return a tuple of all the well names in case.

        If the pattern variable is different from None only wells
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq

        """
        if pattern is not None and type(pattern ) is not str:
            raise TypeError('pattern argument must be a string.')
        if pattern is None:
            return tuple(self.wells)
        else:
            return tuple(fnmatch.filter(self.wells, pattern ) )

    @property
    def groups(self):
        if self.nameSeparator in [None, '', False]:
            return []
        objs = []
        for each in list(self.columns ):
            if type(each) is str and self.nameSeparator in each and each[0] == 'G':
                objs += [each.split(self.nameSeparator )[-1]]
        return tuple(set(objs))

    def get_Groups(self, pattern=None):
        """
        Will return a tuple of all the group names in case.

        If the pattern variable is different from None only groups
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq

        """
        if pattern is not None and type(pattern ) is not str:
            raise TypeError('pattern argument must be a string.')
        if pattern is None:
            return self.groups
        else:
            return tuple(fnmatch.filter(self.groups, pattern ) )

    @property
    def regions(self):
        if self.nameSeparator in [None, '', False]:
            return []
        objs = []
        for each in list(self.columns ):
            if type(each) is str and self.nameSeparator in each and each[0] == 'R':
                objs += [each.split(self.nameSeparator )[-1]]
        return tuple(set(objs))

    def get_Regions(self, pattern=None):
        """
        Will return a tuple of all the region names in case.

        If the pattern variable is different from None only regions
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq
        """
        if pattern is not None and type(pattern ) is not str:
            raise TypeError('pattern argument must be a string.')
        if pattern is None:
            return self.regions
        else:
            return tuple(fnmatch.filter(self.regions, pattern ) )

    @property
    def attributes(self):
        if self.nameSeparator in [None, '', False]:
            return { col:[] for col in self.columns }
        atts = {}
        for each in list(self.columns):
            if type(each) is str and self.nameSeparator in each:
                if type(each) is str and each.split(self.nameSeparator )[0] in atts:
                    atts[each.split(self.nameSeparator )[0]] += [each.split(self.nameSeparator )[-1]]
                else:
                    atts[each.split(self.nameSeparator )[0]] = [each.split(self.nameSeparator )[-1]]
            else:
                if each not in atts:
                    atts[each] = []
        for att in atts:
            atts[att] = list(set(atts[att]))
        return atts

    @property
    def properties(self):
        if len(self.attributes.keys()) > 0:
            return tuple(self.attributes.keys())
        else:
            return tuple()

    def get_Attributes(self, pattern=None):
        """
        Will return a dictionary of all the attributes names in case as keys
        and their related items as values.

        If the pattern variable is different from None only attributes
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq
        """
        if pattern is None:
            return tuple(self.attributes.keys())
        else:
            return tuple(fnmatch.filter(tuple(self.attributes.keys()), pattern ) )

    def get_Keys(self, pattern=None):
        """
        Will return a tuple of all the key names in case.

        If the pattern variable is different from None only keys
        matching the pattern will be returned; the matching is based
        on fnmatch():
            Pattern     Meaning
            *           matches everything
            ?           matches any single character
            [seq]       matches any character in seq
            [!seq]      matches any character not in seq

        """
        if pattern is not None and type(pattern) is not str and type(pattern) not in [int,float]:
            raise TypeError('pattern argument must be a string.\nreceived '+str(type(pattern))+' with value '+str(pattern))
        if type(pattern) in [int,float]:
            if pattern in self.columns:
                return self[pattern]
            else:
                raise KeyError("The requested key: "+str(pattern)+"is not present in this SimDataFrame.")
        if pattern is None:
            return tuple(self.columns)
        else:
            return tuple(fnmatch.filter(map(str,tuple(self.columns)), pattern))

    def find_Keys(self, criteria=None):
        """
        Will return a tuple of all the key names in case.

        If criteria is provided, only keys matching the pattern will be returned.
        Accepted criterias can be:
            > well, group or region names.
              All the keys related to that name will be returned
            > attributes.
              All the keys related to that attribute will be returned
            > a fmatch compatible pattern:
                Pattern     Meaning
                *           matches everything
                ?           matches any single character
                [seq]       matches any character in seq
                [!seq]      matches any character not in seq

            additionally, ! can be prefixed to a key to return other keys but
            that particular one:
                '!KEY'     will return every key but not 'KEY'.
                           It will only work with a single key.
        """
        if criteria is None:
            return tuple(self.columns )
        keys = []
        if type(criteria) is str and len(criteria.strip()) > 0:
            if criteria.strip()[0] == '!' and len(criteria.strip()) > 1:
                keys = list(self.columns)
                keys.remove(criteria[1:])
                return tuple(keys )
            criteria = [criteria]
        elif type(criteria) is not list:
            try:
                criteria = list(criteria)
            except:
                pass
        for key in criteria:
            if type(key) is str and key not in self.columns:
                if key in self.wells or key in self.groups or key in self.regions:
                    keys += list(self.get_Keys('*'+self.nameSeparator+key))
                elif key in self.attributes:
                    keys += list(self.keyGen(key, self.attributes[key]))
                else:
                    keys += list(self.get_Keys(key))
            elif type(key) is str and key in self.columns:
                keys += [ key ]
            else:
                keys += list(self.find_Keys(key))
        return tuple(keys)

    def get_units(self, items=None):
        return self.get_Units(items)

    def get_Units(self, items=None):
        """
        returns a dictionary with the units for the selected 'items' (or columns)
        or for all the columns in this SimDataFrame

        Parameters
        ----------
        items : str of iterable (i.e. list), optional
            The columns or items to return their units.
            The default is None, and then al the entire units dictionary will be returned.

        Returns
        -------
        dict
            A dictionary {column:units}
        """
        if self.units is None:
            self.units = {}

        if items is None:
            return self.units.copy()
        uDic = {}
        if not isinstance(items,(list,tuple,dict,set,Index)):
            items = [items]
        for each in items:
            if each in self.units:
                uDic[each] = self.units[each]
            elif each in self.wells or each in self.groups or each in self.regions:
                for Key in self.get_Keys('*'+self.nameSeparator+each):
                    uDic[each] = self.units[each]
            elif each in self.attributes:
                for att in self.keyGen(each, self.attributes[each]):
                    if att in self.units:
                        uDic[att] = self.units[att]
                    else:
                        uDic[att] = 'UNITLESS'
            elif len(self.get_Keys(each)) > 0:
                for key in self.get_Keys(each):
                    uDic[key] = self.units[key] if key in self.units else ''
        return uDic

    def get_UnitsString(self, items=None):
        if len(self.get_Units(items)) == 1:
            return list(self.get_Units(items).values())[0]
        elif len(set(self.get_Units(items).values() )) == 1:
            return list(set(self.get_Units(items).values() ))[0]

    def set_units(self, units, item=None):
        """
        This method can be used to define the units related to the values of a column (item).

        Parameters
        ----------
        units : str or list of str
            the units to be assigned
        item : str, optional
            The name of the column to apply the units.
            The default is None. In this case the unit

        Raises
        ------
        ValueError
            when units can't be applied.
        TypeError
            when units or item has the wrong format.

        Returns
        -------
        None.

        """
        return self.set_Units(units=units, item=item)

    def set_Units(self, units, item=None):
        """
        This method can be used to define the units related to the values of a column (item).

        Parameters
        ----------
        units : str or list of str
            the units to be assigned
        item : str, optional
            The name of the column to apply the units.
            The default is None. In this case the unit

        Raises
        ------
        ValueError
            when units can't be applied.
        TypeError
            when units or item has the wrong format.

        Returns
        -------
        None.

        """
        if item is not None and item not in self.columns and item != self.index.name and item not in self.index.names:
            if units in self.columns or units == self.index.name or units in self.index.names:
                return self.set_Units(item,units)
            raise ValueError("the required item '" + str(item) + "' is not in this SimDataFrame.")
        if type(units) not in (str,dict) and hasattr(units,'__iter__'):
            if item is not None and type(item) is not str and hasattr(item,'__iter__'):
                if len(item) == len(units):
                    return self.set_Units( dict(zip(item,units)) )
                else:
                    raise ValueError("both units and item must have the same length.")
            elif item is None:
                if len(units) == len(self.columns):
                    return self.set_Units( dict(zip(list(self.columns),units)) )
                else:
                    raise ValueError("units list must be the same length of columns in the SimDataFrame or must be followed by a list of items.")
            else:
                raise TypeError("if units is a list, items must be a list of the same length.")

        if type(units) is dict:
            if len([ k for k in units.keys() if k in (self.index if self.transposed else self.columns) ]) >= len([ u for u in units.values() if u in (self.index if self.transposed else self.columns) ]):
                ku = True
            else:
                ku = False
            if ku:
                for k,u in units.items():
                    self.set_Units(u,k)
                return None
            else:
                for u,k in units.items():
                    self.set_Units(u,k)
                return None

        if self.units is None:
            self.units = {}

        if type(self.units) is dict:
            if not self.transposed:
                if item is None and len(self.columns) > 1:
                    raise ValueError("This SimDataFrame has multiple columns, item parameter must be provided.")
                elif item is None and len(self.columns) == 1:
                    return self.set_Units(units,[list(self.columns)[0]])
                elif item is not None:
                    if item in self.columns:
                        if units is None:
                            self.units[item] = None
                        elif type(units) is str:
                            self.units[item] = units.strip()
                        else:
                            raise TypeError("units must be a string.")
                    if item == self.index.name:
                        self.indexUnits = units.strip()
                        self.units[item] = units.strip()
                    if item in self.index.names:
                        self.units[item] = units.strip()
            else:  # if self.transposed:
                if item is None and len(self.index) > 1:
                    raise ValueError("item must not be None")
                elif item is None and len(self.index) == 1:
                    return self.set_Units(units,[list(self.index)[0]])
                elif item is not None:
                    if item in self.index:
                        if units is None:
                            self.units[item] = None
                        elif type(units) is str:
                            self.units[item] = units.strip()
                        else:
                            raise TypeError("units must be a string.")
                    if item == self.index.name:
                        self.indexUnits = units.strip()
                        self.units[item] = units.strip()
                    if item in self.index.names:
                        self.units[item] = units.strip()

    def keysByUnits(self):
        """
        returns a dictionary of the units present in the SimDataFrame as keys
        and a list of the columns that has that units.
        """
        kDic = {}
        for k, v in self.units.items():
            if v in kDic:
                kDic[v] += [k]
            else:
                kDic[v] = [k]
        return kDic

    def new_Units(self, key, units):
        if type(key) is str:
            key = key.strip()
        if type(units) is str:
            units = units.strip()

        if self.units is None:
            self.units = {}

        if key not in self.units:
            self.units[key] = units
        else:
            if units != self.units[key] and self.speak:
                print("overwritting existing units for key '" + key + "': " + self.units[key] + ' -> ' + units )
            self.units[key] = units

    def is_Key(self, Key):
        if type(Key) != str or len(Key)==0:
            return False
        if Key in self.get_Keys():
            return True
        else:
            return False

    def keyGen(self, mainKeys=[], itemKeys=[]):
        """
        returns the combination of every key in keys with all the items.
        keys and items must be list of strings
        """
        if type(itemKeys) is str:
            itemKeys = [itemKeys]
        if type(mainKeys) is str:
            mainKeys = [mainKeys]
        ListOfKeys = []
        for k in mainKeys:
            k.strip(self.nameSeparator)
            if self.is_Key(k):
                ListOfKeys.append(k)
            for i in itemKeys:
                i = i.strip(self.nameSeparator)
                if self.is_Key(k+self.nameSeparator+i):
                    ListOfKeys.append(k+self.nameSeparator+i )
                elif k[0].upper() == 'W':
                    wells = self.get_Wells(i)
                    if len(wells) > 0:
                        for w in wells:
                            if self.is_Key(k+self.nameSeparator+w):
                                ListOfKeys.append(k+self.nameSeparator+w )
                elif k[0].upper() == 'R':
                    pass
                elif k[0].upper() == 'G':
                    pass
        return ListOfKeys

    def filter(self, conditions=None, **kwargs):
        """
        Returns a filtered SimDataFrame based on conditions argument.

        To filter over a column simply use the name of the column in the
        condition:
            'NAME>0'

        In case the column name has white spaces, enclose it in ' or " or [ ]:
            "'BLANK SPACE'>0"
            '"BLANK SPACE">0'
            '[BLANK SPACE]>0'

        To set several conditions together the operatos 'and' and 'or'
        are accepted:
            'NAME>0 and LAST>0'

        To filter only over the index set the condition directly:
            '>0'
        or use the key '.index' or '.i' to refer to the index of the SimDataFrame.

        To remove null values append '.notnull' to the column name:
            'NAME.notnull'
        To keep only null values append '.null' to the column name:
            'NAME'.null

        In case the filter criteria is applied on a DataFrame, not a Series,
        the resulting filter needs to be aggregated into a single column.
        By default, the aggregation criteria will return True if any of the
        columns is True.
        This aggregation behaviour can be changed to return True only if all
        the columns are True:
            'MULTIPLE_COLUMNS'.any  needs just one column True to return True
            'MULTIPLE_COLUMNS'.any  needs all the columns True to return True

        """
        returnString = False
        if 'returnString' in kwargs:
            returnString = bool(kwargs['returnString'] )
        returnFilter = False
        if 'returnFilter' in kwargs:
            returnFilter = bool(kwargs['returnFilter'] )
        returnFrame = False
        if 'returnFrame' in kwargs:
            returnFrame = bool(kwargs['returnFrame'] )
        if not returnFilter and not returnString and 'returnFrame' not in kwargs:
            returnFrame = True


        specialOperation = ['.notnull', '.null', '.isnull', '.abs']
        numpyOperation = ['.sqrt', '.log10', '.log2', '.log', '.ln']
        pandasAggregation = ['.any', '.all']
        PandasAgg = ''
        last = ['']

        def KeyToString(filterStr, key, PandasAgg):
            if len(key) > 0:
                # catch particular operations performed by Pandas
                foundSO, foundNO = '', ''
                if key in specialOperation:
                    if filterStr[-1] == ' ':
                        filterStr = filterStr.rstrip()
                    filterStr += key+'()'
                else:
                    for SO in specialOperation:
                        if key.strip().endswith(SO):
                            key = key[:-len(SO)]
                            foundSO =(SO if SO != '.null' else '.isnull' ) + '()'
                            break
                # catch particular operations performed by Numpy
                if key in numpyOperation:
                    raise ValueError("wrong syntax for '"+key+"(blank space before) in:\n   "+conditions)
                else:
                    for NO in numpyOperation:
                        if key.strip().endswith(NO):
                            key = key[:-len(NO)]
                            NO = '.log' if NO == '.ln' else NO
                            filterStr += 'np' + NO + '('
                            foundNO = ' )'
                            break
                # catch aggregation operations performed by Pandas
                if key in pandasAggregation:
                    PandasAgg = key+'(axis=1)'
                else:
                    for PA in pandasAggregation:
                        if key.strip().endswith(PA):
                            PandasAgg = PA+'(axis=1)'
                            break
                # if key is the index
                if key in ['.i', '.index']:
                    filterStr = filterStr.rstrip()
                    filterStr += ' self.DF.index'
                # if key is a column
                elif key in self.columns:
                    filterStr = filterStr.rstrip()
                    filterStr += " self.DF['"+key+"']"
                # key might be a wellname, attribute or a pattern
                elif len(self.find_Keys(key) ) == 1:
                    filterStr = filterStr.rstrip()
                    filterStr += " self.DF['"+ self.find_Keys(key)[0] +"']"
                elif len(self.find_Keys(key) ) > 1:
                    filterStr = filterStr.rstrip()
                    filterStr += " self.DF["+ str(list(self.find_Keys(key)) ) +"]"
                    PandasAgg = '.any(axis=1)'
                else:
                    filterStr += ' ' + key
                filterStr = filterStr.rstrip()
                filterStr += foundSO + foundNO
                key = ''
                last.append('key')
            return filterStr, key, PandasAgg

        if type(conditions) is not str:
            if type(conditions) is not list:
                try:
                    conditions = list(conditions)
                except:
                    raise TypeError('conditions argument must be a string.')
            conditions = ' and '.join(conditions)

        conditions = conditions.strip() + ' '

        # find logical operators and translate to correct key
        AndOrNot = False
        if ' and ' in conditions:
            conditions = conditions.replace(' and ', ' & ')
        if ' or ' in conditions:
            conditions = conditions.replace(' or ', ' | ')
        if ' not ' in conditions:
            conditions = conditions.replace(' not ', ' ~ ')
        if '&' in conditions:
            AndOrNot = True
        elif '|' in conditions:
            AndOrNot = True
        elif '~' in conditions:
            AndOrNot = True

        # create Pandas compatible condition string
        filterStr =  ' ' + '('*AndOrNot
        key = ''
        cond, oper = '', ''
        i = 0
        while i < len(conditions):

            # catch logital operators
            if conditions[i] in ['&', "|", '~']:
                filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                filterStr = filterStr.rstrip()
                auto = ' self.DF.index' if last[-1] in ['(', 'cond', 'oper'] else ''
                filterStr += auto + ' )' + PandasAgg + ' ' + conditions[i] + '('
                last.append('log')
                PandasAgg = ''
                i += 1
                continue

            # catch enclosed strings
            if conditions[i] in ['"', "'", '[']:
                if conditions[i] in ['"', "'"]:
                    try:
                        f = conditions.index(conditions[i], i+1 )
                    except:
                        raise ValueError('wring syntax, closing ' + conditions[i] + ' not found in:\n   '+conditions)
                else:
                    try:
                        f = conditions.index(']', i+1 )
                    except:
                        raise ValueError("wring syntax, closing ']' not found in:\n   "+conditions)
                if f > i+1:
                    key = conditions[i+1:f]
                    filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                    i = f+1
                    continue

            # pass blank spaces
            if conditions[i] == ' ':
                filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                if len(filterStr) > 0 and filterStr[-1] != ' ':
                    filterStr += ' '
                i += 1
                continue

            # pass parenthesis
            if conditions[i] in ['(', ')']:
                if conditions[i] == ')' and filterStr.rstrip()[-1] == '(':
                    filterStr = filterStr.rstrip()[:-1]
                    last.pop()
                else:
                    if last[-1] in ['cond', 'oper'] : key = 'self.DF.index'
                    filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                    filterStr += conditions[i]
                    last.append(conditions[i])
                i += 1
                continue

            # catch conditions
            if conditions[i] in ['=', '>', '<', '!']:
                cond = ''
                f = i+1
                while conditions[f] in ['=', '>', '<', '!']:
                    f += 1
                cond = conditions[i:f]
                if cond == '=':
                    cond = '=='
                elif cond in ['=>', '=<', '=!']:
                    cond = cond[::-1]
                elif cond in ['><', '<>']:
                    cond = '!='
                if key == '' : key = 'self.DF.index'
                filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                filterStr = filterStr.rstrip()
                filterStr += ' ' + cond
                last.append('cond')
                i += len(cond)
                continue

            # catch operations
            if conditions[i] in ['+', '-', '*', '/', '%', '^']:
                oper = ''
                f = i+1
                while conditions[f] in ['+', '-', '*', '/', '%', '^']:
                    f += 1
                oper = conditions[i:f]
                oper = oper.replace('^', '**')
                if last[-1] not in ['key'] : key = 'self.DF.index'
                filterStr, key, PandasAgg = KeyToString(filterStr, key, PandasAgg)
                filterStr = filterStr.rstrip()
                filterStr += ' ' + oper
                last.append('oper')
                i += len(oper)
                continue

            # catch other characters
            else:
                key += conditions[i]
                i += 1
                continue

        # clean up
        filterStr = filterStr.strip()
        # check missing key, means .index by default
        if filterStr[0] in ['=', '>', '<', '!']:
            filterStr = 'self.DF.index ' + filterStr
        elif filterStr[-1] in ['=', '>', '<', '!']:
            filterStr = filterStr + ' self.DF.index'
        # close last parethesis and aggregation
        filterStr += ' )' * bool(AndOrNot + bool(PandasAgg)) + PandasAgg
        # open parenthesis for aggregation, if needed
        if not AndOrNot and bool(PandasAgg):
            filterStr = '(' + filterStr

        retTuple = []
        if returnString:
            retTuple += [ filterStr ]
        if returnFilter or returnFrame:
            try:
                filterArray = eval(filterStr)
            except:
                return None
        if returnFilter:
            retTuple += [ filterArray ]
        if returnFrame:
            retTuple += [ self.DF[ filterArray ] ]

        if len(retTuple ) == 1:
            return retTuple[0]
        else:
            return tuple(retTuple)

    def integrate(self, method='trapz', at=None):
        """
        Calculates numerical integration, using trapezoidal method,
        or constant value of the columns values over the index values.

        method parameter can be: 'trapz' to use trapezoidal method
                                 'const' or 'avg' constant vale multiplied
                                         by delta-index
                                 'month' constant value multiplied by days in month
                                         index must be a datetime-index
                                 'year'  constant value multiplied by days in year
                                         index must be a datetime-index
                                         or integer representing a year

        at parameter defines the row where cumulative will written, only for the
        'const' method
            Possible values are: 'same' to write the cumulative in the same row
                                        of the input value, considering the cumulative
                                        is at the end of the period represented by the row index.
                                 'next' to write the cumulative in the next row, considering the
                                        cumulative is reached at the instant represented
                                        by the row index.

        Returns a new SimDataFrame
        """
        method = method.lower().strip()

        sl1 = slice(0,-1)
        sl2 = slice(1,len(self))

        if method[0] == 't':
            pass
            # sl1 = slice(0,-1)
            # sl2 = slice(1,len(self))
        elif method[0] in 'ac':
            if at is None:
                at = 'next'
            elif str(at).lower().strip() not in ['same','next']:
                raise ValueError("parameter 'at' must be 'same' or 'next'.")
            else:
                at = str(at).lower().strip()
            # sl1 = slice(1,len(self))
            # sl2 = slice(0,-1)
        elif method[0] in 'my':
            pass
        else:
            raise ValueError("'method' parameter must be 'trapz' or 'const'")

        if len(self) < 2:
            print("less than two rows, nothing to integrate.")
            return None

        if method[0] in 'tac':
            dt = np.diff(self.index)
            dtUnits = self.indexUnits
            if str(dt.dtype).startswith('timedelta'):
                dt = dt.astype('timedelta64[s]').astype('float64')/60/60/24
                dtUnits = 'DAYS'
        elif method[0] in 'm':
            dt = daysInMonth(self.index)
            dtUnits = 'DAYS'
        elif method[0] in 'y':
            dt = daysInYear(self.index)
            dtUnits = 'DAYS'

        # if method in ['trapz', 'trapeziod']:
        #     Vmin = np.minimum(self.DF[:-1].set_index(self.index[1:]), self.DF[1:] )
        #     Vmax = np.maximum(self.DF[:-1].set_index(self.index[1:]), self.DF[1:] )
        #     Cumulative =(dt * Vmin.transpose() ).transpose() +(dt *(Vmax - Vmin ).transpose() / 2.0 ).transpose()
        # elif method in ['const', 'constant']:
        #     Cumulative = (dt *(self.DF[:-1]).transpose() ).transpose()[1:]
        if method[0] in 't':
            Vmin = np.minimum(self.DF[sl1].set_index(self.index[sl2], ), self.DF[sl2])
            Vmax = np.maximum(self.DF[sl1].set_index(self.index[sl2], ), self.DF[sl2])
            Cumulative =(dt * Vmin.transpose() ).transpose() +(dt *(Vmax - Vmin ).transpose() / 2.0 ).transpose()
        elif method[0] in 'ac':
            if at == 'same':
                Cumulative = (dt *(self.DF[sl1]).transpose() ).transpose()  # [sl2]
            if at == 'next':
                Cumulative = (dt * (self.DF[sl1].set_index(self.index[sl2], )).transpose()).transpose()
        elif method[0] in 'm':
            Cumulative = ( dt * self.DF.transpose() ).transpose()

        newUnits = {}
        for C, U in self.units.items():
            if U is None:
                newUnits[C] = None
            elif len(U.split('/')) == 2 and (U.split('/')[-1].upper() == dtUnits.upper() or (U.split('/')[-1].upper() in ['DAY', 'DAYS'] and dtUnits.upper() == 'DAYS' ) ):
                newUnits[C] = U.split('/')[0]
            else:
                newUnits[C] = U + '*' + dtUnits

        params = self._SimParameters
        params['units'] = newUnits

        if method[0] in 't' or (method[0] in 'ac' and at == 'next'):
            if str(dt.dtype).startswith('timedelta'):
                firstRow = DataFrame(dict(zip(self.columns, [0.0]*len(self.columns))), index=['0']).set_index(DatetimeIndex([self.index[0]]))
            else:
                firstRow = DataFrame(dict(zip(self.columns, [0.0]*len(self.columns))), index=[self.index[0]])
            # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
            # return SimDataFrame(data=np.cumsum(firstRow.append(Cumulative)), **params)
            return SimDataFrame(data=np.cumsum(pd.concat([firstRow, Cumulative], axis=0)), **params)
        elif method[0] in 'ac' and at == 'same':
            if str(dt.dtype).startswith('timedelta'):
                lastRow = DataFrame(dict(zip(self.columns, [0.0]*len(self.columns))), index=[str(len(self)-1)]).set_index(DatetimeIndex([self.index[-1]]))
            else:
                lastRow = DataFrame(dict(zip(self.columns, [0.0]*len(self.columns))), index=[self.index[-1]])
            # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
            # return SimDataFrame(data=np.cumsum(Cumulative.append(lastRow)), **params)
            return SimDataFrame(data=np.cumsum(pd.concat([Cumulative, lastRow], axis=0)), **params)
        else:
            return SimDataFrame(data=np.cumsum(Cumulative), **params)

    def differenciate(self, na_position='last'):
        """
        Calculates numerical differentiation of the columns values over the index values.

        Returns a new SimDataFrame
        """
        # method=method.lower().strip()

        if len(self) < 2:
            print("less than two rows, nothing to differenciate.")
            return None

        dt = np.diff(self.index)
        dtUnits = self.indexUnits
        if str(dt.dtype).startswith('timedelta'):
            dt = dt.astype('timedelta64[s]').astype('float64')/60/60/24
            dtUnits = 'DAYS'

        diff = np.diff(self.DF.to_numpy(),axis=0)
        diff = diff / dt.reshape(-1,1)

        newUnits = {}
        if self.units is not None:
            for C, U in self.units.items():
                if U is None:
                    newUnits[C] = str(U) + '/' + str(dtUnits)
                elif len(U.split('/')) == 2 and (U.split('/')[-1].upper() == dtUnits.upper() or (U.split('/')[-1].upper() in ['DAY', 'DAYS'] and dtUnits.upper() == 'DAYS' ) ):
                    newUnits[C] = U + '/' + U.split('/')[-1]
                elif len(U.split('*')) == 2 and (U.split('*')[-1].upper() == dtUnits.upper() or (U.split('*')[-1].upper() in ['DAY', 'DAYS'] and dtUnits.upper() == 'DAYS' ) ):
                    newUnits[C] = U.split('*')[0]
                else:
                    newUnits[C] = str(U) + '/' + str(dtUnits)

        if na_position == 'first':
            if str(dt.dtype).startswith('timedelta'):
                NaNRow = DataFrame(dict(zip(self.columns, [None]*len(self.columns))), index=['0']).set_index(DatetimeIndex([self.index[0]]))
            else:
                NaNRow = DataFrame(dict(zip(self.columns, [None]*len(self.columns))), index=[self.index[0]])
            diff = DataFrame(data=diff, index=self.index[1:], columns=self.columns)
            # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead
            # diff = NaNRow.append(diff)
            diff = pd.concat([NaNRow, diff], axis=0)
        else:
            if str(dt.dtype).startswith('timedelta'):
                NaNRow = DataFrame(dict(zip(self.columns, [None]*len(self.columns))), index=['0']).set_index(DatetimeIndex([self.index[-1]]))
            else:
                NaNRow = DataFrame(dict(zip(self.columns, [None]*len(self.columns))), index=[self.index[-1]])
            diff = DataFrame(data=diff, index=self.index[:-1], columns=self.columns)
            # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead
            # diff = diff.append(NaNRow)
            diff = pd.concat([diff, NaNRow], axis=0)

        params = self._SimParameters
        params['units'] = newUnits
        params['indexUnits'] = self.indexUnits
        return SimDataFrame(data=diff, **params)

    def sort_values(self,by=None, axis='--auto', ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None):
        if by is None and axis == '--auto':
            if len(self.index) == 1 and len(self.columns) > 1:
                result = SimDataFrame(data=self.DF.T[self.DF.T.columns[0]].sort_values(axis=0,
                                                                                  ascending=ascending,
                                                                                  inplace=False,
                                                                                  kind=kind,
                                                                                  na_position=na_position,
                                                                                  ignore_index=ignore_index,
                                                                                  key=key).T, **self._SimParameters)
                if inplace:
                    self = result
                    return result
                else:
                    return result
            elif len(self.index) > 1 and len(self.columns) == 1:
                if inplace:
                    super().sort_values(by=self.columns[0], axis=0, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key)
                    return None
                else:
                    return SimDataFrame(data=self.DF.sort_values(by=self.columns[0], axis=0, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key), **self._SimParameters)
            else:
                if axis == '--auto':
                    axis = 0
                if inplace:
                    super().sort_values(axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key)
                    return None
                else:
                    return SimDataFrame(data=self.DF.sort_values(axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key), **self._SimParameters)
        else:
            if axis == '--auto':
                axis = 0
            if inplace:
                super().sort_values(by=by, axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key)
                return None
            else:
                return SimDataFrame(data=self.DF.sort_values(by=by, axis=axis, ascending=ascending, inplace=inplace, kind=kind, na_position=na_position, ignore_index=ignore_index, key=key), **self._SimParameters)

    def head(self,n=5):
        """
        Return the first n rows.

        This function returns first n rows from the object based on position. It is useful for quickly verifying data, for example, after sorting or appending rows.

        For negative values of n, this function returns all rows except the last n rows, equivalent to df[n:].

        Parameters:
        ----------
            n : int, default 5
            Number of rows to select.

        Returns
        -------
            type of caller
            The first n rows of the caller object.
        """
        return SimDataFrame(data=self.DF.head(n),**self._SimParameters)

    def tail(self,n=5):
        """
        Return the last n rows.

        This function returns last n rows from the object based on position. It is useful for quickly verifying data, for example, after sorting or appending rows.

        For negative values of n, this function returns all rows except the first n rows, equivalent to df[n:].

        Parameters:
        ----------
            n : int, default 5
            Number of rows to select.

        Returns
        -------
            type of caller
            The last n rows of the caller object.
        """
        return SimDataFrame(data=self.DF.tail(n),**self._SimParameters)

    def cumsum(self, skipna=True, *args, **kwargs):
        """
        Return cumulative sum over a SimDataFrame.

        Returns a SimDataFrame or SimSeries of the same size containing the cumulative sum.

        Parameters:
            axis : {0 or ‘index’, 1 or ‘columns’}, default 0
                The index or the name of the axis. 0 is equivalent to None or ‘index’.

        skipna: bool, default True
            Exclude NA/null values. If an entire row/column is NA, the result will be NA.

        *args, **kwargs
            Additional keywords have no effect but might be accepted for compatibility with NumPy.

        Returns
            SimSeries or SimDataFrame
            Return cumulative sum of Series or DataFrame.
        """
        return SimDataFrame(data=self.DF.cumsum(skipna=skipna, *args, **kwargs),**self._SimParameters)

    def jitter(self, std=0.10):
        """
        add jitter the values of the SimDataFrame
        """
        return jitter(self, std)

    def melt(self, **kwargs):
        from .._common.functions import _meltDF
        melted = _meltDF(self, FullOutput=False)
        if len(melted[melted.columns[-1]].unique()) == 1:
            params = self._SimParameters
            params['units'] = {melted.columns[0]:melted[melted.columns[-1]].unique()[0]}
            return SimDataFrame(data=melted.iloc[:,:-1], **params)
        else:
            return melted

    def DaysInYear(self, column=None):
        """
        returns a SimSeries with the number of days in a particular year

        Parameters
        ----------
        column : str
            The selected column must be an array of dtype integer, date, datetime containing
            the year to calculate the number of day.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        return self.daysInYear(column=column)

    def daysinyear(self, column=None):
        """
        returns a SimSeries with the number of days in a particular year

        Parameters
        ----------
        column : str
            The selected column must be an array of dtype integer, date, datetime containing
            the year to calculate the number of day.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        return self.daysInYear(column=column)

    def daysInYear(self, column=None):
        """
        returns a SimSeries with the number of days in a particular year

        Parameters
        ----------
        column : str
            The selected column must be an array of dtype integer, date, datetime containing
            the year to calculate the number of day.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        params = self._SimParameters
        params['index'] = self.index
        if column is not None:
            if type(column) is str and column in self.columns:
                if self[column].dtype in ('int','int64') and self[column].min() > 0:
                    params['name'] = 'DaysInYear'
                    params['units'] = 'days'
                    return SimSeries( data=daysInYear(self[column].to_numpy()), **params )
                elif 'datetime' in str(self[column].dtype):
                    return daysInYear(self[column])
                else:
                    raise ValueError('selected column is not a valid date or year integer')
            elif type(column) is str and column not in self.columns:
                raise ValueError('the selected column is not in this SimDataFrame')
            elif type(column) is not str and hasattr(column,'__iter__'):
                result = self._class(data={}, index=self.index, **self._SimParameters)
                for col in column:
                    if col in self.columns:
                        result[col] = daysInYear(self[col])
                        result.set_Units('days',col)
                return result
        else:
            if self.index.dtype in ('int','int64') and self.index.min() > 0:
                params['name'] = 'DaysInYear'  # params['indexName'] = 'DaysInYear'
                params['indexUnits'] = self.indexUnits
                params['index'] = self.index  # params['index'] = list(daysInYear(self.index.to_numpy()))
                # params['columns'] = self.columns
                params['units'] = 'days'  # params['units'] = self.units.copy()
                return SimSeries( data=list(daysInYear(self.index.to_numpy())), **params )  # self._class( data=self.DF.values, **params )
            elif 'datetime' in str(self.index.dtype):
                params['name'] = 'DaysInYear'
                params['units'] = 'days'
                params['indexUnits'] = self.indexUnits
                params['index'] = self.index
                return SimSeries( data=list(daysInYear(self.index)), **params ) # self._class( data=self.DF.values, index=list(daysInYear(self.index)), columns=self.columns, **self._SimParameters )
            else:
                raise ValueError('index is not a valid date or year integer')

    def RealYear(self,column=None):
        """
        returns a SimSeries with the year and cumulative days as fraction

        Parameters
        ----------
        column : str
            The selected column must be a datetime array.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        return self.realYear(column)

    def realyear(self,column=None):
        """
        returns a SimSeries with the year and cumulative days as fraction

        Parameters
        ----------
        column : str
            The selected column must be a datetime array.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        return self.realYear(column)

    def realYear(self,column=None):
        """
        returns a SimSeries with the year and cumulative days as fraction

        Parameters
        ----------
        column : str
            The selected column must be a datetime array.

        Returns
        -------
        a new SimSeries with the resulting array and same index as the input.
        """
        params = self._SimParameters
        params['index'] = self.index
        params['name'] = 'realYear'
        params['units'] = 'Years'
        if column is not None:
            if type(column) is str and column in self.columns:
                if 'datetime' in str(self[column].dtype):
                    return SimSeries(data=realYear(self[column]) , **params)
                else:
                    raise ValueError('selected column is not a valid date format')
            elif type(column) is str and column not in self.columns:
                raise ValueError('the selected column is not in this SimDataFrame')
            elif type(column) is not str and hasattr(column,'__iter__'):
                result = self._class(data={},index=self.index,**self._SimParameters)
                for col in column:
                    if col in self.columns:
                        result[col] = daysInYear(self[col])
                return result
        else:
            if 'datetime' in str(self.index.dtype):
                return SimSeries(data=list(realYear(self.index)), **params)
            else:
                raise ValueError('index is not a valid date or year integer')

    def slope(self, x=None, y=None, window=None, slope=True, intercept=False):
        """
        Calculates the slope of column Y vs column X or vs index if 'x' is None

        Parameters
        ----------
        x : str, optional
            The name of the column to be used as X.
            If None, the index of the DataFrame will be used as X.
            The default is None.
        y : str, optional
            The name of the column to be used as Y.
            If None, the first argument will be considered as Y (not as X).
            The default is None.
        window : int, float or str, optional
            The half-size of the rolling window to calculate the slope.
            if None : the slope will be calculated from the entire dataset.
            if int : window rows before and after of each row will be used to calculate the slope
            if float : the window size will be variable, with window values of X arround each row's X. Not compatible with datetime columns
            if str : the window string will be used as timedelta arround the datetime X
            The default is None.
        slope : bool, optional
            Set it True to return the slope of the linear fit. The default is True.
        intercept : bool, optional
            Set it True to return the intersect of the linear fit. The default is False.
        if both slope and intercept are True, a tuple of both results will be returned

        Returns
        -------
        numpy array
            The array containing the desired output.

        """
        params = self._SimParameters
        if x is not None and y is not None:
            if x in self.columns and y in self.columns:
                xUnits = str(self.get_Units(x)[x])
            elif x in self.columns and y not in self.columns:
                xUnits = str(self.indexUnits)
        else:
            xUnits = str(self.indexUnits)
        for col in self.columns:
            if col is not None and len(self.get_Units(col)) == 1:
                params['units']['slope_of_' + str(col)] = str(self.get_Units(col)[col]) + '/' + xUnits
        names = ['slope_of_' + str(col) for col in self.columns]
        slopeDF = _slope(df=self, x=x, y=y, window=window, slope=slope, intercept=intercept)
        return SimDataFrame(data=slopeDF, index=self.index, columns=names, **params)

    def plot(self, y=None, x=None, others=None, figsize=None, dpi=None, **kwargs):
        """
        wrapper of Pandas plot method, with some superpowers

        Parameters
        ----------
        y : string, list or index; optional
            Column name to plot. The default is None.
        x : string, optional
            The columns to be used for x coordinates. The default is the index.
        others : SimDataFrame, SimSeries, DataFrame or Series; optional
            Other Frames to include in the plot, for the same selected columns. The default is None.
        figsize : (float, float), optional
            Width, height in inches.
            It will be passed to matplotlib.pyplot.figure to create the figure.
            Only valid for a new figure ('figure' keyword not found in kwargs).
        dpi : float, optional
            The resolution of the figure in dots-per-inch.
            It will be passed to matplotlib.pyplot.figure to create the figure.
            Only valid for a new figure ('figure' keyword not found in kwargs).
        xMin, xMin, yMin, yMax : as per values of X or Y axes.
            A shorcut to xlim and ylim matplotlib keywords,
            must be provided as keyword arguments.
        **kwargs : matplotlib_keyword='paramenter'
            any other keyword argument for matplolib.

        Returns
        -------
        matplotlib AxesSubplot.
        """
        y = self.columns if y is None else [y] if type(y) is str else y
        y = [ i for i in y if i != x ] if x is not None else y

        if 'xMin' in kwargs:
            if 'xlim' in kwargs:
                kwargs['xlim'] = (kwargs['xMin'], kwargs['xlim'][1])
            else:
                kwargs['xlim'] = (kwargs['xMin'], None)
            del kwargs['xMin']
        if 'xMax' in kwargs:
            if 'xlim' in kwargs:
                kwargs['xlim'] = (kwargs['xlim'][0], kwargs['xMax'])
            else:
                kwargs['xlim'] = (None, kwargs['xMax'])
            del kwargs['xMax']
        if 'yMin' in kwargs:
            if 'ylim' in kwargs:
                kwargs['ylim'] = (kwargs['yMin'], kwargs['ylim'][1])
            else:
                kwargs['ylim'] = (kwargs['yMin'], None)
            del kwargs['yMin']
        if 'yMax' in kwargs:
            if 'ylim' in kwargs:
                kwargs['ylim'] = (kwargs['ylim'][0], kwargs['yMax'])
            else:
                kwargs['ylim'] = (None, kwargs['yMax'])
            del kwargs['yMax']

        if type(others) is str:
            marker = [m for m in '.,ov^<>12348spP*hH+xXDd|_' if m in others]
            if len(marker) > 0:
                kwargs['marker'] = marker[0]
            linestyle = [l for l in ['--','-','-.',':'] if l in others]
            if len(linestyle) > 0:
                kwargs['linestyle'] = linestyle[0]
            else:
                kwargs['linestyle'] = 'None'
            color = [c for c in 'bgrcmykw' if c in others]
            if len(color) > 0:
                if 'marker' in kwargs:
                    kwargs['markerfacecolor'] = color[0]
                kwargs['color'] = color[0]
            others = None

        if figsize is not None or dpi is not None:
            if 'figure' not in kwargs and 'ax' not in kwargs:
                kwargs['figure'], kwargs['ax'] = plt.subplots(figsize=figsize, dpi=dpi)

        labels = None
        if others is None:
            if 'labels' in kwargs:
                if type(kwargs['labels']) is not list:
                    kwargs['labels'] = [kwargs['labels']]
                if len(kwargs['labels']) == len(y):
                    labels = kwargs['labels']
                del kwargs['labels']
            if 'ylabel' not in kwargs:
                kwargs['ylabel'] = ('\n').join([ str(yi) + (' [' + str(self.get_units(yi)[yi]) +']' ) if self.get_units(yi)[yi] is not None else '' for yi in y ])
            if x is not None:
                if x in self.columns:
                    if labels is None:
                        fig = self.DF.plot(x=x, y=y, **kwargs)
                    else:
                        fig = self.DF.plot(x=x, y=y, label=labels, **kwargs)
                    plt.tight_layout()
                    return fig
                else:
                    raise ValueError("Required 'x', " + str(x) + " is not a column name in this SimDataFrame")
            else:
                if labels is None:
                    fig = self[y].DF.plot(**kwargs)
                else:
                    fig = self[y].DF.plot(label=labels, **kwargs)
                plt.tight_layout()
                return fig
        else:
            if type(others) not in (list,tuple):
                others = [others]
            if len(others) > 10 and 'legend' not in kwargs:
                kwargs['legend'] = False
            if 'labels' in kwargs:
                if type(kwargs['labels']) is list:
                    if len(kwargs['labels']) == len(others) + 1:
                        if len(y) == 1:
                            labels = [ (la if type(la) is list else [str(la)]) for la in kwargs['labels'] ]
                        else:
                            labels = [ (la if type(la) is list else [str(ys)+' '+str(la) for ys in y ]) for la in kwargs['labels'] ]
                del kwargs['labels']
            if 'ax' in kwargs and kwargs['ax'] is not None:
                if labels is None:
                    kwargs['ax'] = self.plot(y=y, x=x, others=None, **kwargs)
                else:
                    kwargs['ax'] = self.plot(y=y, x=x, others=None, label=labels[0], **kwargs)
            else:
                fig = self.plot(y=y, x=x, others=None, **kwargs)
                kwargs['ax'] = fig

            labcount = 0
            for oth in others:
                labcount += 1
                if type(oth) in (SimDataFrame,SimSeries):
                    newY = [ ny for ny in self.columns if ny in oth ]
                    if labels is None:
                        kwargs['ax'] = oth[newY].to(self.get_units()).plot(y=y, x=x, others=None, **kwargs)
                    else:
                        kwargs['ax'] = oth[newY].to(self.get_units()).plot(y=y, x=x, others=None,
                                                                           label=labels[labcount], **kwargs)
                elif isinstance(oth,DataFrame):
                    newY = [ ny for ny in self.columns if ny in oth ]
                    if labels is None:
                        kwargs['ax'] = oth[newY].plot(**kwargs)
                    else:
                        kwargs['ax'] = oth[newY].plot(label=labels[labcount], **kwargs)
                elif isinstance(oth,Series):
                    if labels is None:
                        kwargs['ax'] = oth.plot(**kwargs)
                    else:
                        kwargs['ax'] = oth.plot(label=labels[labcount], **kwargs)
                else:
                    raise TypeError("others must be SimDataFrame, DataFrame, SimSeries or Series")
            return kwargs['ax']

    def concat(self, objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True, squeeze=True):
        """
        wrapper of pandas.concat enhaced with units support

        Return:
            SimDataFrame
        """
        if type(objs) not in [list, SimDataFrame, DataFrame, SimSeries, Series]:
            raise TypeError("objs must be a list of DataFrames or SimDataFrames")
        if len(objs) == 1:
            print("WARNING: only 1 DataFrame received.")
            return [objs][0]
        if type(objs) is not list:
            objs =  [objs]
        return concat([self]+objs, axis=axis, join=join, ignore_index=ignore_index, keys=keys, levels=levels, names=names, verify_integrity=verify_integrity, sort=sort, copy=copy, squeeze=squeeze)

    def to_schedule(self,path,units='FIELD',ControlMode=None,ShutStop=None):
        """
        export a eclipse style schedule file.

        Parameters
        ----------
        units : str or dict, optional
            a string 'FIELD', 'METRIC', LAB or PVT-M will convert the data to the corresponding eclipse simulator units system.
            a dictionary should contain desired units for all the columns to be converted. The default is None.
        ControlMode : str or dict, optional
            a string defining the control mode for the simulation:'ORAT','WRAT','GRAT'
            a dictionary with pairs of item:ControlModel for each item (well or group).
        ShutStop : str, optional
            a string 'OPEN, 'SHUT' or 'STOP' indicating what to do with the wells when their rate is zero.


        Returns
        -------
        None.
        """
        from .._common.stringformat import date as strDate
        from .._Classes.Errors import OverwritingError
        import os

        if os.path.isfile(path):
            raise OverwritingError("The output file already exists:\n  '" + str(path) + "'")

        eclipseUnits0 = {'FIELD':{'OPR':'stb/day',  # Oil rate
                                 'WPR':'stb/day',  # Water rate
                                 'GPR':'Mscf/day',  # Gas rate
                                 'LPR':'stb/day',  # Liquid rate
                                 # 'RFR':'rb/day',  # Reservoir fluid volume rate
                                 'BHP':'psia',  # BHP
                                 'THP':'psia',  # THP
                                 # 'WGPR': 'Mscf/day',  # Wet gas production rate
                                 # 'TMR':'lb-M/day',  # Total molar rate
                                 # 'SPR': 'stb/day',  # Steam production rate
                                 },
                        'METRIC':{'OPR':'sm3/day',  # Oil rate
                                 'WPR':'sm3/day',  # Water rate
                                 'GPR':'sm3/day',  # Gas rate
                                 'LPR':'sm3/day',  # Liquid rate
                                 # 'RFR':'rm3/day',  # Reservoir fluid volume rate
                                 'BHP':'barsa',  # BHP
                                 'THP':'barsa',  # THP
                                 # 'WGPR': 'sm3/day',  # Wet gas production rate
                                 # 'TMR':'kg-M/day',  # Total molar rate
                                 # 'SPR': 'sm3/day',  # Steam production rate
                                 },
                        'LAB':{'OPR':'scc/hr',  # Oil rate
                                 'WPR':'scc/hr',  # Water rate
                                 'GPR':'scc/hr',  # Gas rate
                                 'LPR':'scc/hr',  # Liquid rate
                                 # 'RFR':'rcc/hr',  # Reservoir fluid volume rate
                                 'BHP':'atma',  # BHP
                                 'THP':'atma',  # THP
                                 # 'WGPR': 'Mscf/day',  # Wet gas production rate
                                 # 'TMR':'lb-M/day',  # Total molar rate
                                 # 'SPR': 'stb/day',  # Steam production rate
                                 },
                        'PVT-M':{'OPR':'sm3/day',  # Oil rate
                                 'WPR':'sm3/day',  # Water rate
                                 'GPR':'sm3/day',  # Gas rate
                                 'LPR':'sm3/day',  # Liquid rate
                                 # 'RFR':'rm3/day',  # Reservoir fluid volume rate
                                 'BHP':'atma',  # BHP
                                 'THP':'atma',  # THP
                                 # 'WGPR': 'Mscf/day',  # Wet gas production rate
                                 # 'TMR':'lb-M/day',  # Total molar rate
                                 # 'SPR': 'stb/day',  # Steam production rate
                                 }}

        # create dictionary for keyword parameters
        if units in eclipseUnits0:
            # eclipseUnits = {}
            # for each in eclipseUnits0[units]:
            #     for X in 'FGW':
            #         for H in ' H':
            #             eclipseUnits[X+each+H.strip()] = eclipseUnits0[units][each]
            # del eclipseUnits0
            # units = eclipseUnits
            units = { X+each+H.strip():eclipseUnits0[units][each] for each in eclipseUnits0[units] for X in 'FGW' for H in ' H' }
            del eclipseUnits0

        data = self.to(units).wellStatus().melt()

        indexName = data.index.name
        itemName = data.columns[2]

        if indexName is not None and itemName is not None and len(indexName)>0 and len(itemName)>0:
            data = data.reset_index().sort_values(by=[indexName,itemName,'attribute'],axis=0,ascending=True).set_index(indexName)
        else:
            data = data.melt().sort_index(axis=0,ascending=True)

        out = {'WCONHIST':DataFrame(index=data[itemName].unique(), columns=range(2,13)),
               'WCONINJH':DataFrame(index=data[itemName].unique(), columns=range(2,13)),
               'WCONPROD':DataFrame(index=data[itemName].unique(), columns=range(2,21)),
               'WCONINJE':DataFrame(index=data[itemName].unique(), columns=range(2,16))}

        if ShutStop is None:
            ShutStop = 'STOP'

        if type(ControlMode) is str:
            ControlMode = { item:ControlMode for item in data[itemName].unique() }

        itemCol = 2
        valueCol = 0
        attCol = 1

        curtime = ''
        lastime = None
        i = 0

        GORcriteria = 10

        outstr = []

        for i in range(len(data)):
            curtime = data.iloc[i].name
            if i == 0:
                lastime = curtime

            if lastime != curtime or i == len(data)-1:
                # prepare keywords to write
                out['WCONHIST']['keyword'] = 'WCONHIST'
                out['WCONINJH']['keyword'] = 'WCONINJH'
                out['WCONPROD']['keyword'] = 'WCONPROD'
                out['WCONINJE']['keyword'] = 'WCONINJE'
                keywords = out['WCONHIST'].append(out['WCONINJH']).append(out['WCONPROD']).append(out['WCONINJE'])
                keywords.dropna(axis=0, how='all',subset=range(2,13),inplace=True)

                prodh = keywords['keyword'] == 'WCONHIST'
                keywords.loc[prodh,2] = [ 'OPEN' if each else ShutStop for each in (keywords.loc[prodh,4:6].sum(axis=1) > 0) ]

                injeh = keywords['keyword'] == 'WCONINJH'
                keywords.loc[injeh,3] = [ 'OPEN' if each else ShutStop for each in (keywords.loc[injeh,4] > 0) ]

                prodf = keywords['keyword'] == 'WCONPROD'
                keywords.loc[prodf,2] = [ 'OPEN' if each else ShutStop for each in (keywords.loc[prodf,4:7].sum(axis=1) > 0) ]

                injef = keywords['keyword'] == 'WCONINJE'
                keywords.loc[injef,3] = [ 'OPEN' if each else ShutStop for each in (keywords.loc[injef,5:6].sum(axis=1) > 0) ]

                if ControlMode is None or item not in ControlMode:
                    notnull = keywords.loc[prodh,[4,6,5]].notna()
                    checkgor = DataFrame({4: keywords.loc[prodh,4].fillna(0) * GORcriteria > keywords.loc[prodh,6].fillna(0) , 5: (keywords.loc[prodh,5].notna()) & ((keywords.loc[prodh,4].isna()) & (keywords.loc[prodh,6].isna())) , 6: keywords.loc[prodh,4].fillna(0) * GORcriteria <= keywords.loc[prodh,6].fillna(0) })
                    keywords.loc[prodh,3] = ((notnull*checkgor).astype(int) *   np.array(['ORAT','GRAT','WRAT']).reshape(1,-1)).sum(axis=1)
                else:
                    keywords.loc[:,3] = [ ControlMode[item] for item in keywords.loc[:].index ]

# working on how to select from the several keyword lines for each well which is the correct keyword to write

                keywords['ranking'] = keywords.loc[:,4:20].count(axis=1)

                keywords.reset_index().sort_values(['index','keyword','ranking'],axis=0,ascending=[True,True,False]).groupby('index').first()[['keyword']]


                # write keywords
                for kw in keywords['keyword'].unique():
                    outstr.append(kw)
                    for i in range(len(keywords[keywords['keyword'] == kw])):
                        line = ' ' + ' '.join(map(str,keywords.reset_index().iloc[0].fillna('1*').drop('keyword').to_list())) + ' /'
                        outstr.append(line)
                    outstr.append('/')
                    outstr.append('\n')

                # write lastime
                if type(lastime) in (int,float):
                    outstr.append('TSTEP')
                    outstr.append(' ' + str(lastime) + ' /')
                    outstr.append('/')
                else:
                    outstr.append('DATES')
                    outstr.append(' ' + dt.datetime(lastime).strftime("%d %d %Y %H:%M:%S") + ' /')
                    outstr.append('/')
                outstr.append('\n')

                # reset out (keywords) dictionary
                out = {'WCONHIST':DataFrame(index=data[itemName].unique(), columns=range(2,13)),
                       'WCONINJH':DataFrame(index=data[itemName].unique(), columns=range(2,13)),
                       'WCONPROD':DataFrame(index=data[itemName].unique(), columns=range(2,21)),
                       'WCONINJE':DataFrame(index=data[itemName].unique(), columns=range(2,16))}

            # read the input table and put the values in the corresponding parameter of the keywords
            if data.iloc[i,attCol] == 'WSTATUS':  # oil production rate
                out['WCONHIST'].loc[data.iloc[i,itemCol],'Status'] = data.iloc[i,valueCol]
                out['WCONINJH'].loc[data.iloc[i,itemCol],'Status'] = data.iloc[i,valueCol]
                out['WCONPROD'].loc[data.iloc[i,itemCol],'Status'] = data.iloc[i,valueCol]
                out['WCONINJE'].loc[data.iloc[i,itemCol],'Status'] = data.iloc[i,valueCol]

            elif data.iloc[i,attCol] == 'WOPRH':  # oil production rate
                out['WCONHIST'].loc[data.iloc[i,itemCol],4] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WWPRH':  # water production rate
                out['WCONHIST'].loc[data.iloc[i,itemCol],5] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WGPRH':  # gas production rate
                out['WCONHIST'].loc[data.iloc[i,itemCol],6] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WVFPH':  # well VFP table number
                out['WCONHIST'].loc[data.iloc[i,itemCol],7] = data.iloc[i,valueCol]
                out['WCONINJH'].loc[data.iloc[i,itemCol],7] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WALQH':  # Artificial lift quantity
                out['WCONHIST'].loc[data.iloc[i,itemCol],8] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WTHPH':  # tubing head pressure (THP)
                out['WCONHIST'].loc[data.iloc[i,itemCol],9] = data.iloc[i,valueCol]
                out['WCONINJH'].loc[data.iloc[i,itemCol],6] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WBHPH':  # bottom hole pressure (BHP)
                out['WCONHIST'].loc[data.iloc[i,itemCol],10] = data.iloc[i,valueCol]
                out['WCONINJH'].loc[data.iloc[i,itemCol],5] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WWGPRH':  # wet gas production rate
                out['WCONHIST'].loc[data.iloc[i,itemCol],11] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] in ('WNPRH','WNLPRH'):  # NGL rate
                out['WCONHIST'].loc[data.iloc[i,itemCol],12] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WOIRH':
                out['WCONINJH'].loc[data.iloc[i,itemCol],4] = data.iloc[i,valueCol]
                out['WCONINJH'].loc[data.iloc[i,itemCol],2] = 'OIL'
            elif data.iloc[i,attCol] == 'WWIRH':
                out['WCONINJH'].loc[data.iloc[i,itemCol],4] = data.iloc[i,valueCol]
                out['WCONINJH'].loc[data.iloc[i,itemCol],2] = 'WATER'
            elif data.iloc[i,attCol] == 'WGIRH':
                out['WCONINJH'].loc[data.iloc[i,itemCol],4] = data.iloc[i,valueCol]
                out['WCONINJH'].loc[data.iloc[i,itemCol],2] = 'GAS'
            elif data.iloc[i,attCol] == 'WCTRL':
                out['WCONHIST'].loc[data.iloc[i,itemCol],3] = data.iloc[i,valueCol]
                out['WCONINJH'].loc[data.iloc[i,itemCol],12] = data.iloc[i,valueCol]
                out['WCONPROD'].loc[data.iloc[i,itemCol],3] = data.iloc[i,valueCol]
                out['WCONINJE'].loc[data.iloc[i,itemCol],4] = data.iloc[i,valueCol]

            elif data.iloc[i,attCol] == 'WOPR':  # oil production rate
                out['WCONPROD'].loc[data.iloc[i,itemCol],4] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WWPR':  # water production rate
                out['WCONPROD'].loc[data.iloc[i,itemCol],5] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WGPR':  # gas production rate
                out['WCONPROD'].loc[data.iloc[i,itemCol],6] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WLPR':  # liquid production rate
                out['WCONPROD'].loc[data.iloc[i,itemCol],7] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WVFP':  # Reservoir fluid volume rate
                out['WCONPROD'].loc[data.iloc[i,itemCol],8] = data.iloc[i,valueCol]
                # out['WCONINJH'].loc[data.iloc[i,itemCol],7] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WALQ':  # Artificial lift quantity
                out['WCONPROD'].loc[data.iloc[i,itemCol],12] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WVFP':  # well VFP table number
                out['WCONPROD'].loc[data.iloc[i,itemCol],11] = data.iloc[i,valueCol]
                out['WCONINJE'].loc[data.iloc[i,itemCol],9] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WTHP':  # tubing head pressure (THP)
                out['WCONPROD'].loc[data.iloc[i,itemCol],10] = data.iloc[i,valueCol]
                out['WCONINJE'].loc[data.iloc[i,itemCol],8] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WBHP':  # bottom hole pressure (BHP)
                out['WCONPROD'].loc[data.iloc[i,itemCol],9] = data.iloc[i,valueCol]
                out['WCONINJE'].loc[data.iloc[i,itemCol],7] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WWGPR':  # wet gas production rate
                out['WCONPROD'].loc[data.iloc[i,itemCol],13] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] in ('WNPR','WNLPR'):  # NGL rate
                out['WCONPROD'].loc[data.iloc[i,itemCol],20] = data.iloc[i,valueCol]
            # elif data.iloc[i,attCol] == 'WNPR':  # Total molar rate
            #     out['WCONPROD'].loc[data.iloc[i,itemCol],14] = data.iloc[i,valueCol]
            # elif data.iloc[i,attCol] == 'WNPR':  # Steam production rate
            #     out['WCONPROD'].loc[data.iloc[i,itemCol],15] = data.iloc[i,valueCol]
            # elif data.iloc[i,attCol] == 'WNPR':  # Calorific rate
            #     out['WCONPROD'].loc[data.iloc[i,itemCol],18] = data.iloc[i,valueCol]
            # elif data.iloc[i,attCol] == 'WNPR':  # Linearly combined rate
            #     out['WCONPROD'].loc[data.iloc[i,itemCol],19] = data.iloc[i,valueCol]
            elif data.iloc[i,attCol] == 'WOIR':  # Surface flow rate
                out['WCONINJE'].loc[data.iloc[i,itemCol],5] = data.iloc[i,valueCol]
                out['WCONINJE'].loc[data.iloc[i,itemCol],2] = 'OIL'
            elif data.iloc[i,attCol] == 'WWIR':  # Surface flow rate
                out['WCONINJE'].loc[data.iloc[i,itemCol],5] = data.iloc[i,valueCol]
                out['WCONINJE'].loc[data.iloc[i,itemCol],2] = 'WATER'
            elif data.iloc[i,attCol] == 'WGIR':  # Surface flow rate
                out['WCONINJE'].loc[data.iloc[i,itemCol],5] = data.iloc[i,valueCol]
                out['WCONINJE'].loc[data.iloc[i,itemCol],2] = 'GAS'
            # elif data.iloc[i,attCol] == 'WGIR':  # Vaporized oil concentration in the injected gas, or dissolved gas concentration in the injected oil
            #     out['WCONINJE'].loc[data.iloc[i,itemCol],10] = data.iloc[i,valueCol]
            # elif data.iloc[i,attCol] == 'WGIR':  # Thermal: ratio of gas volume to steam volume (C.W.E.) for a STEAM-GAS injector
            #     out['WCONINJE'].loc[data.iloc[i,itemCol],11] = data.iloc[i,valueCol]
            # elif data.iloc[i,attCol] == 'WGIR':  # Surface volume proportion of oil in a multiphase injecto
            #     out['WCONINJE'].loc[data.iloc[i,itemCol],12] = data.iloc[i,valueCol]
            # elif data.iloc[i,attCol] == 'WGIR':  # Surface volume proportion of water in a multiphase injecto
            #     out['WCONINJE'].loc[data.iloc[i,itemCol],13] = data.iloc[i,valueCol]
            # elif data.iloc[i,attCol] == 'WGIR':  # Surface volume proportion of gas in a multiphase injecto
            #     out['WCONINJE'].loc[data.iloc[i,itemCol],14] = data.iloc[i,valueCol]
            # elif data.iloc[i,attCol] == 'WGIR':  # Ratio of oil volume to steam volume (C.W.E.) for a STEAM-OIL injector (for use with steam-solvent injection).
            #     out['WCONINJE'].loc[data.iloc[i,itemCol],15] = data.iloc[i,valueCol]

            lastime = curtime

    def to_SimationResults(self):
        """
        loads the current frame into a SimulationResults excelObject.

        return XLSX instance from Simulation Results
        """
        from datafiletoolbox.SimulationResults.excelObject import XLSX
        return XLSX(frames=self)

    def info(self,*args,**kwargs):
        """
        wrapper for pandas.DataFrame.info() but with Units.
        """
        def fillblank(string,length):
            if len(string.strip()) > length:
                return string.strip() + ' '
            return string.strip() + ' '*(length - len(string.strip()) + 1)

        print(type(self))
        print( str(type(self.DF.index)).split('.')[-1][:-2] + ': ' + str(len(self)) + ' entries, ' + str(self.index[0]) + ' to ' + str(self.index[-1]))

        columns = [ str(col) for col in self.columns ]
        notnulls = [ str(self.iloc[:,col].notnull().sum()) for col in range(len(self.columns)) ]
        dtypes = [ str(self.iloc[:,col].dtype) for col in range(len(self.columns)) ]
        units = [ str(self.units[col]) for col in self.columns ]

        print('Data columns (total ' + str(len(columns)) + ' columns):')

        line = ' ' + fillblank('#', len(str(len(columns))))
        line = line + ' ' + fillblank('Column', max(len('Column'), max(map(len,columns))))
        line = line + ' ' + fillblank('Non-Null Count', max(len('Non-Null Count'), len(str(len(self))) + len(' non-null')))
        line = line + ' ' + fillblank('Dtype',max(len('Dtype'), max(map(len,dtypes))))
        line = line + ' ' + fillblank('Units',max(len('Units'), max(map(len,units))))
        print(line)

        line = fillblank('---', len(str(len(columns))))
        line = line + ' ' + fillblank('------', max(map(len,columns)))
        line = line + ' ' + fillblank('--------------', len(str(len(self))) + len(' non-null '))
        line = line + ' ' + fillblank('-----',max(map(len,dtypes)))
        line = line + ' ' + fillblank('-----',max(map(len,units)))
        print(line)

        for i in range(len(columns)):
            line = ' ' + fillblank(str(i), max(len('# '), len(str(len(columns)))))
            line = line + ' ' + fillblank(columns[i], max(len('Column'), max(map(len,columns))))
            line = line + ' ' + fillblank(notnulls[i] + ' non-null', max(len('Non-Null Count'), len(str(len(self))) + len(' non-null')))
            line = line + ' ' + fillblank(dtypes[i], max(len('Dtype'), max(map(len,dtypes))))
            line = line + ' ' + fillblank(units[i], max(len('Units'), max(map(len,units))))
            print(line)

        print('dtypes: ' + ', '.join([ each + '(' + str(dtypes.count(each)) + ')' for each in sorted(set(dtypes)) ]))

        print( 'memory usage: ' + str(int(getsizeof(self)/1024/1024*10)/10) + '+ MB')

        return None

    def wellStatus(self, inplace=False):
        """
        define if a well if producer or injector at each row

        Parameters
        ----------
        inplace : bool, optional
            apply the results to the original dataframe. The default is False.

        Returns
        -------
        SimDataFrame
            with a new categorical column for each well 'WSTATUS'
            containing the string 'PRODUCER' or 'INJECTOR'.

        """
        tempdf = SimDataFrame(self)

        for w in tempdf.wells:
            try:
                temp = tempdf['W?PR*:'+str(w)]
                tempdf['_PROD:'+str(w)] = (temp != 0).sum(axis=1)
            except:
                tempdf['_PROD:'+str(w)] = 0
            try:
                temp = tempdf['W?IR*:'+str(w)]
                tempdf['_INJE:'+str(w)] = (temp != 0).sum(axis=1)
            except:
                tempdf['_INJE:'+str(w)] = 0

            tempdf['WSTATUS:'+str(w)] = [ 'PRODUCER' if tempdf['_PROD:'+str(w)].iloc[i] > tempdf['_INJE:'+str(w)].iloc[i] else 'INJECTOR' if tempdf['_PROD:'+str(w)].iloc[i] < tempdf['_INJE:'+str(w)].iloc[i] else None for i in range(len(tempdf)) ]

        tempdf['WSTATUS:'+str(w)] = tempdf['WSTATUS:'+str(w)].fillna(method='ffill').fillna(method='bfill').astype('category')

        if inplace:
            self['WSTATUS:'+str(w)] = tempdf['WSTATUS:'+str(w)]
        else:
            return tempdf.drop(columns=['_INJE:'+str(w), '_PROD:'+str(w)], inplace=True)


    # def rolling(self, window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None, method='single'):
    #     return SimRolling(self.df, window, min_periods=min_periods, center=center, win_type=win_type, on=on, axis=axis, closed=closed, method=method,
    #         SimParameters=self._SimParameters,
    #         )


def daysInYear(year):
    """
    returns the number of days in a particular year

    Parameters
    ----------
    year : int, date, datetime or array-like of int, date, or datetime
        The year to calculate the number of days.
        Can a single year, represented as an integer or as date or datetime object
        Also, list or array of year is accepted.

    Returns
    -------
    int or array of ints, according to the input
    """
    if type(year) in (int,float):
        return dt.date(int(year), 12, 31).timetuple().tm_yday
    if type(year) in (dt.date, dt.datetime):
        return dt.date(year.timetuple().tm_year, 12, 31).timetuple().tm_yday
    if type(year) is pd.Timestamp:
        return dt.date(year.year,12,31).timetuple().tm_yday

    if type(year) in (list,tuple,np.ndarray):
        if np.array(year).dtype in ('int','int64','float','float64'):
            return np.array([ dt.date(int(Y), 12, 31).timetuple().tm_yday for Y in year ], dtype=int)
        elif 'datetime' in str(np.array(year).dtype):
            return np.array([ dt.date(Y.astype(object).timetuple().tm_year, 12, 31).timetuple().tm_yday for Y in year ], dtype=int)
        elif len(set(map(type,year))) == 1 and list(set(map(type,year)))[0] in (dt.date, dt.datetime):
            return np.array([ dt.date(Y.timetuple().tm_year, 12, 31).timetuple().tm_yday for Y in year ], dtype=int)
        elif len(set(map(type,year))) == 2 and list(set(map(type,year)))[0] in (dt.date, dt.datetime) and list(set(map(type,year)))[1] in (dt.date, dt.datetime):
            return np.array([ dt.date(Y.timetuple().tm_year, 12, 31).timetuple().tm_yday for Y in year ], dtype=int)
    if isinstance(year,pd.DatetimeIndex):
        return np.array([ dt.date(Y.year, 12, 31).timetuple().tm_yday for Y in year ], dtype=int)

    if isinstance(year,SimSeries):
        params = year._SimParameters
        params['name'] = 'DaysInYear'
        params['units'] = 'days'
        return SimSeries(data=np.array([ dt.date(Y.year, 12, 31).timetuple().tm_yday for Y in year ], dtype=int), index=year.index, **params)

    if isinstance(year,Series):
        return Series(data=np.array([ dt.date(Y.year, 12, 31).timetuple().tm_yday for Y in year ], dtype=int), index=year.index)

    raise ValueError("input 'year' is not a valid date or year integer")

def daysInMonth(month,year=None):
    """
    returns the number of days in a particular month of particular year

    Parameters
    ----------
    month : str, int, date, datetime or array-like of int, date, or datetime
        The month to calculate the number of days.
        Can a single month, represented as an integer or as date or datetime object
        Also, list or array of months is accepted.
    year : integer, optional
        If 'month' is provided as integer, year can be used to specify the year
        when to calculate the number of days in the month.
        This is only useful for February

    Returns
    -------
    int or array of ints, according to the input
    """
    daysinmonths = {1:31,
                    2:28,
                    3:31,
                    4:30,
                    5:31,
                    6:30,
                    7:31,
                    8:31,
                    9:30,
                    10:31,
                    11:30,
                    12:31}
    monthsnames = {'JAN':1,
                   'ENE':1,
                   'GEN':1,
                   'FEB':2,
                   'MAR':3,
                   'APR':4,
                   'ABR':4,
                   'MAY':5,
                   'JUN':6,
                   'GIU':6,
                   'JUL':7,
                   'JLY':7,
                   'LUG':7,
                   'AUG':8,
                   'AGO':8,
                   'SEP':9,
                   'SET':9,
                   'OCT':10,
                   'OTT':10,
                   'NOV':11,
                   'DEC':12,
                   'DIC':12,
                   }
    if type(month) is str:
        if month.upper() in monthsnames:
            month = monthsnames[month.upper()]
        elif month.isdigit():
            return daysInMonth(int(month),year)
        elif year is None:
            try:
                month = pd.to_datetime(month)
                return daysInMonth(month.month,month.year)
            except:
                raise ValueError("input 'month' not recognized.")
        else:
            raise ValueError("input 'month' not recognized.")

    if type(month) in (int,float):
        if year is None:
            return daysinmonths[int(month)]
        if type(year) is not int:
            raise ValueError("input 'year' is not a valid year integer")
        if dt.date(int(year), 12, 31).timetuple().tm_yday == 366 and month == 2:
            return 29
        else:
            return daysinmonths[int(month)]

    if type(month) in (dt.date, dt.datetime):
        return daysInMonth(month.timetuple().tm_mon, month.timetuple().tm_year)

    if type(month) is pd.Timestamp:
        return daysInMonth(month.month, month.year)

    if isinstance(month,pd.DatetimeIndex):
        return np.array([ daysInMonth(M.month, M.year) for M in month ], dtype=int)

    if type(month) in (list,tuple):
        month = np.array(month)

    if str(month.dtype).startswith('date'):
        return np.array([ daysInMonth(M.month, M.year) for M in pd.to_datetime(month) ], dtype=int)
    if str(month.dtype) in ('int','int64','float','float64'):
        if len(month.shape) == 1:
            return np.array([ daysInMonth(M) for M in month ], dtype=int)
        elif month.shape[1] == 2:
            return np.array([ daysInMonth(M[0],M[1]) for M in month ], dtype=int)

    # if type(month) is np.ndarray:
    #     if np.array(month).dtype in ('int','int64','float','float64'):
    #         return np.array([ daysInMonth(M,year) for M in month ], dtype=int)
    #     elif 'datetime' in str(np.array(year).dtype):
    #         return np.array([ M.astype(object).timetuple().tm_mon for M in month ], dtype=int)
    #     elif len(set(map(type,month))) == 1 and list(set(map(type,month)))[0] in (dt.date, dt.datetime):
    #         return np.array([ M.timetuple().tm_mon for M in month ], dtype=int)
    #     elif len(set(map(type,month))) == 2 and list(set(map(type,month)))[0] in (dt.date, dt.datetime) and list(set(map(type,month)))[1] in (dt.date, dt.datetime):
    #         return np.array([ M.timetuple().tm_mon for M in month ], dtype=int)

    if isinstance(month,SimSeries):
        params = month._SimParameters
        params['name'] = 'DaysInMonth'
        params['units'] = 'days'
        return SimSeries(data=np.array([ daysInMonth(M.month) for M in month ], dtype=int), index=month.index, **params)

    if isinstance(month,Series):
        return Series(data=np.array([ M.month for M in month ], dtype=int), index=month.index)

    raise ValueError("input 'month' is not a valid date or month integer")

def realYear(date):
    """
    returns a float corresponding for the year and the fraction of year represented by the date.

    Parameters
    ----------
    date : date, datetime, or array of date objects

    Returns
    -------
    float
    """
    if type(date) in (dt.date, dt.datetime):
        return date.timetuple().tm_year + date.timetuple().tm_yday / dt.date(date.timetuple().tm_year, 12, 31).timetuple().tm_yday
    if type(date) is pd.Timestamp:
        return date.year + dt.date(date.year,date.month,date.day).timetuple().tm_yday / dt.date(date.year, 12, 31).timetuple().tm_yday

    if type(date) is np.ndarray and 'datetime' in str(np.array(date).dtype):
            return np.array([ Y.year + dt.date(Y.year, Y.month, Y.day).timetuple().tm_yday / dt.date(Y.year, 12, 31).timetuple().tm_yday for Y in pd.to_datetime(date) ], dtype=float)
    if type(date) in (list,tuple):
        if len(set(map(type,date))) == 1 and list(set(map(type,date)))[0] in (dt.date, dt.datetime):
            return np.array([ Y.timetuple().tm_year + Y.timetuple().tm_yday / dt.date(Y.timetuple().tm_year, 12, 31).timetuple().tm_yday for Y in date ], dtype=float)
        elif len(set(map(type,date))) == 2 and list(set(map(type,date)))[0] in (dt.date, dt.datetime) and list(set(map(type,date)))[1] in (dt.date, dt.datetime):
            return np.array([ Y.timetuple().tm_year + Y.timetuple().tm_yday / dt.date(Y.timetuple().tm_year, 12, 31).timetuple().tm_yday for Y in date ], dtype=float)
    if isinstance(date,pd.DatetimeIndex):
        return np.array([ Y.year + dt.date(Y.year,Y.month,Y.day).timetuple().tm_yday / dt.date(Y.year, 12, 31).timetuple().tm_yday for Y in date ], dtype=float)

    if isinstance(date,SimSeries):
        params = date._SimParameters
        params['name'] = 'Year'
        params['units'] = 'year'
        return SimSeries(data=realYear(date.to_Pandas()), **params)

    if isinstance(date,Series):
        return Series(data=np.array([ Y.year + dt.date(Y.year, Y.month, Y.day).timetuple().tm_yday / dt.date(Y.year, 12, 31).timetuple().tm_yday for Y in date ], dtype=float), index=date.index)

def _MergeIndex(left, right, how='outer', *, drop_duplicates=True, keep='first'):
    """
    returns an left and right Frames or Series reindexed with a common index.

    Parameters
    ----------
    left : Series, SimSeries, DataFrame or SimDataFrame
        The left frame to merge
    right : Series, SimSeries, DataFrame or SimDataFrame
        The right frame to merge
    how : str, optional
        The merge method to be used.
        The default is 'outer'.
    drop_duplicates : boo, optional
        If True, drop lines with duplicated indexes to avoid reindexing error due to repeated index.
        If False, will drop the lines of duplicated indexes to avoid error and then put back line
    Raises
    ------
    ValueError
        If how parameter is not valid.

    Returns
    -------
    Series, SimSeries, DataFrame or SimDataFrame
        Reindexed to the merged index.
    Series, SimSeries, DataFrame or SimDataFrame
        Reindexed to the merged index.

    """

    def mergeAppend(frame, newIndex):
        if type(frame) is SimSeries:
            frame = frame.sdf
        elif type(frame) is Series:
            frame = SimDataFrame(frame)
        if frame.index.duplicated('first').sum() > 0:
            dupframe = frame[frame.index.duplicated('first')]
            temp = frame[~frame.index.duplicated('first')].reindex(index=newIndex)
            newframe = None
            for dup in range(len(dupframe.index)):
                if newframe is None:
                    # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead
                    # newframe = temp.iloc[0:list(temp.index).index(dupframe.index[dup])+1].append(dupframe.iloc[dup])
                    newframe = pd.concat([temp.iloc[0:list(temp.index).index(dupframe.index[dup])+1], dupframe.iloc[dup]], axis=0)
                else:
                    # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead
                    # newframe = newframe.append([temp.iloc[list(temp.index).index(dup-1):list(temp.index).index(dup)] , dupframe.iloc[dup]])
                    newframe = pd.concat([newframe, temp.iloc[list(temp.index).index(dup-1):list(temp.index).index(dup)] , dupframe.iloc[dup]], axis=0)
            # to avoid FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead
            # newframe = newframe.append(temp.iloc[list(temp.index).index(dupframe.index[dup])+1:])
            newframe = pd.concat([newframe, temp.iloc[list(temp.index).index(dupframe.index[dup])+1:]], axis= 0)
        else:
            newframe = frame.reindex(index=newIndex)
        return SimDataFrame(newframe, **frame._SimParameters)

    if how not in ('outer','inner','left','right','cross'):
        raise ValueError("how must be 'outer', 'iner', 'left', 'right' or 'cross'")

    # if both indexes are equal
    if len(left.index) == len(right.index) and (left.index == right.index).all():
        return left, right

    # if are different, extract a Series accoring to the type of input
    else:
        # from datafiletoolbox import SimSeries, SimDataFrame
        # from pandas import Series, DataFrame
        # checking left
        if type(left) is SimDataFrame:
            ileft = left.DF.iloc[:,0]
        elif type(left) is SimSeries:
            ileft = left.S
        elif type(left) is DataFrame:
            ileft = left.iloc[:,0]
        elif type(left) is Series:
            ileft = left

        # checking right
        if type(right) is SimDataFrame:
            iright = right.DF.iloc[:,0]
        elif type(right) is SimSeries:
            iright = right.S
        elif type(right) is DataFrame:
            iright = right.iloc[:,0]
        elif type(right) is Series:
            iright = right

        # merge the indexes
        newIndex= pd.merge(ileft,iright,how=how,left_index=True,right_index=True).index
        # return original dataframes reindexed to the merged index
        if bool(drop_duplicates):
            return left[~left.index.duplicated(keep)].reindex(index=newIndex), right[~right.index.duplicated(keep)].reindex(index=newIndex)
            # return left.drop_duplicates().reindex(index=newIndex), right.drop_duplicates().reindex(index=newIndex)
        else:
            return mergeAppend(left, newIndex), mergeAppend(right, newIndex)


def merge_units(left, right=None, suffixes=('_x', '_y')):
    """
    return a dictionary with the units of both SimDataFrames merged, corresponding to the merged DataFrame.

    Parameters
    ----------
    left : SimDataFrame
    right : SimDataFrame
    suffixes : tuple of str, optional
        tuple indicating the suffixes to be used for repeated column names. The default is ('_x', '_y').

    Returns
    -------
    dict of units
    """
    if type(left) in (list, tuple) and len(left) > 1 and right is None:
        merged = left[0]
        for i in range(1,len(left)):
            merged = merge_units(merged,left[i])
        return merged

    merged = {}
    if type(left) in [SimDataFrame, SimSeries] and type(right) in [SimDataFrame, SimSeries]:
        for col in left.columns:
            if col in right.columns:
                merged[col + suffixes[0]] = left.get_units(col)[col]
            else:
                merged[col] = left.get_units(col)[col]
        for col in right.columns:
            if col in left.columns:
                merged[col + suffixes[1]] = right.get_units(col)[col]
            else:
                merged[col] = right.get_units(col)[col]

    elif type(left) in [SimDataFrame, SimSeries] and type(right) not in [SimDataFrame, SimSeries]:

        if isinstance(right,DataFrame):
            columns = right.columns
        elif isinstance(right,Series) and type(right.name) is str and len(right.name.strip()) > 0:
            columns = [right.name]
        else:
            columns = []

        for col in left.columns:
            if col in columns:
                merged[col + suffixes[0]] = left.get_units(col)[col]
            else:
                merged[col] = left.get_units(col)[col]
        for col in columns:
            if col in left.columns:
                merged[col + suffixes[1]] = 'UNDEFINED'
            else:
                merged[col] = 'UNDEFINED'

    elif type(left) not in [SimDataFrame, SimSeries] and type(right) in [SimDataFrame, SimSeries]:

        if isinstance(left,DataFrame):
            columns = left.columns
        elif isinstance(left,Series) and type(left.name) is str and len(left.name.strip()) > 0:
            columns = [left.name]
        else:
            columns = []

        for col in right.columns:
            if col in columns:
                merged[col + suffixes[0]] = right.get_units(col)[col]
            else:
                merged[col] = right.get_units(col)[col]
        for col in columns:
            if col in right.columns:
                merged[col + suffixes[1]] = 'UNDEFINED'
            else:
                merged[col] = 'UNDEFINED'

    else:
        raise TypeError("'left' and 'right' paramenters most be SimDataFrame or SimSeries")

    return merged

def merge_SimParameters(left,right=None):
    """
    return a dictionary with the SimParameters of both SimDataFrames merged, corresponding to the merged DataFrame.

    Parameters
    ----------
    left : SimDataFrame
    right : SimDataFrame

    Returns
    -------
    dict of SimParameters
    """
    if type(left) in (list, tuple) and len(left) > 1 and right is None:
        merged = left[0]
        for i in range(1,len(left)):
            merged = merge_SimParameters(merged,left[i])
        return merged

    merged = {}
    if type(left) in [SimDataFrame, SimSeries] and type(right) in [SimDataFrame, SimSeries]:
        merged['speak'] = bool(int(left.speak) + int(right.speak))
        if left.index.name == right.index.name:
            merged['indexName'] = left.index.name
        else:
            merged['indexName'] = ( str(left.index.name) if left.index.name is not None else ''
                                   +
                                    str(right.index.name) if right.index.name is not None else '' )
        if left.indexUnits == right.indexUnits:
            merged['indexUnits'] = left.indexUnits
        else:
            # what to do if index units are different? should convert index if possible...
            merged['indexUnits'] = left.indexUnits

        renameSeparatorRight = False
        renameSeparatorLeft = False
        if left.nameSeparator == right.nameSeparator:
            merged['nameSeparator'] = left.nameSeparator
        else:
            if left.nameSeparator in ' '.join(list(left.columns)) and right.nameSeparator in ' '.join(list(right.columns)):
                if left.nameSeparator not in ' '.join(list(right.columns)):
                    merged['nameSeparator'] = left.nameSeparator
                    # must rename right to use left nameSeparator
                    renameSeparatorRight = True
                elif right.nameSeparator not in ' '.join(list(left.columns)):
                    merged['nameSeparator'] = right.nameSeparator
                    # must rename right to use left nameSeparator
                    renameSeparatorLeft = True
                else:
                    # should look for a new common name separator
                    merged['nameSeparator'] = left.nameSeparator + right.nameSeparator
                    renameSeparatorLeft = True
                    renameSeparatorRight = True

        renameIntersectionRight = False
        renameIntersectionLeft = False
        if left.intersectionCharacter == right.intersectionCharacter:
            merged['intersectionCharacter'] = left.intersectionCharacter
        else:
            if left.intersectionCharacter in ' '.join(list(left.columns)) and right.intersectionCharacter in ' '.join(list(right.columns)):
                if left.intersectionCharacter not in ' '.join(list(right.columns)):
                    merged['intersectionCharacter'] = left.intersectionCharacter
                    # must rename right to use left intersectionCharacter
                    renameIntersectionRight = True
                elif right.intersectionCharacter not in ' '.join(list(left.columns)):
                    merged['intersectionCharacter'] = right.intersectionCharacter
                    # must rename right to use left intersectionCharacter
                    renameIntersectionLeft = True
                else:
                    # should look for a new common name separator
                    merged['intersectionCharacter'] = left.intersectionCharacter + right.intersectionCharacter
                    renameIntersectionLeft = True
                    renameIntersectionRight = True

        merged['autoAppend'] = bool(int(left.autoAppend) + int(right.autoAppend))

    elif type(left) in [SimDataFrame, SimSeries] and type(right) not in [SimDataFrame, SimSeries]:
        merged = left._SimParameters.copy()

    elif type(left) not in [SimDataFrame, SimSeries] and type(right) in [SimDataFrame, SimSeries]:
        merged = right._SimParameters.copy()

    else:
        raise TypeError("'left' and 'right' paramenters most be SimDataFrame or SimSeries")

    return merged

def merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None):
    """
    Wrapper of Pandas merge, to merge also the units dictionary.
    Merge SimDataFrame, DataFrame or named SimSeries or Series objects with a database-style join.

    The join is done on columns or indexes. If joining columns on columns, the DataFrame indexes will be ignored. Otherwise if joining indexes on indexes or indexes on a column or columns, the index will be passed on. When performing a cross merge, no column specifications to merge on are allowed.

    Parameters
    ----------
    left : SimDataFrame or DataFrame or named SimSeries or Series
        Object to merge
    right : SimDataFrame or DataFrame or named SimSeries or Series
        Object to merge with.
    how : {‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, default ‘inner’
        Type of merge to be performed.
        · left: use only keys from left frame, similar to a SQL left outer join; preserve key order.
        · right: use only keys from right frame, similar to a SQL right outer join; preserve key order.
        · outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
        · inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.
        · cross: creates the cartesian product from both frames, preserves the order of the left keys.
    on : label or list
        Column or index level names to join on. These must be found in both DataFrames.
        If on is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.
    left_on : label or list, or array-like
        Column or index level names to join on in the left DataFrame. Can also be an array or list of arrays of the length of the left DataFrame. These arrays are treated as if they are columns.
    right_on : label or list, or array-like
        Column or index level names to join on in the right DataFrame. Can also be an array or list of arrays of the length of the right DataFrame. These arrays are treated as if they are columns.
    left_index : bool, default False
        Use the index from the left DataFrame as the join key(s). If it is a MultiIndex, the number of keys in the other DataFrame (either the index or a number of columns) must match the number of levels.
    right_index : bool, default False
        Use the index from the right DataFrame as the join key. Same caveats as left_index.
    sort : bool, default False
        Sort the join keys lexicographically in the result DataFrame. If False, the order of the join keys depends on the join type (how keyword).
    suffixes : list-like, default is (“_x”, “_y”)
        A length-2 sequence where each element is optionally a string indicating the suffix to add to overlapping column names in left and right respectively. Pass a value of None instead of a string to indicate that the column name from left or right should be left as-is, with no suffix. At least one of the values must not be None.
    copy : bool, default True
        If False, avoid copy if possible.
    indicator : bool or str, default False
        If True, adds a column to the output DataFrame called “_merge” with information on the source of each row. The column can be given a different name by providing a string argument. The column will have a Categorical type with the value of “left_only” for observations whose merge key only appears in the left DataFrame, “right_only” for observations whose merge key only appears in the right DataFrame, and “both” if the observation’s merge key is found in both DataFrames.
    validate : str, optional
        If specified, checks if merge is of specified type.
        · “one_to_one” or “1:1”: check if merge keys are unique in both left and right datasets.
        · “one_to_many” or “1:m”: check if merge keys are unique in left dataset.
        · “many_to_one” or “m:1”: check if merge keys are unique in right dataset.
        · “many_to_many” or “m:m”: allowed, but does not result in checks.

    Returns
    -------
    SimDataFrame
        A SimDataFrame of the two merged objects.
    """
    params = {}

    # checking right
    if type(right) is SimDataFrame:
        iright = right.DF
        params = right._SimParameters
    elif type(right) is SimSeries:
        iright = right.S
        params = right._SimParameters
    elif type(right) is DataFrame:
        iright = right
    elif type(right) is Series:
        iright = right

    # checking left
    if type(left) is SimDataFrame:
        ileft = left.DF
        if type(right) in [SimDataFrame,SimSeries]:
            params = merge_SimParameters(left, right)
        else:
            params = left._SimParameters
    elif type(left) is SimSeries:
        ileft = left.S
        params = left._SimParameters
    elif type(left) is DataFrame:
        ileft = left
    elif type(left) is Series:
        ileft = left

    mergeddata = pd.merge(ileft, iright, how=how, on=on, left_on=left_on, right_on=right_on, left_index=left_index, right_index=right_index, sort=sort, suffixes=suffixes, copy=copy, indicator=indicator, validate=validate)
    params['units'] = merge_units(left, right, suffixes=suffixes)
    return SimDataFrame(data=mergeddata,**params)

def znorm(df):
    return (df - df.mean()) / df.std()

def minmaxnorm(df):
    return (df - df.min()) / (df.max() - df.min())