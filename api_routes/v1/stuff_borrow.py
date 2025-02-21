from flask import jsonify,request # type: ignore
from . import api_v1

#统计借物总数
@api_v1.route('/stuff-borrow/statistic',methods=['GET'])
def get_borrow_statistic():
    return jsonify({"message":"Get all borrow records"})

#删除某条特定的借物申请
@api_v1.route('/stuff-borrow/<str:sb_id>',methods=['DELETE'])
def delete_stuff_borrow(sb_id):
    return jsonify({"message":f"Cancel booking {sb_id}"}),204

#获取用户的借物历史
@api_v1.route('/stuff-borrow/user/<str:userid>/history',methods=['GET'])
def get_borrow_history(userid):
    page=request.args.get('page',1,type=int)
    size=request.args.get('size',10,type=int)
    return jsonify({"message":f"Get {userid} borrow history"})

#更新某一条借物申请
@api_v1.route('/stuff-borrow/<str:sb_id>',methods=['PUT'])
def update_borrow_request(sb_id):
    data=request.get_json()
    return jsonify({"message":f"Update {sb_id} borrow request","data":data}),200

#获取某条借物申请条目
@api_v1.route('/stuff-borrow/<str:sb_id>',methods=['GET'])
def get_borrow_request(sb_id):
    return jsonify({"message":f"Get {sb_id} borrow request"})

#获取借物总表
@api_v1.route('/stuff-borrow',methods=['GET'])
def get_borrow_record():
    page=request.args.get('page',1,type=int)
    size=request.args.get('size',10,type=int)
    state=request.args.get('state',None,type=int)
    return jsonify({"message":"Get borrow record"})

#获取某个用户的借物总表
@api_v1.route('/stuff-borrow/user/<str:userid>',methods=['GET'])
def get_user_borrow_record():
    page=request.args.get('page',1,type=int)
    size=request.args.get('size',10,type=int)
    state=request.args.get('state',None,type=int)
    return jsonify({"message":"Get user borrow record"})

#增加一条借物申请条目
@api_v1.route('/stuff-borrow',methods=['POST'])
def create_borrow_request():
    data=request.get_json()
    return jsonify({"message":"Successful application","data":data}),200
    