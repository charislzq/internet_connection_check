import requests, time
#from requests.exceptions import ConnectionError

import os

### Note from wayne: might want to consider the flags used as it works differently for different system
def internet_connection_test(url:str):
  print(f'Attempting to connect to {url} to determine internet connection status.')
  
  try:
    # ping uses ICMP protocol
  	# pinging with 5 packets via -c flag with 10 second timeout
   response = os.popen(f"ping -c 5 -t 10 {url}")
   for line in response.readlines():
      print(line)
  except:
    print(f"Failed with unparsed reason.")
    
  # uses HTTP protocol
	# try:
	# 	print(url)
	# 	resp = requests.get(url, timeout = 10)
	# 	resp.text
	# 	resp.status_code
	# 	print(f'Connection to {url} was successful.')
	# 	return True
	# except ConnectionError as e:
	# 	requests.ConnectionError
	# 	print(f'Failed to connect to {url}.')
	# 	return False
	# except:
	# 	print(f'Failed with unparsed reason.')
	# 	return False
 


# --------------------------------------------------------------
### Charis's suggestion: Could use an existing library (eg. speedtest/pyspeedtest) for more accurate and comprehensive download speed measurement (streamline)
# Need to install speedtest module first (pip install speedtest-cli)
import speedtest

#creates an instance of the Speedtest class
#interact with the speedtest module and perform measurements
st = speedtest.Speedtest()
#retrieves information about available speedtest servers 
#chooses the one that is considered to be the "best" for the current location based on factors like ping and latency
best_server = st.get_best_server()

print(f"Testing download speed from server {best_server['host']}...")
#initiates a download test from the chosen server and measures the download speed
#bytes per second
download_speed = st.download()

#divides download speed in bytes per second by 1024**2 to convert it to megabits per second (Mbps)
# 1 byte = 8 bits - not sure if need to divide by 8 as well
# 1 kilobyte = 1024 bytes
# 1 megabit = 1024 bits
print(f"Download Speed: {download_speed / (1024**2):.2f} Mbps")
# --------------------------------------------------------------


def bytes_to_mb(bytes:float):
  # 1e+6
  return float(bytes / pow(1024, 2))

def check_download_speed(url:str):
  print(f'Attempting to downloade file from {url} to determine download speed.')
  try:
    start_time = time.time()
    response = requests.get(url, stream=True)
    
    '''
    From wayne: response.headers.get('content-length') is an information obtained from HTTP header,
    which might not measure the total time taken to download the file.
    The suggested code will provide iteration over the downloaded file, and will exit the loop once
    the file fully downloaded.
    Also note that the time elapsed will seem similar compared with your existing method because the
    file size is too small to see a difference.
    '''
    # total_length = 0
    # for data in response.iter_content(chunk_size=4096):
    #   total_length += len(data)
    # elapsed_time = time.time() - start_time
    # print(f'Elapsed time: {elapsed_time}')
      
    # download_speed_mbps = bytes_to_mb(total_length) / elapsed_time
    
    # print(f'Total length in mb: {round(bytes_to_mb(total_length), 1)}')
    # print(f'Download speed in mbps: {round(download_speed_mbps, 1)}')
    ################################

    # in Bytes
    total_length = float(response.headers.get('content-length'))
    
    if total_length is not None:
      # time since epoch in seconds
      elapsed_time = time.time() - start_time
      print(f'Elapsed time: {elapsed_time}')
      
      download_speed_mbps = bytes_to_mb(total_length) / elapsed_time
      
      print(f'Total length in mb: {round(bytes_to_mb(total_length), 1)}')
      print(f'Download speed in mbps: {round(download_speed_mbps, 1)}')
  except:
    print(f"Failed with unparsed reason.")

internet_connection_test(url='google.com')
check_download_speed(url='https://drive.google.com/uc?export=download&id=1B6rLZwZx9QkzulhB0Pcgci4BXPlHEu3Z')

