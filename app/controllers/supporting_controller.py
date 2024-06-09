from ..services.supporting_service import SupportingTalkService
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from datetime import datetime

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
        
    def get_supportingTalks(self):
        user_id = get_jwt_identity()
        date_str = request.args.get('date')
        if not date_str:
            return jsonify({"error": "Date header is missing"}), 400

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            supporting_talks = SupportingTalkService.get_supporting_talks(user_id, date)
            supporting_talks_data = {
                "id": supporting_talks.id,
                "message": supporting_talks.message,
                "created_on": supporting_talks.created_on,
                "updated_on": supporting_talks.updated_on,
                "user_id": supporting_talks.user_id
            }
            return jsonify(supporting_talks_data), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return jsonify({"error": "Server error"}), 500
