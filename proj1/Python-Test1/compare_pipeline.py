
from pathlib import Path
import jsondiff, os, argparse, json, subprocess, time

parser = argparse.ArgumentParser(description='ArgumentParser for firebom generation tool')
parser.add_argument("--pipelinename", required=True, help="This is the pipeline name that needs to be compared")
parser.add_argument("--output_directory", required=True, help="This is the output directory for json")
parser.add_argument("--step", choices=["1", "2", "3"], required=True, help='''This is the step that you want to run \n 
1. Download Pipeline from Environment1. Example Dev2, \n 
2. Download Pipeline from Environment2. Example QA1\n 
3. Compare pipelines from Environment1 & Environment2\n''')
args = parser.parse_args()
print(f"Received Inputs: {args}")

home = str(Path.home())

os.chdir(f"{home}/.spin")

if args.step == "1":

    os.system("~/vpnutil start ASE-Dev2")
    time.sleep(10)
    out = subprocess.check_output(f"spin pipeline get -k -a datatier -n {args.pipelinename} \
    --config config_dev2", shell=True)
    os.system("~/vpnutil stop ASE-Dev2")

    out = out.decode('utf8')#.replace("'", '"').replace("\n", '')

    if out == 'null':
        raise Exception(f"Error Occurred when downloading Pipeline {args.pipelinename}")
    Pipeline_Dev2 = json.loads(out)
    with open(f"{args.output_directory}/{args.pipelinename}_Dev2.json", "w") as write_file:
        json.dump(Pipeline_Dev2, write_file)


if args.step == "2":
    os.system("~/vpnutil start ASEQA")
    time.sleep(10)
    out = subprocess.check_output(f"spin pipeline get -k -a datatier -n {args.pipelinename} \
    --config config_qa1", shell=True)
    os.system("~/vpnutil stop ASEQA")
    out = out.decode('utf8').replace("'", '"').replace("\n", '')

    if out == 'null':
        raise Exception(f"Error Occurred when downloading Pipeline {args.pipelinename}")

    Pipeline_QA1 = json.loads(out)
    with open(f"{args.output_directory}/{args.pipelinename}_QA1.json", "w") as write_file:
        json.dump(Pipeline_QA1, write_file)

if args.step == "3":
    with open(f"{args.output_directory}/{args.pipelinename}_Dev2.json", "r") as read_file:
        Pipeline_Dev2 = json.load(read_file)

    with open(f"{args.output_directory}/{args.pipelinename}_QA1.json", "r") as read_file:
        Pipeline_QA1 = json.load(read_file)

    if 'id' in Pipeline_Dev2.keys():
        del Pipeline_Dev2['id']

    if 'id' in Pipeline_QA1.keys():
        del Pipeline_QA1['id']

    if 'lastModifiedBy' in Pipeline_Dev2.keys():
        del Pipeline_Dev2['lastModifiedBy']
    if 'lastModifiedBy' in Pipeline_QA1.keys():
        del Pipeline_QA1['lastModifiedBy']

    if 'updateTs' in Pipeline_Dev2.keys():
        del Pipeline_Dev2['updateTs']
    if 'lastModifiedBy' in Pipeline_QA1.keys():
        del Pipeline_QA1['updateTs']

    print(f'Pipeline: {args.pipelinename} has the following differences')
    print('#'*50)
    x=jsondiff.diff(Pipeline_Dev2, Pipeline_QA1)
    for k,v in x.items():
        print(k, v)
        print('')
    print('#'*50)
    print("Done")


