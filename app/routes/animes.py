from flask import Blueprint, request
import psycopg2
from app.controllers.controllers import delete_one, update_anime
from app.exceptions.exceptions import AnimeNotFound, InvalidKeys


from app.models import Anime


bp_animes = Blueprint('anime', __name__, url_prefix='/animes')

@bp_animes.route('', methods=['GET', 'POST'])
def get_create():
    data = request.get_json()
    if request.method == 'POST': 
        
        try:
            Anime.check_data(data)
            create = Anime(**data)
            return create.create_anime(),201
        except psycopg2.errors.UniqueViolation:
            return {'error': 'anime already exists'},409
        except InvalidKeys as error:
            return (*error.args, 422)
    
    else:
        return Anime.get_all_animes()
    
@bp_animes.get('/<int:anime_id>')
def filter(anime_id):
        
    try:
        return Anime.get_one_anime(anime_id),200
    except AnimeNotFound as error:
        return(*error.args, 404)


@bp_animes.patch('/<int:anime_id>')
def update(anime_id):
    data = request.get_json()
        
    try:
        Anime.check_data(data)
        return  update_anime(data,anime_id),200
    except AnimeNotFound as error:
        return(*error.args, 404)


@bp_animes.delete('/<int:anime_id>')
def delete(anime_id):
        
    try:
        return  delete_one(anime_id),204
    except AnimeNotFound as error:
        return(*error.args, 404)