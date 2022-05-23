Feature: 安徽社区个人端登录

  Scenario: 手机号验证码登录成功
    When 手机个人端登录获取验证码     ##/api/user/code/check_send_sms
    Then 手机个人端登录           #/api/user/login/mobileCheckLogin

  Scenario: 手机号密码登录成功
    When 手机个人端密码登录     #/api/user/login/login


  Scenario: 联合登录   ##待定
    When 已知手机银行信息
    Then 联合登录     ##/api/user/login/loginUnion