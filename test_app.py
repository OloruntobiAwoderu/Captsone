import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from database.models import setup_db, db_drop_and_create_all, Actor, Movie, Performance, db_drop_and_create_all
from config import bearer_tokens, database_credentials
from sqlalchemy import desc
from datetime import date


casting_assistant_auth_header = {
    'Authorization': bearer_tokens['casting_assistant']
}

casting_director_auth_header = {
    'Authorization': bearer_tokens['casting_director']
}

executive_producer_auth_header = {
    'Authorization': bearer_tokens['executive_producer']
}


class AgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ.get('DATABASE_URL', "postgres://{}:{}@{}/{}".format(database_credentials["username"], database_credentials["password"], database_credentials["port"], database_credentials["development_database"]))

        setup_db(self.app, self.database_path)
        db_drop_and_create_all()
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_post_new_actor(self):
        json_create_actor = {
            'name': 'Crisso',
            'age': 25
        }

        res = self.client().post('/actors', json=json_create_actor,
                                 headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['created'], 2)

    def test_error_401_new_actor(self):
        json_create_actor = {
            'name': 'Crisso',
            'age': 25
        }

        res = self.client().post('/actors', json=json_create_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Expects Authorization Header')

    def test_error_422_post_new_actor(self):
        json_create_actor_without_name = {
            'age': 25
        }

        res = self.client().post('/actors', json=json_create_actor_without_name,
                                 headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'no name provided.')

    def test_get_all_actors(self):
        res = self.client().get('/actors?page=1', headers=casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

    def test_error_401_get_all_actors(self):
        res = self.client().get('/actors?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Expects Authorization Header')

    def test_error_404_get_actors(self):
        res = self.client().get('/actors?page=1125125125',
                                headers=casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'no actors found in database.')

#----------------------------------------------------------------------------#
# Tests for /actors PATCH
#----------------------------------------------------------------------------#

    def test_patch_actor(self):
        json_edit_actor_with_new_age = {
            'age': 30
        }
        res = self.client().patch('/actors/1', json=json_edit_actor_with_new_age,
                                  headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actor']) > 0)
        self.assertEqual(data['updated'], 1)

    def test_error_400_patch_actor(self):
        res = self.client().patch('/actors/123412', headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(
            data['message'], 'request does not contain a valid JSON body.')

    def test_error_404_patch_actor(self):
        json_edit_actor_with_new_age = {
            'age': 30
        }
        res = self.client().patch('/actors/123412', json=json_edit_actor_with_new_age,
                                  headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(
            data['message'], 'Actor with id 123412 not found in database.')

#----------------------------------------------------------------------------#
# Tests for /actors DELETE
#----------------------------------------------------------------------------#

    def test_error_401_delete_actor(self):
        res = self.client().delete('/actors/1', headers=casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permissions not found')

    def test_error_403_delete_actor(self):
        res = self.client().delete('/actors/1', headers=casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permissions not found')

    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], '1')

    def test_error_404_delete_actor(self):
        res = self.client().delete('/actors/15125', headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(
            data['message'], 'Actor with id 15125 not found in database.')

#----------------------------------------------------------------------------#
# Tests for /movies POST
#----------------------------------------------------------------------------#

    def test_post_new_movie(self):
        json_create_movie = {
            'title': 'Crisso Movie',
            'release_date': date.today()
        }

        res = self.client().post('/movies', json=json_create_movie,
                                 headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['created'], 2)

    def test_error_422_post_new_movie(self):
        json_create_movie_without_name = {
            'release_date': date.today()
        }

        res = self.client().post('/movies', json=json_create_movie_without_name,
                                 headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'no title provided.')

#----------------------------------------------------------------------------#
# Tests for /movies GET
#----------------------------------------------------------------------------#

    def test_get_all_movies(self):
        res = self.client().get('/movies?page=1', headers=casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) > 0)

    def test_error_401_get_all_movies(self):
        res = self.client().get('/movies?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Expects Authorization Header')

    def test_error_404_get_movies(self):
        res = self.client().get('/movies?page=1125125125',
                                headers=casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'no movies found in database.')

#----------------------------------------------------------------------------#
# Tests for /movies PATCH
#----------------------------------------------------------------------------#

    def test_patch_movie(self):
        json_edit_movie = {
            'release_date': date.today()
        }
        res = self.client().patch('/movies/1', json=json_edit_movie,
                                  headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movie']) > 0)

    def test_error_400_patch_movie(self):
  
  
        res = self.client().patch('/movies/1', headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(
            data['message'], 'request does not contain a valid JSON body.')

    def test_error_404_patch_movie(self):
        json_edit_movie = {
            'release_date': date.today()
        }
        res = self.client().patch('/movies/123412', json=json_edit_movie,
                                  headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(
            data['message'], 'Movie with id 123412 not found in database.')

#----------------------------------------------------------------------------#
# Tests for /movies DELETE
#----------------------------------------------------------------------------#

    def test_error_401_delete_movie(self):
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Expects Authorization Header')

    def test_error_403_delete_movie(self):
        res = self.client().delete('/movies/1', headers=casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permissions not found')

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], '1')

    def test_error_404_delete_movie(self):
        res = self.client().delete('/movies/151251', headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(
            data['message'], 'Movie with id 151251 not found in database.')



if __name__ == "__main__":
    unittest.main()
