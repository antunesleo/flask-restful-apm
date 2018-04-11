from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

app.config['ELASTIC_APM'] ={
    'SERVICE_NAME': 'ElasticBreno',
    'SECRET_TOKEN': 'BrEnO',
    'SERVER_URL': 'http://localhost:8200',
    'DEBUG': True,
}
apm = ElasticAPM(app, logging=True)


class ElasticBrenoResource(Resource):
    def get(self):
        for i in range(1, 10):
            try:
                1 / 0
            except ZeroDivisionError:
                app.logger.error(
                    'Breninho is hereeeee',
                    exc_info=True,
                    extra={
                        'am_i_agent_breno': True,
                    }
                )

            try:
                a = [1, 2, 3]
                print a[4]
            except IndexError:
                app.logger.error(
                    'Breno is here',
                    exc_info=True,
                    extra={
                        'am_i_agent_breno': True,
                    }
                )

        return {'Heeeeeey': 'Im generating a lot of error to you'}


api.add_resource(ElasticBrenoResource, '/error')

if __name__ == '__main__':
    handler = LoggingHandler(client=apm.client)
    handler.setLevel('WARN')
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=9999, debug=True)
