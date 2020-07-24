import requests

with open("seacms.txt") as f:
    lines = [x.strip() for x in f.readlines()]

for url in lines:
    try:
        if requests.get(url + "/data/mysqli_error_trace.php").status_code == 200:
            print(url)
    except Exception as e:
        print(url + "\t" + str(e))
