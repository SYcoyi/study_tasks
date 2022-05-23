Feature: 安徽社区名优商品收货人信息

  Scenario: 新增名优商品收货人
    When 手机个人端密码登录
    Then 新增名优收货地址   #/api/user/receiver/update


  Scenario:名优商品收货人列表展示
    When 手机个人端密码登录
    Then 名优收货人列表    #/api/user/area/shippingList