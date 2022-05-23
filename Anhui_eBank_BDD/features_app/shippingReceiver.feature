Feature: 安徽社区个人端名优特惠收货人信息

  Scenario: 新增名优特惠收货人
    When 手机个人端密码登录
    Then 新增名优特惠收货地址   #/api/user/receiver/update


  Scenario:名优特惠收货人列表展示
    When 手机个人端密码登录
    Then 名优特惠收货人列表    #/api/user/area/shippingList