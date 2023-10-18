from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from usecase.en_to_esl import get_prediction, create_video
from constants import *

def test(request):
    return Response(json={"message": "API deployment successful!"})

def english_to_esl(request):
    english_sentence = request.json_body.get("english_sentence")
    print("Waiting for response:", english_sentence)

    # Perform your English to ESL conversion here
    # Replace the following lines with your actual logic
    prediction = "The american army is Angry"
    output = get_prediction(prediction)
    print(create_video(output))

    return Response(json={"video_path": "bruh.mp4"})

if __name__ == "__main__":
    config = Configurator()
    config.add_route("test", "/test")
    config.add_view(test, route_name="test", renderer="json")

    config.add_route("predict", "/predict")
    config.add_view(english_to_esl, route_name="predict", renderer="json", request_method="POST")

    app = config.make_wsgi_app()
    server = make_server(HOST, PORT, app)
    server.serve_forever()