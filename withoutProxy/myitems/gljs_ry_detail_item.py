from scrapy import Field, Item

# 公路建设 人员
class gljs_ry_detail_item(Item):
    staff_id = Field()
    idcard = Field()
    gs_id = Field()
    gljs_xm = Field()
    gljs_xb = Field()
    gljs_birth = Field()
    gsmc = Field()
    gljs_xl = Field()
    gljs_byyx = Field()
    gljs_sxzy = Field()
    gljs_zw = Field()
    gljs_ksgznf = Field()
    person_link = Field()
    created = Field()
    modified = Field()
    valid = Field()
    gljs_typy = Field()
    xxly = Field()
    fugai = Field()

    # 职称信息
    zcc = Field()
    zsbh = Field()  # 证书标号
    zczy = Field()
    hfjg= Field()  # 职称专业
    hfrq= Field()  # 核发机关



    # 执业资格信息
    zclb = Field()
    zcdj = Field()
    fzjg = Field()
    fzrq = Field()
    zcyxqz = Field()

    # 履历信息
    xm = Field()
    zwlx = Field()
    zw = Field()
    rzzt = Field()
    rzsj = Field()
    lzsj = Field()

    proj_id = Field()
    gljs_xmname = Field()
    gljs_bdname = Field()
    gljs_drzw = Field()
    gljs_start_time = Field()
    gljs_end_time  = Field()


    gryj_list_list = Field()
    flxx_list = Field()
    zyzgxx_list = Field()
    zcxx_list = Field()
    jbxx_list = Field()

    pipline_func = Field() # 每一个item中都默认加上