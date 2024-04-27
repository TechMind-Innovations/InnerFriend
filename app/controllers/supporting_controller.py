from ..services.supporting_service import SupportingTalkService
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

class SupportingTalkController:
    def create_supporting_talks(self):
        data = request.get_json()
        user = get_jwt_identity()
        try:
            supporting_talk = SupportingTalkService.create_supporting_talk(
                message=data['message'],
                user_id=user
            )
            return({"id":supporting_talk.id, "message":supporting_talk.message}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except KeyError as e:
            return jsonify({"error": f"Missing field: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": "Server error"}), 500
        
    def update_supporting_talks(self):
        id = request.args.get('id')
        data = request.get_json()
        data.pop('user_id',None)
        try:
            supporting_talks = SupportingTalkService.update_supporting_talks(id, data)
            return jsonify({"id": supporting_talks.id, "message": supporting_talks.message}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Server error"}), 500