# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Path to the invitation image
    invitation_image_path = '/static/invitation.png'  # Update with your invitation image path
    
    # Link to the Google Maps location (Church)
    church_map_link = 'https://maps.app.goo.gl/K74ujwk28JwJv4QW6'
    
    # Link to the Google Maps location (Reception)
    reception_map_link = 'https://maps.app.goo.gl/s9hChbe9baJsEVNS7'
    
    return render_template('index.html', 
                           invitation_image_path=invitation_image_path,
                           church_map_link=church_map_link,
                           reception_map_link=reception_map_link)

if __name__ == '__main__':
    app.run(debug=True)
