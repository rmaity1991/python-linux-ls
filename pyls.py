import json
import datetime
from argparse import ArgumentParser


def fromTimeStamp(data):
    months={
        1:"Jan",
        2:"Feb",
        3:"Mar",
        4:"Apr",
        5:"May",
        6:"June",
        7:"July",
        8:"Aug",
        9:"Sep",
        10:"Oct",
        11:"Nov",
        12:"Dec",
    }
    converted=datetime.datetime.fromtimestamp(data)
    print(f"{months[converted.month]} {converted.day} {converted.hour}:{converted.minute}",end="\t")

try:
    with open("file.json","r") as file:
        json_data=json.load(file)
except Exception as e:
    print("The JSON File reding is an error")
    exit()

parser=ArgumentParser(prog="ls",description="This python file will imitate the working of ls command in Linux")
parser.add_argument("-A","--all",required=False,dest="all",help="Prints all the files and directories including files starting with .",action='store_true')

parser.add_argument("-l","--list_all",required=False,dest="list_all",help="Prints the results vertically with additional information",action='store_true')

parser.add_argument("-r","--reverse_all",required=False,dest="reverse_all",help="Prints the results in reverse",action='store_true')

parser.add_argument("-t","--sorted_time",required=False,dest="sort_time",help="Prints the results sorted by time_modified",action='store_true')

parser.add_argument("-f","--filter",required=False,dest="filter_folder_files",help="This command will filter the output based on given option- file or dir or None",type=str,choices=["file","dir",None])

args=parser.parse_args()

reverse_count=len(json_data["contents"])-1

def time_sorted(data_item):
    return  data_item["time_modified"]
            

if args.sort_time:
    json_data["contents"]=sorted(json_data["contents"],key=time_sorted,reverse=True)


for items in json_data["contents"]:
    
    if args.filter_folder_files == None:
        if items["name"].startswith(".") and not args.all:
            pass
        elif args.list_all:
            """
            -rw-r--r-- 1071 Nov 14 11:27 LICENSE
            """  
            if not args.reverse_all:
                print(items["permissions"],end="\t")
                print(items["size"],end="\t")
                fromTimeStamp(items["time_modified"])
                print(items["name"],end="\n")
            else:
                print(json_data["contents"][reverse_count]["permissions"],end="\t")
                print(json_data["contents"][reverse_count]["size"],end="\t")
                fromTimeStamp(json_data["contents"][reverse_count]["time_modified"])
                print(json_data["contents"][reverse_count]["name"],end="\n")
                reverse_count-=1
        else:
            print(items["name"],end="\t")
    elif args.filter_folder_files == "dir":
        if "." in items["name"] and not args.all:
            pass
        elif args.list_all:
            """
            -rw-r--r-- 1071 Nov 14 11:27 LICENSE
            """  
            if not args.reverse_all:
                print(items["permissions"],end="\t")
                print(items["size"],end="\t")
                fromTimeStamp(items["time_modified"])
                print(items["name"],end="\n")
            else:
                print(json_data["contents"][reverse_count]["permissions"],end="\t")
                print(json_data["contents"][reverse_count]["size"],end="\t")
                fromTimeStamp(json_data["contents"][reverse_count]["time_modified"])
                print(json_data["contents"][reverse_count]["name"],end="\n")
                reverse_count-=1
        else:
            print(items["name"],end="\t")
    elif args.filter_folder_files == "file":
        if not "." in items["name"] and not args.all:
            pass
        elif args.list_all:
            """
            -rw-r--r-- 1071 Nov 14 11:27 LICENSE
            """  
            if not args.reverse_all:
                print(items["permissions"],end="\t")
                print(items["size"],end="\t")
                fromTimeStamp(items["time_modified"])
                print(items["name"],end="\n")
            else:
                print(json_data["contents"][reverse_count]["permissions"],end="\t")
                print(json_data["contents"][reverse_count]["size"],end="\t")
                fromTimeStamp(json_data["contents"][reverse_count]["time_modified"])
                print(json_data["contents"][reverse_count]["name"],end="\n")
                reverse_count-=1
        else:
            print(items["name"],end="\t")






