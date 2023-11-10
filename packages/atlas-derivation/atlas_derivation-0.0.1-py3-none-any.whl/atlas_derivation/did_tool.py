from typing import Union, List, Optional, Dict
import os
import re
import json
import glob
from time import sleep
from fnmatch import fnmatch

import numpy as np
import pandas as pd

try:
    from rucio.client import didclient, scopeclient
    from rucio.common.utils import extract_scope
    from rucio.common.exception import RucioException
except ImportError:
    print("""rucio is not setup, run
lsetup rucio
""")
    raise
except ModuleNotFoundError:
    print("""rucio is not setup, run
lsetup rucio
""")
    raise
    
class DIDTool:
    
    EXAMPLES = {
        'DAOD': [
            'mc16_13TeV.700370.Sh_sig_1xSM_JO.merge.EVNT.e8324_e7400',
            'data16_13TeV.00303059.physics_Main.deriv.DAOD_HIGG1D1.r9264_p3083_p4205_tid21856266_00'
        ],
        'AOD': [
            
        ]
    }
    
    did_regex = re.compile(r"(?P<scope>[\w_]+).(?P<run_number>[\w]+).(?P<stream_name>[\w]+)."
                           r"(?P<prod_step>[\w]+).(?P<data_type>[\w]+).(?P<version>[\w]+)")
    def __init__(self):
        self.client = didclient.DIDClient()
    
    @staticmethod
    def is_valid_did(name:str):
        match = DIDTool.did_regex.match(name)
        if not match:
            return False
        return True
    
    @staticmethod
    def get_did_without_tid(name:str):
        return name.split("_tid")[0]
    
    @staticmethod
    def get_did_attributes(name:str, detailed:bool=True):
        match = DIDTool.did_regex.match(name)
        if not match:
            raise RuntimeError("not a valid did name")
        attributes = match.groupdict()
        if not detailed:
            return attributes
        tokens = attributes['version'].split('tid')
        if len(tokens) == 2:
            attributes['tid'] = tokens[-1]
        elif len(tokens) > 2:
            raise RuntimeError("unknown did format")
        tokens = tokens[0].strip("_")
        tags = {}
        for tag in tokens.split('_'):
            tag_type = tag[0]
            tag_label = '{}tag'.format(tag_type)
            if tag_label not in tags:
                tags[tag_label] = []
            tags[tag_label].append(tag[1:])
        for tag_label, value in tags.items():
            if len(value) == 1:
                tags[tag_label] = value[0]
        for key, value in tags.items():
            if isinstance(value, list):
                tags[key] = sorted(value, key = lambda item: -int(item))
        attributes.update(tags)
        return attributes
    
    def get_account(self):
        return self.client.account
    
    def get_scope(self, did:str):
        try:
            scope, name = extract_scope(did)
            return scope, name
        except TypeError:
            scopes = self.list_scopes()
            scope, name = extract_scope(did, scopes)
            return scope, name
        return None, did

    def list_scopes(self):
        client = scopeclient.ScopeClient()
        return client.list_scopes()
    
    def list_scopes_for_account(self, account:Optional[str]=None):
        if account is None:
            account = self.client.account
        client = scopeclient.ScopeClient()
        return client.list_scopes_for_account(account)
    
    def get_did_content(self, name:str):
        scope, did = self.get_scope(name)
        content = list(self.client.list_content(scope, name))
        if content:
            return content[0]
        return content
    
    def get_did_content_history(self, name:str):
        scope, did = self.get_scope(name)
        content = list(self.client.list_content_history(scope, name))
        if content:
            return content[0]
        return content
    
    def get_did_metadata(self, name:str, detailed:bool=False):
        scope, did = self.get_scope(name)
        if detailed:
            return self.client.get_metadata(scope, name)
        return self.client.get_did(scope, name)
    
    def list_files(self, did:str, long:Optional[bool]=None):
        scope, did = self.get_scope(did)
        return list(self.client.list_files(scope, did, long=long))
    
    def list_dids(self, name:str, did_type:Optional[str]='all', long:bool=False):
        scope, did = self.get_scope(name)
        did_list = list(self.client.list_dids(scope, {"name": did}, did_type=did_type, long=long))
        return did_list
    
    def list_dids_extended(self, scope:str, run_number:Optional[str]=None,
                           stream_name:Optional[str]=None, prod_step:Optional[str]=None,
                           data_type:Optional[str]=None, version:Optional[str]=None,
                           did_type:Optional[str]='all', long:bool=False):
        did_expr = self._format_did_expr(scope=scope, run_number=run_number,
                                         stream_name=stream_name, prod_step=prod_step,
                                         data_type=data_type, version=version)
        return self.list_dids(name=did_expr, did_type=did_type)    
    
    @staticmethod
    def to_dataframe(dids:List[Union[Dict,str]], detailed:bool=False):
        data = []
        for did in dids:
            attributes = {}
            if isinstance(did, dict):
                attributes['did'] = did['name']
                attributes['did_type'] = did['did_type'].replace("DIDType.", "")
                attributes.update(DIDTool.get_did_attributes(did['name'], detailed=detailed))
                attributes['scope'] = did['scope']
            else:
                attributes['did'] = did
                attributes.update(DIDTool.get_did_attributes(did, detailed=detailed))
            data.append(attributes)
        import pandas as pd
        return pd.DataFrame(data)
    
    def get_dids_ptag_variants(self, names:List[str], sort:bool=True):
        dids = {}
        n = len(names)
        for i, name in enumerate(names):
            sleep(0.5)
            print(f"Sample ({i}/{n}): {name}")
            dids[name] = self.get_did_ptag_variants(name, sort=sort)
        return dids
    
    def get_did_all_versions(self, name:str):
        attributes = self.get_did_attributes(name, detailed=False)
        attributes['version'] = "*"
        return self.list_dids_extended(**attributes)
    
    def get_did_ptag_variants(self, name:str, sort:bool=True):
        attributes = self.get_did_attributes(name, detailed=True)
        if 'ptag' not in attributes:
            raise RuntimeError(f"no ptag found for the did {name}")
        ptags = attributes['ptag']
        tid   = attributes.get('tid', None)
        attributes = self.get_did_attributes(name, detailed=False)
        for ptag in ptags:
            attributes['version'] = attributes['version'].replace(ptag, "*")
        if tid is not None:
            attributes['version'] = attributes['version'].replace(tid, "*")
        dids = self.list_dids_extended(**attributes)
        if sort:
            dids = sorted(dids, key=lambda did: self.get_did_attributes(did)['ptag'])[::-1]
        return dids
    
    def get_did_container_sum_events(self, did:str):
        file_data = self.list_files(did)
        return sum([data['events'] for data in file_data])
    
    def list_derived_samples(self, pattern:str,
                             single_rtag:bool=True,
                             single_ptag:bool=True,
                             latest_ptag:bool=False,
                             esrp_tags_only:bool=True,
                             did_type:str='container',
                             not_empty:bool=False,
                             data_type:str='',
                             fmt:str='dataframe'):
        did_list = self.list_dids(pattern, did_type=did_type, long=True)
        from .did_collection import DIDCollection
        collection = DIDCollection(did_list)
        collection.filter_derived_samples(single_rtag=single_rtag,
                                          single_ptag=single_ptag,
                                          latest_ptag=latest_ptag,
                                          esrp_tags_only=esrp_tags_only,
                                          did_type=did_type,
                                          not_empty=not_empty,
                                          data_type=data_type,
                                          inplace=True)
        if fmt == "dataframe":
            return collection.df
        elif fmt == "dict":
            return collection.df.to_dict('records')
        elif fmt == "list":
            return collection.get_dids()
    
    @staticmethod
    def _format_did_expr(scope:Optional[str]=None, run_number:Optional[str]=None,
                         stream_name:Optional[str]=None, prod_step:Optional[str]=None,
                         data_type:Optional[str]=None, version:Optional[str]=None):
        maps = {
            'scope'      : "*" if scope is None else scope,
            'run_number' : "*" if run_number is None else run_number,
            'stream_name': "*" if stream_name is None else stream_name,
            'prod_step'  : "*" if prod_step is None else prod_step,
            'data_type'  : "*" if data_type is None else data_type,
            'version'    : "*" if version is None else version,
        }
        
        did_expr = "{scope}.{run_number}.{stream_name}.{prod_step}.{data_type}.{version}".format(**maps)
        
        return did_expr
     
    @staticmethod
    def get_mc_sample_fields(name):
        tokens = name.split('.')
        if len(tokens) != 6:
            raise ValueError("invalid DID name {}".format(name))
        fields = {
            'scope': tokens[0],
            'id': tokens[1],
            'process': tokens[2],
            'step': tokens[3],
            'object': tokens[4],
        }
        tags = {}
        for tag in tokens[-1].split('_'):
            tag_type = tag[0]
            if tag_type not in ['e', 's', 'r', 'p', 'a']:
                raise ValueError('invalid tag "{}"'.format(tag_type))
            tag_label = '{}-tag'.format(tag_type)
            if tag_label not in tags:
                tags[tag_label] = []
            tags[tag_label].append(tag[1:])
        fields['tags'] = tags
        return fields
    
    def check_dids(self, input_list:Union[List, str], did_type="all"):
        if isinstance(input_list, str):
            input_list = [ l.strip().split(":")[-1] for l in open(input_list, 'r').readlines() if l.strip()]
        samples = {'exist': [], 'missing': []}
        for name in input_list:
            scope = name.split('.')[0]
            if list(self.client.list_dids(scope, filters={"name": name}, type=did_type)):
                samples['exist'].append(name)
            else:
                samples['missing'].append(name)
        return samples

    def get_mc_samples(self, scope="mc16_13TeV", mc_id=None, process=None, step=None, objects=None, 
                       etag=None, stag=None, rtag=None, ptag=None, atag=None, did_type="container"):
        if (mc_id is None) and (process is None):
            raise ValueError("require at least MC ID or process description")
        def get_expression(*fields):
            expr = ["*" if field is None else field for field in fields] + ['*']
            return ".".join(expr)
        obj = objects if isinstance(objects, str) else None
        expression = get_expression(scope, mc_id, process, step, obj)
        mc_samples = list(self.client.list_dids(scope, filters={"name": expression}, type=did_type))
        def filter_tag(source, tag_type, tag_id=None):
            if tag_id is None:
                return source
            else:
                return [s for s in source if '{}{}'.format(tag_type, tag_id) in s]
        mc_samples = filter_tag(mc_samples, 'e', etag)
        mc_samples = filter_tag(mc_samples, 's', stag)
        mc_samples = filter_tag(mc_samples, 'r', rtag)
        mc_samples = filter_tag(mc_samples, 'p', ptag)
        mc_samples = filter_tag(mc_samples, 'a', atag)
        if isinstance(objects, list):
            mc_samples = [s for s in mc_samples if self.get_mc_sample_fields(s)['object'] in objects]
        mc_samples = sorted(mc_samples)
        return mc_samples

    def check_DAOD_from_AOD(self, input_list:Union[List, str]):
        AOD_samples = self.check_mc_samples(input_list)['exist']
        AOD_samples = [s for s in AOD_samples if self.get_mc_sample_fields(s)['object'] == 'AOD']
        DAOD_samples = {}
        for AOD in AOD_samples:
            expression = AOD.replace(".recon.", ".deriv.").replace('.merge.', '.deriv.').replace(".AOD.", ".DAOD*.")
            expression += '_*'
            scope = AOD.split('.')[0]
            samples = list(self.client.list_dids(scope, filters={"name": expression}, type="container"))
            DAOD_samples[AOD] = samples
        return DAOD_samples