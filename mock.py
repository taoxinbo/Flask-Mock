from flask import Flask, jsonify, request, make_response

app = Flask(__name__)


@app.route('/api/login/', methods=['GET', 'POST'])
def create_task():
    if request.method == "POST":
        data = {"payload": {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mbyI6eyJhY2NvdW50SWQiOiIyODY3IiwiZW50ZXJwcmlzZUNvZGUiOiJkYWFzdGVzdCIsInRlbmFudElkIjoiOTg1ZTAyOTg3MGJhNDczOTk5MzNhNmJmNWUwOGViM2QiLCJ1c2VySWQiOiIxMDc1OSIsInVzZXJuYW1lIjoieGlld2VuaHVpIn0sImlhbVR5cGUiOiJjbGllbnQiLCJ1c2VyX25hbWUiOiJ4aWV3ZW5odWkiLCJzY29wZSI6WyJhbGwiXSwiZXhwIjoxNjI1MDYzNzE4LCJqdGkiOiIzZmFkZDZhMi04N2QwLTQyZjktOGY5ZC04NWUxNzY1MWFiNDIiLCJjbGllbnRfaWQiOiJkZWVwZXhpIn0.kERmncFGAqqotv47eLBAvypHCayaElQgHJm3OUu-aOk",
            "token_type": "bearer",
            "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mbyI6eyJhY2NvdW50SWQiOiIyODY3IiwiZW50ZXJwcmlzZUNvZGUiOiJkYWFzdGVzdCIsInRlbmFudElkIjoiOTg1ZTAyOTg3MGJhNDczOTk5MzNhNmJmNWUwOGViM2QiLCJ1c2VySWQiOiIxMDc1OSIsInVzZXJuYW1lIjoieGlld2VuaHVpIn0sImlhbVR5cGUiOiJjbGllbnQiLCJ1c2VyX25hbWUiOiJ4aWV3ZW5odWkiLCJzY29wZSI6WyJhbGwiXSwiYXRpIjoiM2ZhZGQ2YTItODdkMC00MmY5LThmOWQtODVlMTc2NTFhYjQyIiwiZXhwIjoxNjI1NjY4NTE4LCJqdGkiOiJkZjJiNGUzMS01ZDllLTQxOTgtYjVlYS0yNWYzZDAzNTk2NTIiLCJjbGllbnRfaWQiOiJkZWVwZXhpIn0.qO5X_QrnOeUC1w2mDTUJoaMvmy7L9XwnhbVWFyn0E9M",
            "expires_in": 43200, "scope": "all", "userInfo": {"accountId": "2867", "enterpriseCode": "daastest",
                                                              "tenantId": "985e029870ba47399933a6bf5e08eb3d",
                                                              "userId": "10759", "username": "luren3"},
            "iamType": "client", "jti": "3fadd6a2-87d0-42f9-8f9d-85e17651ab42"}, "code": "0", "msg": "ok"}
        return make_response(jsonify(data), 200)
    else:
        data = {"payload": {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mbyI6eyJhY2NvdW50SWQiOiIyODY3IiwiZW50ZXJwcmlzZUNvZGUiOiJkYWFzdGVzdCIsInRlbmFudElkIjoiOTg1ZTAyOTg3MGJhNDczOTk5MzNhNmJmNWUwOGViM2QiLCJ1c2VySWQiOiIxMDc1OSIsInVzZXJuYW1lIjoieGlld2VuaHVpIn0sImlhbVR5cGUiOiJjbGllbnQiLCJ1c2VyX25hbWUiOiJ4aWV3ZW5odWkiLCJzY29wZSI6WyJhbGwiXSwiZXhwIjoxNjI1MDYzNzE4LCJqdGkiOiIzZmFkZDZhMi04N2QwLTQyZjktOGY5ZC04NWUxNzY1MWFiNDIiLCJjbGllbnRfaWQiOiJkZWVwZXhpIn0.kERmncFGAqqotv47eLBAvypHCayaElQgHJm3OUu-aOk",
            "token_type": "bearer",
            "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mbyI6eyJhY2NvdW50SWQiOiIyODY3IiwiZW50ZXJwcmlzZUNvZGUiOiJkYWFzdGVzdCIsInRlbmFudElkIjoiOTg1ZTAyOTg3MGJhNDczOTk5MzNhNmJmNWUwOGViM2QiLCJ1c2VySWQiOiIxMDc1OSIsInVzZXJuYW1lIjoieGlld2VuaHVpIn0sImlhbVR5cGUiOiJjbGllbnQiLCJ1c2VyX25hbWUiOiJ4aWV3ZW5odWkiLCJzY29wZSI6WyJhbGwiXSwiYXRpIjoiM2ZhZGQ2YTItODdkMC00MmY5LThmOWQtODVlMTc2NTFhYjQyIiwiZXhwIjoxNjI1NjY4NTE4LCJqdGkiOiJkZjJiNGUzMS01ZDllLTQxOTgtYjVlYS0yNWYzZDAzNTk2NTIiLCJjbGllbnRfaWQiOiJkZWVwZXhpIn0.qO5X_QrnOeUC1w2mDTUJoaMvmy7L9XwnhbVWFyn0E9M",
            "expires_in": 43200, "scope": "all", "userInfo": {"accountId": "2867", "enterpriseCode": "daastest",
                                                              "tenantId": "985e029870ba47399933a6bf5e08eb3d",
                                                              "userId": "10759", "username": "luren3"},
            "iamType": "client", "jti": "3fadd6a2-87d0-42f9-8f9d-85e17651ab42"}, "code": "0", "msg": "ok"}
    # 返回参数
    return make_response(jsonify(data), 200)


# 这个接口请求地址就是   http://127.0.0.1:8000/task/search， 支持的请求方式为 get、post
@app.route('/task/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":

        # data 就是想要返回的参数
        data = {"payload": {"totalElements": 17, "content": [
            {"id": "1409442994448281653", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 2975,
             "isDeleted": False,
             "createdBy": "daastest", "createdTime": "2021-06-28 17:26:11", "updatedBy": "",
             "updatedTime": "2021-06-29 00:00:00", "taskType": 0, "relType": 1, "datasourceType": "sqlserver",
             "datasourceId": "1394557645356052514", "collectPeriod": 0, "status": 6, "timeConsuming": 1170,
             "executedTime": "1625050074000", "message": None, "messageDetail": None,
             "datasourceName": "run_history_sqlServer"},
            {"id": "1409439747377508421", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 17,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-28 17:13:17", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 17:25:07", "taskType": 1, "relType": 1, "datasourceType": "mysql",
             "datasourceId": "1409431170558504972", "collectPeriod": 4, "status": 4, "timeConsuming": 424,
             "executedTime": "1624872311000", "message": None, "messageDetail": None,
             "datasourceName": "cz_test_mysql"},
            {"id": "1409418809084784656", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 0,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-28 15:50:04", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 15:50:04", "taskType": 1, "relType": 1, "datasourceType": "postgresql",
             "datasourceId": "1379995903267479587", "collectPeriod": 4, "status": 0, "timeConsuming": None,
             "executedTime": None, "message": None, "messageDetail": None, "datasourceName": "postgresql_test"},
            {"id": "1409358010693759036", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 8,
             "isDeleted": False, "createdBy": "xiongmin", "createdTime": "2021-06-28 11:48:29", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 15:31:25", "taskType": 1, "relType": 1, "datasourceType": "mysql",
             "datasourceId": "1379998963679141957", "collectPeriod": 4, "status": 0, "timeConsuming": 1047,
             "executedTime": "1624863490000", "message": None, "messageDetail": None, "datasourceName": "service_test"},
            {"id": "1408320014737518614", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 7322,
             "isDeleted": False, "createdBy": "xiongmin", "createdTime": "2021-06-25 15:03:51", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 14:41:36", "taskType": 0, "relType": 1, "datasourceType": "kudu",
             "datasourceId": "1399273514602639407", "collectPeriod": 0, "status": 6, "timeConsuming": 330,
             "executedTime": "1624636800000", "message": None, "messageDetail": None,
             "datasourceName": "kudu_dev_kerberos_1"},
            {"id": "1408039445621420037", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 64,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-24 20:28:59", "updatedBy": "",
             "updatedTime": "2021-06-30 19:03:00", "taskType": 0, "relType": 1, "datasourceType": "clickhouse",
             "datasourceId": "1385532218310434839", "collectPeriod": 0, "status": 4, "timeConsuming": 617,
             "executedTime": "1625050980000", "message": None, "messageDetail": None, "datasourceName": "clickhouse2"},
            {"id": "1408030166751424585", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 12,
             "isDeleted": False, "createdBy": "xiongmin", "createdTime": "2021-06-24 19:52:06", "updatedBy": "xiongmin",
             "updatedTime": "2021-06-24 19:52:06", "taskType": 1, "relType": 1, "datasourceType": "mysql",
             "datasourceId": "1381501791220310016", "collectPeriod": 4, "status": 4, "timeConsuming": 4230,
             "executedTime": "1624949791000", "message": None, "messageDetail": None, "datasourceName": "cw_sales"},
            {"id": "1407993386727682060", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 10,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-24 17:25:57", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 15:59:17", "taskType": 1, "relType": 1, "datasourceType": "postgresql",
             "datasourceId": "1384074382552375379", "collectPeriod": 4, "status": 4, "timeConsuming": 597,
             "executedTime": "1624936641000", "message": None, "messageDetail": None, "datasourceName": "postgresql"},
            {"id": "1407985078872617023", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 8769,
             "isDeleted": False, "createdBy": "xiongmin", "createdTime": "2021-06-24 16:52:57", "updatedBy": "xiongmin",
             "updatedTime": "2021-06-26 17:15:45", "taskType": 0, "relType": 1, "datasourceType": "hive",
             "datasourceId": "1407602233842905136", "collectPeriod": 0, "status": 6, "timeConsuming": 6413,
             "executedTime": "1624698926000", "message": None, "messageDetail": None, "datasourceName": "删除测试"},
            {"id": "1407965937176457298", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 53,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-24 15:36:53", "updatedBy": "daastest",
             "updatedTime": "2021-06-29 11:18:49", "taskType": 1, "relType": 1, "datasourceType": "postgresql",
             "datasourceId": "1392367204250464269", "collectPeriod": 4, "status": 4, "timeConsuming": 920,
             "executedTime": "1625051836000", "message": None, "messageDetail": None,
             "datasourceName": "postgresql_zz"}]
            , "number": 1, "size": 10, "totalPages": 2, "numberOfElements": 10}, "code": "0", "msg": "ok"}

        # 200就是接口返回的状态码
        return make_response(jsonify(data), 200)
    else:
        data = {"payload": {"totalElements": 17, "content": [
            {"id": "1409442994448281653", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 2975,
             "isDeleted": False,
             "createdBy": "daastest", "createdTime": "2021-06-28 17:26:11", "updatedBy": "",
             "updatedTime": "2021-06-29 00:00:00", "taskType": 0, "relType": 1, "datasourceType": "sqlserver",
             "datasourceId": "1394557645356052514", "collectPeriod": 0, "status": 6, "timeConsuming": 1170,
             "executedTime": "1625050074000", "message": None, "messageDetail": None,
             "datasourceName": "run_history_sqlServer"},
            {"id": "1409439747377508421", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 17,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-28 17:13:17", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 17:25:07", "taskType": 1, "relType": 1, "datasourceType": "mysql",
             "datasourceId": "1409431170558504972", "collectPeriod": 4, "status": 4, "timeConsuming": 424,
             "executedTime": "1624872311000", "message": None, "messageDetail": None,
             "datasourceName": "cz_test_mysql"},
            {"id": "1409418809084784656", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 0,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-28 15:50:04", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 15:50:04", "taskType": 1, "relType": 1, "datasourceType": "postgresql",
             "datasourceId": "1379995903267479587", "collectPeriod": 4, "status": 0, "timeConsuming": None,
             "executedTime": None, "message": None, "messageDetail": None, "datasourceName": "postgresql_test"},
            {"id": "1409358010693759036", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 8,
             "isDeleted": False, "createdBy": "xiongmin", "createdTime": "2021-06-28 11:48:29", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 15:31:25", "taskType": 1, "relType": 1, "datasourceType": "mysql",
             "datasourceId": "1379998963679141957", "collectPeriod": 4, "status": 0, "timeConsuming": 1047,
             "executedTime": "1624863490000", "message": None, "messageDetail": None, "datasourceName": "service_test"},
            {"id": "1408320014737518614", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 7322,
             "isDeleted": False, "createdBy": "xiongmin", "createdTime": "2021-06-25 15:03:51", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 14:41:36", "taskType": 0, "relType": 1, "datasourceType": "kudu",
             "datasourceId": "1399273514602639407", "collectPeriod": 0, "status": 6, "timeConsuming": 330,
             "executedTime": "1624636800000", "message": None, "messageDetail": None,
             "datasourceName": "kudu_dev_kerberos_1"},
            {"id": "1408039445621420037", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 64,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-24 20:28:59", "updatedBy": "",
             "updatedTime": "2021-06-30 19:03:00", "taskType": 0, "relType": 1, "datasourceType": "clickhouse",
             "datasourceId": "1385532218310434839", "collectPeriod": 0, "status": 4, "timeConsuming": 617,
             "executedTime": "1625050980000", "message": None, "messageDetail": None, "datasourceName": "clickhouse2"},
            {"id": "1408030166751424585", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 12,
             "isDeleted": False, "createdBy": "xiongmin", "createdTime": "2021-06-24 19:52:06", "updatedBy": "xiongmin",
             "updatedTime": "2021-06-24 19:52:06", "taskType": 1, "relType": 1, "datasourceType": "mysql",
             "datasourceId": "1381501791220310016", "collectPeriod": 4, "status": 4, "timeConsuming": 4230,
             "executedTime": "1624949791000", "message": None, "messageDetail": None, "datasourceName": "cw_sales"},
            {"id": "1407993386727682060", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 10,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-24 17:25:57", "updatedBy": "daastest",
             "updatedTime": "2021-06-28 15:59:17", "taskType": 1, "relType": 1, "datasourceType": "postgresql",
             "datasourceId": "1384074382552375379", "collectPeriod": 4, "status": 4, "timeConsuming": 597,
             "executedTime": "1624936641000", "message": None, "messageDetail": None, "datasourceName": "postgresql"},
            {"id": "1407985078872617023", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 8769,
             "isDeleted": False, "createdBy": "xiongmin", "createdTime": "2021-06-24 16:52:57", "updatedBy": "xiongmin",
             "updatedTime": "2021-06-26 17:15:45", "taskType": 0, "relType": 1, "datasourceType": "hive",
             "datasourceId": "1407602233842905136", "collectPeriod": 0, "status": 6, "timeConsuming": 6413,
             "executedTime": "1624698926000", "message": None, "messageDetail": None, "datasourceName": "删除测试"},
            {"id": "1407965937176457298", "tenantId": "985e029870ba47399933a6bf5e08eb3d", "version": 53,
             "isDeleted": False, "createdBy": "daastest", "createdTime": "2021-06-24 15:36:53", "updatedBy": "daastest",
             "updatedTime": "2021-06-29 11:18:49", "taskType": 1, "relType": 1, "datasourceType": "postgresql",
             "datasourceId": "1392367204250464269", "collectPeriod": 4, "status": 4, "timeConsuming": 920,
             "executedTime": "1625051836000", "message": None, "messageDetail": None,
             "datasourceName": "postgresql_zz"}]
            , "number": 1, "size": 10, "totalPages": 2, "numberOfElements": 10}, "code": "0", "msg": "ok"}
    return make_response(jsonify(data), 200)


# host 自定义接口地址， port 自定义端口
app.run(host='127.0.0.1', port=8000, debug=True)
