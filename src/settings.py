def init():
    global base_url
    base_url = ''
    global enable_kafka
    enable_kafka = False
    global quiet
    quiet = False
    global watchdog
    watchdog = False
    global topic_name, producer
    topic_name, producer = '' , ''