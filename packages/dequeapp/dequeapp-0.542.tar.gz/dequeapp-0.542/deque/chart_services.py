import datetime
import json
import os
import subprocess
import traceback

import coolname

from deque.rest_connect import RestConnect
from deque.deque_environment import AGENT_API_SERVICE_URL
from deque.redis_services import RedisServices
import pickle
import multiprocessing
from deque.parsing_service import ParsingService
from deque.datatypes import Image, Audio, Histogram, BoundingBox2D
from deque.util import MODEL, CODE, DATA, ENVIRONMENT, RESOURCES
import requests
import glob
import time
import psutil
import GPUtil
import socket
from datatypes import Table



class Run:

    # _submission_count = 1
    def __init__(self, data: Table, chart_type ):
