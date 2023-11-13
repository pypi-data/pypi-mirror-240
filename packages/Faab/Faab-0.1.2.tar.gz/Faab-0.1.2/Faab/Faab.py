from flask_cors import *
from flask import request, redirect, url_for, render_template, Flask
from Faab.FaabJWT import jwt_authentication
# 自定义组件
# from utils.jupload import jcompress, is_image_file
# 模型注册
# from model.oldPlay import gas_users

# 初始化
from .factory import create_app

app = Flask(__name__)


def faab(models, db_config, run=None):
    apps = create_app(app, models, db_config)
    CORS(apps, resources=r'/*')
    print("""

                    ██╗   ██╗ ██████╗  ██████╗ ██████╗ ██╗████████╗ ██████╗███╗   ██╗    
                    ╚██╗ ██╔╝██╔═══██╗██╔═══██╗██╔══██╗██║╚══██╔══╝██╔════╝████╗  ██║    
                     ╚████╔╝ ██║   ██║██║   ██║██████╔╝██║   ██║   ██║     ██╔██╗ ██║    
                      ╚██╔╝  ██║   ██║██║   ██║██╔══██╗██║   ██║   ██║     ██║╚██╗██║    
                       ██║   ╚██████╔╝╚██████╔╝██████╔╝██║   ██║██╗╚██████╗██║ ╚████║    
                       ╚═╝    ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝   ╚═╝╚═╝ ╚═════╝╚═╝  ╚═══╝                                                          
                """)
    apps.run(debug=True, port=8011, host='0.0.0.0')


# class Faab:
#     self.app = app
#     def __init__(self, models, run):
#
#
#         # 通用API模块

@app.route('/admin/login', methods=['POST', 'GET'])
def logins():
    return render_template('admin/login.html')


@app.route('/admin/logins', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return redirect('/admin')
    else:
        user = request.args.get('txt')
        return redirect(url_for('success', name=user))


@app.before_request
def auth():
    jwt_authentication()
