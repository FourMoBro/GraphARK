from py2neo import Graph

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

user = os.environ.get("NEO4J_USER")
password = os.environ.get("NEO4J_PASSWORD")
bolt_url = "bolt://localhost:7687"

graph = Graph(bolt_url, auth=(user, password))
