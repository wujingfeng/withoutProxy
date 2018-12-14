from scrapy import Field, Item

# 公路建设 id
class gljs_id_detail_item(Item):
    gsmc = Field()
    comp_id = Field()

    pipline_func = Field()