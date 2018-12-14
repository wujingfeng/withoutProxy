#彭青山
#全国奖惩记录
from scrapy import Field, Item


class allcountry_info_detail_item(Item):
    title = Field()
    xmmc = Field()
    dlink = Field()
    type = Field()
    fnumber = Field()
    qymc = Field()
    jddw = Field()
    jddate = Field()
    nr = Field()
    pipline_func = Field() # 每一个item中都默认加上