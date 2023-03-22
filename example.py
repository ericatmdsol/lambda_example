import logging

from flask import Flask

app = Flask(__name__)
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#the lambda_handler is referenced in the zappa_config file
@app.route("/", methods=["GET", "POST"])
def lambda_handler(event=None, context=None):
    logger.info("Lambda function invoked index()")

    return "Flask says Hello!!"


if __name__ == "__main__":
    app.run(debug=True)
