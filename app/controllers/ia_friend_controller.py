from ..services.ia_friend_service import IA_FriendService
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

class IA_FriendController:
    def create_ia_friend(self):
        user = get_jwt_identity()
        data = request.get_json()
        try:
            ia_friend = IA_FriendService.create_ia_friend(
                name=data['name'],
                sex_ia=data['sex_ia'],
                age_average=data['age_average'],
                user_id=user
            )
            return({"id":ia_friend.id, "name":ia_friend.name}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except KeyError as e:
            return jsonify({"error": f"Missing field: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": "Server error"}), 500 
        
    def update_ia_friend(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        data.pop('user_id',None)
        try:
            ia_friend = IA_FriendService.update_ia_friend(user_id, data)
            return jsonify({"id": ia_friend.id, "name": ia_friend.name}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Server error"}), 500
        
    def get_ia_friend(self):
        user_id = get_jwt_identity()
        try:
            ia_friend = IA_FriendService.get_ia_friend(user_id)
            ia_friend_data = {
            "id": ia_friend.id,
            "name": ia_friend.name,
            "sex_ia": ia_friend.sex_ia.name,
            "age_average": ia_friend.age_average,
            "user_id": ia_friend.user_id
            }
            return jsonify(ia_friend_data), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return jsonify({"error": "Server error"}), 500


