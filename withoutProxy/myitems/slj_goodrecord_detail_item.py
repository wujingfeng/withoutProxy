#彭青山
#全国水利良好
from scrapy import Field, Item


class slj_goodrecord_detail_item(Item):
     cj_id = Field()
     gs_id = Field()
     gsmc = Field()
     p_type = Field()
     s_type = Field()
     total = Field()
     tmp_list = Field()
     pipline_func = Field()  # 每一个item中都默认加上
    # gs_id = Field()
    # gsmc = Field()
    # xxly = Field()
    # link = Field()
    # jl_type = Field()
    # dwhj_jxmc = Field()
    # dwhj_jxjb = Field()
    # dwhj_bjdw = Field()
    # dwhj_bjwh = Field()
    # dwhj_bjsj = Field()
    #
    # gchj_xmmc = Field()
    # gchj_jxmc = Field()
    # gchj_jxlb = Field()
    # gchj_jxjb = Field()
    # gchj_bjdw = Field()
    # gchj_bjwh = Field()
    # gchj_bjsj = Field()
    #
    # gyhd_sj = Field()
    # gyhd_cy_or_zc = Field()
    #
    # patents_name = Field()
    # patents_num = Field()
    # patents_sq_time = Field()
    # patents_valid = Field()
    #
    # gf_name = Field()
    # gf_num = Field()
    # gf_pz_time = Field()
    # gf_valid = Field()
    #
    # jcqk_name = Field()
    # jcqk_num = Field()
    # jcqk_time = Field()
    # jcqk_bz = Field()
    #
    # zsqkfb_tm = Field()
    # zsqkfb_zz = Field()
    # zsqkfb_name = Field()
    # zsqkfb_num = Field()
    # zsqkfb_time = Field()
    #
    # xgyff_name = Field()
    # xgyff_lb = Field()
    # xgyff_jdjg = Field()
    # xgyff_time = Field()
    #
    # rjzzq_name = Field()
    # rjzzq_num = Field()
    # rjzzq_zsh = Field()
    # rjzzq_djrq = Field()
    #
    # zbjsbz_name = Field()
    # zbjsbz_num = Field()
    # zbjsbz_fb_time = Field()
    # zbjsbz_ss_time = Field()
    # zbjsbz_bz = Field()

