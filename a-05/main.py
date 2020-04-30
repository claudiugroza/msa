import sensor #sensor stub
import chart_studio.plotly as plot #plotly API
import json #extract credentials
import time #delay
import datetime #temp-time chart association

def init_plotly_stream():
    # init credentials
    with open('./credentials.json') as credentials_file:
        plotly_user_config = json.load(credentials_file)

    # authenticate with provided credentials
    plot.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

    # configure the plot
    url = plot.plot([
        {
            'x': [],
            'y': [],
            'type': 'scatter',
            'mode':'lines+markers',
            'stream': {
                'token': plotly_user_config['plotly_streaming_tokens'][0],
                'maxpoints': 200
                },
        }], filename='MS-Temperature')

    print ("View your streaming graph here: ", url)

    # attach a stream to the plot
    stream = plot.Stream(plotly_user_config['plotly_streaming_tokens'][0])

    return stream

def read_and_post(stream):
    # read temperature from our sensor module
    temp = sensor.read_temp()
    
    # post data to plotly
    if temp is not None:
        stream.write({'x': datetime.datetime.now(), 'y': temp})

def main():
    # stream setup
    stream = init_plotly_stream()
    stream.open()

    time.sleep(5)

    while True:
        # it's time to perform a reading
        read_and_post(stream)
        # delay between posts
        time.sleep(2)

try:
    main()
finally:
    pass
