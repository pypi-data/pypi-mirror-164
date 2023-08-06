# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.exceptions import TeaException, UnretryableException
from Tea.request import TeaRequest
from Tea.core import TeaCore
from antchain_alipay_util.antchain_utils import AntchainUtils
from typing import Dict

from antchain_sdk_ak_7365e031a87c467bbe817bec28a2a1dc import models as ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient


class Client:
    _endpoint: str = None
    _region_id: str = None
    _access_key_id: str = None
    _access_key_secret: str = None
    _protocol: str = None
    _user_agent: str = None
    _read_timeout: int = None
    _connect_timeout: int = None
    _http_proxy: str = None
    _https_proxy: str = None
    _socks_5proxy: str = None
    _socks_5net_work: str = None
    _no_proxy: str = None
    _max_idle_conns: int = None
    _security_token: str = None
    _max_idle_time_millis: int = None
    _keep_alive_duration_millis: int = None
    _max_requests: int = None
    _max_requests_per_host: int = None

    def __init__(
        self, 
        config: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.Config,
    ):
        """
        Init client with Config
        @param config: config contains the necessary information to create a client
        """
        if UtilClient.is_unset(config):
            raise TeaException({
                'code': 'ParameterMissing',
                'message': "'config' can not be unset"
            })
        self._access_key_id = config.access_key_id
        self._access_key_secret = config.access_key_secret
        self._security_token = config.security_token
        self._endpoint = config.endpoint
        self._protocol = config.protocol
        self._user_agent = config.user_agent
        self._read_timeout = UtilClient.default_number(config.read_timeout, 20000)
        self._connect_timeout = UtilClient.default_number(config.connect_timeout, 20000)
        self._http_proxy = config.http_proxy
        self._https_proxy = config.https_proxy
        self._no_proxy = config.no_proxy
        self._socks_5proxy = config.socks_5proxy
        self._socks_5net_work = config.socks_5net_work
        self._max_idle_conns = UtilClient.default_number(config.max_idle_conns, 60000)
        self._max_idle_time_millis = UtilClient.default_number(config.max_idle_time_millis, 5)
        self._keep_alive_duration_millis = UtilClient.default_number(config.keep_alive_duration_millis, 5000)
        self._max_requests = UtilClient.default_number(config.max_requests, 100)
        self._max_requests_per_host = UtilClient.default_number(config.max_requests_per_host, 100)

    def do_request(
        self,
        version: str,
        action: str,
        protocol: str,
        method: str,
        pathname: str,
        request: dict,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        """
        Encapsulate the request and invoke the network
        @param action: api name
        @param protocol: http or https
        @param method: e.g. GET
        @param pathname: pathname of every api
        @param request: which contains request params
        @param runtime: which controls some details of call api, such as retry times
        @return: the response
        """
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': UtilClient.default_number(runtime.read_timeout, self._read_timeout),
            'connectTimeout': UtilClient.default_number(runtime.connect_timeout, self._connect_timeout),
            'httpProxy': UtilClient.default_string(runtime.http_proxy, self._http_proxy),
            'httpsProxy': UtilClient.default_string(runtime.https_proxy, self._https_proxy),
            'noProxy': UtilClient.default_string(runtime.no_proxy, self._no_proxy),
            'maxIdleConns': UtilClient.default_number(runtime.max_idle_conns, self._max_idle_conns),
            'maxIdleTimeMillis': self._max_idle_time_millis,
            'keepAliveDurationMillis': self._keep_alive_duration_millis,
            'maxRequests': self._max_requests,
            'maxRequestsPerHost': self._max_requests_per_host,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl,
            # 阿里云数据导出任务checkpoint类
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.protocol = UtilClient.default_string(self._protocol, protocol)
                _request.method = method
                _request.pathname = pathname
                _request.query = {
                    'method': action,
                    'version': version,
                    'sign_type': 'HmacSHA1',
                    'req_time': AntchainUtils.get_timestamp(),
                    'req_msg_id': AntchainUtils.get_nonce(),
                    'access_key': self._access_key_id,
                    'base_sdk_version': 'TeaSDK-2.0',
                    'sdk_version': '1.0.0',
                    '_prod_code': 'ak_7365e031a87c467bbe817bec28a2a1dc',
                    '_prod_channel': 'saas'
                }
                if not UtilClient.empty(self._security_token):
                    _request.query['security_token'] = self._security_token
                _request.headers = TeaCore.merge({
                    'host': UtilClient.default_string(self._endpoint, 'openapi.antchain.antgroup.com'),
                    'user-agent': UtilClient.get_user_agent(self._user_agent)
                }, headers)
                tmp = UtilClient.anyify_map_value(RPCUtilClient.query(request))
                _request.body = UtilClient.to_form_string(tmp)
                _request.headers['content-type'] = 'application/x-www-form-urlencoded'
                signed_param = TeaCore.merge(_request.query,
                    RPCUtilClient.query(request))
                _request.query['sign'] = AntchainUtils.get_signature(signed_param, self._access_key_secret)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                raw = UtilClient.read_as_string(_response.body)
                obj = UtilClient.parse_json(raw)
                res = UtilClient.assert_as_map(obj)
                resp = UtilClient.assert_as_map(res.get('response'))
                if AntchainUtils.has_error(raw, self._access_key_secret):
                    raise TeaException({
                        'message': resp.get('result_msg'),
                        'data': resp,
                        'code': resp.get('result_code')
                    })
                return resp
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def do_request_async(
        self,
        version: str,
        action: str,
        protocol: str,
        method: str,
        pathname: str,
        request: dict,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        """
        Encapsulate the request and invoke the network
        @param action: api name
        @param protocol: http or https
        @param method: e.g. GET
        @param pathname: pathname of every api
        @param request: which contains request params
        @param runtime: which controls some details of call api, such as retry times
        @return: the response
        """
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': UtilClient.default_number(runtime.read_timeout, self._read_timeout),
            'connectTimeout': UtilClient.default_number(runtime.connect_timeout, self._connect_timeout),
            'httpProxy': UtilClient.default_string(runtime.http_proxy, self._http_proxy),
            'httpsProxy': UtilClient.default_string(runtime.https_proxy, self._https_proxy),
            'noProxy': UtilClient.default_string(runtime.no_proxy, self._no_proxy),
            'maxIdleConns': UtilClient.default_number(runtime.max_idle_conns, self._max_idle_conns),
            'maxIdleTimeMillis': self._max_idle_time_millis,
            'keepAliveDurationMillis': self._keep_alive_duration_millis,
            'maxRequests': self._max_requests,
            'maxRequestsPerHost': self._max_requests_per_host,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl,
            # 阿里云数据导出任务checkpoint类
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.protocol = UtilClient.default_string(self._protocol, protocol)
                _request.method = method
                _request.pathname = pathname
                _request.query = {
                    'method': action,
                    'version': version,
                    'sign_type': 'HmacSHA1',
                    'req_time': AntchainUtils.get_timestamp(),
                    'req_msg_id': AntchainUtils.get_nonce(),
                    'access_key': self._access_key_id,
                    'base_sdk_version': 'TeaSDK-2.0',
                    'sdk_version': '1.0.0',
                    '_prod_code': 'ak_7365e031a87c467bbe817bec28a2a1dc',
                    '_prod_channel': 'saas'
                }
                if not UtilClient.empty(self._security_token):
                    _request.query['security_token'] = self._security_token
                _request.headers = TeaCore.merge({
                    'host': UtilClient.default_string(self._endpoint, 'openapi.antchain.antgroup.com'),
                    'user-agent': UtilClient.get_user_agent(self._user_agent)
                }, headers)
                tmp = UtilClient.anyify_map_value(RPCUtilClient.query(request))
                _request.body = UtilClient.to_form_string(tmp)
                _request.headers['content-type'] = 'application/x-www-form-urlencoded'
                signed_param = TeaCore.merge(_request.query,
                    RPCUtilClient.query(request))
                _request.query['sign'] = AntchainUtils.get_signature(signed_param, self._access_key_secret)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                raw = await UtilClient.read_as_string_async(_response.body)
                obj = UtilClient.parse_json(raw)
                res = UtilClient.assert_as_map(obj)
                resp = UtilClient.assert_as_map(res.get('response'))
                if AntchainUtils.has_error(raw, self._access_key_secret):
                    raise TeaException({
                        'message': resp.get('result_msg'),
                        'data': resp,
                        'code': resp.get('result_code')
                    })
                return resp
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def update_baas_chain_dataexport_status(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusResponse:
        """
        Description: 修改导出任务状态（启动、暂停、删除）
        Summary: 修改导出任务状态（启动、暂停、删除）
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_baas_chain_dataexport_status_ex(request, headers, runtime)

    async def update_baas_chain_dataexport_status_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusResponse:
        """
        Description: 修改导出任务状态（启动、暂停、删除）
        Summary: 修改导出任务状态（启动、暂停、删除）
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_baas_chain_dataexport_status_ex_async(request, headers, runtime)

    def update_baas_chain_dataexport_status_ex(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusResponse:
        """
        Description: 修改导出任务状态（启动、暂停、删除）
        Summary: 修改导出任务状态（启动、暂停、删除）
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusResponse(),
            self.do_request('1.0', 'baas.chain.dataexport.status.update', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    async def update_baas_chain_dataexport_status_ex_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusResponse:
        """
        Description: 修改导出任务状态（启动、暂停、删除）
        Summary: 修改导出任务状态（启动、暂停、删除）
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportStatusResponse(),
            await self.do_request_async('1.0', 'baas.chain.dataexport.status.update', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    def create_baas_chain_dataexport_task(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskResponse:
        """
        Description: 阿里云数据导出需求创建数据导出任务
        Summary: 创建数据导出任务
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_baas_chain_dataexport_task_ex(request, headers, runtime)

    async def create_baas_chain_dataexport_task_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskResponse:
        """
        Description: 阿里云数据导出需求创建数据导出任务
        Summary: 创建数据导出任务
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_baas_chain_dataexport_task_ex_async(request, headers, runtime)

    def create_baas_chain_dataexport_task_ex(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskResponse:
        """
        Description: 阿里云数据导出需求创建数据导出任务
        Summary: 创建数据导出任务
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskResponse(),
            self.do_request('1.0', 'baas.chain.dataexport.task.create', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    async def create_baas_chain_dataexport_task_ex_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskResponse:
        """
        Description: 阿里云数据导出需求创建数据导出任务
        Summary: 创建数据导出任务
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.CreateBaasChainDataexportTaskResponse(),
            await self.do_request_async('1.0', 'baas.chain.dataexport.task.create', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    def update_baas_chain_dataexport_task(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskResponse:
        """
        Description: 修改导出任务（名称、描述、告警地址）
        Summary: 修改导出任务（名称、描述、告警地址）
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_baas_chain_dataexport_task_ex(request, headers, runtime)

    async def update_baas_chain_dataexport_task_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskResponse:
        """
        Description: 修改导出任务（名称、描述、告警地址）
        Summary: 修改导出任务（名称、描述、告警地址）
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_baas_chain_dataexport_task_ex_async(request, headers, runtime)

    def update_baas_chain_dataexport_task_ex(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskResponse:
        """
        Description: 修改导出任务（名称、描述、告警地址）
        Summary: 修改导出任务（名称、描述、告警地址）
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskResponse(),
            self.do_request('1.0', 'baas.chain.dataexport.task.update', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    async def update_baas_chain_dataexport_task_ex_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskResponse:
        """
        Description: 修改导出任务（名称、描述、告警地址）
        Summary: 修改导出任务（名称、描述、告警地址）
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.UpdateBaasChainDataexportTaskResponse(),
            await self.do_request_async('1.0', 'baas.chain.dataexport.task.update', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    def get_baas_plus_dataservice_blockchainheight(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightResponse:
        """
        Description: 获取区块链当前块高
        Summary: 区块链数据服务-获取区块链当前块高
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_baas_plus_dataservice_blockchainheight_ex(request, headers, runtime)

    async def get_baas_plus_dataservice_blockchainheight_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightResponse:
        """
        Description: 获取区块链当前块高
        Summary: 区块链数据服务-获取区块链当前块高
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_baas_plus_dataservice_blockchainheight_ex_async(request, headers, runtime)

    def get_baas_plus_dataservice_blockchainheight_ex(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightResponse:
        """
        Description: 获取区块链当前块高
        Summary: 区块链数据服务-获取区块链当前块高
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightResponse(),
            self.do_request('1.0', 'baas.plus.dataservice.blockchainheight.get', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    async def get_baas_plus_dataservice_blockchainheight_ex_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightResponse:
        """
        Description: 获取区块链当前块高
        Summary: 区块链数据服务-获取区块链当前块高
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceBlockchainheightResponse(),
            await self.do_request_async('1.0', 'baas.plus.dataservice.blockchainheight.get', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    def list_baas_plus_dataservice_lastblocks(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksResponse:
        """
        Description: 获取链最近n条块信息
        Summary: 区块链数据服务-获取链最近n条块信息
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_baas_plus_dataservice_lastblocks_ex(request, headers, runtime)

    async def list_baas_plus_dataservice_lastblocks_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksResponse:
        """
        Description: 获取链最近n条块信息
        Summary: 区块链数据服务-获取链最近n条块信息
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_baas_plus_dataservice_lastblocks_ex_async(request, headers, runtime)

    def list_baas_plus_dataservice_lastblocks_ex(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksResponse:
        """
        Description: 获取链最近n条块信息
        Summary: 区块链数据服务-获取链最近n条块信息
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksResponse(),
            self.do_request('1.0', 'baas.plus.dataservice.lastblocks.list', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    async def list_baas_plus_dataservice_lastblocks_ex_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksResponse:
        """
        Description: 获取链最近n条块信息
        Summary: 区块链数据服务-获取链最近n条块信息
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.ListBaasPlusDataserviceLastblocksResponse(),
            await self.do_request_async('1.0', 'baas.plus.dataservice.lastblocks.list', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    def get_baas_plus_dataservice_transactioncount(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountResponse:
        """
        Description: 获取链交易总数
        Summary: 区块链数据服务-获取链交易总数
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_baas_plus_dataservice_transactioncount_ex(request, headers, runtime)

    async def get_baas_plus_dataservice_transactioncount_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountResponse:
        """
        Description: 获取链交易总数
        Summary: 区块链数据服务-获取链交易总数
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_baas_plus_dataservice_transactioncount_ex_async(request, headers, runtime)

    def get_baas_plus_dataservice_transactioncount_ex(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountResponse:
        """
        Description: 获取链交易总数
        Summary: 区块链数据服务-获取链交易总数
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountResponse(),
            self.do_request('1.0', 'baas.plus.dataservice.transactioncount.get', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    async def get_baas_plus_dataservice_transactioncount_ex_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountResponse:
        """
        Description: 获取链交易总数
        Summary: 区块链数据服务-获取链交易总数
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioncountResponse(),
            await self.do_request_async('1.0', 'baas.plus.dataservice.transactioncount.get', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    def get_baas_plus_dataservice_transactioninfo(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoResponse:
        """
        Description: 根据交易hash获取交易详情
        Summary: 区块链数据服务-获取交易详情
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_baas_plus_dataservice_transactioninfo_ex(request, headers, runtime)

    async def get_baas_plus_dataservice_transactioninfo_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoRequest,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoResponse:
        """
        Description: 根据交易hash获取交易详情
        Summary: 区块链数据服务-获取交易详情
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_baas_plus_dataservice_transactioninfo_ex_async(request, headers, runtime)

    def get_baas_plus_dataservice_transactioninfo_ex(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoResponse:
        """
        Description: 根据交易hash获取交易详情
        Summary: 区块链数据服务-获取交易详情
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoResponse(),
            self.do_request('1.0', 'baas.plus.dataservice.transactioninfo.get', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )

    async def get_baas_plus_dataservice_transactioninfo_ex_async(
        self,
        request: ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoResponse:
        """
        Description: 根据交易hash获取交易详情
        Summary: 区块链数据服务-获取交易详情
        """
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ak__7365e_031a_87c_467bbe_817bec_28a_2a_1dc_models.GetBaasPlusDataserviceTransactioninfoResponse(),
            await self.do_request_async('1.0', 'baas.plus.dataservice.transactioninfo.get', 'HTTPS', 'POST', f'/gateway.do', TeaCore.to_map(request), headers, runtime)
        )
