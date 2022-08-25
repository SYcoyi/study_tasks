"""
百度鉴权仿写--生成鉴权
"""
import falcon
import hug


@hug.post("/oauth/2.0/token", output=hug.output_format.json)
@hug.get("/oauth/2.0/token", output=hug.output_format.json)    # 这个方法既支持get 又支持post，output中锁定了返回为json类型
def get_oauth_token(client_id, client_secret, grant_type):
    magic_client_secret = "78SJFSF9SFAFSDFF08S"
    magic_client_id = "SDF98SDFSD9SADF"
    if client_id == magic_client_id and client_secret == magic_client_secret and grant_type == "client_credentials":
        return {
            "refresh_token": "456.3464dfsf.werwe25.464613213",
            "expires_in": 259200,
            "scope": "public wise_adapt",
            "session_key": "24OUOUSF4646SFSDFASAGAGSAF45A4SFSAFSA54F6SA4F64S6A4FA",
            "access_token": "54646798.4646.4679687.45464sfsfsf",
            "session_secret": "5476416werwerwe46s4dfsdfsd5fs"
        }
    elif client_secret != magic_client_secret:
        return {
            "error": "invalid client_secret",
            "error_description": "Client authentication failed"
        }
    else:
        return None


@hug.post("/text2audio")
@hug.get("/text2audio")
def text2audio(body, response):
    access_token = body.get('tok')
    if access_token != "54646798.4646.4679687.45464sfsfsf":
        response.status = falcon.HTTP_502
        return {"err_no": 502, "err_msg": "Not Support", "sn": "sfsafsaf", "idx": 1}
    elif (body.get('tex') and body.get('cuid') and body.get('ctp') and body.get('lan')) is None:
        response.status = falcon.HTTP_501
        return {"err_no": 501, "err_msg": "input params incorrect", "sn": "sfsafsaf", "idx": 2}
    elif len(body['tex']) > 2048 or len(body['cuid']) > 60 or body['ctp'] != '1' or body['lan'] != 'zh':
        response.status = falcon.HTTP_501
        return {"err_no": 501, "err_msg": "input params incorrect", "sn": "sfsafsaf", "idx": 2}
    else:
        response.status = falcon.HTTP_200
        return "success"


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)



