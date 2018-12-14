#---------- 人员信息
from scrapy import Field, Item


class slj_ry_detail_item(Item):
    cj_id = Field()
    gsmc = Field()
    xm = Field()
    zw = Field()
    sfzh = Field()
    zybh = Field()
    zgzbh = Field()
    zc = Field()
    zgzsh = Field()
    zczsh = Field()
    yxqz = Field()
    zczy = Field()
    zczsbh = Field()
    dj = Field()
    zylb = Field()
    zszy = Field()
    gw = Field()
    gwzsh = Field()
    zslb = Field()
    zsbh = Field()
    zygz = Field()
    fzjg = Field()
    zcyzy = Field()
    start_year = Field()
    xl = Field()
    fzzzlb = Field()
    ssbm = Field()
    lb = Field()
    ry_type = Field()
    created = Field()
    link  = Field()

    data_list = Field()
    sjl_zgzs_list=Field()
    lsj_lb_list = Field()
    pipline_func = Field() # 每一个item中都默认加上

