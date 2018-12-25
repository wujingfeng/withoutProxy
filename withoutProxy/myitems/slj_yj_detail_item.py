# 孙国强
# 水利建设--业绩信息
from scrapy import Field, Item


class slj_yj_detail_item(Item):
    #  slj_gcyj_hj 表
    jbxx_id = Field()  # 基本信息
    gs_id = Field()  # 公司id
    gsmc = Field()  # 公司名称
    xmmc = Field()  # 项目名称
    jxmc = Field()  # 奖项名称
    jxlb = Field()  # 奖项类别
    jxjb = Field()  # 奖项级别
    jxdb = Field()  # 奖项等别
    bjdw = Field()  # 颁奖单位
    bjwh = Field()  # 颁奖文号
    bjsj = Field()  # 颁奖时间
    created = Field()  # 创建时间
    modified = Field()  # 修改时间

    #  slj_gcyj_jbxx 表
    xmbh = Field()  # 项目编号
    htmc = Field()  # 合同名称
    gczt = Field()  # 工程状态
    szd = Field()  # 所在地
    xmfzr = Field()  # 项目负责人
    jsfzr = Field()  # 技术负责人
    jsdw = Field()  # 建设单位
    gcdj_db = Field()  # 工程等级-等别
    gcdj_jb = Field()  # 工程等级-级别
    kgrq = Field()  # 开工日期
    wgrq = Field()  # 完工日期
    htgq = Field()  # 合同工期
    gjzb = Field()  # 工程关键指标
    htje = Field()  # 合同金额(万元)
    jsje = Field()  # 结算金额(万元)
    zynr = Field()  # 合同主要内容
    spbm = Field()  # 审批部门
    jclx = Field()  # 检测类型
    type = Field()  # 业绩类型
    xglsjl = Field()  # 修改历史记录
    link = Field()  # 网站链接

    #  slj_gcyj_ry 表
    name = Field()  # 姓名
    zw = Field()  # 职务
    zc = Field()  # 职称
    zsmc = Field()  # 证书名称
    zsbh = Field()  # 证书编号
    zszy = Field()  # 证书专业
    dj = Field()  # 等级

    # slj_statistic 表
    cj_id = Field()
    p_type = Field()  # 大类名称
    s_type = Field()  # 子类名称
    total = Field()  # 条数

    # 集合
    jbxx_list = Field()
    hjxx_list = Field()
    ryxx_list = Field()
    tjxx_list = Field()


    pipline_func = Field()  # 每一个item中都默认加上