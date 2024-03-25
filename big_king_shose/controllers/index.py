from flask import render_template, request, redirect, url_for, Blueprint
from services.index import ShoseService
from flask import jsonify

shose_blueprint = Blueprint('shose', __name__)
shose_service = ShoseService()

@shose_blueprint.route('/')
def index():
    return 

@shose_blueprint.route('/get_store', methods=['GET'])
def get_store():
    return

@shose_blueprint.route('/post_store', methods=['POST'])
def post_store():
    return

@shose_blueprint.route('/get_shose', methods=['GET'])
def get_shose():
    # 모든 신발 정보를 가져오는 함수 호출
    shoes = shose_service.get_shose()
    
    # JSON 형태로 변환하여 반환
    return jsonify(shoes)

@shose_blueprint.route('/post_shose', methods=['POST'])
def post_shoes(): 
    return

@shose_blueprint.route('/get_inventory', methods=['GET'])
def get_inventory():
    response = shose_service.getInventory()
    return jsonify(response)

@shose_blueprint.route('/post_inventory', methods=['POST'])
def post_inventory():
    # 클라이언트로부터 신발 정보를 받아오기
    shoe_name = 3
    brand = 3
    size = 10
    quantity = 10
    
    # 받아온 정보를 이용하여 Inventory 테이블에 데이터 삽입
    shose_service.insert_shoe(shoe_name, brand, size, quantity)
    
    return 'Inventory added successfully.'  # 성공 메시지 반환


@shose_blueprint.route('/post_discount', methods=['PUT'])
def post_discount():  # 이 함수는 재고를 감소시키는 기능을 담당합니다.
    shose_service.decrease_inventory(1, 2, 8)  # 예시로 shoe_id가 1, store_id가 2, size가 8인 신발의 재고를 감소시킵니다.
    return 'Inventory decreased successfully.'  # 적절한 응답을 반환하세요.

@shose_blueprint.route('/post_increase', methods=['POST'])
def post_increase():
    shoe_id = 1  # 폼에서 신발 ID를 가져옵니다.
    store_id = 2  # 폼에서 매장 ID를 가져옵니다.
    size = 8  # 폼에서 사이즈를 가져옵니다.
    increase_amount = 10  # 폼에서 추가할 수량을 가져옵니다.
    
    # 가져온 값들을 이용하여 신발의 재고를 증가시킵니다.
    shose_service.increase_inventory(shoe_id, store_id, size, increase_amount)
    
    return 'Inventory increased successfully.'  # 적절한 응답을 반환합니다.