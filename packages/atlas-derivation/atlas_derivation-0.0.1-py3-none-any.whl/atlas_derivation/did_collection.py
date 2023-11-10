from typing import Union, Optional, List, Dict

import numpy as np
import pandas as pd

from .did_tool import DIDTool

class DIDCollection:
    
    DEFAULT_DISPLAY = ['did', 'did_type', 'nevent']
    
    DEFAULT_TABLE_STYLE = 'psql'
    DEFAULT_TABLE_ALIGN = 'left'
    
    def __init__(self, dids:List[Union[Dict, str, "pandas.DataFrame"]], detailed:bool=True):
        self.load(dids)
    
    def load(self, dids:List[Union[Dict, str, "pandas.DataFrame"]], detailed:bool=True):
        if isinstance(dids, pd.DataFrame):
            self.df = dids.copy()
        else:
            self.df = DIDTool.to_dataframe(dids, detailed=detailed)
    
    def filter_by_attributes(scope:Optional[str]=None, run_number:Optional[str]=None,
                             stream_name:Optional[str]=None, prod_step:Optional[str]=None,
                             data_type:Optional[str]=None, version:Optional[str]=None,
                             inplace:bool=False):
        df = self.df
        attributes = {
            'scope'      : scope,
            'run_number' : run_number,
            'stream_name': stream_name,
            'prod_step'  : prod_step,
            'data_type'  : data_type,
            'version'    : version
        }
        for attribute, value in attributes.items():
            if isinstance(value, str):
                df = df[df[attribute] == value]
            elif isinstance(value, list):
                df = df[df[attribute].isin(value)]
        if len(df) == 0:
            df = self.df.loc[[]]
        df = df.reset_index(drop=True)
        if inplace:
            self.df = df
            return None
        else:
            return df
    
    def get_dids(self):
        return self.df['did'].values
        
    def filter_by_tags(self, single_rtag:bool=False,
                       single_ptag:bool=False,
                       latest_ptag:bool=False,
                       esrp_tags_only:bool=False,
                       inplace:bool=False):
        df = self.df.copy()
        if single_rtag:
            if 'rtag' not in df.columns:
                df = df.loc[[]]
            else:
                df = df[df['rtag'].apply(lambda x: not isinstance(x, list) and (x is not None))]
        if single_ptag:
            if 'ptag' not in df.columns:
                df = df.loc[[]]
            else:
                df = df[df['ptag'].apply(lambda x: not isinstance(x, list) and (x is not None))]
        if esrp_tags_only:
            esrp_tags_set = set(['etag', 'stag', 'rtag', 'ptag'])
            lambda_func = lambda x: set(x[x.keys().str.endswith('tag') & ~x.isna()].keys()) == esrp_tags_set
            df = df[df.apply(lambda_func, axis=1)]
        if latest_ptag:
            df_tmp = df.copy()
            for column in ['etag', 'stag', 'rtag', 'ptag']:
                if column not in df_tmp.columns:
                    df_tmp[column] = None
            # remove dids without ptag
            df_tmp = df_tmp[~df_tmp['ptag'].isna()]
            # account for cases with multiple e, s or r tags which are unhashable
            def get_merged_tag(x):
                if isinstance(x, list):
                    return '_'.join(x)
                return x
            df_tmp['merged_etag'] = df_tmp['etag'].apply(get_merged_tag)
            df_tmp['merged_stag'] = df_tmp['stag'].apply(get_merged_tag)
            df_tmp['merged_rtag'] = df_tmp['rtag'].apply(get_merged_tag)
            # make sure the ptag is treated as integer when finding the max value
            def get_primary_ptag(x):
                if isinstance(x, str):
                    return int(x)
                elif isinstance(x, list):
                    return np.array(x, dtype=int).max()
                elif x is None:
                    return 0
                else:
                    return x
            df_tmp['primary_ptag'] = df_tmp['ptag'].apply(get_primary_ptag)
            df_tmp = df_tmp.fillna(-999)
            dids = []
            for name, df_grouped in df_tmp.groupby(['run_number', 'data_type',
                                                    'merged_etag', 'merged_stag',
                                                    'merged_rtag']):
                idxmax = df_grouped['primary_ptag'].idxmax()
                did = df_grouped.loc[idxmax]['did']
                dids.append(did)
            dids = np.array(dids)
            df = df.set_index('did').loc[dids].reset_index()
        if len(df) == 0:
            df = self.df.loc[[]]
        df = df.reset_index(drop=True)
        if inplace:
            self.df = df
            return None
        else:
            return df
    
    def fill_attributes(self, file_data:bool=False, did_type:bool=False,
                        inplace:bool=False):
        df = self.df.copy()
        if len(df) > 0:  
            if file_data and (('nevent' not in self.df.columns) or 'bytes' not in self.df.columns):
                tool = DIDTool()
                dids = df['did'].values
                did_nevent = []
                did_nbytes = []
                for did in dids:
                    file_data = tool.list_files(did)
                    nevent = np.sum([data['events'] for data in file_data])
                    nbytes = np.sum([data['bytes'] for data in file_data])
                    did_nevent.append(nevent)
                    did_nbytes.append(nbytes)
                df.loc[:, ['nevent']] = np.array(did_nevent)
                df.loc[:, ['bytes']] = np.array(did_nbytes)
            if did_type and ('did_type' not in self.df.columns):
                tool = DIDTool()
                dids = df['did'].values
                did_type = []
                for did in dids:
                    did_type.append(tool.get_did_content(did)['type'])
                did_type = np.array(did_type)
                df.loc[:, ['did_type']] = did_type
            if 'bytes' in df.columns:
                def sizeof_fmt(num, suffix="B"):
                    for unit in ("", "K", "M", "G", "T", "P", "E", "Z"):
                        if abs(num) < 1024.0:
                            return f"{num:3.1f} {unit}{suffix}"
                        num /= 1024.0
                    return f"{num:.1f} Y{suffix}"
                df['size'] = df['bytes'].apply(sizeof_fmt)
        if inplace:
            self.df = df
            return None
        else:
            return df
        
    def filter_daods(self, single_rtag:bool=True,
                     single_ptag:bool=True,
                     latest_ptag:bool=False,
                     esrp_tags_only:bool=True,
                     did_type:str='container',
                     not_empty:bool=False,
                     inplace:bool=False):
        return self.filter_derived_samples(single_rtag=single_rtag,
                                           single_ptag=single_ptag,
                                           latest_ptag=latest_ptag,
                                           esrp_tags_only=esrp_tags_only,
                                           did_type=did_type,
                                           not_empty=not_empty,
                                           inplace=inplace,
                                           data_type='DAOD')
    
    def filter_ntup_pileups(self, single_rtag:bool=True,
                            single_ptag:bool=True,
                            latest_ptag:bool=False,
                            esrp_tags_only:bool=True,
                            did_type:str='container',
                            not_empty:bool=False,
                            inplace:bool=False):
        return self.filter_derived_samples(single_rtag=single_rtag,
                                           single_ptag=single_ptag,
                                           latest_ptag=latest_ptag,
                                           esrp_tags_only=esrp_tags_only,
                                           did_type=did_type,
                                           not_empty=not_empty,
                                           inplace=inplace,
                                           data_type='NTUP_PILEUP')
            
    def filter_derived_samples(self, single_rtag:bool=True,
                               single_ptag:bool=True,
                               latest_ptag:bool=False,
                               esrp_tags_only:bool=True,
                               did_type:str='container',
                               data_type:str='',
                               not_empty:bool=False,
                               inplace:bool=False):
        df = self.df
        if data_type:
            df = df[df['data_type'].str.startswith(data_type)]
        collection = DIDCollection(df)
        df = collection.fill_attributes(file_data=not_empty,
                                        did_type=did_type.lower() != 'all')
        # filter empty did
        if not_empty:
            df = df[df['nevent'] > 0]
        # filter by did type
        if did_type.lower() != 'all':
            df = df[df['did_type'].str.lower() == did_type.lower()]
        collection.df = df
        df = collection.filter_by_tags(single_rtag=single_rtag,
                                       single_ptag=single_ptag,
                                       esrp_tags_only=esrp_tags_only,
                                       latest_ptag=latest_ptag)
        df = df.reset_index(drop=True)

        if inplace:
            self.df = df
            return None
        else:
            return df
        
    def print_table(self, attributes:Optional[List[str]]=None,
                    tableformat:Optional[str]=None,
                    stralign:Optional[str]=None):
        if attributes is None:
            attributes = list(self.DEFAULT_DISPLAY)
        if tableformat is None:
            tableformat = self.DEFAULT_TABLE_STYLE
        if stralign is None:
            stralign = self.DEFAULT_TABLE_ALIGN
        columns = [attribute for attribute in attributes if attribute in self.df.columns]
        df_display = self.df[columns]
        from tabulate import tabulate
        table = tabulate(df_display, showindex=False,
                         headers=df_display.columns, 
                         tablefmt=tableformat,
                         stralign=stralign)
        print(table)