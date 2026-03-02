from quart import Blueprint
from app.routes import bp

@bp.route('/x', methods=['GET'])
async def x():
    return f"""
    <html>
    <head><style></style></head>
    <body></body>
    </html>
    """