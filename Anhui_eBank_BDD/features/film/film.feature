#Feature: 安徽社区app用户端-电影首页
#
#  Scenario: 电影首页
#    When 手机个人端登录获取验证码
#    Then 手机个人端登录
#    When 通过渠道编码，展位类型获取展位信息
#    When 通过手机GPS定位获取城市信息
#    When 获取展位下的上架的活动列表
#    When 查询在映影片列表
#    When 查询距离最近影院
#    When 获取当前用户的电影卡信息
#    Then 获取电影票城市
#
#  Scenario: 会员卡
#    When 手机个人端登录获取验证码
#    Then 手机个人端登录
#    When 获取展位下的上架的活动列表
#    Given 查看活动奖品领取信息
#    When 电影票参加活动
#    Given 获取会员开卡选项列表信息
#    Given 获取当前用户的会员卡信息
#    Given 电影票获取当前用户
#    When 开通会员卡
#    Then 查看开卡记录
#
#  Scenario: 影片
#    When 手机个人端登录获取验证码
#    Then 手机个人端登录
#    When 查询在映影片列表
#    Then 获取影片详情信息
#    Then 获取视频剧照信息列表
#    When 写影评
#    When 获取影片全部评论
#    Then 点赞
#
#  Scenario: 影院
#    When 手机个人端登录获取验证码
#    Then 手机个人端登录
#    Given 查询城市包含区县列表
#    Given 查询按经纬度定位离我最近影院列表
#    When 查看影院详情
#    When 查询影院在映影片列表
#    Then 查看影院影片场次
#    When 查看影院评价
#    When 评价电影院
#    Given 查看动态座位图
#    When 锁定座位
#    When 查询订单信息
#    Then 购买电影票
#    # 验证解锁座位
#    Given 查看动态座位图
#    When 锁定座位
#    Then 解锁座位