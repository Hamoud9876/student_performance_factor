import logging

def setup_logging():
    logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="""%(asctime)s [%(levelname)s] %(name)s 
    (%(filename)s:%(funcName)s:%(lineno)d): %(message)s""",
    force=True,
)