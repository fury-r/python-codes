from werkzeug.wrappers import request
from DS.DS_project.webapp.gameObject.ludo import Ludo, Player
from webapp import app
import requests
players={}
@app.route('/v1/send_player',methods=['POST'])
def get_player_info():
    data=request.json()
    players=['players']
    ludo=Ludo
    player=Player
    ludo_player=[]
@app.rout('/v1/start')
