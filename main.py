from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)

@app.route('/get_profile_pic', methods=['GET'])
def get_profile_pic():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Initialize Instaloader instance
    loader = instaloader.Instaloader()
    
    try:
        # Load the Instagram profile
        profile = instaloader.Profile.from_username(loader.context, username)
        # Get the URL of the profile picture
        profile_pic_url = profile.profile_pic_url
        
        return jsonify({"profile_pic_url": profile_pic_url})
    
    except instaloader.exceptions.InstaloaderException as e:
        return jsonify({"error": "Could not fetch profile picture. " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
