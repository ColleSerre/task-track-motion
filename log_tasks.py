from datetime import datetime
import requests

key = ""

with open("key.txt") as f:
    key = f.read().strip()
    f.close()

if key == "":
    print("No key found!")
    exit()


# get completed tasks
def get_completed_tasks():

    workspace_ids = {
        # "TCE - 1": "YCbfZUx5w5YkqpAsvvWa4",
        # "TCE - 2": "VJp1NdMZMXlb9nEoj__GP",
        # "UCL": "p0qSaI5ODJKiafrrNkJslg",
        "Personal": "c1TXt-nAhkKhgJmVU0Npo",
    }

    for i, j in workspace_ids.items():
        headers = {
            "X-API-Key": key,
            "accept": "application/json",
        }

        params = {
            "workspaceId": j,
            "status": "Completed",
        }

        r = requests.get("https://api.usemotion.com/v1/tasks",
                         headers=headers, params=params)
        r = r.json()
        return [i["name"] for i in r["tasks"]]


def diff(list_a, list_b):
    return len(set(list_b) - set(list_a))


def write_progress(completed_tasks: int):
    t = datetime.now().strftime("%d/%m")
    with open("log.csv", "w+") as f:
        f.write(f"{t},{completed_tasks}\n")
        f.close()


tasks = get_completed_tasks()
previous_day = None

with open("log.csv") as f:
    # read last line
    previous_day = f.readlines()[-1].strip().split(",")
    f.close()

if previous_day is None:
    print("Error reading log.csv for previous data")
    exit()

today_completed_tasks = diff(tasks, previous_day[1])
write_progress(today_completed_tasks)
