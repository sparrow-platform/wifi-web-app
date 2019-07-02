#This dummy API to test if app works


from flask import Flask, session, render_template, make_response, jsonify, request, send_from_directory, g, url_for
from flask_cors import CORS

app = Flask(
    __name__
)

CORS(app)


@app.route('/send', methods = ['POST'])
def handleMessageReceived():
    print(request)
    data = request.form['data']
    print(data)
    return "Success"


@app.route('/receive', methods = ['GET'])
def getMessages():
    #DummyData
    val1 = {"key":"sparrow_sparrow:dfad_1562021354341","userID":"sparrow","timeStamp":1562021354341,"destination":"sparrow:jay","message":"one "}
    val2 = {"key":"sparrow_sparrow:dfad_1562021354390","userID":"sparrow","timeStamp":1562021354390,"destination":"sparrow:jay","message":"two "}
    val3 = {"key":"sparrow_sparrow:dfad_1562021352332","userID":"sparrow","timeStamp":1562021352332,"destination":"sparrow:jay","message":"three "}
    val4 = {"key":"sparrow_sparrow:dfad_1562021352532","userID":"sparrow","timeStamp":1562021352532,"destination":"sparrow:jay2","message":"four "}
    data = [val1, val2, val3, val4]
    return jsonify(data)

if __name__ == '__main__':
    app.run()



