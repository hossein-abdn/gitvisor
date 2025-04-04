from webapi.model import Repository
from webapi.util import jsonify


class RepositoryController:
    def get_repositories():
        return jsonify(state=501, code=101)

    def get_repository(repository_id):
        return jsonify(state=501, code=101)

    def create_repository():
        return jsonify(state=501, code=101)

    def update_repository(repository_id):
        return jsonify(state=501, code=101)

    def delete_repository(repository_id):
        return jsonify(state=501, code=101)
