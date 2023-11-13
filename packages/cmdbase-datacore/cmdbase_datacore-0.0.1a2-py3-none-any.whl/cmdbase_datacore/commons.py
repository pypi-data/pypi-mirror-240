from __future__ import annotations
import logging
from time import sleep
from typing import Iterable
from zut import JSONApiClient, _UNSET
from cmdbase_utils import BaseContext, BaseEntity

logger = logging.getLogger(__name__)


class Context(JSONApiClient, BaseContext):
    prog = 'cmdbase-datacore'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._retry_succeeded = False
        self._cached_objs: dict[str,dict[str]] = {}
        self._cached_perfs: dict[str,dict[str]] = {}


    def __enter__(self):
        admin = self._get_option('admin_host', fallback=None)
        self.controller = self._get_option('controller_host')
        if admin:
            self.host = admin
        else:
            self.host = self.controller
        
        self.nonversionned_base_url = f'http://{self.host}/RestService/rest.svc'
        self.base_url = f'{self.nonversionned_base_url}/1.0'

        return self


    def get_request_headers(self, url: str):
        if not hasattr(self, '_headers'):
            user = self._get_option('controller_user')
            password = self._getsecret_option('controller_password')

            logger.info(f'connect to datacore controller {self.host} with user {user}')

            self._headers = super().get_request_headers(url)
            self._headers['ServerHost'] = self.controller
            self._headers['Authorization'] = f'Basic {user} {password}'
        
        return self._headers


    def get_with_retries(self, endpoint: str, *, params: dict = None, api_version: str = None, retries = 5):
        """
        Necessary because datacore API returns empty data the first time it is run.
        """
        if api_version:
            url = self.prepare_url(endpoint, params=params, base_url=f"{self.nonversionned_base_url}/{api_version}")
        else:
            url = self.prepare_url(endpoint, params=params)

        def cache(response):
            if not params and not api_version and isinstance(response, list) and len(response) >= 1 and isinstance(response[0], dict) and 'Id' in response[0]:
                self._cached_objs[endpoint] = {}
                for obj in response:
                    self._cached_objs[endpoint][obj["Id"].lower()] = obj
                
            return response

        response = self.get(url, params=params)
        if response or self._retry_succeeded:
            return cache(response)
         
        while retries > 0:
            logger.info(f'waiting for data ({retries} retries remaining)')
            sleep(1)

            response = self.get(url, params=params)
            if response:
                self._retry_succeeded = True
                return cache(response)
            
            retries -= 1

        raise ValueError('max retries reached')


    def get_cached_obj(self, endpoint: str, id: str, default = _UNSET, *, prop: str = None):
        if not id:        
            if default is _UNSET:
                raise KeyError(f"requested empty id for endpoint {endpoint}")
            return default

        if not endpoint in self._cached_objs:
            self.get_with_retries(endpoint)
            if not endpoint in self._cached_objs:
                if default is _UNSET:
                    raise KeyError(f"endpoint {endpoint}")
                return default

        lower_id = id.lower()
        if lower_id in self._cached_objs[endpoint]:
            obj = self._cached_objs[endpoint][lower_id]
            if prop is not None:
                return obj[prop]
            return obj
        else:
            if default is _UNSET:
                raise KeyError(f"id {id} in endpoint {endpoint}")
            return default


    def get_cached_perf(self, endpoint: str, id: str, default = _UNSET, *, prop: str = None):
        if not id:        
            if default is _UNSET:
                raise KeyError(f"requested empty id for endpoint {endpoint}")
            return default

        if not endpoint in self._cached_perfs or not self._cached_perfs[endpoint]:
            self._cached_perfs[endpoint] = self._get_perfs(endpoint)

        lower_id = id.lower()
        if lower_id in self._cached_perfs[endpoint]:
            obj = self._cached_perfs[endpoint][lower_id]
            if prop is not None:
                return obj[prop]
            return obj
        else:
            if default is _UNSET:
                raise KeyError(f"id {id} in endpoint {endpoint}")
            return default
        

    def init_perfs(self, *perf_endpoints: str):
        """
        Initialize performance data counters.
        
        See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/Getting_Performance_Statistcs.htm
        """
        if not perf_endpoints:
            raise ValueError(f"at least one enpoint must be provided")
        
        for endpoint in perf_endpoints:
            self.get(f'performancebytype/{endpoint}')
        

    def _get_perfs(self, perf_endpoint: str):
        """
        Retrieve performance data.
        
        See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/Getting_Performance_Statistcs.htm
        """
        results = self.get(f'performancebytype/{perf_endpoint}')

        if not results:
            logger.info(f"wait for 2.5 seconds to retrieve {perf_endpoint}")
            sleep(2.5)
            results = self.get(f'performancebytype/{perf_endpoint}')

            if not results:
                raise ValueError(f"could not retrieve {perf_endpoint}")
        
        perfs = {}
        for result in results:
            perfs[result['ObjectId']] = result['PerformanceData']
        return perfs


class Entity(BaseEntity[Context, dict]):
    @property
    def name(self):
        return self.obj['Caption']


    @classmethod
    def get_endpoint(cls) -> str:
        try:
            return cls.endpoint
        except AttributeError:
            pass

        cls.endpoint = cls.get_itemname() + 's'
        return cls.endpoint


    @classmethod
    def extract_objs(cls, context: Context) -> Iterable[dict]:
        return context.get_with_retries(cls.get_endpoint())
