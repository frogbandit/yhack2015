from flask import Flask, jsonify, render_template, request, json
import requests, random, urllib2

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", api_data='')

# @app.route('/search', methods=['GET','POST'])
# def search():
#     locations = []
#     location1 = request.form['l1']
#     r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+location1+"&key=AIzaSyC-V_7-ahl7rPf9iJWWQ4lFPPmqhzQNjzU")
#     l1 = r.json()
#     location1 = {'address': l1['results'][0]['formatted_address'], 'lat': l1['results'][0]['geometry']['location']['lat'], 'lng': l1['results'][0]['geometry']['location']['lng']}
#     locations.append(location1)
#     location2 = request.form['l2']
#     r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+location2+"&key=AIzaSyC-V_7-ahl7rPf9iJWWQ4lFPPmqhzQNjzU")
#     l2 = r.json()
#     location1 = {'address': l2['results'][0]['formatted_address'], 'lat': l2['results'][0]['geometry']['location']['lat'], 'lng': l2['results'][0]['geometry']['location']['lng']}
#     locations.append(location1)
#     location3 = request.form['l3']
#     r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+location3+"&key=AIzaSyC-V_7-ahl7rPf9iJWWQ4lFPPmqhzQNjzU")
#     l3 = r.json()
#     location1 = {'address': l3['results'][0]['formatted_address'], 'lat': l3['results'][0]['geometry']['location']['lat'], 'lng': l3['results'][0]['geometry']['location']['lng']}
#     locations.append(location1)
#     location4 = request.form['l4']
#     r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+location4+"&key=AIzaSyC-V_7-ahl7rPf9iJWWQ4lFPPmqhzQNjzU")
#     l4 = r.json()
#     location1 = {'address': l4['results'][0]['formatted_address'], 'lat': l4['results'][0]['geometry']['location']['lat'], 'lng': l4['results'][0]['geometry']['location']['lng']}
#     locations.append(location1)

#     print locations 
#     return render_template("index.html", api_data=locations)

if __name__ == '__main__':
	app.run(host='0.0.0.0')