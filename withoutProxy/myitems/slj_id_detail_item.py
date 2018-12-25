from scrapy import Field, Item

# 水利建设 公司id
class slj_id_detail_item(Item):
    comp_id = Field()

    pipline_func = Field()