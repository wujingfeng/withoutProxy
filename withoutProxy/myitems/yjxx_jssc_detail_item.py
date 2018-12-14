#张峻珲
#全国公路建设市场(业绩信息)
from scrapy import Field, Item


class yjxx_jssc_detail_item(Item):
    #公司表id
    gs_id = Field()
    #官网业绩id
    proj_id = Field()
    #公司名称
    gsmc = Field()
    # 项目名称
    xmmc = Field()
    # 链接
    link = Field()
    # 合同价（万元）
    htj = Field()
    # 结算价（万元）
    jsj = Field()
    # 开工时间
    kgsj = Field()
    # 主要工程量
    zygcl = Field()
    # 1=已建,2=在建
    yz = Field()
    # 1=主包,2=分包
    zf = Field()
    # 所在省份
    szsf = Field()
    # 业绩类型：1：省厅录入，2：省厅审核
    yj_type = Field()
    # 标段类型（省厅录入）
    bdlx = Field()
    # 标段名称（省厅录入）
    bdmc = Field()
    # 中标企业（省厅录入）
    zbqy = Field()
    # 是否完工（省厅录入）
    sfwg = Field()
    # 交工验收得分（省厅录入）
    jgysdf = Field()
    # 合同段建设规模（省厅录入）
    jsgm = Field()
    # 其它需要描述的合同段信息（省厅录入）
    other = Field()
    # 项目类型（省厅审核）
    xmlx = Field()
    # 技术等级（省厅审核）
    jsdj = Field()
    # 合同段名称（省厅审核）
    htdmc = Field()
    # 竣工日期（省厅审核）
    jgrq = Field()
    # 交工日期（省厅审核）
    jgsj = Field()
    # 合同段开始桩号（省厅审核）
    kszh = Field()
    # 合同段结束桩号（省厅审核）
    jszh = Field()
    # 质量评定情况（省厅审核）
    zlpdqk = Field()
    # 项目代码（省厅审核）
    xmdm = Field()
    # 1：有效数据 0：无效
    valid = Field()
    # 写入时间
    created = Field()
    # 修改时间
    modified = Field()
    #业绩人员表
    # 业绩表id
    yj_id = Field()
    # 姓名
    name = Field()
    # 担任岗位或专业负责人
    gw = Field()
    # 任职日期
    rzsj = Field()
    # 业绩类型：1：省厅录入，2：省厅审核
    type = Field()
    # 是否有效 1 有效 0 无效
    validx = Field()
    # 创建时间
    createdx = Field()
    # 修改时间
    modifiedx = Field()
    # list
    ry_list = Field()
    items = Field()

    pipline_func = Field()  # 每一个item中都默认加上