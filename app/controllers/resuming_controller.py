from ..services.resuming_service import ResumingTalkService
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from datetime import datetime

class ResumingTalkController:
    def create_resuming_talks(self):
        data = request.get_json()
        user = get_jwt_identity()
        try:
            resuming_talk = ResumingTalkService.create_resuming_talk(
                message=data['message'],
                user_id=user
            )
            return({"id":resuming_talk.id, "message":resuming_talk.message}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except KeyError as e:
            return jsonify({"error": f"Missing field: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": "Server error"}), 500
        
    def update_resuming_talks(self):
        id = request.args.get('id')
        data = request.get_json()
        data.pop('user_id',None)
        try:
            resuming_talks = ResumingTalkService.update_resuming_talks(id, data)
            return jsonify({"id": resuming_talks.id, "message": resuming_talks.message}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Server error"}), 500
        
    def get_resumingTalks(self):
        user_id = get_jwt_identity()
        date_str = request.args.get('date')
        if not date_str:
            return jsonify({"error": "Date header is missing"}), 400
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            resumingTalks = ResumingTalkService.get_resuming_talks(user_id, date)
            resumingTalksData = {
                "id": resumingTalks.id,
                "message": resumingTalks.message,
                "created_on": resumingTalks.created_on,
                "updated_on": resumingTalks.updated_on,
                "user_id": resumingTalks.user_id
            }
            return jsonify(resumingTalksData), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return jsonify({"error": "Server error"}), 500
        
        
