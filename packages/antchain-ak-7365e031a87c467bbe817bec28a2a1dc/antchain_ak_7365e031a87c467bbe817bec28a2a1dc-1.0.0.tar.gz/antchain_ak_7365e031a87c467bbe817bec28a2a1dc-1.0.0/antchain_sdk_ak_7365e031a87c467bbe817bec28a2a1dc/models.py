# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class Config(TeaModel):
    """
    Model for initing client
    """
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        security_token: str = None,
        protocol: str = None,
        read_timeout: int = None,
        connect_timeout: int = None,
        http_proxy: str = None,
        https_proxy: str = None,
        endpoint: str = None,
        no_proxy: str = None,
        max_idle_conns: int = None,
        user_agent: str = None,
        socks_5proxy: str = None,
        socks_5net_work: str = None,
        max_idle_time_millis: int = None,
        keep_alive_duration_millis: int = None,
        max_requests: int = None,
        max_requests_per_host: int = None,
    ):
        # accesskey id
        self.access_key_id = access_key_id
        # accesskey secret
        self.access_key_secret = access_key_secret
        # security token
        self.security_token = security_token
        # http protocol
        self.protocol = protocol
        # read timeout
        self.read_timeout = read_timeout
        # connect timeout
        self.connect_timeout = connect_timeout
        # http proxy
        self.http_proxy = http_proxy
        # https proxy
        self.https_proxy = https_proxy
        # endpoint
        self.endpoint = endpoint
        # proxy white list
        self.no_proxy = no_proxy
        # max idle conns
        self.max_idle_conns = max_idle_conns
        # user agent
        self.user_agent = user_agent
        # socks5 proxy
        self.socks_5proxy = socks_5proxy
        # socks5 network
        self.socks_5net_work = socks_5net_work
        # 长链接最大空闲时长
        self.max_idle_time_millis = max_idle_time_millis
        # 长链接最大连接时长
        self.keep_alive_duration_millis = keep_alive_duration_millis
        # 最大连接数（长链接最大总数）
        self.max_requests = max_requests
        # 每个目标主机的最大连接数（分主机域名的长链接最大总数
        self.max_requests_per_host = max_requests_per_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.read_timeout is not None:
            result['readTimeout'] = self.read_timeout
        if self.connect_timeout is not None:
            result['connectTimeout'] = self.connect_timeout
        if self.http_proxy is not None:
            result['httpProxy'] = self.http_proxy
        if self.https_proxy is not None:
            result['httpsProxy'] = self.https_proxy
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.no_proxy is not None:
            result['noProxy'] = self.no_proxy
        if self.max_idle_conns is not None:
            result['maxIdleConns'] = self.max_idle_conns
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.socks_5proxy is not None:
            result['socks5Proxy'] = self.socks_5proxy
        if self.socks_5net_work is not None:
            result['socks5NetWork'] = self.socks_5net_work
        if self.max_idle_time_millis is not None:
            result['maxIdleTimeMillis'] = self.max_idle_time_millis
        if self.keep_alive_duration_millis is not None:
            result['keepAliveDurationMillis'] = self.keep_alive_duration_millis
        if self.max_requests is not None:
            result['maxRequests'] = self.max_requests
        if self.max_requests_per_host is not None:
            result['maxRequestsPerHost'] = self.max_requests_per_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('readTimeout') is not None:
            self.read_timeout = m.get('readTimeout')
        if m.get('connectTimeout') is not None:
            self.connect_timeout = m.get('connectTimeout')
        if m.get('httpProxy') is not None:
            self.http_proxy = m.get('httpProxy')
        if m.get('httpsProxy') is not None:
            self.https_proxy = m.get('httpsProxy')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('noProxy') is not None:
            self.no_proxy = m.get('noProxy')
        if m.get('maxIdleConns') is not None:
            self.max_idle_conns = m.get('maxIdleConns')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('socks5Proxy') is not None:
            self.socks_5proxy = m.get('socks5Proxy')
        if m.get('socks5NetWork') is not None:
            self.socks_5net_work = m.get('socks5NetWork')
        if m.get('maxIdleTimeMillis') is not None:
            self.max_idle_time_millis = m.get('maxIdleTimeMillis')
        if m.get('keepAliveDurationMillis') is not None:
            self.keep_alive_duration_millis = m.get('keepAliveDurationMillis')
        if m.get('maxRequests') is not None:
            self.max_requests = m.get('maxRequests')
        if m.get('maxRequestsPerHost') is not None:
            self.max_requests_per_host = m.get('maxRequestsPerHost')
        return self


class CheckPointStructBody(TeaModel):
    def __init__(
        self,
        height: str = None,
        index: str = None,
        type: str = None,
        last_error: str = None,
        error_count: str = None,
        total_count: str = None,
    ):
        # 高度
        self.height = height
        # 序号
        self.index = index
        # 类型
        self.type = type
        # last_error
        self.last_error = last_error
        # 错误统计
        self.error_count = error_count
        # 统计
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.index is not None:
            result['index'] = self.index
        if self.type is not None:
            result['type'] = self.type
        if self.last_error is not None:
            result['last_error'] = self.last_error
        if self.error_count is not None:
            result['error_count'] = self.error_count
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('last_error') is not None:
            self.last_error = m.get('last_error')
        if m.get('error_count') is not None:
            self.error_count = m.get('error_count')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class BlockInfo(TeaModel):
    def __init__(
        self,
        biz_data: str = None,
        biz_id: str = None,
        block_hash: str = None,
        height: int = None,
        parent_hash: str = None,
        size: int = None,
        timestamp: int = None,
        transaction_size: int = None,
        version: str = None,
    ):
        # 业务数据
        self.biz_data = biz_data
        # 区块链唯一性标识
        self.biz_id = biz_id
        # 区块哈希
        self.block_hash = block_hash
        # 块高
        self.height = height
        # 上一个区块的hash
        self.parent_hash = parent_hash
        # size
        self.size = size
        # 出块时间
        self.timestamp = timestamp
        # 包含交易数
        self.transaction_size = transaction_size
        # 版本
        self.version = version

    def validate(self):
        self.validate_required(self.biz_data, 'biz_data')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.block_hash, 'block_hash')
        self.validate_required(self.height, 'height')
        self.validate_required(self.parent_hash, 'parent_hash')
        self.validate_required(self.size, 'size')
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.transaction_size, 'transaction_size')
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_data is not None:
            result['biz_data'] = self.biz_data
        if self.biz_id is not None:
            result['biz_id'] = self.biz_id
        if self.block_hash is not None:
            result['block_hash'] = self.block_hash
        if self.height is not None:
            result['height'] = self.height
        if self.parent_hash is not None:
            result['parent_hash'] = self.parent_hash
        if self.size is not None:
            result['size'] = self.size
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.transaction_size is not None:
            result['transaction_size'] = self.transaction_size
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_data') is not None:
            self.biz_data = m.get('biz_data')
        if m.get('biz_id') is not None:
            self.biz_id = m.get('biz_id')
        if m.get('block_hash') is not None:
            self.block_hash = m.get('block_hash')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('parent_hash') is not None:
            self.parent_hash = m.get('parent_hash')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('transaction_size') is not None:
            self.transaction_size = m.get('transaction_size')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class TriggerDTOStructBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        source: str = None,
        create_time: str = None,
        error_message: str = None,
        status: str = None,
        option: str = None,
        checkpoint: CheckPointStructBody = None,
        pending_error_logs: str = None,
    ):
        # 名称
        self.name = name
        # 类型
        self.type = type
        # 源
        self.source = source
        # 创建时间
        self.create_time = create_time
        # 错误信息
        self.error_message = error_message
        # 状态
        self.status = status
        # option（map结构，由于金融云无map接口所以通过string类型传输json格式）
        self.option = option
        # checkpoint类
        self.checkpoint = checkpoint
        # 待处理的错误事件总数
        self.pending_error_logs = pending_error_logs

    def validate(self):
        if self.checkpoint:
            self.checkpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.source is not None:
            result['source'] = self.source
        if self.create_time is not None:
            result['create_time'] = self.create_time
        if self.error_message is not None:
            result['error_message'] = self.error_message
        if self.status is not None:
            result['status'] = self.status
        if self.option is not None:
            result['option'] = self.option
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint.to_map()
        if self.pending_error_logs is not None:
            result['pending_error_logs'] = self.pending_error_logs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('create_time') is not None:
            self.create_time = m.get('create_time')
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('option') is not None:
            self.option = m.get('option')
        if m.get('checkpoint') is not None:
            temp_model = CheckPointStructBody()
            self.checkpoint = temp_model.from_map(m['checkpoint'])
        if m.get('pending_error_logs') is not None:
            self.pending_error_logs = m.get('pending_error_logs')
        return self


class UpdateBaasChainDataexportStatusRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        ant_chain_id: str = None,
        consortium_id: str = None,
        trigger_name: str = None,
        status_action: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        self.product_instance_id = product_instance_id
        # 链id
        self.ant_chain_id = ant_chain_id
        # 联盟id
        self.consortium_id = consortium_id
        # "9481b612d6ca4cfdbecc5c5d395eda423f007745-233d-4860-8fd4-a107233ace6c"
        self.trigger_name = trigger_name
        # "Enabled/Disabled/DELETE"
        self.status_action = status_action

    def validate(self):
        self.validate_required(self.ant_chain_id, 'ant_chain_id')
        self.validate_required(self.consortium_id, 'consortium_id')
        self.validate_required(self.trigger_name, 'trigger_name')
        self.validate_required(self.status_action, 'status_action')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.ant_chain_id is not None:
            result['ant_chain_id'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['consortium_id'] = self.consortium_id
        if self.trigger_name is not None:
            result['trigger_name'] = self.trigger_name
        if self.status_action is not None:
            result['status_action'] = self.status_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('ant_chain_id') is not None:
            self.ant_chain_id = m.get('ant_chain_id')
        if m.get('consortium_id') is not None:
            self.consortium_id = m.get('consortium_id')
        if m.get('trigger_name') is not None:
            self.trigger_name = m.get('trigger_name')
        if m.get('status_action') is not None:
            self.status_action = m.get('status_action')
        return self


class UpdateBaasChainDataexportStatusResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        result: TriggerDTOStructBody = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 结果码，一般OK表示调用成功
        self.result_code = result_code
        # 异常信息的文本描述
        self.result_msg = result_msg
        # {}
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('result') is not None:
            temp_model = TriggerDTOStructBody()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateBaasChainDataexportTaskRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        ant_chain_id: str = None,
        consortium_id: str = None,
        trigger: TriggerDTOStructBody = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        self.product_instance_id = product_instance_id
        # 链id
        self.ant_chain_id = ant_chain_id
        # 联盟id
        self.consortium_id = consortium_id
        # {}
        self.trigger = trigger

    def validate(self):
        self.validate_required(self.ant_chain_id, 'ant_chain_id')
        self.validate_required(self.consortium_id, 'consortium_id')
        self.validate_required(self.trigger, 'trigger')
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.ant_chain_id is not None:
            result['ant_chain_id'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['consortium_id'] = self.consortium_id
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('ant_chain_id') is not None:
            self.ant_chain_id = m.get('ant_chain_id')
        if m.get('consortium_id') is not None:
            self.consortium_id = m.get('consortium_id')
        if m.get('trigger') is not None:
            temp_model = TriggerDTOStructBody()
            self.trigger = temp_model.from_map(m['trigger'])
        return self


class CreateBaasChainDataexportTaskResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        result: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 结果码，一般OK表示调用成功
        self.result_code = result_code
        # 异常信息的文本描述
        self.result_msg = result_msg
        # ""
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateBaasChainDataexportTaskRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        consortium_id: str = None,
        ant_chain_id: str = None,
        trigger_name: str = None,
        trigger: TriggerDTOStructBody = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        self.product_instance_id = product_instance_id
        # 联盟id
        self.consortium_id = consortium_id
        # 链id
        self.ant_chain_id = ant_chain_id
        # 任务名称
        self.trigger_name = trigger_name
        # 导出任务接口体
        self.trigger = trigger

    def validate(self):
        self.validate_required(self.consortium_id, 'consortium_id')
        self.validate_required(self.ant_chain_id, 'ant_chain_id')
        self.validate_required(self.trigger_name, 'trigger_name')
        self.validate_required(self.trigger, 'trigger')
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.consortium_id is not None:
            result['consortium_id'] = self.consortium_id
        if self.ant_chain_id is not None:
            result['ant_chain_id'] = self.ant_chain_id
        if self.trigger_name is not None:
            result['trigger_name'] = self.trigger_name
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('consortium_id') is not None:
            self.consortium_id = m.get('consortium_id')
        if m.get('ant_chain_id') is not None:
            self.ant_chain_id = m.get('ant_chain_id')
        if m.get('trigger_name') is not None:
            self.trigger_name = m.get('trigger_name')
        if m.get('trigger') is not None:
            temp_model = TriggerDTOStructBody()
            self.trigger = temp_model.from_map(m['trigger'])
        return self


class UpdateBaasChainDataexportTaskResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        result: TriggerDTOStructBody = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 结果码，一般OK表示调用成功
        self.result_code = result_code
        # 异常信息的文本描述
        self.result_msg = result_msg
        # 修改导出任务（名称、描述、告警地址）信息结构体
        # 
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('result') is not None:
            temp_model = TriggerDTOStructBody()
            self.result = temp_model.from_map(m['result'])
        return self


class GetBaasPlusDataserviceBlockchainheightRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        bizid: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        self.product_instance_id = product_instance_id
        # 区块链的唯一性标示
        self.bizid = bizid

    def validate(self):
        self.validate_required(self.bizid, 'bizid')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.bizid is not None:
            result['bizid'] = self.bizid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('bizid') is not None:
            self.bizid = m.get('bizid')
        return self


class GetBaasPlusDataserviceBlockchainheightResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        data: int = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 结果码，一般OK表示调用成功
        self.result_code = result_code
        # 异常信息的文本描述
        self.result_msg = result_msg
        # 区块链块高
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ListBaasPlusDataserviceLastblocksRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        bizid: str = None,
        size: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        self.product_instance_id = product_instance_id
        # 区块链唯一性标识
        self.bizid = bizid
        # 区块个数
        self.size = size

    def validate(self):
        self.validate_required(self.bizid, 'bizid')
        self.validate_required(self.size, 'size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.bizid is not None:
            result['bizid'] = self.bizid
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('bizid') is not None:
            self.bizid = m.get('bizid')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListBaasPlusDataserviceLastblocksResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        last_block_list: List[BlockInfo] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 结果码，一般OK表示调用成功
        self.result_code = result_code
        # 异常信息的文本描述
        self.result_msg = result_msg
        # 区块信息
        self.last_block_list = last_block_list

    def validate(self):
        if self.last_block_list:
            for k in self.last_block_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        result['last_block_list'] = []
        if self.last_block_list is not None:
            for k in self.last_block_list:
                result['last_block_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        self.last_block_list = []
        if m.get('last_block_list') is not None:
            for k in m.get('last_block_list'):
                temp_model = BlockInfo()
                self.last_block_list.append(temp_model.from_map(k))
        return self


class GetBaasPlusDataserviceTransactioncountRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        bizid: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        self.product_instance_id = product_instance_id
        # 区块链唯一性标示
        self.bizid = bizid

    def validate(self):
        self.validate_required(self.bizid, 'bizid')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.bizid is not None:
            result['bizid'] = self.bizid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('bizid') is not None:
            self.bizid = m.get('bizid')
        return self


class GetBaasPlusDataserviceTransactioncountResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        data: int = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 结果码，一般OK表示调用成功
        self.result_code = result_code
        # 异常信息的文本描述
        self.result_msg = result_msg
        # 交易总数
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetBaasPlusDataserviceTransactioninfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        bizid: str = None,
        hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        self.product_instance_id = product_instance_id
        # 区块链唯一性标识
        self.bizid = bizid
        # 交易hash
        self.hash = hash

    def validate(self):
        self.validate_required(self.bizid, 'bizid')
        self.validate_required(self.hash, 'hash')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.bizid is not None:
            result['bizid'] = self.bizid
        if self.hash is not None:
            result['hash'] = self.hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('bizid') is not None:
            self.bizid = m.get('bizid')
        if m.get('hash') is not None:
            self.hash = m.get('hash')
        return self


class GetBaasPlusDataserviceTransactioninfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        bizid: str = None,
        category: int = None,
        create_time: int = None,
        from_hash: str = None,
        hash: str = None,
        height: int = None,
        to_hash: str = None,
        type: int = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 结果码，一般OK表示调用成功
        self.result_code = result_code
        # 异常信息的文本描述
        self.result_msg = result_msg
        # 区块链唯一性标识
        self.bizid = bizid
        # category
        self.category = category
        # 交易发起时间
        self.create_time = create_time
        # 交易发起方哈希
        self.from_hash = from_hash
        # 交易哈希
        self.hash = hash
        # 块高
        self.height = height
        # 交易接收方哈希
        self.to_hash = to_hash
        # 交易类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.bizid is not None:
            result['bizid'] = self.bizid
        if self.category is not None:
            result['category'] = self.category
        if self.create_time is not None:
            result['create_time'] = self.create_time
        if self.from_hash is not None:
            result['from_hash'] = self.from_hash
        if self.hash is not None:
            result['hash'] = self.hash
        if self.height is not None:
            result['height'] = self.height
        if self.to_hash is not None:
            result['to_hash'] = self.to_hash
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('bizid') is not None:
            self.bizid = m.get('bizid')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('create_time') is not None:
            self.create_time = m.get('create_time')
        if m.get('from_hash') is not None:
            self.from_hash = m.get('from_hash')
        if m.get('hash') is not None:
            self.hash = m.get('hash')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('to_hash') is not None:
            self.to_hash = m.get('to_hash')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


