from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)


###########################################################
# CLIENT KAMERA - FUNGSI UPSTREAM
###########################################################

def upstream():
    @app.route('/')
    def index():
        # template streaming dari web untuk testing
        return render_template('index.html')

    def gen(camera):
        # konfersi nilai object untuk streaming
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    @app.route('/video_feed')
    def video_feed():
        # mengambil nilai balikan object VideoCamera untuk di stream
        return Response(gen(VideoCamera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # inisialisasi object yang akan di stream
    upstream()

    # melakukan streaming ke ip public client
    app.run(host='127.0.0.1', debug=True)
