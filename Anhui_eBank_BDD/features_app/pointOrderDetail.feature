Feature: 安徽社区个人端我的买单订单列表/详情

  Scenario: 我的买单订单列表展示
    When 手机个人端密码登录       ##需要新生成么？
    Then 我的订单_我的买单     #/api/user/myorder/qrcode_list
    Then 我的订单_我的买单_待付款      #接口同上，使用不同参数来进行筛选
    Then 我的订单_我的买单_待评价


  Scenario: 我的买单订单详情页
    When 手机个人端密码登录       ##需要新生成么？
    Then 我的订单_我的买单     #/api/user/myorder/qrcode_list
    Then 买单订单详情页      #/api/user/myorder/qrcode_detail    进入任一订单