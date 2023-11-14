# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from .utils import Api


class EcsApi(Api):

    def __init__(self, **kwargs):
        return super(EcsApi, self).__init__(category='ECS', **kwargs)

    def stop_instance(self, instance, **kwargs):
        from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest
        return self.call(StopInstanceRequest, InstanceId=instance, **kwargs)

    def delete_instance(self, instance, Force=True, **kwargs):
        from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest
        return self.call(DeleteInstanceRequest, InstanceId=instance, Force=Force, **kwargs)

    def start_instance(self, instance, **kwargs):
        from aliyunsdkecs.request.v20140526.StartInstanceRequest import StartInstanceRequest
        return self.call(StartInstanceRequest, InstanceId=instance, **kwargs)

    def list_instances(self, **kwargs):
        from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
        return self.call(DescribeInstancesRequest, 'Instances.Instance', **kwargs)

    def list_regions(self, **kwargs):
        from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
        return self.call(DescribeRegionsRequest, 'Regions.Region', **kwargs)

    def price(self, **kwargs):
        from aliyunsdkecs.request.v20140526.DescribePriceRequest import DescribePriceRequest
        return self.call(DescribePriceRequest, **kwargs)

    def run_instances(self, **kwargs):
        from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
        return self.call(RunInstancesRequest, 'InstanceIdSets', **kwargs)

    def describe_spot_price_history(self, **kwargs):
        from aliyunsdkecs.request.v20140526.DescribeSpotPriceHistoryRequest import DescribeSpotPriceHistoryRequest
        return self.call(DescribeSpotPriceHistoryRequest, 'SpotPrices', **kwargs)
