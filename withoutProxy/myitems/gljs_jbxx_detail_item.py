from scrapy import Field, Item
# 全国公路基本信息
# 孙国强

class gljs_jbxx_detail_item(Item):
    # gljs_baseinfo 基本信息表
    zzjgdm = Field()  # 组织机构代码
    qymc = Field()  # 企业名称
    zcsf = Field()  # 注册省份
    zccs = Field()  # 注册城市
    cymc = Field()  # 曾用名称
    xzzgbm = Field()  # 行政主管部门名称
    yyzzzch = Field()  # 营业执照注册号
    zczj = Field()  # 注册资金
    qylx = Field()  # 企业类型
    qyxz = Field()  # 企业性质
    yyzzzcrq = Field()  # 营业执照注册日期
    clrq = Field()  # 成立日期
    yyfw = Field()  # 营业范围
    link = Field()  # 链接
    corpCode = Field()  # 公司标识
    created = Field()  # 写入时间
    modified = Field()  # 修改时间
    fddbr = Field()  # 法定代表人
    fddbrzc = Field()  # 法定代表人职称
    qyfzr = Field()  # 企业负责人职称
    qyfzrzc = Field()  # 企业负责人职称
    jsfzr = Field()  # 技术负责人
    jsfzrzc = Field()  # 技术负责人职称
    qyqk = Field()  # 资产构成情况及投资关联企业情况
    shxydm = Field()  # 统一社会信用代码


    # gljs_creditrating 信用等级表
    gs_id = Field()  # 公司表id
    companyId = Field()
    gsmc = Field()  # 公司名称
    url = Field()  # 链接
    pjsf = Field()  # 评价省份
    pjnf = Field()  # 评价年份
    dj = Field()  # 等级
    gszt = Field()  # 公示状态
    valid = Field()  # 是否有效 0是 1否
    created = Field()  # 写入时间
    modified = Field()  # 修改时间

    pipline_func = Field()  # 每一个item中都默认加上.