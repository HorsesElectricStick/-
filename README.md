# -
以马自达MX-5为例，使用scrapy的ImagePipeline异步下载图片，重写了ImagePipeline以自定义存储路径，实现不同车型图片分开存放
使用随机UA，IP代理池，下载约2000张高清图，用时10分钟
