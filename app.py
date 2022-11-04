from flask import Flask
import tensorflow as tf
import requests

app = Flask(__name__)

@app.route('/hello/<x>')
def hello_name(x):
    url = 'https://sentimentanalysis-s3bucket.s3.ap-south-1.amazonaws.com/my_model_new.h5/my_model_new.h5'
    r = requests.get(url, allow_redirects=True)
    open('model.h5', 'wb').write(r.content)

    new_model = tf.keras.models.load_model('model.h5')
    a = []
    a.append(float(x))
    y = new_model.predict(a)
    print(y)
    return str(y)

if __name__ == '__main__':
    app.run()