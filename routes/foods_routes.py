from flask import Blueprint
from controllers.foods_controller import index, new, create, edit, update, delete, like

foods_routes = Blueprint('foods_routes', __name__)

foods_routes.route('')(index)
foods_routes.route('/new')(new)
foods_routes.route('', methods=['POST'])(create)
foods_routes.route('/<id>/edit')(edit)
foods_routes.route('/<id>', methods=["POST"])(update)
foods_routes.route('/<id>/delete', methods=["POST"])(delete)
foods_routes.route('/<id>/likes', methods=["POST"])(like)