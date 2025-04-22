# coding=utf-8
from typing import Optional

from flask import Flask, jsonify, request

import config
from google_play_scraper import app
from google_play_scraper.utils.retry_decorator import retry_with_exponential_backoff

# 创建Flask应用
app_server = Flask(__name__)


@retry_with_exponential_backoff(max_retries=3, initial_delay=1.0, backoff_factor=2.0, max_delay=10)
def scraper_gp_app_info(app_id: str) -> Optional[dict]:
    try:
        app_info = app(app_id)
        if app_info:
            return app_info
        raise Exception("app info is None")
    except Exception as e:
        print(f"scraper_gp_app_info error: {e}")
        return None


@app_server.route('/api/app_info', methods=['GET'])
def get_app_info():
    app_id = request.args.get('app_id')

    if not app_id:
        return jsonify({
            'success': False,
            'error': 'Missing app_id parameter'
        }), 400

    result = scraper_gp_app_info(app_id)

    if result is None:
        return jsonify({
            'success': False,
            'error': f'Failed to fetch information for app: {app_id}'
        }), 404

    return jsonify({
        'success': True,
        'data': result
    })


@app_server.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        'success': False,
        'error': str(e)
    }), 500


if __name__ == '__main__':
    # 从配置中获取端口
    port = config.port
    app_server.run(host='0.0.0.0', port=port, debug=False)
