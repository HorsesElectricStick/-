# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline

class AutohomeImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_list = super(AutohomeImagePipeline,self).get_media_requests(item,info)
        for request in request_list:
            request.item = item
        return request_list

    def file_path(self, request, response=None, info=None):
        path = super(AutohomeImagePipeline,self).file_path(request, response, info)
        title = request.item['title']
        final_path = path.replace('full',title)
        return final_path