from flask import current_app, jsonify
from ....extensions import sql
from ....models.questions import Questions

def api_admin_fetch_all_questions():
    try:
        questions = Questions.query.order_by(Questions.date.desc()).all()
        formatted_questions = []

        if questions:
            for question in questions:
                formatted_questions.append({
                    'id': question.id,
                    'date': question.date.strftime("%Y-%m-%d %H:%M:%S"),
                    'question': question.question,
                    'answer': question.answer,
                    'hidden': question.hidden,
                    'ip_address': question.ip_address
                })
                    
        if formatted_questions == []:
            return jsonify(message='No questions yet!'), 200
                    
        return jsonify(formatted_questions), 200

    except Exception as e:
        current_app.logger.error(f"An error occured inside asklvkaszus/actions/rest/admin/fetch_all_questions module: {e}")

        return jsonify(error='An error occurred while fetching questions list! Try again later.'), 500
            
    finally:
        sql.session.close()