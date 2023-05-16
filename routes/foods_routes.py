from flask import Blueprint
from controllers.foods_controller import index, new, create, edit, update, delete

foods_routes = Blueprint('foods_routes', __name__)

foods_routes.route('/')(index)
foods_routes.route('/foods/new')(new)
foods_routes.route('/foods', methods=['POST'])(create)
foods_routes.route('/foods/<id>/edit')(edit)
foods_routes.route('/foods/<id>', methods=["POST"])(update)
foods_routes.route('/foods/<id>/delete', methods=["POST"])(delete)