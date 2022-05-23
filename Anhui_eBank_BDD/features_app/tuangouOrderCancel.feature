Feature: 安徽社区个人端，创建/取消团购商品订单

  Scenario:创建/取消普通团购订单
    When 手机个人端密码登录   ##需增加接口
    Then 创建普通团购订单         ##原接口名称：生成团购商品##/api/user/order/generate
    Then app取消订单

  Scenario:创建/取消券码类团购订单
    When 手机个人端密码登录
    Then 创建券码类团购订单
    Then app取消订单

  Scenario:创建/取消仅信用卡类团购订单
    When 手机个人端密码登录
    Then 创建仅信用卡类团购订单
    Then app取消订单
