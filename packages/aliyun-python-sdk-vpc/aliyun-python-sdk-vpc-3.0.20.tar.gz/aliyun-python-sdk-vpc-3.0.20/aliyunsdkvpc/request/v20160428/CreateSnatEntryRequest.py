# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvpc.endpoint import endpoint_data

class CreateSnatEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateSnatEntry','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_SourceCIDR(self): # String
		return self.get_query_params().get('SourceCIDR')

	def set_SourceCIDR(self, SourceCIDR):  # String
		self.add_query_param('SourceCIDR', SourceCIDR)
	def get_SnatIp(self): # String
		return self.get_query_params().get('SnatIp')

	def set_SnatIp(self, SnatIp):  # String
		self.add_query_param('SnatIp', SnatIp)
	def get_SourceVSwitchId(self): # String
		return self.get_query_params().get('SourceVSwitchId')

	def set_SourceVSwitchId(self, SourceVSwitchId):  # String
		self.add_query_param('SourceVSwitchId', SourceVSwitchId)
	def get_EipAffinity(self): # Integer
		return self.get_query_params().get('EipAffinity')

	def set_EipAffinity(self, EipAffinity):  # Integer
		self.add_query_param('EipAffinity', EipAffinity)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_SnatTableId(self): # String
		return self.get_query_params().get('SnatTableId')

	def set_SnatTableId(self, SnatTableId):  # String
		self.add_query_param('SnatTableId', SnatTableId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SnatEntryName(self): # String
		return self.get_query_params().get('SnatEntryName')

	def set_SnatEntryName(self, SnatEntryName):  # String
		self.add_query_param('SnatEntryName', SnatEntryName)
