from flask_restful import  abort, Api, Resource
from data.news import News
from data import db_session
from flask import jsonify


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(News).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")



class NewsResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        return jsonify({'news': news.to_dict(
            only=('title', 'content', 'user_id', 'is_private'))})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})





class NewsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(News).all()
        return jsonify({'news': [item.to_dict(
            only=('title', 'content', 'user.name')) for item in news]})

    def post(self):
        print("lol")
        parser = reqparse.RequestParser()
        session = db_session.create_session()

        parser.add_argument('title', required=True)
        parser.add_argument('surname', required=True)
        parser.add_argument('age', required=True, type=int)


        news = News(
            title=parser['title'],
            content=parser['content'],
            user_id=parser['user_id'],
            is_private=parser['is_private']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})

