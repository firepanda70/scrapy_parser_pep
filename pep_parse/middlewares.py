from scrapy import signals


# Весь этот код создается автоматически, так что я сам не уверен,
# зачем он нужен и что он делает
class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        sql_pipeline_instance = cls()
        crawler.signals.connect(sql_pipeline_instance.spider_opened,
                                signal=signals.spider_opened)
        return sql_pipeline_instance

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):

        for res in result:
            yield res

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for request in start_requests:
            yield request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        sql_pipeline_instance = cls()
        crawler.signals.connect(sql_pipeline_instance.spider_opened,
                                signal=signals.spider_opened)
        return sql_pipeline_instance

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
