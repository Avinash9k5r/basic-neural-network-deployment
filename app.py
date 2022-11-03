from flask import Flask
import tensorflow as tf

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):

    new_model = tf.keras.models.load_model('mymodel/')
    a = []
    a.append(int(name))
    pred = new_model.predict(a)
    print(pred)
    return str(pred)

if __name__ == '__main__':
    app.run()