from ..services.resuming_service import ResumingTalkService
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

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